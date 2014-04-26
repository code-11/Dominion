from card import *
from player import *
from game_structure import *
from card_library import *

def num_victory_cards(num_players):
    if (num_players==2):
        return 8
    elif (num_players==3):
        return 12
    elif (num_players==4):
        return 12
class game(object):
    players=[]
    def setup_players(self):
        you=player()
        other=comp()
        self.players=[you,other]
    def setup_mat(self):
        num_players=len(players)
        
        golds=deck([gold]*30)
        silvers=deck([silver]*40)    
        coppers=deck([copper]*60)

        vics=num_victory_cards(num_players)
        estates=deck([estate]*vics)
        duchies=deck([duchy]*vics)
        provinces=deck([province]*vics)

        for player in players:
            for i in range(7):
                coppers.draw()
                
        self.the_mat=mat(golds,silvers,coppers,estates,duchies,provinces)

    def setup_hands(self):
        start_deck=deck(([copper]*7)+([estate]*3))
        
if __name__=='__main__':
    
    temp_estates=[estate]*3
    start_deck=deck(temp_estates)
    for i in range(7):
        start_deck.addFrom(coppers)

    
    
    start_deck.print_list()
    first=turn()
    


