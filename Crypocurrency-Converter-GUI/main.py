from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from guiVersion import Ui_guiVersion
import json
import requests


class guiVersion(QMainWindow, Ui_guiVersion):
    def __init__(self, *args, **kwargs):
        super(guiVersion, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        # Vars
        self.new_label = '0'
        self.cur1 = 'BTC'
        self.cur2 = 'USD'
        self.result = ''
        # Connect buttons
        for n in range(0, 10):
            getattr(self,
                    'pushButton_n%s' % n).clicked.connect(self.digit_pressed)
        self.pushButton_n10.clicked.connect(self.decimal_point)
        self.pushButton_del.clicked.connect(self.del_digit)
        self.pushButton_convert.clicked.connect(self.convert_fun)
        self.comboBox.activated[str].connect(self.currencies1)
        self.comboBox_2.activated[str].connect(self.currencies2)

    def digit_pressed(self):
        button = self.sender()
        self.new_label = self.label_1.text() + button.text()
        if '.' in self.new_label:
            self.label_1.setText(str(self.new_label))
        else:
            self.label_1.setText(str(int(self.new_label)))

    def decimal_point(self):
        if '.' in self.label_1.text():
            pass
        else:
            self.label_1.setText(self.label_1.text() + '.')

    def del_digit(self):
        self.new_label = self.new_label[:-1]
        self.label_1.setText(self.new_label)

    def currencies1(self, item1):
        self.cur1 = item1
        # print(self.cur1)

    def currencies2(self, item2):
        self.cur2 = item2
        # print(self.cur2)

    # Live data from API
    def api(self, cur1, cur2):
        api_link = "https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms={}".format(
            cur1, cur2)
        resp = requests.get(api_link)
        # print(r.status_code)
        data = json.loads(resp.content)
        # print(data)
        var = data[self.cur1][self.cur2]
        return var

    def convert_fun(self):
        try:
            if len(self.new_label) == 0:
                self.label_1.setText('0')
                self.label_2.setText('0')
            if '.' in self.new_label:
                self.result = float(self.new_label) * \
                    self.api(self.cur1, self.cur2)
                self.result = round(self.result, 2)
                self.label_2.setText(str(self.result))
            else:
                self.result = int(self.new_label) * \
                    self.api(self.cur1, self.cur2)
                self.result = round(self.result, 2)
                self.label_2.setText(str(self.result))
        except (KeyError, ValueError):
            pass
        except requests.exceptions.ConnectionError:
            print('Please verify your internet connection!')


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("CryptoConverter")
    window = guiVersion()
    app.exec_()
