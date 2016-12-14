import os

import ftrack
import ftrack_template
import ftrack_api


session = ftrack_api.Session()


class Structure(ftrack.Structure):

    def getResourceIdentifier(self, entity):

        templates = ftrack_template.discover_templates()

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


def register(registry, **kw):

    location = ftrack.ensureLocation("project.disk.root")
    location.setAccessor(ftrack.DiskAccessor(prefix=""))
    location.setStructure(Structure())

    registry.add(location)
