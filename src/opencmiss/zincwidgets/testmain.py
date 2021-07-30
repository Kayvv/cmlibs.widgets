import os
from PySide2 import QtWidgets, QtGui, QtCore
from opencmiss.zincwidgets.exportwebgldialog import ExportWebGLDialog
from opencmiss.zincwidgets.materialeditorwidget import MaterialEditorWidget
from opencmiss.zincwidgets.spectrumeditorwidget import SpectrumEditorWidget
from opencmiss.zinc.material import Materialmodule
from opencmiss.argon.core.argondocument import ArgonDocument

if __name__ == '__main__':
    import sys
    filename = r"c:/users/ywan787/mapclient_workflows/argon_viewer\..\..\neondata\neonheart\heart.argon"
    # filename = r"c:/users/ywan787/mapclient_workflows/argon_viewer\..\..\neondata\neoncube\colourcube.argon"
    with open(filename, 'r') as f:
        state = f.read()
        document = ArgonDocument()
        document.initialiseVisualisationContents()
        # set current directory to path from file, to support scripts and fieldml with external resources
        path = os.path.dirname(filename)
        os.chdir(path)
        document.deserialize(state)

    zincContext = document.getZincContext()
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    
    dockWidgetSpectrumEditor = QtWidgets.QDockWidget(w)
    dockWidgetSpectrumEditor.setWindowTitle('Spectrum Editor')
    dockWidgetSpectrumEditor.setObjectName("dockWidgetSpectrumEditor")
    dockWidgetContentsSpectrumEditor = SpectrumEditorWidget(dockWidgetSpectrumEditor)
    dockWidgetContentsSpectrumEditor.setObjectName("dockWidgetContentsSpectrumEditor")
    dockWidgetSpectrumEditor.setWidget(dockWidgetContentsSpectrumEditor)
    dockWidgetContentsSpectrumEditor.setSpectrums(document.getSpectrums())
    w.addDockWidget(QtCore.Qt.DockWidgetArea(QtCore.Qt.LeftDockWidgetArea), dockWidgetSpectrumEditor)

    w.show()
    sys.exit(app.exec_())

    model_changed = False