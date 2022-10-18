import wx
import wx.lib.iewin


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetSize(600,300)
        self.Centre()
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        brush = wx.Brush("blue")
        dc.SetBackground(brush)
        dc.Clear()

        color = wx.Colour(255, 0, 0)
        b = wx.Brush(color)
        dc.SetBrush(b)
        dc.DrawCircle(300, 125, 50)
        dc.SetBrush(wx.Brush(wx.Colour(255, 255, 255)))
        dc.DrawCircle(300, 125, 30)

        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        dc.SetFont(font)
        dc.DrawText("Hello wxPython", 200, 10)

        pen = wx.Pen(wx.Colour(0, 0, 255))
        dc.SetPen(pen)
        dc.DrawLine(200, 50, 350, 50)

        dc.SetBrush(wx.Brush(wx.Colour(0, 255, 0), wx.CROSS_HATCH))
        dc.DrawRectangle(380, 15, 90, 60)

def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()