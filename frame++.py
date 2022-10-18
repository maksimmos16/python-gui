import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetSize(300,200)
        self.panel = wx.Panel(self)
        self.label = wx.StaticText(self.panel, label="Hello World", pos=(100, 50))
        self.Centre()

        toolbar = self.CreateToolBar()
        qtool = toolbar.AddTool(101, 'Quit', wx.Bitmap("q.png") )
        toolbar.AddTool(102, 'New', wx.Bitmap("n.png"))
        toolbar.AddRadioTool(222, 'Right',wx.Bitmap("r.png"))
        toolbar.AddRadioTool(333, 'Center', wx.Bitmap("c.png"))
        toolbar.AddRadioTool(444, 'Justify',wx.Bitmap("j.png"))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnTool, qtool)

    def OnTool(self, e):
        self.label.SetLabel(str(e.GetId()))



def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()