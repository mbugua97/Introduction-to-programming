class Parent:
    def __init__(self,FathersName,FathersAge,MothersName,MothersAge):
        self.FathersName=FathersName #attribute of fathers name in the Father class
        self.FathersAge=FathersAge
        self.MothersName=MothersName
        self.MothersAge=MothersAge
    def showParentDetails(self):
        return f"The parents are {self.FathersName} and {self.MothersName}"

class Child(Parent):
    def __init__(self,ChildName,ChildAge,FathersName,FathersAge,MothersName,MothersAge):
        super().__init__(FathersName,FathersAge=FathersAge,MothersName=MothersName,MothersAge=MothersAge)
        self.ChildName=ChildName
        self.ChildAge=ChildAge
    def ShowChildDetails(self):
        print(f"the Child's Name is {self.ChildName} and the childs age is {self.ChildAge} and the parents are {self.FathersName},{self.MothersName}")


theParent=Parent("Joseph",45,"Mary",43) #Object extending the Parent class

theSecondParents=Parent("Joshua",33,"Eliza",30) #Object extending the Parent class


child1=Child("Mark",12,theParent.FathersName,theParent.FathersAge,theParent.MothersName,theParent.MothersAge) #has inherited theparent attributes
child2=Child("Eva",10,theParent.FathersName,theParent.FathersAge,theParent.MothersName,theParent.MothersAge) #has inherited theparent attributes
child1.ShowChildDetails() #we are calling child 1 showdetail method that is inheriting theparent
child2.ShowChildDetails() #we are calling child 1 showdetail method that is inheriting theparent


child3=Child("Natalie",2,theSecondParents.FathersName,theSecondParents.FathersAge,theSecondParents.MothersName,theSecondParents.MothersAge)
child3.ShowChildDetails()# the object is inheriting thesecondparents Objects