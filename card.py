class card(object):
    price=0
    flavor=""
    name=""
    desc=""
    def __init__(self,price,flavor,name,desc):
        self.price=price
        self.flavor=flavor
        self.name=name
        self.desc=desc
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)
    
class treasure(card):
    value=0
    def __init__(self,price,name,value,desc):
        card.__init__(self,price,"treasure",name,desc)
        self.value=value

class action(card):
    #should have action
    effects={}
    def __init__(self,price,name,effects,desc):
        card.__init__(self,price,"action",name,desc)
        self.effects=effects

class victory(card):
    points=0
    def __init__(self,price,name,points,desc):
        card.__init__(self,price,"victory",name,desc)
        self.points=points

class deck(object):
    inner_list=[]
    def __init__(self, the_list):
        self.inner_list=the_list
    def draw(self):
        to_return=self.inner_list[0]
        self.inner_list.remove(to_return)
        return to_return
    def addFrom(self,other_deck):
        self.inner_list.append(other_deck.draw())
    def print_list(self):
        for item in self.inner_list:
            print item
        

    
