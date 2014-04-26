from card import *


#An effect is a lambda expression that takes one game instance and returns a new one.

woodcutter=action(3,"Woodcutter",{"buy":1,"gold":2},"+1 Buy, +2 Gold")
village=action(2,"Village",{"card":1,"action":2},"+1 Card, +2 Actions")
smithy=action(4,"Smithy",{"card":3},"+3 Cards")
laboratory=action(5,"Laboratory",{"card":2,"action":1},"+2 Cards, +1 Action")
festival=action(5,"Festival",{"action":2,"buy":1,"gold":2},"+2 Actions, +1 Buy, +2 Gold")
market=action(5,"Market",{"action":1,"card":1,"buy":1,"gold":1},"+1 Card, +1 Action, +1 Buy, +1 Gold")

estate=victory(2,"Estate",1,"Worth 1 Victory Point")
duchy=victory(5,"Duchy",3,"Worth 3 Victory Points")
province=victory(8,"Province",6,"Worth 6 Victory Points")

copper=treasure(0,"Copper",1,"Worth 1 Money")
silver=treasure(3,"Silver",2,"Worth 2 Money")
gold=treasure(6,"Gold",3,"Worth 3 Money")

