class Dogs:
    def __init__(self,name,breed,color):
        self.name=name
        self.breed=breed
        self.color=color
    def display(self):
        print("My name is ",self.name)
        print("My breed is ",self.breed)
        print("My color is ",self.color)
German_shepherd=Dogs("Bob","German shepherd","black")
German_shepherd.display()
poodle=Dogs("Rex","Poodle","white")
poodle.display()