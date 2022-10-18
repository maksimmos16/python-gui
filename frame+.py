import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetSize(300,200)
        self.panel = wx.Panel(self)
        label = wx.StaticText(self.panel, label="Hello World", pos=(100, 50))

        self.fileMenu = wx.Menu()
        self.fileMenu.Append(wx.ID_NEW, '&New')
        fileItem = self.fileMenu.Append(wx.ID_EXIT, '&Quit\tCtrl+Q', 'Quit application')
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
        self.panel.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

    def OnRightDown(self, e):
        self.PopupMenu(self.fileMenu)
        print('click')

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()