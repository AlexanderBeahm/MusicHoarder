from os import listdir
from os import path


class FileTraversalResult:
    '''
    Holds result of file traversal.
    '''
    def __init__(self):
        super()
        self.folderstraversed = list()
        self.filestraversed = list()
        self.maximumfolderdepth = 0
        self.__ismutable = True
    
    def addfolders(self, folders):
        '''
        Appends traversed folders to the result list.
        '''
        if self.__ismutable:
            self.folderstraversed.append(folders)

    def addfiles(self, files):
        '''
        Appends traversed files to the result list.
        '''
        if self.__ismutable:
            self.filestraversed.append(files)

    def maximizedepth(self, depth):
        '''
        Sets maximum depth of traversal.
        '''
        if self.__ismutable:        
            if depth > self.maximumfolderdepth:
                self.maximumfolderdepth = depth

    def disablemutability(self):
        '''
        Sets the mutability if possible, will return the post-assignment mutability status (True/False).
        '''
        if self.__ismutable:
            self.__ismutable = False

    def getfolderstraversed(self):
        '''
        Returns folders traversed.
        '''
        return self.folderstraversed

    def getfilestraversed(self):
        '''
        Returns files traversed.
        '''
        return self.filestraversed

    def getmaximumdepth(self):
        '''
        Returns the maximum folder depth reached.
        '''
        return self.maximumfolderdepth

class FileTraversal:
    '''
    File traversal object that will operate on it's constructed targets.
    '''
    def __init__(self, foldermethod, filemethod):
        '''
        Constructor. "foldermethod" is the function called on each folder. "filemethod" is the function called on each file.
        '''
        self.foldermethod = foldermethod
        self.filemethod = filemethod


    def recurse(self, rootpath, depth=0):
        '''
        Recursively traverses the "rootpath" folder, calling the FileTraversal object's "foldermethod" and "filemethod" methods
        as it goes. "depth" is an optional parameter that represents folder depth of the recursive operation.
        '''
        result = FileTraversalResult()
        folderlist = listdir(rootpath)

        #Simple recursive folder and file traversal.
        for entry in folderlist: 
            item = path.join(rootpath, entry)
            if path.isdir(item):
                recursive_result = self.recurse(item, depth + 1)
                result.maximizedepth(depth)
                result.maximizedepth(recursive_result.getmaximumdepth())
                self.foldermethod(item)
                result.addfolders(item)
                result.addfolders(recursive_result.getfolderstraversed())
                result.addfiles(recursive_result.getfilestraversed())
            if path.isfile(item):
                self.filemethod(item)
                result.addfiles(item)

        result.maximizedepth(depth)

        #Finally, disable mutability of the result.
        if(depth == 0):
            result.disablemutability()
        return result
