import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetSize(300,200)
        panel = wx.Panel(self)
        label = wx.StaticText(panel, label="Hello World", pos=(100, 50))
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.AppendSeparator()
        imp = wx.Menu()
        sub=imp.Append(wx.ID_ANY, 'Import newsfeed list...', 'Import',kind=wx.ITEM_CHECK)
        fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)
        imp.Check(sub.GetId(), True)
        fileItem = fileMenu.Append(wx.ID_EXIT, '&Quit\tCtrl+Q', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()