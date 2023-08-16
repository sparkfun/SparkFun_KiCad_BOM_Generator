#!/usr/bin/env python
from dialog.dialog import *

import sys
import subprocess

class MyApp(wx.App):
    def OnInit(self):

        self.dlg = dlg = Dialog(None)

        dlg.bomGrid.SetCellValue(0,4,"SOMETHING")

        dlg.nonBomGrid.SetCellValue(0,3,"SOMETHING ELSE")

        dlg.sparkleCtrl.SetValue("A VERY LONG STRING...................................................................................................................!")

        # Autosize now grid is populated
        dlg.bomGrid.AutoSizeColumns()
        dlg.nonBomGrid.AutoSizeColumns()

        dlg.ShowModal()
        dlg.Destroy()

        return True

app = MyApp()
app.MainLoop()
