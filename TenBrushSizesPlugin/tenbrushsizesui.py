# SPDX-License-Identifier: CC0-1.0

from PyQt5.QtCore import (Qt, qDebug)
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QDoubleSpinBox, QScrollArea, QGridLayout, QLabel, QDialogButtonBox)
from PyQt5.QtGui import QKeySequence
from . import tenbrushsizesdialog
import krita


class TenBrushSizesUI(object):

    def __init__(self):
        self.kritaInstance = krita.Krita.instance()
        self.mainDialog = tenbrushsizesdialog.TenBrushSizesDialog(self, self.kritaInstance.activeWindow().qwindow())

        self.buttonBox = QDialogButtonBox(self.mainDialog)
        self.layout = QVBoxLayout(self.mainDialog)
        self.baseWidget = QWidget()
        self.baseArea = QWidget()
        self.scrollArea = QScrollArea()
        self._layout = QGridLayout()

        self.buttonBox.accepted.connect(self.mainDialog.accept)
        self.buttonBox.rejected.connect(self.mainDialog.reject)

        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.scrollArea.setWidgetResizable(True)

    def initialize(self, TenBrushSizes):
        self.TenBrushSizes = TenBrushSizes

        self.layout.addWidget(QLabel(i18n("Shortcuts can be configured in Settings => Configure Krita => Keyboard Shortcuts => Search \"Set Brush Size\"")))

        for item in range(0, 10):
            self._addRow(item)

        self.baseArea.setLayout(self._layout)
        self.scrollArea.setWidget(self.baseArea)

        self.layout.addWidget(self.scrollArea)
        self.layout.addWidget(self.buttonBox)

        self.mainDialog.show()
        self.mainDialog.activateWindow()
        self.mainDialog.exec_()

    def _addRow(self, key):
        rowPosition = self._layout.rowCount()

        label = QLabel()
        name = self.TenBrushSizes.actions[key].text()
        shortcut = self.TenBrushSizes.actions[key].shortcut().toString(QKeySequence.NativeText)
        label.setText(name + " (" + i18n("Shortcut") +": " + shortcut + ")")

        inputField = QDoubleSpinBox()
        inputField.setMinimum(0.01)
        inputField.setMaximum(self.TenBrushSizes.config["maxSize"])
        inputField.setValue(self.TenBrushSizes.config["sizes"][key])
        inputField.setSuffix("px")

        # self._layout.addRow(label, inputField)
        self._layout.addWidget(label, rowPosition, 0)
        self._layout.addWidget(inputField, rowPosition, 1)

    def saved_sizes(self):
        _saved_sizes = []
        index = 0

        for row in range(self._layout.rowCount()-1):
            inputField = self._layout.itemAt(index+1).widget()
            print(inputField.value())
            _saved_sizes.append(inputField.value())
            index += 2

        return _saved_sizes

