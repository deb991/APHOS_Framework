#!/usr/bin/env python
import os
try:
    from Tkinter import *
except:
    from tkinter import *
from idlelib.tree import TreeItem, TreeNode, FileTreeItem, _tree_widget, ScrolledCanvas

root = Tk()
root.title( '~~~~File Manager~~~~' )

def fileSearch():
    fileSearch  = input('Enter Location to find file:: ')
    print(fileSearch)

def fileWindow():
    SC = ScrolledCanvas( root, bg='White', highlightthickness=0, takefocus=1 )
    SC.frame.pack( expand='True', fill='both', side='right' )

    chdir = FileTreeItem( fileSearch )
    node1 = TreeNode( SC.canvas, None, chdir )
    node1.expand()


root.mainloop()
