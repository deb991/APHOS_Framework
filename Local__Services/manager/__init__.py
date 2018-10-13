#!/usr/bin/env python
import os
try:
    from Tkinter import *
except:
    from tkinter import *
from idlelib.tree import TreeItem, TreeNode, FileTreeItem, _tree_widget, ScrolledCanvas

root = Tk()
root.title( '~~~~File Manager~~~~' )

##++++++++++++++Home+++++++++++++##
home = os.path.expanduser('~')
##+++++++++++++++++++++++++++++++##


class mainWindow():
    def __init__(self):
        root.configure(height = 400, width = 400)
        self.Canvas = Canvas(root, bg = 'grey', height = 380, width = 380)
        self.Canvas.place(x = 340, y=340, anchor=NE)

    def File__Viewer(self):
        Canvas(root, bg='white', height=380, width=380)
        Canvas.place(x = 500, y=800, anchor=SE)





class base__service(mainWindow):
    def __init__(self):
        super( ).__init__( )
        try:
            if os.path.isdir(home):
                print(home)

        except:
            print('Root filesystem :: ~~', home)

        self.home = home

        self.SC = ScrolledCanvas(root, bg='White', highlightthickness=0, takefocus=1)
        self.SC.frame.pack(expand='True',fill='both', side='left')

    def Parent__Dir(self):
        Parent__Directory = self.home
        to__ParentDir = FileTreeItem(self.home)

        home__node = TreeNode(self.SC.canvas, to__ParentDir)
        home__node.expand()

    def Find__Directpry(self):
        find__Dir = input('Enter Directory Path :: \n')
        locate__Dir = FileTreeItem(find__Dir)

        dirLocate__node = TreeNode(self.SC.canvas, None, locate__Dir)
        dirLocate__node.expand()



if __name__ == '__main__':
    inst = base__service()
    #inst.Parent__Dir()
    inst.Find__Directpry()
    root.mainloop( )
