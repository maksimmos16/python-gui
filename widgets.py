import wx
import wx.lib.iewin


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetSize(700,600)
        panel = wx.Panel(self)
        btn = wx.Button(panel, label='Close', pos=(20, 20))
        btn.Bind(wx.EVT_BUTTON, self.OnClose)

        tb = wx.ToggleButton(panel, label='Color', pos=(20, 50))
        tb.Bind(wx.EVT_TOGGLEBUTTON, self.Toggle)
        self.cpnl = wx.Panel(panel, pos=(150, 50), size=(110, 110))
        self.cpnl.SetBackgroundColour(wx.Colour(255,255,255))

        wx.StaticBox(panel, label='Box', pos=(5, 5), size=(270, 170))

        txt='''Text
        Text
        '''
        str = wx.StaticText(panel, label=txt, pos=(20, 80))
        font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.DEFAULT)
        str.SetFont(font)
        wx.StaticLine(panel, pos=(20, 200), size=(200, 5))

        os = ['Ubuntu', 'Arch', 'Fedora', 'Debian', 'Mint']
        cb = wx.ComboBox(panel, pos=(50, 250), choices=os, style=wx.CB_READONLY)
        cb.Select(0)
        self.st = wx.StaticText(panel, label='', pos=(50, 300))
        cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)

        self.cb = wx.CheckBox(panel, pos=(50, 350), label='Show')
        self.cb.SetValue(True)
        self.cb.Bind(wx.EVT_CHECKBOX, self.ShowOrHide)

        self.rb1 = wx.RadioButton(panel, label='Value A', pos=(200, 250), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(panel, label='Value B', pos=(200, 270))
        self.rb1.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
        self.rb2.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
        self.sb = self.CreateStatusBar(2)
        self.sb.SetStatusText("True", 0)
        self.sb.SetStatusText("False", 1)

        self.gauge = wx.Gauge(panel, range=50, size=(250, -1),pos=(20, 370))
        self.btnS = wx.Button(panel, wx.ID_OK, pos=(20, 400))
        self.Bind(wx.EVT_BUTTON, self.OnStart, self.btnS)
        self.timer = wx.Timer(self, 1)
        self.count = 0
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

        sld = wx.Slider(panel, value=200, minValue=150, maxValue=500, pos=(20, 450),style=wx.SL_HORIZONTAL)
        sld.Bind(wx.EVT_SCROLL, self.OnSliderScroll)

        self.sc = wx.SpinCtrl(panel, value='0',pos=(20, 500))
        self.sc.SetRange(-459, 1000)
        self.sc.Bind(wx.EVT_SPINCTRL, self.OnCompute)

        languages = ['C', 'C++', 'Java', 'Python', 'Perl', 'JavaScript', 'PHP', 'VB.NET', 'C#']
        self.text = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos=(300, 20), size=(150, 50))
        lst = wx.ListBox(panel, size=(100, -1), choices=languages, style=wx.LB_SINGLE, pos=(300, 100))
        self.Bind(wx.EVT_LISTBOX, self.onListBox, lst)

        maxint=2**31-1
        players = [('Tendulkar', '15000', '100'), ('Dravid', '14000', '1'),
                   ('Kumble', '1000', '700'), ('KapilDev', '5000', '400'),
                   ('Ganguly', '8000', '50')]
        self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT,pos=(300, 250))
        self.list.InsertColumn(0, 'name', width=100)
        self.list.InsertColumn(1, 'runs', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(2, 'wkts', wx.LIST_FORMAT_RIGHT, 100)

        for i in players:
            index = self.list.InsertStringItem(maxint, i[0])
            self.list.SetStringItem(index, 1, i[1])
            self.list.SetStringItem(index, 2, i[2])

        self.list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnClick, self.list)

        #pip install comtypes
        html = wx.lib.iewin.IEHtmlWindow(panel, pos=(300, 420), size=(300,100))
        html.Navigate('https://www.wxpython.org')


    def OnClick(self, event):
        ind = event.GetIndex()
        item = self.list.GetItem(ind, 1)
        self.sb.SetStatusText(item.GetText(), 0)

    def onListBox(self, event):
        self.text.AppendText("Current selection:"+event.GetEventObject().GetStringSelection()+"\n")

    def OnCompute(self, e):
        fahr = self.sc.GetValue()
        val = round((fahr - 32) * 5 / 9.0, 2)
        self.sb.SetStatusText(str(val), 0)

    def OnSliderScroll(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        self.sb.SetStatusText(str(val), 0)

    def OnStart(self, e):
        if self.count >= 50:
            return
        self.timer.Start(100)
        self.sb.SetStatusText("Task in Progress", 0)

    def OnTimer(self, e):
        self.count = self.count + 1
        self.gauge.SetValue(self.count)
        if self.count == 50:
            self.timer.Stop()
            self.sb.SetStatusText("Task Completed", 0)

    def SetVal(self, e):
        state1 = str(self.rb1.GetValue())
        state2 = str(self.rb2.GetValue())
        self.sb.SetStatusText(state1, 0)
        self.sb.SetStatusText(state2, 1)

    def ShowOrHide(self, e):
        i = e.GetEventObject()
        isChecked = i.GetValue()
        if isChecked:
            self.cb.SetLabel('Show')
        else:
            self.cb.SetLabel('Hide')

    def OnSelect(self, e):
        i = e.GetString()
        self.st.SetLabel(i)

    def Toggle(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        if isPressed:
            self.cpnl.SetBackgroundColour(wx.RED)
        else:
            self.cpnl.SetBackgroundColour(wx.BLUE)
        self.cpnl.Refresh()

    def OnClose(self, e):
        self.Close(True)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()