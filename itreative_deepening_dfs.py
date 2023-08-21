class Tree:
    visited=[]
    def __init__(self,val) -> None:
        self.data = val
        self.child = []

    def itdfs(self):
        if self.data not in Tree.visited:
            print(self.data,end=" ")
            Tree.visited.append(self.data)
        children=[]
        for i in self.child:
            print(i.data,end=" ")
            children.append(i)
            Tree.visited.append(i.data)
        for j in children:
            j.itdfs()

if __name__=="__main__":
    #Tree construction 

    root=Tree(5)
    childl=Tree(3)
    childr =Tree(7)
    childll=Tree(2)
    childrl=Tree(8)
    childlr=Tree(4)
    childlrl=Tree(8)

    root.child.append(childl)
    root.child.append(childr)

    childl.child.append(childll)
    childl.child.append(childlr)

    childlr.child.append(childlrl)

    childr.child.append(childrl)

    root.itdfs()