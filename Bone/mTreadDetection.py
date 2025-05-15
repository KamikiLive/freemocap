# -*- coding: utf-8 -*-
# 功能：图片识别

import threading
from mBigDirDetect import bigdirdetect

class mDirDetection(threading.Thread):
    def __init__(self, notify):
        super().__init__()
        self.__notify = notify
        # Has the current thread been marked as stopped?

    def start_thr(self, sourcedir,  save_dir):
        self.stop_thr()
        self.__sourcedir = sourcedir
        self.__save_dir = save_dir
        self.start()

    def stop_thr(self):
        if self.is_alive():
            self.join()

    def run(self):

        bigdirdetect(self.__sourcedir,self.__save_dir)
        print('Completed')



