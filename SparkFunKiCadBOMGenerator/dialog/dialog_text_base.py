# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class DIALOG_TEXT_BASE
###########################################################################

class DIALOG_TEXT_BASE ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"SparkFun KiCad BOM Generator"), pos = wx.DefaultPosition, size = wx.Size( 900,650 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.SYSTEM_MENU )

        self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

        mainSizer = wx.FlexGridSizer( 5, 1, 0, 0 )
        mainSizer.AddGrowableCol( 0 )
        mainSizer.AddGrowableRow( 0 )
        mainSizer.AddGrowableRow( 2 )
        mainSizer.AddGrowableRow( 4 )
        mainSizer.SetFlexibleDirection( wx.BOTH )
        mainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        bomSizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        bomSizer.AddGrowableCol( 0 )
        bomSizer.AddGrowableRow( 1 )
        bomSizer.SetFlexibleDirection( wx.BOTH )
        bomSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        bomSizer.SetMinSize( wx.Size( -1,150 ) )
        self.bomLabel = wx.StaticText( self, wx.ID_ANY, _(u"BOM Items:"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
        self.bomLabel.Wrap( -1 )

        self.bomLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bomSizer.Add( self.bomLabel, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )

        self.bomGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.bomGrid.CreateGrid( 1, 5 )
        self.bomGrid.EnableEditing( True )
        self.bomGrid.EnableGridLines( True )
        self.bomGrid.EnableDragGridSize( False )
        self.bomGrid.SetMargins( 0, 0 )

        # Columns
        self.bomGrid.AutoSizeColumns()
        self.bomGrid.EnableDragColMove( False )
        self.bomGrid.EnableDragColSize( True )
        self.bomGrid.SetColLabelValue( 0, _(u"Qty") )
        self.bomGrid.SetColLabelValue( 1, _(u"PROD_ID") )
        self.bomGrid.SetColLabelValue( 2, _(u"Refs") )
        self.bomGrid.SetColLabelValue( 3, _(u"Value") )
        self.bomGrid.SetColLabelValue( 4, _(u"Package") )
        self.bomGrid.SetColLabelSize( 30 )
        self.bomGrid.SetColLabelAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )

        # Rows
        self.bomGrid.AutoSizeRows()
        self.bomGrid.EnableDragRowSize( False )
        self.bomGrid.SetRowLabelSize( 1 )
        self.bomGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.bomGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        self.bomGrid.SetMaxSize( wx.Size( -1,300 ) )

        bomSizer.Add( self.bomGrid, 0, wx.ALL|wx.EXPAND, 5 )


        mainSizer.Add( bomSizer, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        mainSizer.Add( self.m_staticline1, 0, wx.ALL|wx.EXPAND, 5 )

        nonBomSizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        nonBomSizer.AddGrowableCol( 0 )
        nonBomSizer.AddGrowableRow( 1 )
        nonBomSizer.SetFlexibleDirection( wx.BOTH )
        nonBomSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        nonBomSizer.SetMinSize( wx.Size( -1,150 ) )
        self.nonBomLabel = wx.StaticText( self, wx.ID_ANY, _(u"Non-BOM Items:"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
        self.nonBomLabel.Wrap( -1 )

        self.nonBomLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        nonBomSizer.Add( self.nonBomLabel, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )

        self.nonBomGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.nonBomGrid.CreateGrid( 1, 4 )
        self.nonBomGrid.EnableEditing( True )
        self.nonBomGrid.EnableGridLines( True )
        self.nonBomGrid.EnableDragGridSize( False )
        self.nonBomGrid.SetMargins( 0, 0 )

        # Columns
        self.nonBomGrid.AutoSizeColumns()
        self.nonBomGrid.EnableDragColMove( False )
        self.nonBomGrid.EnableDragColSize( True )
        self.nonBomGrid.SetColLabelValue( 0, _(u"Qty") )
        self.nonBomGrid.SetColLabelValue( 1, _(u"Refs") )
        self.nonBomGrid.SetColLabelValue( 2, _(u"Value") )
        self.nonBomGrid.SetColLabelValue( 3, _(u"Package") )
        self.nonBomGrid.SetColLabelSize( 30 )
        self.nonBomGrid.SetColLabelAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )

        # Rows
        self.nonBomGrid.AutoSizeRows()
        self.nonBomGrid.EnableDragRowSize( False )
        self.nonBomGrid.SetRowLabelSize( 1 )
        self.nonBomGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.nonBomGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        self.nonBomGrid.SetMaxSize( wx.Size( -1,300 ) )

        nonBomSizer.Add( self.nonBomGrid, 0, wx.ALL|wx.EXPAND, 5 )


        mainSizer.Add( nonBomSizer, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        mainSizer.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        sparkleSizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        sparkleSizer.AddGrowableCol( 0 )
        sparkleSizer.AddGrowableRow( 1 )
        sparkleSizer.SetFlexibleDirection( wx.BOTH )
        sparkleSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.sparkleLabel = wx.StaticText( self, wx.ID_ANY, _(u"Sparkle BOM:"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
        self.sparkleLabel.Wrap( -1 )

        self.sparkleLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        sparkleSizer.Add( self.sparkleLabel, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )

        self.sparkleCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sparkleCtrl.SetMinSize( wx.Size( 300,50 ) )

        sparkleSizer.Add( self.sparkleCtrl, 0, wx.ALL|wx.EXPAND, 5 )


        mainSizer.Add( sparkleSizer, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( mainSizer )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


