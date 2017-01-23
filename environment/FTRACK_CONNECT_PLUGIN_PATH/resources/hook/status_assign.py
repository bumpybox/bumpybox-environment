import getpass

import ftrack


def callback(event):
    """ This plugin assigns users according to groups on a project.

    The plugin will assign users to a task when the task enters a specified
    status, and vice-versa unassign those people from the task when the task
    exits the status. In production we use it to assign supervisors to tasks
    when the tasks status changes to "Supervisor Review". This means the
    supervisor can stay within their "My Tasks" tab and get notified of the
    tasks they need to review.

    Usage:
        You will also need to setup project groups, to assign who needs to
        assigned to what types of tasks. See the attached image.

        - Setup a project group with the name of the status you want to track.
        - Setup a subgroup within the above group with the name of the type of
        task you want to track.
        - Add the people you want to get assigned to a task, when the status
        changes, to the subgroup.
    """

    for entity in event['data'].get('entities', []):

        # Filter non-assetversions
        if entity.get('entityType') == 'task' and entity['action'] == 'update':

            if 'statusid' not in entity.get('keys'):
                return

            # Find task if it exists
            task = None
            try:
                task = ftrack.Task(id=entity.get('entityId'))
            except:
                return

            # remove status assigned users
            if task.getMeta('assignees'):
                for userid in task.getMeta('assignees').split(','):
                    try:
                        task.unAssignUser(ftrack.User(userid))
                    except:
                        pass

            # getting status named group
            task_status_name = task.getStatus().get('name').lower()

            project = task.getParents()[-1]
            status_group = None
            for group in project.getAllocatedGroups():
                if group.getSubgroups():
                    if group.get('name').lower() == task_status_name:
                        status_group = group

            users = []
            if status_group:

                for group in status_group.getSubgroups():
                    task_type_name = task.getType().get('name').lower()
                    if task_type_name == group.get('name').lower():

                        # assigning new users
                        for member in group.getMembers():
                            try:
                                task.assignUser(member)
                                users.append(member.get('userid'))
                            except:
                                pass

            # storing new assignees
            value = ''
            for user in users:
                value += user + ','
            try:
                value = value[:-1]
            except:
                pass
            task.setMeta('assignees', value=value)


def register(registry, **kw):

    # Validate that registry is the correct ftrack.Registry. If not,
    # assume that register is being called with another purpose or from a
    # new or incompatible API and return without doing anything.
    if registry is not ftrack.EVENT_HANDLERS:
        # Exit to avoid registering this plugin again.
        return

    # Subscribe to events with the update topic.
    ftrack.EVENT_HUB.subscribe("topic=ftrack.update", callback)
