import os
import wx
import wx.aui

import pcbnew

from .dialog import Dialog

class BomGeneratorPlugin(pcbnew.ActionPlugin, object):

    # Don't include footprints from these libraries
    unwanted_libraries = ['SparkFun-Jumper', 'SparkFun-Aesthetic']

    # Don't include these footprints
    unwanted_footprints = ['kibuzzard', 'STANDOFF']

    # SparkFun panelizer fiducials are from KiCad Fiducial.pretty: Fiducial_1.5mm_Mask3mm
    fid_name = "Fiducial_1.5mm_Mask3mm"

    # All dimension parameters used by this script are um unless otherwise noted
    # KiCad works in nm (integer)
    SCALE_MM = 1000000 # Convert mm to nm
    SCALE_UM = 1000 # Convert um to nm
    SCALE_MD = 1000 # Convert degrees to microdegrees

    def __init__(self):
        super(BomGeneratorPlugin, self).__init__()

        self.name = "BOM Generator"
        self.category = "Read PCB"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        icon_dir = os.path.dirname(__file__)
        self.icon_file_name = os.path.join(icon_dir, 'icon.png')
        self.description = "Generate SparkFun BOM"
        
        self._pcbnew_frame = None

        self.kicad_build_version = pcbnew.GetBuildVersion()

    def IsVersion(self, VersionStr):
        for v in VersionStr:
            if v in self.kicad_build_version:
                return True
        return False

    def Run(self):
        if self._pcbnew_frame is None:
            try:
                self._pcbnew_frame = [x for x in wx.GetTopLevelWindows() if ('pcbnew' in x.GetTitle().lower() and not 'python' in x.GetTitle().lower()) or ('pcb editor' in x.GetTitle().lower())]
                if len(self._pcbnew_frame) == 1:
                    self._pcbnew_frame = self._pcbnew_frame[0]
                else:
                    self._pcbnew_frame = None
            except:
                pass

        dlg = Dialog(self._pcbnew_frame)

        board = pcbnew.GetBoard()

        bom_items = {}
        non_bom_items = {}
        sparkleBom = ""

        modules = board.GetFootprints()
        for sourceModule in modules:
            # GetFPIDAsString returns both the footprint library name and the individual footprint name, separated by a colon.
            # E.g.: SparkFun-Semiconductor-Standard:TSSOP-16
            pack = sourceModule.GetFPIDAsString()
            unwanted = False
            for lib in self.unwanted_libraries: # Check for aesthetics etc.
                if lib in pack:
                    unwanted = True
            for footprint in self.unwanted_footprints: # Check for KiBuzzard etc.
                if footprint in pack:
                    unwanted = True
            if not unwanted:
                ref = sourceModule.Reference().GetText()
                val = sourceModule.Value().GetText()
                name = pack
                if ":" in name:
                    name = name.split(":")[1]
                prod_id = ""
                hasProdID = False
                if hasattr(sourceModule, "HasProperty"):
                    if sourceModule.HasProperty("PROD_ID"):
                        prod_id = sourceModule.GetPropertyNative("PROD_ID")
                        hasProdID = True
                if hasProdID:
                    if prod_id == "":
                        prod_id = "NONE"
                uniqueRef = name + val + prod_id
                if hasProdID:
                    if prod_id != "NONE":
                        prodIdNum = prod_id.split("-")[1]
                        while prodIdNum[0] == "0":
                            prodIdNum = prodIdNum[1:]
                        if sparkleBom == "":
                            sparkleBom = prodIdNum
                        else:
                            sparkleBom = sparkleBom + "," + prodIdNum
                    if uniqueRef in bom_items.keys():
                        bom_items[uniqueRef]['Qty'] = bom_items[uniqueRef]['Qty'] + 1
                        if ref not in bom_items[uniqueRef]['Refs'].split(","): # Avoid duplicate refs
                            bom_items[uniqueRef]['Refs'] = bom_items[uniqueRef]['Refs'] + "," + ref
                    else:
                        bom_items.setdefault(uniqueRef,
                                            {
                                                'Qty': None,
                                                'PROD_ID': None,
                                                'Refs': None,
                                                'Value': None,
                                                'Package': None
                                            })
                        bom_items[uniqueRef]['Qty'] = 1
                        bom_items[uniqueRef]['PROD_ID'] = prod_id
                        bom_items[uniqueRef]['Refs'] = ref
                        bom_items[uniqueRef]['Value'] = val
                        bom_items[uniqueRef]['Package'] = name
                else:
                    if uniqueRef in non_bom_items.keys():
                        non_bom_items[uniqueRef]['Qty'] = non_bom_items[uniqueRef]['Qty'] + 1
                        if ref not in non_bom_items[uniqueRef]['Refs'].split(","): # Avoid duplicate refs
                            non_bom_items[uniqueRef]['Refs'] = non_bom_items[uniqueRef]['Refs'] + "," + ref
                    else:
                        non_bom_items.setdefault(uniqueRef,
                                            {
                                                'Qty': None,
                                                'Refs': None,
                                                'Value': None,
                                                'Package': None
                                            })
                        non_bom_items[uniqueRef]['Qty'] = 1
                        non_bom_items[uniqueRef]['Refs'] = ref
                        non_bom_items[uniqueRef]['Value'] = val
                        non_bom_items[uniqueRef]['Package'] = name

        # Copy bom_items into grid
        dlg.bomGrid.CreateGrid( len(bom_items.keys()), 5 )
        row = 0
        for name in bom_items.keys():
            if row > 0:
                dlg.bomGrid.AppendRows()
            dlg.bomGrid.SetCellValue(row, 0, str(bom_items[name]['Qty']))
            if bom_items[name]['PROD_ID'] == "NONE":
                dlg.bomGrid.SetCellTextColour(row, 1, wx.RED)
            dlg.bomGrid.SetCellValue(row, 1, str(bom_items[name]['PROD_ID']))
            dlg.bomGrid.SetCellValue(row, 2, str(bom_items[name]['Refs']))
            dlg.bomGrid.SetCellValue(row, 3, str(bom_items[name]['Value']))
            dlg.bomGrid.SetCellValue(row, 4, str(bom_items[name]['Package']))
            row += 1

        # Copy non_bom_items into grid
        dlg.nonBomGrid.CreateGrid( len(non_bom_items.keys()), 4 )
        row = 0
        for name in non_bom_items.keys():
            if row > 0:
                dlg.nonBomGrid.AppendRows()
            dlg.nonBomGrid.SetCellValue(row, 0, str(non_bom_items[name]['Qty']))
            dlg.nonBomGrid.SetCellValue(row, 1, str(non_bom_items[name]['Refs']))
            dlg.nonBomGrid.SetCellValue(row, 2, str(non_bom_items[name]['Value']))
            dlg.nonBomGrid.SetCellValue(row, 3, str(non_bom_items[name]['Package']))
            row += 1

        # Copy Sparkle BOM into TextCrtl
        dlg.sparkleCtrl.SetValue(sparkleBom)

        # Autosize now grid is populated
        dlg.bomGrid.AutoSizeColumns()
        dlg.nonBomGrid.AutoSizeColumns()

        try:
            dlg.ShowModal()

        finally:
            dlg.Destroy()
                        

    