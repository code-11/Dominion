from card import *
class turn(object):
    gold=0
    actions=0
    buys=0
##    hand=deck()
##    in_play=deck()

    def __init__(self):
        self.gold=0
        self.actions=1
        self.buys=1
    
    def draw_cards(self,num):
        pass
    def figure_gold(self):
        pass
    #Checks that there are enough cards in the p_deck
    def check_for_cards(self):
        pass
    def draw_phase (self):
        pass
    def play_phase (self):
        pass
    def buy_phase (self):
        pass
    def clean_up(self):
        pass
    
class mat(object):
    gold=[]
    silver=[]
    copper=[]
    estates=[]
    duchies=[]
    provinces=[]
    actions=[]
    trash=[]
    def __init__(self,g,s,c,e,d,p):
        self.gold=g
        self.silver=s
        self.copper=c
        self.estates=e
        self.duchies=d
        self.provinces=p
        self.trash=deck([])

    
