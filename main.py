from datetime import datetime as datetime_, timedelta

# create time function that works with PySide2 GUI
from PySide2 import QtWidgets, QtCore, QtGui, QtTest

# tools for displaying the GUI
# PySide2 instead of PyQt
import random

# play interesting audio effects with each click
from functools import partial

# pass args to button presses in QT, avoid having to make more methods

import UI_analytics as UI_homescreen

# import frontend_help_ui as UI_help
# import frontend_about_ui as UI_about

"""
LIBRARIES: PyQt5 (PySide2)
Import the GUI that will display when the program is launched
"""
import backend_analytics as dbop

"""
LIBRARIES: pandas, SQlite3, numpy, plotly
Import the variables generated after manipulating
and analyzing a server database in SQL

Create interactive and current data visualizations in plotly based on
current SQL data. create_graph arguments are given as a HomeScreen class
method arguments to customize chart titles and category-specific differences.
"""


import frontend_effects as sfx

"""
LIBRARIES: pygame (audio mixer)
Import and reference audio effects that trigger during GUI animations
and aid in providing feedback for user actions
"""

print(
    "Initializing Analytics.\n\n\
    Please be patient while I process your inventory informatics. :)"
)
# provide a message while data is collected, provide feedback to user


def qWait(t):
    """Create a function that sequentially returns event pauses
    inside of the GUI. Allows animations to play elegantly."""
    end = datetime_.now() + timedelta(milliseconds=t)
    while datetime_.now() < end:
        QtWidgets.QApplication.processEvents()


QtTest.QTest.qWait = qWait
# condolidate the variable into a more succinct format


class HomeScreen(UI_homescreen.Ui_Dialog, QtWidgets.QMainWindow):
    """The main window that appears when launching the program.
    Projects a splash page that gives way to user control inferface"""

    def __init__(self):
        super(HomeScreen, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        # Make the GUI non-rescalable

        """SETTINGS FOR COUNTING TOTAL SAMPLES IN-HOUSE"""
        self.lcd_active.setProperty("value", dbop.lcd_total_read)
        # assign LCD number in title to reflect active samples in database
        self.lcd_disposed.setProperty("value", dbop.lcd_inv_disposed)
        # assign LCD number in title to reflect disposed samples in database
        self.pushButton_begin.clicked.connect(self.anim_splash_screen)
        # start the program

        """SETTINGS FOR MANAGING VISUALIZATION MODE"""
        self.pushButton_countbox.setCheckable(True)
        self.pushButton_countbox.setChecked(False)
        # Makes the pushButton_countbox able to toggle between two states
        self.pushButton_countbox.clicked.connect(self.toggle_visualization)
        # connect to the visualization-toggling Class method
        self.pushButton_countbox.setText(
            "CLICK TO\nBEGIN\nVISUALIZATION\nMODE"
        )
        self.pushButton_countbox.setStyleSheet(
            "background-color:white; color: black"
        )
        # initial color/text for the visualization box
        self.popup = False
        self.viz_notactive = True
        # visualization turned off when popup is False
        self.audio_variety = 0
        # move between four different audio effects by incrementing audio_variety variable

        # CONNECT THE BUTTONS THE APPROPRIATE INSTANCES
        self.pushButton_alpha.clicked.connect(
            partial(
                self.load_inventory,
                "ALPHA",
                dbop.AlphaCalc,
                250,
                "rgb(0,255,255)",
                "blue",
            )
            # Use the 'partial' library to pass in arguments for the function
            # connecting to the function. The prevents needing to use another separate function.
        )
        self.pushButton_alpha_transport.clicked.connect(
            partial(
                self.load_inventory,
                "ALPHA (TRANS)",
                dbop.AlphaTransCalc,
                20,
                "rgb(0,255,255)",
                "blue",
            )
        )
        self.pushButton_beta.clicked.connect(
            partial(
                self.load_inventory,
                "BETA",
                dbop.BetaCalc,
                250,
                "rgb(253,253,150)",
                "red",
            )
        )
        self.pushButton_beta_transport.clicked.connect(
            partial(
                self.load_inventory,
                "BETA (TRANS)",
                dbop.BetaTransCalc,
                20,
                "rgb(253,253,150)",
                "red",
            )
        )
        self.pushButton_gamma.clicked.connect(
            partial(
                self.load_inventory,
                "GAMMA",
                dbop.GammaCalc,
                250,
                "green",
                "rgb(50,205,50)",
            )
        )
        self.pushButton_epsilon.clicked.connect(
            partial(
                self.load_inventory,
                "EPSILON",
                dbop.EpsilonCalc,
                250,
                "black",
                "white",
            )
        )
        self.pushButton_zeta.clicked.connect(
            partial(
                self.load_inventory,
                "ZETA",
                dbop.ZetaCalc,
                250,
                "red",
                "rgb(253,253,150)",
            )
        )

        self.pushButton_total.clicked.connect(
            partial(
                self.load_inventory,
                "TOTAL",
                dbop.TotalCalc,
                1290,
                "white",
                "white",
            )
        )

    def show_message(self, title="", message=""):
        """establish parameters for displaying GUI messages to user"""
        QtWidgets.QMessageBox.information(None, title, message)

        """CLASS METHODS FOR VISUAL AND AUDIO EFFECTS"""

    def toggle_visualization(self):
        """set two different colored animations depending on whether
        visualization mode is on. Change the text to signal off/on
        status for visualization mode."""
        if self.pushButton_countbox.isChecked():
            self.popup = False
            # variable popup decides whether to show visualization
            sfx.yes_viz.play()
            # audio signals 'on' state
            self.pushButton_countbox.setText(
                "VISUALIZATION\nMODE ON\nSTANDBY\n/////\nCLICK TO\nENABLE."
            )
            self.pushButton_countbox.setStyleSheet(
                "background-color:pink; color: red"
            )
            QtTest.QTest.qWait(600)
            self.pushButton_countbox.setStyleSheet(
                "background-color:pink; color: black"
            )
            QtTest.QTest.qWait(200)
            self.pushButton_countbox.setStyleSheet(
                "background-color:white; color: black"
            )
            """ when checked, data visualizations will
            NOT be generated when clicking on a box category"""
        else:
            self.popup = True
            self.viz_notactive = False
            sfx.no_viz.play()
            # audio signals off state
            self.pushButton_countbox.setText("VISUALIZATION\nMODE\nENABLED")
            self.pushButton_countbox.setStyleSheet(
                "background-color:#80CEE1; color: green"
            )
            QtTest.QTest.qWait(600)
            self.pushButton_countbox.setStyleSheet(
                "background-color:#80CEE1; color: black"
            )
            QtTest.QTest.qWait(200)
            self.pushButton_countbox.setStyleSheet(
                "background-color:white; color: black"
            )

            # popup is set to true, generating data visualizations
            # when a box category is selected.

    def anim_splash_screen(self):
        """provide audio and visual feedback to starting the program,
        and then hide all splash screen GUI elements. (2800 milliseconds)
        Element manipulation is synced to sfx.launch audio"""
        sfx.click.play()
        sfx.launch.play()
        self.pushButton_begin.setVisible(False)
        QtTest.QTest.qWait(1100)
        self.label_hide_3.setVisible(False)
        self.label_hide_4.setVisible(False)
        QtTest.QTest.qWait(1000)
        self.label_hide_5.setVisible(False)
        QtTest.QTest.qWait(200)
        self.label_hide_6.setVisible(False)
        QtTest.QTest.qWait(100)
        self.label_hide_7.setVisible(False)
        QtTest.QTest.qWait(100)
        self.label_hide_8.setVisible(False)
        QtTest.QTest.qWait(100)
        self.label_hide_9.setVisible(False)
        QtTest.QTest.qWait(100)
        self.label_hide_1.setVisible(False)
        #self.label_hide_2.setVisible(False)

    def anim_loading(self):
        """provide audio-visual feedback when the user selects a
        category for analysis. Modifies GUI elements and eventually
        sets them back to original values (600 millisecond)"""
        self.label_16.setStyleSheet("background-color: black")
        QtTest.QTest.qWait(100)
        self.label_12.setStyleSheet("background-color: #383838")
        QtTest.QTest.qWait(100)
        self.label_19.setStyleSheet("background-color: black")
        QtTest.QTest.qWait(100)
        sfx.bass.play()
        sfx.click.play()
        # audio launches mid-function for proper timing

        self.label_20.setStyleSheet("background-color: #383838")
        QtTest.QTest.qWait(100)
        self.label_21.setStyleSheet("background-color: black")
        QtTest.QTest.qWait(200)
        self.label_16.setStyleSheet("background-color: white")
        self.label_12.setStyleSheet("background-color: white")
        self.label_19.setStyleSheet("background-color: white")
        self.label_20.setStyleSheet("background-color: white")
        self.label_21.setStyleSheet("background-color: white")

    def anim_visuals(self):
        """flicker visualization area to remind user of mode status"""
        # 383838 is the default alternating color from black, if color visuals are too distracting

        self.audio_variety += 1

        if self.audio_variety == 5:
            # increase variance after 4 moves
            self.audio_variety -= 4
        # switch between odd and even mod, reduce sfx fatigue for graph generation
        if self.audio_variety == 1:
            sfx.gen_2.play()
        if self.audio_variety == 2:
            sfx.gen_1.play()
        if self.audio_variety == 3:
            sfx.gen_4.play()
        if self.audio_variety == 4:
            sfx.gen_3.play()

        if self.pushButton_countbox.isChecked() or self.viz_notactive == True:
            # flash red if visualization mode is off
            # secondary catch for if the user hasn't touch viz button yet
            QtTest.QTest.qWait(300)
            self.label_11.setStyleSheet("background-color: pink")
            QtTest.QTest.qWait(50)
            self.label_11.setStyleSheet("background-color: black")
            QtTest.QTest.qWait(50)
            self.label_11.setStyleSheet("background-color: pink")
            QtTest.QTest.qWait(50)
            self.label_11.setStyleSheet("background-color: black")
        else:
            # flash green if visualizaition mode is on.
            graph_sound = random.choice(sfx.graph_sound_list)
            graph_sound.play()
            QtTest.QTest.qWait(300)
            self.pushButton_countbox.setText("GENERATING\nGRAPH")
            self.pushButton_countbox.setStyleSheet("background-color: #80CEE1")
            self.label_11.setStyleSheet("background-color: #80CEE1")
            QtTest.QTest.qWait(50)
            self.label_11.setStyleSheet("background-color: black")
            QtTest.QTest.qWait(50)
            self.label_11.setStyleSheet("background-color: #80CEE1")
            QtTest.QTest.qWait(50)
            self.label_11.setStyleSheet("background-color: black")
            QtTest.QTest.qWait(1000)
            self.pushButton_countbox.setStyleSheet("background-color: white")
            self.pushButton_countbox.setText("VISUALIZATION\nMODE\nENABLED")

    # metrics method is reliant on anim_loading and anim_visuals to run properly
    def set_metrics(self, title, total_samples, box_use, box_free, avg_fill):
        """a template for updating LCD numbers in the GUI. The last four
        arguments are later derived from the database operations file"""
        self.informatic_title.setText(title)
        sfx.propagate_info.play()
        QtTest.QTest.qWait(300)
        self.lcd_totalsamples.setProperty("value", total_samples)
        sfx.propagate_info.play()
        QtTest.QTest.qWait(300)
        self.lcd_boxes_in_use.setProperty("value", box_use)
        sfx.propagate_info.play()
        QtTest.QTest.qWait(300)
        self.lcd_boxes_free.setProperty("value", box_free)
        sfx.propagate_info.play()
        QtTest.QTest.qWait(300)
        self.lcd_average_fill.setProperty("value", avg_fill)

    def load_inventory(
        self, title, calc_class, max_boxes, graph_barcolor, graph_linecolor
    ):
        """Call the alpha class instance for dbop and propagate the LCD numbers in the QT interface
        PARAMETERS:
        title: What's displayed in the QT interface
        calc_class: call the class to pull metrics from in dbop
        max_boxes: assign a value for the known maximum number of boxes

        graph_barcolor: argument to create category graphs with different colors
        graph_linecolor: same as above arg
        """
        self.anim_loading()

        self.set_metrics(
            title,
            calc_class.filter_len,
            calc_class.filter_in_use,
            max_boxes - calc_class.filter_in_use,
            calc_class.boxfill_mean,
        )

        self.anim_visuals()

        if self.popup is True:
            calc_class.create_graph(graph_barcolor, graph_linecolor)
            # the variables in create_graph are specified during the button call.
            # this is for whatever class instance you're using (alpha, beta, etc)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = HomeScreen()
    qt_app.show()
    app.exec_()
