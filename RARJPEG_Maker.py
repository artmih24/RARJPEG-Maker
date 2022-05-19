from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from RARJPEG_Maker_Window import Ui_MainWindow
from RARJPEG_Maker_about import about_window
import RARJPEG_Maker_Icon as icon
from RARJPEG_Maker_TableWidget import *
import sys, os, subprocess


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.icon_data = icon.Get_icon(icon.icon_str)
        self.setWindowIcon(self.icon_data)
        self.setGeometry(750, 400, 441, 195)
        self.setMinimumSize(441, 195)
        self.setStyleSheet('QMainWindow {background-color: white;}')
        self.ui.pushButton_3.setEnabled(False)
        self.ui.label_2.setFixedHeight(16)
        self.ui.label_3.setStyleSheet('QLabel {color: #AA0000}')
        self.ui.tableWidget = MyTableWidget(self.ui.tableWidget)
        self.ui.gridLayout.addWidget(self.ui.tableWidget, 1, 0, 3, 1)
        self.ui.tableWidget.setFixedHeight(70)
        self.ui.tableWidget.horizontalScrollBar().setDisabled(True)
        self.ui.tableWidget.horizontalScrollBar().setVisible(False)
        self.ui.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.about_window = about_window()
        m = self.menuBar().addMenu("Меню")
        a = m.addAction("О программе")
        a.triggered.connect(self.aboutClicked)
        self.ui.pushButton.clicked.connect(self.SelectImageButtonClicked)
        self.ui.pushButton_2.clicked.connect(self.SelectArchiveButtonClicked)
        self.ui.pushButton_3.clicked.connect(self.CreateRARJPEGButtonClicked)
        self.ui.tableWidget.updated_image.connect(self.ImageUpdated)
        self.ui.tableWidget.updated_archive.connect(self.ArchiveUpdated)

        self.WidthIfImage = 85
        self.WidthIfPDF = 87
        self.WidthIfArchive = 43
        self.ImageExistsFlag = False
        self.ArchiveExistsFlag = False

    def CreateRARJPEGButtonClicked(self):
        s = QMessageBox()
        s.setWindowIcon(self.icon_data)
        #InputImageName = self.ui.lineEdit.text()
        InputImageName = self.ui.tableWidget.item(0, 1).text()
        #InputArchiveName = self.ui.lineEdit_2.text()
        InputArchiveName = self.ui.tableWidget.item(1, 1).text()
        PreRARJPEGName = '.'.join(['.'.join(InputImageName.split('.')[:-1]), InputArchiveName.split('.')[-1], InputImageName.split('.')[-1]])
        if InputImageName.split('.')[-1] == 'pdf':
            RARJPEGName = QFileDialog.getSaveFileName(self, "Сохранить файл", PreRARJPEGName, f"Документ-архив (*.{'.'.join([InputArchiveName.split('.')[-1], InputImageName.split('.')[-1]])})")[0]
        else:
            RARJPEGName = QFileDialog.getSaveFileName(self, "Сохранить файл", PreRARJPEGName, f"Изображение-архив (*.{'.'.join([InputArchiveName.split('.')[-1], InputImageName.split('.')[-1]])})")[0]
        CmdInputImageName = InputImageName.replace('/', '\\')
        CmdInputArchiveName = InputArchiveName.replace('/', '\\')
        CmdRARJPEGName = RARJPEGName.replace('/', '\\')
        try:
            subprocess.call(f'copy /b "{CmdInputImageName}"+"{CmdInputArchiveName}" "{CmdRARJPEGName}"', shell=True)
        except:
            if os.path.exists(InputImageName) and os.path.exists(InputArchiveName):
                QMessageBox.critical(s, "RARJPEG Maker", f"Один из файлов {InputImageName} и {InputArchiveName} поврежден.\nОперация прервана", QMessageBox.Ok)
            elif os.path.exists(InputImageName) and not os.path.exists(InputArchiveName):
                QMessageBox.critical(s, "RARJPEG Maker", f"Файл {InputArchiveName} не существует.\nОперация прервана", QMessageBox.Ok)
            elif not os.path.exists(InputImageName) and os.path.exists(InputArchiveName):
                QMessageBox.critical(s, "RARJPEG Maker", f"Файл {InputImageName} не существует.\nОперация прервана", QMessageBox.Ok)
            elif not os.path.exists(InputImageName) and not os.path.exists(InputArchiveName):
                QMessageBox.critical(s, "RARJPEG Maker", f"Файлы {InputImageName} и {InputArchiveName} не существуют.\nОперация прервана", QMessageBox.Ok)
            else:
                QMessageBox.critical(s, "RARJPEG Maker", f"Файлы {InputImageName} и {InputArchiveName} не существуют.\nОперация прервана", QMessageBox.Ok)
        else:
            QMessageBox.information(s, "RARJPEG Maker", f"Файл {RARJPEGName} успешно создан!", QMessageBox.Ok)

    def SelectImageButtonClicked(self):
        InputFilesFormats = ["Все типы изображений (*.jpg *.jpeg *.jpe *.jfif *.png *.bmp *.gif)",
                             "Изображение JPEG (*.jpg *.jpeg *.jpe *.jfif)",
                             "Изображение PNG (*.png)",
                             "Изображение BMP (*.bmp)",
                             "Изображение GIF (*.gif)",
                             "Документ PDF (*.pdf)"]
        InputFilesFormatsStr = ';; '.join(InputFilesFormats)
        InputImageName = QFileDialog.getOpenFileName(self, "Выбрать изображение", "/home", InputFilesFormatsStr)[0]
        if InputImageName != '':
            InputFileExtension = InputImageName.split('.')[-1]
            if InputFileExtension == 'pdf':
                self.ui.tableWidget.horizontalHeader().resizeSection(0, self.WidthIfPDF)
                self.ui.tableWidget.setItem(0, 0, QTableWidgetItem('Документ PDF:'))
            else:
                self.ui.tableWidget.horizontalHeader().resizeSection(0, self.WidthIfImage)
                self.ui.tableWidget.setItem(0, 0, QTableWidgetItem('Изображение:'))
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(InputImageName))
            self.ImageExistsFlag = True
        else:
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(''))
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(''))
            self.ImageExistsFlag = False
            if self.ArchiveExistsFlag:
                self.ui.tableWidget.horizontalHeader().resizeSection(0, self.WidthIfArchive)
        self.ui.pushButton_3.setEnabled(self.ImageExistsFlag and self.ArchiveExistsFlag)
        # if self.ImageExistsFlag and self.ArchiveExistsFlag:
        #     self.ui.pushButton_3.setEnabled(True)
        # else:
        #     self.ui.pushButton_3.setEnabled(False)
        #self.ui.lineEdit.setText(InputImageName)
        #if self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() != "": self.ui.pushButton_3.setEnabled(True)
        #else: self.ui.pushButton_3.setEnabled(False)

    def SelectArchiveButtonClicked(self):
        InputFilesFormats = ["Все типы архивов (*.rar *.7z *.zip)",
                             "Архив RAR (*.rar)",
                             "Архив 7-Zip (*.7z)",
                             "Архив ZIP (*.zip)"]
        InputFilesFormatsStr = ';; '.join(InputFilesFormats)
        InputArchiveName = QFileDialog.getOpenFileName(self, "Выбрать архив", "/home", InputFilesFormatsStr)[0]
        if InputArchiveName != '':
            self.ui.tableWidget.setItem(1, 0, QTableWidgetItem('Архив:'))
            self.ui.tableWidget.setItem(1, 1, QTableWidgetItem(InputArchiveName))
            self.ArchiveExistsFlag = True
            if not self.ImageExistsFlag:
                self.ui.tableWidget.horizontalHeader().resizeSection(0, self.WidthIfArchive)
        else:
            self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(''))
            self.ui.tableWidget.setItem(1, 1, QTableWidgetItem(''))
        self.ui.pushButton_3.setEnabled(self.ImageExistsFlag and self.ArchiveExistsFlag)
        # if self.ImageExistsFlag and self.ArchiveExistsFlag:
        #     self.ui.pushButton_3.setEnabled(True)
        # else:
        #     self.ui.pushButton_3.setEnabled(False)
        #self.ui.lineEdit_2.setText(InputArchiveName)
        #if self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() != "": self.ui.pushButton_3.setEnabled(True)
        #else: self.ui.pushButton_3.setEnabled(False)

    def ImageUpdated(self):
        self.ImageExistsFlag = True
        if not self.ArchiveExistsFlag:
            self.ui.tableWidget.horizontalHeader().resizeSection(0, self.WidthIfImage)
        self.ui.pushButton_3.setEnabled(self.ImageExistsFlag and self.ArchiveExistsFlag)
        # if self.ImageExistsFlag and self.ArchiveExistsFlag:
        #     self.ui.pushButton_3.setEnabled(True)
        # else:
        #     self.ui.pushButton_3.setEnabled(False)

    def ArchiveUpdated(self):
        self.ArchiveExistsFlag = True
        if not self.ImageExistsFlag:
            self.ui.tableWidget.horizontalHeader().resizeSection(0, self.WidthIfArchive)
        self.ui.pushButton_3.setEnabled(self.ImageExistsFlag and self.ArchiveExistsFlag)
        # if self.ImageExistsFlag and self.ArchiveExistsFlag:
        #     self.ui.pushButton_3.setEnabled(True)
        # else:
        #     self.ui.pushButton_3.setEnabled(False)

    def aboutClicked(self):
        self.about_window.show()
        """
        q = QMessageBox()
        q.setWindowIcon(self.icon_data)
        q.setStyleSheet('QMessageBox {background-color: white; font-family: Consolas; font-size: 13px;}')
        # q.setStyleSheet('QMessageBox {background-color: white; font-family: Consolas;}')
        QMessageBox.about(q, "О программе", '''RARJPEG Maker 1.2\n
Автор программы:\n
   ____             _             _ _     ____  _  _
  / __ \  __ _ _ __| |_ _ __ ___ (_) |__ |___ \| || |
 / / _` |/ _` | '__| __| '_ ` _ \| | '_ \  __) | || |_
| | (_| | (_| | |  | |_| | | | | | | | | |/ __/|__   _|
 \ \__,_|\__,_|_|   \__|_| |_| |_|_|_| |_|_____|  |_|
  \____/''')
"""

    def closeEvent(self, e) -> None:
        self.about_window.close()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())