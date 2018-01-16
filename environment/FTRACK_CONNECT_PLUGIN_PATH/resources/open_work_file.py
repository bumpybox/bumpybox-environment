import os
import sys

from Qt import QtWidgets, QtCore


class Window(QtWidgets.QDialog):
    """"""

    def __init__(self, work_file, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Work File Loader.")
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setWindowFlags(
            self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint
        )
        self.work_file = work_file

        # Layout
        body = QtWidgets.QVBoxLayout(self)

        label = QtWidgets.QLabel('Lastet version: "{0}"'.format(work_file))
        body.addWidget(label)

        title = "Open latest version"
        self.latest_version_button = QtWidgets.QPushButton(title)
        body.addWidget(self.latest_version_button)

        title = "Open previous version"
        self.previous_version_button = QtWidgets.QPushButton(title)
        body.addWidget(self.previous_version_button)

        # Functionality
        self.latest_version_button.clicked.connect(self.open_latest)
        self.previous_version_button.clicked.connect(self.open_previous)

    def open_latest(self):
        self.deleteLater()

    def open_previous(self):
        ext = os.path.splitext(self.work_file)[1]
        path = QtWidgets.QFileDialog.getOpenFileName(
            caption="Work File Loader",
            dir=os.path.dirname(self.work_file),
            filter="*" + ext
        )[0]

        if path:
            self.work_file = path

        self.deleteLater()

    def closeEvent(self, event):
        self.work_file = ""
        event.accept()


QtWidgets.QApplication(sys.argv)
win = Window(sys.argv[1])
win.exec_()
print win.work_file
