from DownloaderGUI import DownloaderMainWindow
from PyQt5 import QtWidgets
import sys

def main():
    print('Initializing GUI.....')
    app = QtWidgets.QApplication(sys.argv)
    window = DownloaderMainWindow()
    window.show()
    sys.exit(app.exec())




if __name__ == '__main__':
    main()