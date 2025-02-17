import wx

class DeleteDialog(wx.Dialog):
    def __init__(self, parent, book=None):
        super(DeleteDialog, self).__init__(parent, title='Delete dialog', size=(400,150))
        self.nameTextCtrl = None
        self.phoneTextCtrl = None
        self.addressTextCtrl = None
        self.book = book
        self.deleteName = ""
        self.init_view()

    def init_view(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        namelabel = wx.StaticText(panel, label='Name:')
        hbox1.Add(namelabel, flag=wx.RIGHT, border=5)
        self.nameTextCtrl = wx.TextCtrl(panel)
        hbox1.Add(self.nameTextCtrl, proportion=1)
        searchButton = wx.Button(panel, label='Search')
        hbox1.Add(searchButton, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        phonelabel = wx.StaticText(panel, label='Phone:')
        hbox2.Add(phonelabel, flag=wx.RIGHT, border=5)
        self.phoneTextCtrl = wx.TextCtrl(panel)
        hbox2.Add(self.phoneTextCtrl, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        addresslabel = wx.StaticText(panel, label='Address:')
        hbox3.Add(addresslabel, flag=wx.RIGHT, border=5)
        self.addressTextCtrl = wx.TextCtrl(panel)
        hbox3.Add(self.addressTextCtrl, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        deleteButton = wx.Button(panel, label='Delete')
        hbox2.Add(deleteButton, proportion=1)

        cancelButton = wx.Button(panel, label='Cancel')
        hbox2.Add(cancelButton, proportion=1)

        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        panel.SetSizer(vbox)

        self.phoneTextCtrl.Disable()
        self.addressTextCtrl.Disable()

        searchButton.Bind(wx.EVT_BUTTON, self.OnSearchButton)
        deleteButton.Bind(wx.EVT_BUTTON, self.OnDeleteButton)
        cancelButton.Bind(wx.EVT_BUTTON, self.OnCancelButton)

    def OnSearchButton(self, event):
        name = self.nameTextCtrl.GetValue().encode('ascii','ignore')
        info = self.book.search(name)

        if info:
            self.deleteName = name
            self.nameTextCtrl.SetValue(info.name)
            self.phoneTextCtrl.SetValue(info.phone)
            self.addressTextCtrl.SetValue(info.address)
        else:
            self.deleteName = ""
            self.nameTextCtrl.Clear()
            self.phoneTextCtrl.Clear()
            self.addressTextCtrl.Clear()
            wx.MessageBox('Can not found : %s' % name, 'Warning', wx.OK | wx.ICON_WARNING)

    def OnDeleteButton(self, event):
        if self.deleteName:
            ynDialog = wx.MessageBox('Do you delete searched item?', 'Yes or No', wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION)
            if ynDialog == wx.YES:
                self.book.remove(self.deleteName)
                wx.MessageBox('%s is deleted' % self.deleteName, 'Info', wx.OK|wx.ICON_INFORMATION)
                self.Destroy()

    def OnCancelButton(self, event):
        self.Destroy()


