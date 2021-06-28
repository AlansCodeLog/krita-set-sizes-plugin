# SPDX-License-Identifier: CC0-1.0

from PyQt5.QtWidgets import QDialog


class TenBrushSizesDialog(QDialog):

    def __init__(self, ui, parent=None):
        super(TenBrushSizesDialog, self).__init__(parent)

        self.ui = ui

    def accept(self):
        self.ui.TenBrushSizes.writeSettings()

        super(TenBrushSizesDialog, self).accept()

    def closeEvent(self, event):
        event.accept()
