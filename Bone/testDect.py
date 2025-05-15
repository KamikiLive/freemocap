import sys
from PyQt5.QtWidgets import QApplication
import mPicTJ

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mPicTJ.picTJ()
    w.show()
    app.exec()




