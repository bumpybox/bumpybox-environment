class mock_entity(dict):
    """Mock entity for faking Ftrack entities
    Requires keyword argument "entity_type" on creation.
    """

    def __init__(self, *args, **kwargs):
        dict.__init__(self, args)

        if "entity_type" not in kwargs.keys():
            raise ValueError('Need the keyword argument "entity_type"')

        self.__dict__ = kwargs


workfile_extensions = [".nk", ".mb"]

single_files = {
    ".mb": "scene",
    ".ma": "scene",
    ".nk": "scene",
    ".mov": "mov",
    ".abc": "cache"
}

sequence_files = {".exr": "img"}
