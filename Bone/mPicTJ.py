
import mQueXianUI
import mTreadDetection

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog,  QFileDialog
import mBigDirDetect
import os
import glob
from PIL import Image
import numpy as np
errPicsList=[]
rawPicsList=[]
picID=0

class picTJ(QDialog):
    def __init__(self):
        super().__init__()
        self.__ui =  mQueXianUI.Ui_MainWindow()
        self.__ui.setupUi(self)
        mBigDirDetect.init_result_back(self)

        ##### Function: Start recognition #####
        self.__ui.pushButton.clicked.connect(self.select_onepic)
        self.__ui.pushButton_2.clicked.connect(self.thread_detection)


    def  pics_show3(self,img1):

        height, width, depth = img1.shape
        img2 = QImage(img1.data, width, height, width * depth, QImage.Format_RGB888)
        pix = QPixmap.fromImage(img2)
        pix2 = pix.scaled(self.__ui.label_3.width(),self.__ui.label_3.height())
        self.__ui.label_3.setPixmap(pix2)

    def  pics_show(self,img1):
        height, width, depth = img1.shape
        img2 = QImage(img1.data, width, height, width * depth, QImage.Format_RGB888)
        pix = QPixmap.fromImage(img2)
        pix2 = pix.scaled(self.__ui.label.width(),self.__ui.label.height())
        self.__ui.label.setPixmap(pix2)

    def result_back_detect(self, results_output):

        #Original image
        img1 = results_output[0]
        self.pics_show3(img1)

        #Detection image
        img2 = results_output[1]
        self.pics_show(img2)

    # Select video file
    def select_onepic(self):
        fname = QFileDialog.getOpenFileName(self, 'Select video file', "*.mp4")
        if fname[0]:
            self.__ui.lineEdit.setText(fname[0])



    def thread_detection(self):

        sourcept= self.__ui.lineEdit.text()  #Source file path
        save_dir = 'DetectResults'
        self.__thrCal_realtimedetection = mTreadDetection.mDirDetection(self)
        self.__thrCal_realtimedetection.start_thr(sourcept,  save_dir)










