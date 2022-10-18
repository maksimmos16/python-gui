import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetSize(300,300)
        panel = wx.Panel(self)
        label1 = wx.StaticText(panel, label="Label1")
        label2 = wx.StaticText(panel, label="Label2")
        label3 = wx.StaticText(panel, label="Label3")
        self.Centre()
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(label1, proportion=0, flag=wx.RIGHT, border=8)
        hbox.Add(label2, proportion=1, flag=wx.LEFT|wx.TOP, border=50)
        hbox.Add(label3, proportion=2, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
        panel.SetSizer(hbox)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()