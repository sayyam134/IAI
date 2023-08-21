visited=[]
queue=[]

class Tree:
    def __init__(self,val=0):
        self.data = val
        self.child = []
        
    def bfs(self):
        visited.append(self)
        queue.append(self)
        
        while queue:
            m= queue.pop(0)
            print(m.data ,end=" ")

            for child in m.child:
                if child not in visited:
                    visited.append(child)
                    queue.append(child)

if __name__=="__main__":
    
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

    
    root.bfs()
    