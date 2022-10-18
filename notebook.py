import wx
import wx.lib.iewin


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetSize(300,300)
        self.Centre()

        nb = wx.Notebook(self)
        panel1 = wx.Panel(nb)
        panel2 = wx.Panel(nb)
        nb.AddPage(panel1, "Page1")
        nb.AddPage(panel2, "Page2")
        txt1 = wx.StaticText(panel1, -1, style=wx.ALIGN_CENTER)
        txt1.SetLabel("Page1")
        txt2 = wx.StaticText(panel2, -1, style=wx.ALIGN_CENTER)
        txt2.SetLabel("Page2")

def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()