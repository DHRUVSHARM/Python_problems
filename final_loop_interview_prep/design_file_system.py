"""
The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters.

/{one or more lowercase chars}

bool createPath(string path, int value) 

Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.

int get(string path) 

Returns the value associated with path or returns -1 if the path doesn't exist.
observation : every node is a path label 

/c/d

split on the /


     ""
    /   
  neet - 1
  /
  code - 2


  return 2
  false


"""

"""
The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters.

/{one or more lowercase chars}

bool createPath(string path, int value) 

Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.

int get(string path) 

Returns the value associated with path or returns -1 if the path doesn't exist.
observation : every node is a path label 

/c/d

split on the /


     ""
    /   
  neet - 1
  /
  code - 2


  return 2
  false


"""

class Trienode:
    def __init__(self , val=-1 , path=""):
        self.val = val # to indicate invalid path value , # -1 indicates that the path does not exist yet  
        self.path = path
        self.children = {}

class FileSystem:

    def __init__(self):
        self.trie = Trienode()

    def createPath(self, path: str, value: int) -> bool:
        created , curr , path = False , self.trie , path.split("/")
        #   /c -> ["" , c]
        for index in range(1 , len(path) - 1):
            if path[index] not in curr.children:
                # invalid parent path 
                return False
            curr = curr.children[path[index]]
        
        # we are the last point 
        if path[-1] not in curr.children:
            # can create path 
            curr.children[path[-1]] = Trienode()

        if path[-1] in curr.children:
            if curr.children[path[-1]].val != -1:
                # path already exists
                return False
            else:
                # prefix exists not the path 
                pass

        curr = curr.children[path[-1]]
        curr.val = value
        return True        

    def get(self, path: str) -> int:
        # return -1 if the path is not found 
        curr , path = self.trie , path.split("/")        
        index = 1
        while index < len(path):
            if path[index] not in curr.children:
                return -1
            curr = curr.children[path[index]]
            index += 1

        if index == len(path):
            return curr.val # if this is not a path it will return -1 anyways, although the input is only valid paths
        else:
            return -1 # not completed path 


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
