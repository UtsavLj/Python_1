class FileNode:
    def __init__(self, name, is_directory:bool=False,parent=None):
        self.name = name                
        self.is_directory = is_directory
        self.children = {}              
        self.parent = parent              
        self.size = 0                   

    def add_child(self, child_node):
        """Adds a child (file or folder) to this node if it's a directory."""
        if self.is_directory and child_node.name not in self.children:
            child_node.parent = self
            self.children[child_node.name]=child_node
        else:
            raise Exception(f"{self.name} is not a directory!")

    def remove_child(self,name:str):
        """Removes a child (file or folder) to this node if it's a directory."""
        if self.is_directory:
            if name in self.children:
                self.children[name].parent = None
                self.children.pop(name)
            else:
                raise Exception(f"{name} not present in {self.name}")
        else:
            raise Exception(f"{self.name} is not a directory!")

    def __str__(self):
        """Returns a string representation of the node."""
        if self.is_directory:
            return f"{self.name}/"
        else:
            return f"{self.name}[{self.size} bytes]"

class FileSystem:
    def __init__(self):
        self.root=FileNode("root",True)
        self.cwd=self.root

    def mkdir(self,name:str):
        if name.strip().lower() not in self.cwd.children and name.strip() !="..":
            self.cwd.add_child(FileNode(name.lower(),True))
    
    def rmdir(self,name:str):
        if name.lower() in self.cwd.children:
            self.cwd.remove_child(name.lower())
        else:
            print(f"{name} not found in {self.cwd.name}")
    
    def cd(self,name:str):
        if name.lower() in self.cwd.children:
            self.cwd=self.cwd.children[name.lower()]
            return 1
        elif name=="..":
            if self.cwd.parent!=None:
                self.cwd=self.cwd.parent
            return 1
        else:
            print(f"{name} not found in {self.cwd.name}")
            return 0
    
    def mk(self,name:str,size:int=0):
        if name.strip().lower() not in self.cwd.children and name.strip() !="..":
            file=FileNode(name.lower())
            file.size=size
            self.cwd.add_child(file)
    
    def rm(self,name:str):
        if name.strip().lower() in self.cwd.children:
            self.cwd.remove_child(name.lower())
        else:
            print(f"{name} not found in {self.cwd.name}")

    def ls(self)->str:
        for child in self.cwd.children:
            print(f"{self.cwd.children[child]}",end=" ")
            print()

    def print_dir(self,node=None,level=0):
        node = self.root if node ==None else node
        print(" "*(level*4)+"|-"+str(node))
        if not node.is_directory:
            return
        else:
            for child in node.children:
                self.print_dir(node.children[child],level+1)
                
def CLI(Cursor:FileSystem):
    path="#root"
    while(True):
        command=input(f"{path}>").strip().split(" ")
        if command[0]=="ls":
            Cursor.ls()
        elif command[0]=="quit":    
            return Cursor
        elif len(command)==2:
            match command[0]:
                case "cd":
                    if Cursor.cd(command[1]):
                        if command[1]=="..":
                            path=path.rsplit("/",1)[0]
                        else:
                            path+=f"/{command[1]}"
                case "mkdir":
                    Cursor.mkdir(command[1])
                case "rmdir":
                    Cursor.rmdir(command[1])
                case "mk":
                    Cursor.mk(command[1])
                case "rm":
                    Cursor.rm(command[1])
                case _:
                    print("Invalid Command")
        else:
            print("Invalid Command!")
             
CLI(FileSystem()).print_dir()