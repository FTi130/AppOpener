# -*- coding:utf -8 -*-
import wx
import os
import sys

"""
В конфигурационном файл должен лежать путь/имя приложения.
Каждое в новой строке без пробелов.
Проверить работоспособность пути/приложения можно поместив это в окно,
появляющееся после нажатися Win+R.
Приятного использования
"""

text_file = open("config.txt", "r")
lines = text_file.readlines()
global data_list
data_list = [word.strip() for word in lines]
text_file.close()


class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Binding Multiple Widgets")
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour("Dark Grey")

        sizer = wx.BoxSizer(wx.VERTICAL)

        app_buttons = []
        for app in data_list:
            if ":" in app or ("\\" in app):
                app_name = app.split('\\')[-1]
                base_name, ext = os.path.splitext(app_name)
                app_name = base_name
            else:
                app_name = app
            print "Path: ", app
            print "Name: ", app_name, "\n---"
            app_buttons.append(wx.Button(panel, label=str(app_name), name=str(app)))

        for button in app_buttons:
            self.buildButtons(button, sizer)

        panel.SetSizer(sizer)
        panel.Fit()

    def buildButtons(self, btn, sizer):
        """"""
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        # Adjust window to buttons
        sizer.Add(btn, flag=wx.EXPAND)

    def onButton(self, event):
        """
        Данный метод запускается, когда нажат соответствующая кнопка.
        """
        button = event.GetEventObject()
        button_id = event.GetId()
        button_by_id = self.FindWindowById(button_id)
        # Opening an application
        os.popen(str(button.GetName()))


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Fit() # Adjusting
    frame.Show()
    app.MainLoop()
