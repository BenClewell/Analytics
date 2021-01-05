# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DEMO_box_analysis_help.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(834, 736)
        Dialog.setMinimumSize(QtCore.QSize(834, 736))
        Dialog.setMaximumSize(QtCore.QSize(834, 736))
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(60, 210, 711, 471))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.title_retest_queue_2 = QtWidgets.QLabel(Dialog)
        self.title_retest_queue_2.setGeometry(QtCore.QRect(50, 30, 811, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.title_retest_queue_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Android 101")
        font.setPointSize(48)
        self.title_retest_queue_2.setFont(font)
        self.title_retest_queue_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.title_retest_queue_2.setIndent(75)
        self.title_retest_queue_2.setObjectName("title_retest_queue_2")
        self.title_retest_queue_3 = QtWidgets.QLabel(Dialog)
        self.title_retest_queue_3.setGeometry(QtCore.QRect(0, 110, 811, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.title_retest_queue_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Android 101")
        font.setPointSize(28)
        self.title_retest_queue_3.setFont(font)
        self.title_retest_queue_3.setStyleSheet("color: rgb(122, 122, 122);")
        self.title_retest_queue_3.setIndent(75)
        self.title_retest_queue_3.setObjectName("title_retest_queue_3")
        self.title_retest_queue_3.raise_()
        self.textEdit.raise_()
        self.title_retest_queue_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Help"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Welcome to Bin Analytics, a powerful tool to help you learn about our inventory\'s composition. In this tutorial, you\'ll learn how to view categorical inventory information, use the </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">Visualization Mode</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">, and go over some of the ways you can put logistical data to work in our workspace.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">In this demonstration version, we are looking at the inventory on a theoretical spaceship in charge of storing alien tissue. To learn more about what kind of alien tissue is kept on the ship, check out the bottom of this tutorial. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">LOOKING AT INVENTORY CATEGORIES</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">At the top of the program, you\'ll see a row of black rectangles with our inventory\'s various categories on it. To switch to that category, click on the rectangle. This will bring up four different pieces of information on that inventory category:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">TOTAL SAMPLES:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"> The number of recorded samples (undisposed) in a sample category.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">BINS IN USE: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">The number of bins with at least one sample entry present.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">BINS FREE:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"> The number of bins that we have free in a given category. Each major category has a total of 250 bins, and each transport category has a total of 20 bins.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">AVERAGE FILL PER BIN:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"> The mean number of sample entries for all used bins.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-style:italic;\">These four markers are valuable for setting </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600; font-style:italic;\">disposal guidelines</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-style:italic;\"> for sample categories, and for deciding when to </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600; font-style:italic;\">reconsolidate</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-style:italic;\"> samples.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-style:italic;\">Exact guidelines should be set and interpreted by team leadership.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">USING VISUALIZATION MODE</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">The most powerful tool you have at your fingertips is the robust </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">Visualization Mode. </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">By clicking on the large button on the righthand side of the program, you can toggle this mode on and off. When </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">enabled </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">(Indicator will flash blue), you will automatically create an interactive visualization of an inventory\'s data, and launch it in your default browser. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-style:italic;\">You may receive a warning about enabling content when using certain browsers. You can disable these warnings in your browser settings, or simply allow the content each time you generate a graph.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">You may </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">mouse over data points </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">on the chart to see the box number and sample fill, and may drag a rectangle over sections of the visualization to </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">zoom in closer. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Visualization mode may be turned </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">off</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"> and </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">on</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"> at any time, if you would like to generate a graph (or not) every time that you select a category. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">USING VISUALIZATION MODE TO MAINTAIN INVENTORY HEALTH</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Visualization Mode allows you to see exactly how many samples are in each bin, catch suspicious inventory situations, and make sure that sample categories are being maintained according to their storage guidelines.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Here are some things to look out for when using a non-procedurally-generated database with the potential for human error:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; text-decoration: underline;\">Tall Bars</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">While this can simply be a case of many tightly-packed samples, it can also indicate that a user has entered a bin number wrong (</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-style:italic;\">ALPH1 instead of ALPHA1, for example</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">), and that the visualizer is binning those two charts together.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">If you mouse-over a bar, and the number that appears doesn\'t match up with the bar\'s actual height on the graph, there is a bin somewhere in our database that has been entered wrong, and has a number of \'ghost samples\' contained inside of it. Investigate this issue further in the inventory program, and rescan the correct bin\'s contents into inventory once more for consistency.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; text-decoration: underline;\">Outlier Entries</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Keep an eye out for visualization entries that seem suspicious. Maybe it\'s a transport bin, and you know all samples have been inventoried already (eg, nothing should be in transport). Maybe it\'s an inventory bin that isn\'t grouped with other filled boxes. It\'s always worth taking a look in the inventory if something about the data seems off. .</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">There are many instances where \'ghost samples\' can be entered into real, properly-formatted bins. If you see a bin in the visualizer that doesn\'t physically contain a sample, make sure to delete the sample from the bin in the inventory program. Bin entries in our inventory should perfectly reflect their real-life contents.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Thank you for taking the time to learn about what the Analytics program can do-- and hopefully, you can put some of the data to use to keep our inventory healthy, accurate, and ready in times of heavy stress.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">Good luck!  :)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">A SUMMARY OF OUR MOCK DATA:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:8pt; color:#24292e; background-color:#ffffff;\">For our theoretical inventory, imagine yourself on a spaceship that\'s in charge of holding five unique species of alien. Each year, tens of thousands of alien tissue samples are held on the ship, in one of 250 holding bins. Bins closer to 0 are held in colder conditions, and bins closer to 250 are held in hotter conditions. Different alien species must have their tissue differently distributed in their species\' bins according to their curation needs.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:8pt; color:#24292e; background-color:#ffffff;\">ALPHA:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:8pt; color:#24292e;\" style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">Alpha tissue samples do not have hard temperature limits regarding their storage, although colder temperatures are preferred. When the average number of alpha tissue samples per bin exceeds 20, it is important to spread out the samples across the available storage range, in a downward linear manner.</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:8pt; color:#24292e; background-color:#ffffff;\">BETA:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:8pt; color:#24292e;\" style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">These tissues samples are sensitive to mid-warm temperatures, and must be stored from cold-to-mid temperatures, and in hot temperatures-- but storing these alien tissues in the upper-middle of the bin range is never reccomended.</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:8pt; color:#24292e; background-color:#ffffff;\">GAMMA:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:8pt; color:#24292e;\" style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">These samples should be stored in a bell distribution-- with the majority of tissue samples in the middle of the bin range.</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:8pt; color:#24292e; background-color:#ffffff;\">EPSILON:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:8pt; color:#24292e;\" style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">An alien species known for their hot homeworld, it is never reccomended to store epsilon tissue at a colder temperature. Therefore, one should favor the bins on the higher limit.</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:8pt; color:#24292e; background-color:#ffffff;\">ZETA:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:8pt; color:#24292e;\" style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">Zeta aliens are our most adaptable species, and are to be stored in a stochastic manner across all of our available bins. It\'s important to have a wide variety of Zeta tissue storage conditions for research!</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"><br /></p></body></html>"))
        self.title_retest_queue_2.setText(_translate("Dialog", "BIN ANALYTICS"))
        self.title_retest_queue_3.setText(_translate("Dialog", "HOW TO INVESTIGATE SAMPLES"))
