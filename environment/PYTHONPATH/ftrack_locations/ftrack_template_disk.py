import os

import ftrack_api
import ftrack
import ftrack_template


class NewStructure(ftrack_api.structure.base.Structure):

    def get_resource_identifier(self, entity, context=None):

        templates = ftrack_template.discover_templates()

        path = ftrack_template.format(
            {}, templates, entity=entity
        )[0].replace("\\", "/").replace("//", "/")

        if entity.entity_type == "SequenceComponent":

            padding = entity["padding"]
            if padding:
                expression = "%0{0}d".format(padding)
            else:
                expression = "%d"

            filetype = entity["file_type"]
            path = path.replace(
                filetype, "/{0}.{1}{2}".format(
                    os.path.splitext(os.path.basename(path))[0],
                    expression,
                    filetype
                )
            )

        return path


def get_new_location(session):

    location = session.query(
        "Location where name is \"project.disk.root\""
    ).one()
    location.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix="")
    location.structure = NewStructure()
    location.priority = 50
    return location


class OldStructure(ftrack.Structure):

    def getResourceIdentifier(self, entity):

        templates = ftrack_template.discover_templates()
        session = ftrack_api.Session()

        path = ftrack_template.format(
            {}, templates, entity=session.get("Component", entity.getId())
        )[0].replace("\\", "/").replace("//", "/")

        if entity.isSequence():

            padding = entity.getPadding()
            if padding:
                expression = "%0{0}d".format(padding)
            else:
                expression = "%d"

            filetype = entity.getFileType()
            path = path.replace(
                filetype, "/{0}.{1}{2}".format(
                    os.path.splitext(os.path.basename(path))[0],
                    expression,
                    filetype
                )
            )

        return path


def get_old_location():

    location = ftrack.ensureLocation("project.disk.root")
    location.setAccessor(ftrack.DiskAccessor(prefix=""))
    location.setStructure(OldStructure())
    return location
