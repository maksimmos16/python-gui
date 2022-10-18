import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetSize(300,300)
        panel = wx.Panel(self)

        self.Centre()
        gs = wx.GridSizer(4, 4, 5, 5)

        for i in range(1, 17):
            btn = "Btn" + str(i)
            gs.Add(wx.Button(panel, label=btn), flag=wx.ALL|wx.EXPAND, border=10)

        panel.SetSizer(gs)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()