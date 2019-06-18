import configparser
import os
import requests
from zipfile import ZipFile
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.textinput import TextInput
from keyboard_listener import KeyboardListener
from kivy.uix.button import Button
from mopopup import MOPopup


class DownloadableCharactersScreen(Popup):
    main_window = ObjectProperty(None)
    scroll_lay = ObjectProperty(None)
    download_all_button = ObjectProperty(None)
    dlc_window = ObjectProperty(None)
    download_from_catalogue_button = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DownloadableCharactersScreen, self).__init__(**kwargs)
        self.fill_popup()

    def fill_popup(self):
        self.download_all_button.bind(on_press=lambda x: self.download_all())
        dlc_list = App.get_running_app().get_main_screen().character_list_for_dlc
        for text in dlc_list:
            arguments = text.split('#', 1)
            char = arguments[0]
            link = arguments[1]
            button = Button(text=char, size_hint_y=None, height=50, width=self.width)
            button.bind(on_press=lambda x: self.download_character(char, link))
            self.dlc_window.add_widget(button)

    def download_character(self, char_name, link):
        try:
            if link.find("drive.google.com") == -1: #checks for google drive link
                try:
                    direct_link = link
                except Exception as e:
                    print("Error: " + e)
            else:
                try:
                    file_id = link.split('id=')
                    try:
                        direct_link = 'https://drive.google.com/uc?export=download&id=' + file_id[1]
                    except IndexError:
                        dlc_list = App.get_running_app().get_main_screen().character_list_for_dlc
                        char = char_name + '#' + link
                        dlc_list.remove(char)
                        self.dismiss()
                        temp_pop = MOPopup("Error downloading", "Can't download " + char_name, "OK")
                        temp_pop.open()
                        return
                except Exception as e:
                    print("Error: " + e)
            path = 'characters/' + char_name + '.zip'
            r = requests.get(direct_link, allow_redirects=True)
            open(path, 'wb').write(r.content)
            with ZipFile(path) as zipArch:
                zipArch.extractall("characters")
            os.remove(path)
            dlc_list = App.get_running_app().get_main_screen().character_list_for_dlc
            char = char_name + '#' + link
            dlc_list.remove(char)
            self.overwrite_ini(char_name, link)
            KeyboardListener.refresh_characters()
            self.dismiss(animation=False)
            self.clean(char_name)
        except KeyError:
            self.dismiss()
            temp_pop = MOPopup("Error downloading", "Can't download " + char_name, "OK")
            temp_pop.open()
        except Exception as e:
            print("Error 2: " + e)

    def download_all(self):
        dlc_list = App.get_running_app().get_main_screen().character_list_for_dlc
        for text in dlc_list:
            arguments = text.split('#', 1)
            char = arguments[0]
            shared_link = arguments[1]
            try:
                if shared_link.find("drive.google.com") == -1:  # checks for google drive shared_link
                    try:
                        direct_link = shared_link
                    except Exception as e:
                        print("Error: " + e)
                else:
                    try:
                        file_id = shared_link.split('id=')
                        try:
                            direct_link = 'https://drive.google.com/uc?export=download&id=' + file_id[1]
                        except IndexError:
                            dlc_list = App.get_running_app().get_main_screen().character_list_for_dlc
                            char_link = char + '#' + shared_link
                            dlc_list.remove(char)
                            self.dismiss()
                            temp_pop = MOPopup("Error downloading", "Can't download " + char, "OK")
                            temp_pop.open()
                            return
                    except Exception as e:
                        print("Error: " + e)
                path = 'characters/' + char + '.zip'
                r = requests.get(direct_link, allow_redirects=True)
                open(path, 'wb').write(r.content)
                with ZipFile(path) as zipArch:
                    zipArch.extractall("characters")
                os.remove(path)
                self.clean(arguments[0])
                char = arguments[0] + '#' + arguments[1]
                self.overwrite_ini(arguments[0], arguments[1])
            except KeyError:
                dlc_list = App.get_running_app().get_main_screen().character_list_for_dlc
                char_link = char + '#' + shared_link
                dlc_list.remove(char_link)
                temp_pop = MOPopup("Error downloading", "Can't download " + char, "OK")
                temp_pop.open()
        App.get_running_app().get_main_screen().character_list_for_dlc = []
        KeyboardListener.refresh_characters()
        self.dismiss(animation=False)

    def clean(self, char_name):
        path = "characters/{0}/".format(char_name)
        for fname in os.listdir(path):
            fname = fname.lower()
            if not fname.endswith(".png") and not fname.endswith(".atlas") and not fname.endswith(".ini"):
                os.remove(path + fname)

    def overwrite_ini(self, char_name, link):
        config = configparser.ConfigParser()
        path = "characters/{0}/".format(char_name)
        config.read(path + "settings.ini")
        char = config['character']
        char['download'] = link
        with open(path + "settings.ini", 'w') as configfile:
            config.write(configfile)

    def download_from_catalogue(self):
        return
