import os

from avalon import io, api


def import_full_resolution_movie():
    raise NotImplementedError("This is not implemented yet.")


def import_half_resolution_movie():
    raise NotImplementedError("This is not implemented yet.")


def import_rigging():
    shot = io.find_one({"type": "asset", "name": os.environ["AVALON_ASSET"]})
    for id in shot["data"]["inputs"]:
        subset = io.find_one(
            {"type": "subset", "name": "rigMain", "parent": id}
        )
        versions = io.find({"type": "version", "parent": subset["_id"]})
        latest_version = None
        latest_version_number = 0
        for version in versions:
            if version["name"] > latest_version_number:
                latest_version = version
                latest_version_number = version["name"]

        representation = io.find_one(
            {"type": "representation", "parent": latest_version["_id"]}
        )

        loader_plugin = None
        for Loader in api.discover(api.Loader):
            if representation["name"] not in Loader.representations:
                continue

            if "rig" not in Loader.families:
                continue

            loader_plugin = Loader

        api.load(Loader=loader_plugin, representation=representation["_id"])


def import_tracking():
    raise NotImplementedError("This is not implemented yet.")


def import_audio():
    raise NotImplementedError("This is not implemented yet.")


def import_animation():
    raise NotImplementedError("This is not implemented yet.")


def import_lookdev():
    raise NotImplementedError("This is not implemented yet.")
