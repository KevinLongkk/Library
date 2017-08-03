import wx, qrcode


class Mywin(wx.Frame):

    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(400, 250))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.btn = wx.Button(panel, -1, "借书")
        vbox.Add(self.btn, 0, wx.ALIGN_CENTER)
        self.btn.Bind(wx.EVT_BUTTON, self.OnClicked)

        self.Centre()
        self.Show()
        self.Fit()

    def OnClicked(self, event):
        result = qrcode.lesen()
        print(result)


app = wx.App()
Mywin(None, "图书管理系统")
app.MainLoop()
