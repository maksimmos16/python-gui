import wx
import wx.lib.iewin


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetSize(300,300)

        splitter = wx.SplitterWindow(self, -1)
        panel = wx.Panel(splitter,size=(100, 300))
        self.text = wx.TextCtrl(panel, size=(120, 250), style=wx.TE_MULTILINE)
        panelS = wx.Panel(splitter, size=(100, 300))
        languages = ['C', 'C++', 'Java', 'Python', 'Perl',
                     'JavaScript', 'PHP', 'VB.NET', 'C#']
        lst = wx.ListBox(panelS, size=(100, 250), choices=languages, style=wx.LB_SINGLE)
        splitter.SplitVertically(panelS, panel)
        self.Bind(wx.EVT_LISTBOX, self.onListBox, lst)

    def onListBox(self, event):
        self.text.AppendText("Current selection: " + event.GetEventObject().GetStringSelection() + "\n")

def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()