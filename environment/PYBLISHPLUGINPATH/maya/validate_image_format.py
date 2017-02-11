import pyblish.api


class BumpyboxEnvironmentMayaValidateImageFormat(pyblish.api.InstancePlugin):

    order = pyblish.api.ValidatorOrder
    label = "Image Format"
    families = ["renderlayer"]
    optional = True
    hosts = ["maya"]

    def process(self, instance):

        ext = instance.data["collection"].format("{tail}")
        valid_extensions = [".exr", ".png", ".jpeg"]

        msg = "Output \"{0}\" image format is not valid.".format(ext)
        assert ext in valid_extensions, msg
