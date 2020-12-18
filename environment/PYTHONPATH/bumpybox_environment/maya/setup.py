import pymel.core as pc

from avalon import api
from Qt import QtWidgets, QtCore


class CameraWindow(QtWidgets.QDialog):

    def __init__(self, cameras):
        super(CameraWindow, self).__init__()
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        self.camera = None

        self.widgets = {
            "label": QtWidgets.QLabel("Select camera for image plane."),
            "list": QtWidgets.QListWidget(),
            "warning": QtWidgets.QLabel("No cameras selected!"),
            "buttons": QtWidgets.QWidget(),
            "okButton": QtWidgets.QPushButton("Ok"),
            "cancelButton": QtWidgets.QPushButton("Cancel")
        }

        # Build warning.
        self.widgets["warning"].setVisible(False)
        self.widgets["warning"].setStyleSheet("color: red")

        # Build list.
        for camera in cameras:
            self.widgets["list"].addItem(camera)

        # Build buttons.
        layout = QtWidgets.QHBoxLayout(self.widgets["buttons"])
        layout.addWidget(self.widgets["okButton"])
        layout.addWidget(self.widgets["cancelButton"])

        # Build layout.
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.widgets["label"])
        layout.addWidget(self.widgets["list"])
        layout.addWidget(self.widgets["buttons"])
        layout.addWidget(self.widgets["warning"])

        self.widgets["okButton"].pressed.connect(self.on_ok_pressed)
        self.widgets["cancelButton"].pressed.connect(self.on_cancel_pressed)
        self.widgets["list"].itemPressed.connect(self.on_list_itemPressed)

    def on_list_itemPressed(self, item):
        self.camera = item.text()

    def on_ok_pressed(self):
        if self.camera is None:
            self.widgets["warning"].setVisible(True)
            return

        self.close()

    def on_cancel_pressed(self):
        self.camera = None
        self.close()


def animation_create():
    default_cameras = [
        "frontShape", "perspShape", "sideShape", "topShape"
    ]
    cameras = [
        x for x in pc.ls(type="camera") if x.name() not in default_cameras
    ]
    camera_names = {x.getParent().name(): x for x in cameras}
    camera_names["Create new camera."] = "create_camera"
    window = CameraWindow(camera_names.keys())
    window.exec_()

    camera = camera_names.get(window.camera)

    if camera == "create_camera":
        camera = pc.createNode("camera")

    if camera:
        camera = camera.getTransform()

    instances = [
        {"name": "cameraMain", "family": "camera", "nodes": [camera]},
        {"name": "pointcacheMain", "family": "pointcache"},
        {"name": "reviewMain", "family": "review", "nodes": [camera]},
        {
            "name": "reviewPrecomp",
            "family": "review",
            "nodes": [camera],
            "attributes": {
                "isolate": True, "keepImages": True, "imagePlane": False
            }
        }
    ]

    for instance in instances:
        instance["asset"] = api.Session["AVALON_ASSET"]
        attributes = instance.pop("attributes", [])
        nodes = instance.pop("nodes", [])

        object_set = api.create(**instance)
        object_set = pc.PyNode(object_set)

        for attr_name in attributes:
            attr = getattr(object_set, attr_name)
            attr.set(attributes[attr_name])

        for node in nodes:
            if node is None:
                continue
            object_set.add(node)
