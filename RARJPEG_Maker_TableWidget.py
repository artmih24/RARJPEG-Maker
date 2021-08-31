import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyTableWidget(QTableWidget):
    updated = pyqtSignal()
    updated_image = pyqtSignal()
    updated_archive = pyqtSignal()
    def __init__(self, parent):
        super(MyTableWidget, self).__init__(parent)
        self.setRowCount(2)
        self.setColumnCount(2)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
        self.setHorizontalHeaderItem(0, item)
        self.setColumnWidth(0, 1000000)
        self.setAutoScroll(False)
        self.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.setShowGrid(False)
        self.setWordWrap(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setMinimumSectionSize(34)
        self.verticalHeader().setDefaultSectionSize(34)
        self.verticalHeader().setMaximumSectionSize(34)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.setStyleSheet('QTableWidget {selection-color: white; selection-background-color: #0078d7;} QHeaderView {background-color: white;}')
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.WidthIfImage = 85
        self.WidthIfPDF = 87
        self.WidthIfArchive = 43
        self.ImageExistsFlag = False
        self.ArchiveExistsFlag = False


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            flag = False
            if len(event.mimeData().urls()) == 1:
                if event.mimeData().urls()[0].path().split('.')[-1] == 'jpg' \
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'jpeg' \
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'jpe' \
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'jfif' \
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'png' \
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'bmp' \
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'gif' \
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'pdf' \
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'rar' \
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'zip' \
                        or event.mimeData().urls()[0].path().split('.')[-1] == '7z':
                    flag = True
            elif len(event.mimeData().urls()) == 2:
                if ((event.mimeData().urls()[0].path().split('.')[-1] == 'jpg'
                    or event.mimeData().urls()[0].path().split('.')[-1] == 'jpeg'
                    or event.mimeData().urls()[0].path().split('.')[-1] == 'jpe'
                    or event.mimeData().urls()[0].path().split('.')[-1] == 'jfif'
                    or event.mimeData().urls()[0].path().split('.')[-1] == 'png'
                    or event.mimeData().urls()[0].path().split('.')[-1] == 'bmp'
                    or event.mimeData().urls()[0].path().split('.')[-1] == 'gif'
                    or event.mimeData().urls()[0].path().split('.')[-1] == 'pdf')
                    and (event.mimeData().urls()[1].path().split('.')[-1] == 'rar'
                         or event.mimeData().urls()[1].path().split('.')[-1] == '7z'
                         or event.mimeData().urls()[1].path().split('.')[-1] == 'zip')) \
                    or ((event.mimeData().urls()[0].path().split('.')[-1] == 'rar'
                         or event.mimeData().urls()[0].path().split('.')[-1] == '7z'
                         or event.mimeData().urls()[0].path().split('.')[-1] == 'zip')
                        and (event.mimeData().urls()[1].path().split('.')[-1] == 'jpg'
                             or event.mimeData().urls()[1].path().split('.')[-1] == 'jpeg'
                             or event.mimeData().urls()[1].path().split('.')[-1] == 'jpe'
                             or event.mimeData().urls()[1].path().split('.')[-1] == 'jfif'
                             or event.mimeData().urls()[1].path().split('.')[-1] == 'png'
                             or event.mimeData().urls()[1].path().split('.')[-1] == 'bmp'
                             or event.mimeData().urls()[1].path().split('.')[-1] == 'gif'
                             or event.mimeData().urls()[1].path().split('.')[-1] == 'pdf')):
                    flag = True
            if flag == True:
                self.setStyleSheet('QTableWidget {background-color: #DDFFDD;} QHeaderView {background-color: white;}')
                event.acceptProposedAction()
            else:
                #self.setStyleSheet('QTableWidget {background-color: #FFDDDD;}  QHeaderView {background-color: white;}')
                super(MyTableWidget, self).dragEnterEvent(event)
        else:
            #self.setStyleSheet('QTableWidget {background-color: #FFDDDD;}  QHeaderView {background-color: white;}')
            pass
            #super(MyTableWidget, self).dragEnterEvent(event)

    def dragLeaveEvent(self, event):
        self.setStyleSheet('QTableWidget {selection-color: white; selection-background-color: #0078d7;} QHeaderView {background-color: white;}')
        super(MyTableWidget, self).dragLeaveEvent(event)

    def dragMoveEvent(self, event):
        super(MyTableWidget, self).dragMoveEvent(event)

    def dropEvent(self, event):
        self.setStyleSheet('QTableWidget {selection-color: white; selection-background-color: #0078d7;} QHeaderView {background-color: white;}')
        if event.mimeData().hasUrls():
            if len(event.mimeData().urls()) == 2:
                if ((event.mimeData().urls()[0].path().split('.')[-1] == 'jpg'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'jpeg'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'jpe'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'jfif'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'png'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'bmp'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'gif'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'pdf')
                        and (event.mimeData().urls()[1].path().split('.')[-1] == 'rar'
                             or event.mimeData().urls()[1].path().split('.')[-1] == '7z'
                             or event.mimeData().urls()[1].path().split('.')[-1] == 'zip')):
                    if (event.mimeData().urls()[0].path().split('.')[-1] == 'jpg'
                            or event.mimeData().urls()[0].path().split('.')[-1] == 'jpeg'
                            or event.mimeData().urls()[0].path().split('.')[-1] == 'jpe'
                            or event.mimeData().urls()[0].path().split('.')[-1] == 'jfif'
                            or event.mimeData().urls()[0].path().split('.')[-1] == 'png'
                            or event.mimeData().urls()[0].path().split('.')[-1] == 'bmp'
                            or event.mimeData().urls()[0].path().split('.')[-1] == 'gif'):
                        self.setItem(0, 0, QTableWidgetItem('Изображение:'))
                        self.horizontalHeader().resizeSection(0, self.WidthIfImage)
                    elif event.mimeData().urls()[0].path().split('.')[-1] == 'pdf':
                        self.setItem(0, 0, QTableWidgetItem('Документ PDF:'))
                        self.horizontalHeader().resizeSection(0, self.WidthIfPDF)
                    self.setItem(1, 0, QTableWidgetItem('Архив:'))
                    self.setItem(0, 1, QTableWidgetItem(event.mimeData().urls()[0].path()[1:]))
                    self.setItem(1, 1, QTableWidgetItem(event.mimeData().urls()[1].path()[1:]))
                    self.ImageExistsFlag = True
                    self.ArchiveExistsFlag = True
                    self.updated_image.emit()
                    self.updated_archive.emit()
                elif ((event.mimeData().urls()[1].path().split('.')[-1] == 'jpg'
                     or event.mimeData().urls()[1].path().split('.')[-1] == 'jpeg'
                     or event.mimeData().urls()[1].path().split('.')[-1] == 'jpe'
                     or event.mimeData().urls()[1].path().split('.')[-1] == 'jfif'
                     or event.mimeData().urls()[1].path().split('.')[-1] == 'png'
                     or event.mimeData().urls()[1].path().split('.')[-1] == 'bmp'
                     or event.mimeData().urls()[1].path().split('.')[-1] == 'gif'
                     or event.mimeData().urls()[1].path().split('.')[-1] == 'pdf')
                        and (event.mimeData().urls()[0].path().split('.')[-1] == 'rar'
                             or event.mimeData().urls()[0].path().split('.')[-1] == '7z'
                             or event.mimeData().urls()[0].path().split('.')[-1] == 'zip')):
                    if (event.mimeData().urls()[1].path().split('.')[-1] == 'jpg'
                            or event.mimeData().urls()[1].path().split('.')[-1] == 'jpeg'
                            or event.mimeData().urls()[1].path().split('.')[-1] == 'jpe'
                            or event.mimeData().urls()[1].path().split('.')[-1] == 'jfif'
                            or event.mimeData().urls()[1].path().split('.')[-1] == 'png'
                            or event.mimeData().urls()[1].path().split('.')[-1] == 'bmp'
                            or event.mimeData().urls()[1].path().split('.')[-1] == 'gif'):
                        self.setItem(0, 0, QTableWidgetItem('Изображение:'))
                        self.horizontalHeader().resizeSection(0, self.WidthIfImage)
                    elif event.mimeData().urls()[0].path().split('.')[-1] == 'pdf':
                        self.setItem(0, 0, QTableWidgetItem('Документ PDF:'))
                        self.horizontalHeader().resizeSection(0, self.WidthIfPDF)
                    self.setItem(1, 0, QTableWidgetItem('Архив:'))
                    self.setItem(0, 1, QTableWidgetItem(event.mimeData().urls()[1].path()[1:]))
                    self.setItem(1, 1, QTableWidgetItem(event.mimeData().urls()[0].path()[1:]))
                    self.ImageExistsFlag = True
                    self.ArchiveExistsFlag = True
                    self.updated_image.emit()
                    self.updated_archive.emit()
            elif len(event.mimeData().urls()) == 1:
                if (event.mimeData().urls()[0].path().split('.')[-1] == 'jpg'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'jpeg'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'jpe'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'jfif'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'png'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'bmp'
                     or event.mimeData().urls()[0].path().split('.')[-1] == 'gif'):
                    self.setItem(0, 0, QTableWidgetItem('Изображение:'))
                    self.horizontalHeader().resizeSection(0, self.WidthIfImage)
                    self.setItem(0, 1, QTableWidgetItem(event.mimeData().urls()[0].path()[1:]))
                    self.ImageExistsFlag = True
                    self.updated_image.emit()
                elif event.mimeData().urls()[0].path().split('.')[-1] == 'pdf':
                    self.setItem(0, 0, QTableWidgetItem('Документ PDF:'))
                    self.horizontalHeader().resizeSection(0, self.WidthIfPDF)
                    self.setItem(0, 1, QTableWidgetItem(event.mimeData().urls()[0].path()[1:]))
                    self.ImageExistsFlag = True
                    self.updated_image.emit()
                elif (event.mimeData().urls()[0].path().split('.')[-1] == 'rar'
                      or event.mimeData().urls()[0].path().split('.')[-1] == '7z'
                      or event.mimeData().urls()[0].path().split('.')[-1] == 'zip'):
                    self.setItem(1, 0, QTableWidgetItem('Архив:'))
                    self.setItem(1, 1, QTableWidgetItem(event.mimeData().urls()[0].path()[1:]))
                    self.ArchiveExistsFlag = True
                    self.updated_archive.emit()
                    #if self.ImageExistsFlag == False:
                        #self.horizontalHeader().resizeSection(0, self.WidthIfArchive)
            #self.setData(self.index(0, 1), Qt.AlignRight, Qt.TextAlignmentRole)
            event.acceptProposedAction()
            #self.selectRow(0)
            #self.clearSelection()
            #FilesToJoin_Names = []
            #for i in range(self.rowCount()):
            #    FilesToJoin_Names.append(self.item(i, 0).text())
            #print(datetime.datetime.now(), "| Выбраны файлы", ', '.join(FilesToJoin_Names))
            self.updated.emit()
        else:
            pass
            #super(MyTableWidget,self).dropEvent(event)