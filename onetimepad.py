# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 24 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame12
###########################################################################

class MyFrame12 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Program", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar3 = wx.MenuBar( 0 )
		self.m_menu5 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Krypter", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem3 )

		self.m_menubar3.Append( self.m_menu5, u"Krypter" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Dekrypter", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem4 )

		self.m_menubar3.Append( self.m_menu2, u"Dekrypter" )

		self.SetMenuBar( self.m_menubar3 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.encrypt, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.decrypt, id = self.m_menuItem4.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def encrypt( self, event ):
		event.Skip()

	def decrypt( self, event ):
		event.Skip()


###########################################################################
## Class EncryptFrame
###########################################################################

class EncryptFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Krypter", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_filePicker4 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gSizer5.Add( self.m_filePicker4, 0, wx.ALL, 5 )


		bSizer8.Add( gSizer5, 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"krypter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button10, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Key:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer14.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer14.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Dummy key:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer14.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer14.Add( self.m_staticText10, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer14, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class DecryptFrame
###########################################################################

class DecryptFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Dekrypter", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Key:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer15.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Dummy key:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer15.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_textCtrl4, 0, wx.ALL, 5 )


		bSizer15.Add( gSizer15, 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Dekrypter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button11, 0, wx.ALL, 5 )


		bSizer15.Add( bSizer16, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass