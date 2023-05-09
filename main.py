# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QFileInfo, QTime, QTimer, Qt, QEvent, QDir, QEvent


# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "BJTU_VSR_Demo - Modern GUI via PyDracula"
        description = "BJTU_VSR_Demo - Modern GUI via PyDracula"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        # event filter installation
        self.ui.videoWidget_1.installEventFilter(self)
        self.ui.videoWidget_2.installEventFilter(self)
        self.ui.videoWidget_3.installEventFilter(self)
        self.ui.videoWidget_4.installEventFilter(self)

        # Connection with slot and signal (not only LEFT MENUS)
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)        
        widgets.btn_theme.clicked.connect(self.buttonClick) # new to change theme color
        widgets.btn_filechooser.clicked.connect(self.buttonClick) # new to choose media
        
        # START MENU
        # ///////////////////////////////////////////////////////////////
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)


        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        # only for exe files with forzen absPath setting
        if getattr(sys, 'frozen', False):
            # frozen
            absPath = os.path.dirname(os.path.abspath(sys.executable))
        elif __file__:
            # unfrozen
            absPath = os.path.dirname(os.path.abspath(__file__))

        # load and apply style sheet (Default)    
        useCustomDarkTheme = False
        self.useCustomDarkTheme = useCustomDarkTheme
        self.absPath = absPath
        themeFile = os.path.abspath(os.path.join(absPath, "themes\py_dracula_dark.qss"))

        # SET THEME AND HACKS
        if useCustomDarkTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)
            # SET HACKS
            AppFunctions.setThemeHack(self)
            # initialization
            self.useCustomDarkTheme = not self.useCustomDarkTheme

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        # Video Player and Dir./
        # ///////////////////////////////////////////////////////////////
        self.curPath = QDir.currentPath()
        self.player1 = QMediaPlayer(self)
        self.player2 = QMediaPlayer(self)
        self.player3 = QMediaPlayer(self)
        self.player4 = QMediaPlayer(self)
        # Warning: it's not recommended to use different audio outputs for different media players, which is too noisy.
        self.audioOutput1 = QAudioOutput()
        self.audioOutput2 = QAudioOutput()
        self.audioOutput3 = QAudioOutput()
        self.audioOutput4 = QAudioOutput()
        # Video Player ouput location
        self.player1.setVideoOutput(self.ui.videoWidget_1)
        self.player2.setVideoOutput(self.ui.videoWidget_2)
        self.player3.setVideoOutput(self.ui.videoWidget_3)
        self.player4.setVideoOutput(self.ui.videoWidget_4)

        # Video Player Sliders
        # Slider_1
        self.ui.Slider1.setMinimum(0)
        self.ui.Slider1.setMinimum(1000)
        self.ui.Slider1.sliderMoved.connect(self.setPosition1)
        self.player1.positionChanged.connect(self.update_position1)
        self.player1.durationChanged.connect(self.update_duration1)
        # Slider_2
        self.ui.Slider2.setMinimum(0)
        self.ui.Slider2.setMinimum(1000)
        self.ui.Slider2.sliderMoved.connect(self.setPosition2)
        self.player2.positionChanged.connect(self.update_position2)
        self.player2.durationChanged.connect(self.update_duration2)
        # Slider_3
        self.ui.Slider3.setMinimum(0)
        self.ui.Slider3.setMinimum(1000)
        self.ui.Slider3.sliderMoved.connect(self.setPosition3)
        self.player3.positionChanged.connect(self.update_position3)
        self.player3.durationChanged.connect(self.update_duration3)
        # Slider_4
        self.ui.Slider4.setMinimum(0)
        self.ui.Slider4.setMinimum(1000)
        self.ui.Slider4.sliderMoved.connect(self.setPosition4)
        self.player4.positionChanged.connect(self.update_position4)
        self.player4.durationChanged.connect(self.update_duration4)
        # QTimer to control the single click and double click for different signals #TODO
        # self.timer = QTimer(self)
        # self.timer.setInterval(250)
        # self.timer.setSingleShot(True)
        # self.timer.timeout.connect(self.onTimeout)


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # CHANGE THEME
        if btnName == "btn_theme":
            if self.useCustomDarkTheme:
                themeFile = os.path.abspath(os.path.join(self.absPath, "themes\py_dracula_dark.qss"))
                UIFunctions.theme(self, themeFile, True)
                # set hacks
                AppFunctions.setThemeHack(self)
                self.useCustomDarkTheme = not self.useCustomDarkTheme
            else:
                themeFile = os.path.abspath(os.path.join(self.absPath, "themes\py_dracula_light.qss"))
                UIFunctions.theme(self, themeFile, True)
                # set hacks
                AppFunctions.setThemeHack(self)
                self.useCustomDarkTheme = not self.useCustomDarkTheme

        # CHOOSER MEDIA
        if btnName == "btn_filechooser":
            curPath = QDir.currentPath() # present working directory
            title = "Open Video" 
            filt = "video files(*.wmv *avi *.mp4 *.mov);;all files(*.*)" # filter for files
            fileName, flt = QFileDialog.getOpenFileName(self, title, curPath, filt)
            if fileName == "":
                return "no files selected"
            # label name
            self.ui.videolabel_1.setText("LRVideo")
            self.ui.videolabel_2.setText("Model_EDVR")
            self.ui.videolabel_3.setText("Model_TCNet")
            self.ui.videolabel_4.setText("Model_KSNet")
            # fileinfos and names
            fileInfo = QFileInfo(fileName)
            baseName = fileInfo.fileName()
            self.ui.labelVersion_3.setText(fileName)
            self.ui.lineEdit.setText(baseName)
            # play media
            media = QUrl.fromLocalFile(fileName)
            # Warning: it's not recommended to use different audio outputs for different media players, which is too noisy.
            self.player1.setAudioOutput(self.audioOutput1)
            self.player1.setSource(media)
            self.player1.play()
            self.player2.setAudioOutput(self.audioOutput2)
            self.player2.setSource(media)
            self.player2.play()
            self.player3.setAudioOutput(self.audioOutput3)
            self.player3.setSource(media)
            self.player3.play()
            self.player4.setAudioOutput(self.audioOutput4)
            self.player4.setSource(media)
            self.player4.play()
        if btnName == "btn_save":
            print("Save BTN clicked!")
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # Video contentes position and Slider:
    # ///////////////////////////////////////////////////////////////
    # Video_1
    def setPosition1(self, position):
        self.player1.setPosition(position * 1000)
    def update_position1(self, position):
        self.ui.Slider1.setValue(position / 1000)
    def update_duration1(self, duration):
        self.ui.Slider1.setRange(0, duration / 1000)
    # Video_2
    def setPosition2(self, position):
        self.player2.setPosition(position * 1000)
    def update_position2(self, position):
        self.ui.Slider2.setValue(position / 1000)
    def update_duration2(self, duration):
        self.ui.Slider2.setRange(0, duration / 1000)
    # Video_3
    def setPosition3(self, position):
        self.player3.setPosition(position * 1000)
    def update_position3(self, position):
        self.ui.Slider3.setValue(position / 1000)
    def update_duration3(self, duration):
        self.ui.Slider3.setRange(0, duration / 1000)
    # Video_4
    def setPosition4(self, position):
        self.player4.setPosition(position * 1000)
    def update_position4(self, position):
        self.ui.Slider4.setValue(position / 1000)
    def update_duration4(self, duration):
        self.ui.Slider4.setRange(0, duration / 1000)

    # EVENTS:
    # ///////////////////////////////////////////////////////////////
    # VIDEO PALYER EVENTS
    def closeEvent(self, event):
        if (self.player1.playbackState() == QMediaPlayer.PlaybackState.PlayingState):
            self.player1.stop()
        if (self.player2.playbackState() == QMediaPlayer.PlaybackState.PlayingState):
            self.player2.stop()
        if (self.player3.playbackState() == QMediaPlayer.PlaybackState.PlayingState):
            self.player3.stop()
        if (self.player4.playbackState() == QMediaPlayer.PlaybackState.PlayingState):
            self.player4.stop()

    def eventFilter(self, watched, event):
        # Mouse single click and double click events
        # video_1
        if (watched == self.ui.videoWidget_1):
            # left click for pause and for play
            if (event.type() == QEvent.MouseButtonPress and event.buttons() == Qt.LeftButton):
                if (self.player1.playbackState() == QMediaPlayer.PlaybackState.PlayingState):
                    self.player1.pause()
                else:
                    self.player1.play()
            # double click for fullscreen
            elif (event.type() == QEvent.MouseButtonDblClick):
                if (self.ui.videoWidget_1.isFullScreen()):
                    self.ui.videoWidget_1.setFullScreen(False)
                else:
                    self.ui.videoWidget_1.setFullScreen(True)
            elif (event.type() == QEvent.Type.KeyPress):
                if (event.key() == Qt.Key_Escape):
                    if (self.ui.videoWidget_1.isFullScreen()):
                        self.ui.videoWidget_1.setFullScreen(False)
        # video_2
        if (watched == self.ui.videoWidget_2):
            if (event.type() == QEvent.MouseButtonPress and event.buttons() == Qt.LeftButton):
                if (self.player2.playbackState() == QMediaPlayer.PlaybackState.PlayingState):
                    self.player2.pause()
                else:
                    self.player2.play()
            elif (event.type() == QEvent.MouseButtonDblClick):
                if (self.ui.videoWidget_2.isFullScreen()):
                    self.ui.videoWidget_2.setFullScreen(False)
                else:
                    self.ui.videoWidget_2.setFullScreen(True)
            elif (event.type() == QEvent.Type.KeyPress):
                if (event.key() == Qt.Key_Escape):
                    if (self.ui.videoWidget_2.isFullScreen()):
                        self.ui.videoWidget_2.setFullScreen(False)
        # video_3
        if (watched == self.ui.videoWidget_3):
            if (event.type() == QEvent.MouseButtonPress and event.buttons() == Qt.LeftButton):
                if (self.player3.playbackState() == QMediaPlayer.PlaybackState.PlayingState):
                    self.player3.pause()
                else:
                    self.player3.play()
            elif (event.type() == QEvent.MouseButtonDblClick):
                if (self.ui.videoWidget_3.isFullScreen()):
                    self.ui.videoWidget_3.setFullScreen(False)
                else:
                    self.ui.videoWidget_3.setFullScreen(True)
            elif (event.type() == QEvent.Type.KeyPress):
                if (event.key() == Qt.Key_Escape):
                    if (self.ui.videoWidget_3.isFullScreen()):
                        self.ui.videoWidget_3.setFullScreen(False)
        # video_4
        if (watched == self.ui.videoWidget_4):
            if (event.type() == QEvent.MouseButtonPress and event.buttons() == Qt.LeftButton):
                if (self.player4.playbackState() == QMediaPlayer.PlaybackState.PlayingState):
                    self.player4.pause()
                else:
                    self.player4.play()
            elif (event.type() == QEvent.MouseButtonDblClick):
                if (self.ui.videoWidget_4.isFullScreen()):
                    self.ui.videoWidget_4.setFullScreen(False)
                else:
                    self.ui.videoWidget_4.setFullScreen(True)
            elif (event.type() == QEvent.Type.KeyPress):
                if (event.key() == Qt.Key_Escape):
                    if (self.ui.videoWidget_4.isFullScreen()):
                        self.ui.videoWidget_4.setFullScreen(False)  
        return super().eventFilter(watched, event)
    
    # Timer to control singel and double click #TODO
    # def onTimeout(self):
    #     if self.timer.isActive():
    #         self.timer.stop()
    #     pass

    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        # self.dragPos = event.globalPos()
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())



