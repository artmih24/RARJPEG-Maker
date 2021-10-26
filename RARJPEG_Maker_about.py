from PyQt5 import QtWidgets
from RARJPEG_Maker_about_window import Ui_AboutWindow
import sys, webbrowser
import RARJPEG_Maker_Icon as icon
import RARJPEG_Maker_Big_Icon as big_icon
import VK_logo, Telegram_logo, Instagram_Logo, GitHub_Logo, Mail_Logo


class about_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(about_window, self).__init__()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)
        # настройка значка окна
        self.icon_data = icon.Get_icon(icon.icon_str)
        self.setWindowIcon(self.icon_data)
        self.big_icon_data = big_icon.Get_big_icon(big_icon.big_icon_str).scaled(100, 100)
        self.ui.label_10.setPixmap(self.big_icon_data)
        # настройка свойств формы
        self.setWindowTitle('RARJPEG Maker - О программе')
        self.setFixedSize(582, 283)
        self.statusBar().setSizeGripEnabled(False)
        self.setStyleSheet('QMainWindow {background-color: white;}')
        # настройка ссылок
        self.vk_logo_data = VK_logo.Get_vk_logo(VK_logo.vk_logo_str).scaled(40, 40)
        self.telegram_logo_data = Telegram_logo.Get_telegram_logo(Telegram_logo.telegram_logo_str).scaled(40, 40)
        self.instagram_logo_data = Instagram_Logo.Get_instagram_logo(Instagram_Logo.instagram_logo_str).scaled(40, 40)
        self.github_logo_data = GitHub_Logo.Get_github_logo(GitHub_Logo.github_logo_str).scaled(40, 40)
        self.mail_logo_data = Mail_Logo.Get_mail_logo(Mail_Logo.mail_logo_str).scaled(40, 40)
        self.ui.label_5.setPixmap(self.vk_logo_data)
        self.ui.label_6.setPixmap(self.telegram_logo_data)
        self.ui.label_7.setPixmap(self.instagram_logo_data)
        self.ui.label_8.setPixmap(self.github_logo_data)
        self.ui.label_9.setPixmap(self.mail_logo_data)
        # настройка событий элементов формы
        self.ui.label_5.installEventFilter(self)
        self.ui.label_6.installEventFilter(self)
        self.ui.label_7.installEventFilter(self)
        self.ui.label_8.installEventFilter(self)
        self.ui.label_9.installEventFilter(self)


    def eventFilter(self, obj, e):
        if obj == self.ui.label_5 and e.type() == 2:
            webbrowser.open_new_tab('https://vk.com/artmih24')
            print('VK: @artmih24')
        elif obj == self.ui.label_6 and e.type() == 2:
            webbrowser.open_new_tab('https://t.me/artmih24')
            print('Telegram: @artmih24')
        elif obj == self.ui.label_7 and e.type() == 2:
            webbrowser.open_new_tab('https://www.instagram.com/artmih24/')
            print('Instagram: @artmih24')
        elif obj == self.ui.label_8 and e.type() == 2:
            webbrowser.open_new_tab('https://github.com/artmih24')
            print('GitHub: @artmih24')
        elif obj == self.ui.label_9 and e.type() == 2:
            webbrowser.open_new_tab('mailto:artmih24@vk.com')
            print('E-Mail: artmih24@vk.com')
        return super(about_window, self).eventFilter(obj,e)

if __name__ == '__main__':
    app_about = QtWidgets.QApplication([])
    application_about = about_window()
    application_about.show()

    sys.exit(app_about.exec())