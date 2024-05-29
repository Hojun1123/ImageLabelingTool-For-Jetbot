import shutil
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QPainter, QPen, QImage, QPixmap, QBrush, QColor
from PySide6.QtGui import QStandardItemModel, QStandardItem, QAction, QIcon, QKeySequence
from mainUI import Ui_MainWindow, QMenuBar
import os
import uuid
import datetime as dt
import glob
import cv2
import numpy as np
import sys

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # basic code
        super().__init__()
        self.setupUi(self)

        # 멤버 선언
        self.imgHeight = 448
        self.imgWidth = 448

        self.imgFileList = []   # 이미지 파일 이름 목록
        self.imgPath = './images'   # 이미지 파일 경로
        self.imgFileLength = 0      # 이미지 총 개수
        self.imgFiles = []          # 실제 이미지 데이터(opencv)
        self.currType = 1           # 처음 보여지는 타입(기본 값) - 미사용
        self.currImageNumber = 1    # 처음 보여지는 이미지의 번호(기본 값)

        self.y = 0
        self.x = 0

        #self.currImg = None         # 현재 이미지(opencv)

        # ui
        self.frame = QLabel()  # 이벤트 처리와 이미지 변환을 위해 QLabel
        self.frame.setParent(self.imageArea)
        # list 수정 금지 설정
        self.listWidget.setEditTriggers(QAbstractItemView.EditTrigger(0))
        # save
        # menuBar 객체 선언
        self.menu = self.menuBar()
        self.menuFile = self.menu.addMenu("&File")
        self.saveAction = QAction("&Save", self)
        self.saveAction.setShortcut(QKeySequence("Ctrl+S"))
        self.saveAction.triggered.connect(self.saveLabelingData)
        self.menuFile.addAction(self.saveAction)

        #event
        self.imageArea.mousePressEvent = self.mouseClickEvent

        # main
        self.readImage()
        self.main()

    def readImage(self):
        # 이미지 파일 Load
        try:
            fileList = os.listdir(self.imgPath)  # glob : 경로명까지, listdir은 파일만
        except FileExistsError:
            print('[ERROR] FileExistsError')

        self.imgFileList = [_ for _ in fileList if _.endswith('.jpg')]
        self.imgFileLength = len(self.imgFileList)
        self.y = [-1 for i in range(self.imgFileLength)]  # 라벨링 값 y
        self.x = [-1 for i in range(self.imgFileLength)]  # 라벨링 값 x
        print(f'[INFO] File : {self.imgFileLength} 개')

        # opencv img load
        for name in self.imgFileList:
            self.imgFiles.append(cv2.imread('./' + self.imgPath + '/' + name))
        print('[INFO] Image Load Finished')

        # img size에 맞게 bar 범위 설정
        if self.imgFileLength > 0:
            self.bar_1.setRange(1, self.imgFileLength)
            self.spinBox.setRange(1, self.imgFileLength)
        # bar 2 미사용
        self.bar_2.setRange(1, 1)
        self.spinBox_2.setRange(1, 1)

        # 이미지 업데이트
        self.renderImage()

        # 읽어온 이미지 목록 리스트
        cnt = 1
        for name in self.imgFileList:
            row = '%d. %s' % (cnt, name)
            self.listWidget.addItem(row)
            cnt += 1

        for i in range(self.imgFileLength):
            self.listWidget.item(i).setBackground((QBrush(QColor(236,234,228))))
        self.listWidget.clicked.connect(self.clickItemOfList)

    def clickItemOfList(self, e):
        e.row()
        self.input1(e.row() + 1)

    def main(self):
        pass

    def mouseClickEvent(self, e):
        index = self.currImageNumber - 1
        x = self.x[index] = int(e.position().x())
        y = self.y[index] = int(e.position().y())
        x //= 2
        y //= 2
        print(f'{index + 1}img clicked: ({x}, {y})')

        # 리스트 텍스트 업데이트
        # 1. normalization, 0 ~ 223 -> 0 ~ 100
        # x = self.x[index] * 100 / self.imgWidth
        # y = self.y[index] * 100 / self.imgHeight
        # 2. mouse Pos
        name = self.imgFileList[index]
        row = '%d %s (x: %d, y: %d)' % (index + 1, name, x, y)
        self.listWidget.item(index).setText(row)
        self.listWidget.item(index).setBackground((QBrush(QColor(204, 226, 203))))
        #self.listWidget.item(index).setBackground((QBrush(QColor(236, 234, 228))))

        # 이미지 업데이트
        self.renderImage()


    def keyPressEvent(self, e):
        #print(f'[INFO] press {e.key()}')
        if e.key() == Qt.Key_W:
            self.bar_2.setValue(self.bar_2.value() + 1)
        elif e.key() == Qt.Key_S:
            self.bar_2.setValue(self.bar_2.value() - 1)
        elif e.key() == Qt.Key_D:
            self.bar_1.setValue(self.bar_1.value() + 1)
        elif e.key() == Qt.Key_A:
            self.bar_1.setValue(self.bar_1.value() - 1)

        '''
        elif e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_F:
            self.showFullScreen()
        elif e.key() == Qt.Key_N:
            self.showNormal()
        '''

    def renderImage(self):
        index = self.currImageNumber - 1
        x = self.x[index]
        y = self.y[index]

        # arrow 데이터가 있/없는지
        image = self.drawArrow(x, y) if x >= 0 and y >= 0 else self.imgFiles[index]
        # 이미지 사이즈 변경 (width * 2, height * 2)
        img = cv2.resize(image, dsize=(self.imgWidth, self.imgHeight))
        # cv2 -> image 변환
        convert = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format.Format_BGR888)
        # frame에 이미지 채우기
        self.frame.setPixmap(QPixmap.fromImage(convert))

        '''
        def changeImage(self):
            # 이미지 사이즈 변경 (width * 2, height * 2)
            img = cv2.resize(self.currImg, dsize=(448, 448))
            # cv2 -> image 변환
            convert = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format.Format_BGR888)
            # frame에 이미지 채우기
            self.frame.setPixmap(QPixmap.fromImage(convert))

            # bg-img
            self.currImg = np.copy(self.imgFiles[self.currImageNumber - 1])
            currImagePath = './images/' + self.imgFileList[self.currImageNumber - 1]
            bg = u"background-image: url(" + currImagePath + ");"
            self.imageArea.setStyleSheet(bg + "background-color: rgb(170, 255, 255);\n"
                                              "background-size: ;\n"
                                              "background-repeat: no-repeat;\n"
                                              "background-position: center;\n")
            '''

    def drawArrow(self, x, y):
        # 원본 이미지의 크기
        index = self.currImageNumber - 1
        height, width, channels = self.imgFiles[index].shape
        # print(height, width, channels)
        # 높이, 너비에 대해 축소 비율 계산
        heightReductionRatio = height / self.imgHeight
        widthReductionRatio = width / self.imgWidth

        # arrow의 너비, 반지름
        radius = thickness = min(width, height) // 100
        center = (width // 2, height)

        # 비율 보정
        x *= widthReductionRatio
        y *= heightReductionRatio

        # circle 의 인자는 정수
        x = int(x)
        y = int(y)
        tmpImg = np.copy(self.imgFiles[index])
        image = cv2.circle(tmpImg, (x, y), radius, (0, 255, 0), thickness)
        image = cv2.circle(image, center, radius, (0, 0, 255), thickness)
        return cv2.line(image, (x, y), center, (255, 0, 0), thickness)

    def getFilename(self, index):
        # index 0 ~ fileLength - 1
        # "xy_xValue_yValue_UUID.jpg"
        fileFormat = '.jpg'

        # normalization, 0 ~ 223 -> 0 ~ 100
        x = self.x[index] * 100 / self.imgWidth
        y = self.y[index] * 100 / self.imgHeight

        if x < 0 or y < 0:
            return 'nn'
        return 'xy_%03d_%03d_%s' % (x, y, uuid.uuid1()) + fileFormat


    def input1(self, value):
        self.bar_1.setValue(value)
        self.spinBox.setValue(value)
        self.currImageNumber = value
        self.renderImage()

    def input2(self, value):
        self.bar_2.setValue(value)
        self.spinBox_2.setValue(value)
        self.currImageNumber = value

    def saveLabelingData(self):
        print('save ...')
        if not os.path.isdir('./result'):
            print('[INFO] generate images folder')
            os.makedirs('./result')
        else:
            print('[ERROR] already exist folder')
            msg = QMessageBox()
            msg.setText("[ERROR] already exist folder")
            msg.exec()
            return

        cnt = 0
        for name in self.imgFileList:
            srcPath = self.imgPath
            dstPath = './result/'
            filename = self.getFilename(cnt)
            if filename == 'nn':
                print('[ERROR] labeling error')
                cnt += 1
                continue
            shutil.copy(srcPath + '/' + name, dstPath + filename)
            print(f'[INFO] {cnt}. {name} saved to {dstPath + filename}')
            cnt += 1


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()

