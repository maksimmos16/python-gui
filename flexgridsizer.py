import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetSize(300,300)
        panel = wx.Panel(self)

        self.Centre()
        fgs = wx.FlexGridSizer(3, 2, 10,10)

        for i in range(1, 7):
            btn = "Btn" + str(i)
            fgs.Add(wx.Button(panel, label=btn), flag=wx.ALL|wx.EXPAND, border=10)

        fgs.AddGrowableCol(1, 1)
        fgs.AddGrowableRow(2, 1)
        panel.SetSizer(fgs)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()