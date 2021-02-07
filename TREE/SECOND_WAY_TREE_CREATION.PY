class Tree:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        p=self.parent
        level=0
        while  p:
            level+=1
            p=p.parent
        return level
    def printtree(self):
        l=self.get_level()
        space=" "*l*3
        prefix=space+"|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.printtree()
if __name__ == '__main__':
    root=Tree("HSC")
    eng=Tree("ENGINEERING")
    med=Tree("MEDICAL")
    dp=Tree("DIPLOMA")

    root.add_child(eng)
    root.add_child(med)
    root.add_child(dp)

    cs=Tree("COMPUTER ENGINEERING")
    me=Tree("MECHANICAL ENGINEERING")
    it=Tree("INFORMATION AND TECHNOLOGY")

    eng.add_child(cs)
    eng.add_child(me)
    eng.add_child(it)

    do=Tree("SKIN DOCTOR")
    de=Tree("DENTIST")

    med.add_child(do)
    med.add_child(de)

    root.printtree()

        