circuits = ['Mushroom Cup', 'Leaf Cup', 'Flower Cup', 'Shell Cup', 'Special Cup',
'Banana Cup']
tracks = ['Moo Moo Meadows', 'Mushroom Gorge', 'Toads Factory', 'Luigi Circuit', 'Desert Hills',
'Bowsers Castle I', 'Jungle Parkway', 'Mario Circuit II', 'Mario Circuit I', 'Coconut Mall',
'Snowboard Cross', 'Warios Gold Mine', 'Peach Beach', 'Yoshi Falls', 'Ghost Valley', 
'Mario Raceway', 'Dry Dry Ruins', 'Moonview Highway', 'Bowsers Castle II', 
'Rainbow Road', 'Sherbert Land', 'Shy Guy Beach', 'Delfino Square', 'Waluigi Stadium']
powerups = ['Mushroom', 'Golden Mushroom', 'Mega Mushroom', 'Banana', 'Green Shell',
'Red Shell', 'Spiny Shell', 'Star', 'Thunder Cloud', 'Blooper', 'Bullet Bill',
'Pow']


class Item(object):
    def __init__(self, name):
        self.name = name
        
class Circuit(Item):
    def __init__(self, name, track1, track2, track3, track4):
        super(Circuit, self).__init__(name)
        self.track1 = track1
        self.track2 = track2
        self.track3 = track3
        self.track4 = track4

#----------------Printing-----------------------
print 'Pick a circuit: Mushroom Cup, Leaf Cup, Flower Cup, Shell Cup, \
Special Cup, or Banana Cup.' 

class select(Circuit):
    def __init__(self, name, subs, appx_time):
        super(select, self).__init__(name, subs, appx_time)
        self.name = name
        self.subs = subs
        self.appx_time = appx_time
      
    def choose_circuit(track):
        print track.Name
        print "The four races in this circuit are %s." %track.subs
        print "This track should take you about %s minutes." %track.appx_time
        
MushroomCup = select('Mushroom Cup', 'Moo Moo Meadows, Mushroom Gorge, \
Toad\'s Factory, and Luigi Circuit', appx_time = 8)
LeafCup = select('Leaf Cup', 'Desert Hills, Bowsers Castle I, Jungle \
Parkway, and Mario Circuit II', appx_time = 10)
FlowerCup = select('Flower Cup', 'Mario Circuit I, Coconut Mall, Snowboard Cross \
and Wario\'s Gold Mine', appx_time = 9)
ShellCup = select('Shell Cup', 'Peach Beach, Yoshi Falls, Ghost Valley, and \
Mario Raceway', appx_time = 7)
SpecialCup = select('Special Cup', 'Dry Dry Ruins, Moonview Highway, Bowser\'s \
Castle, and Rainbow Road', appx_time = 10)
BananaCup = select('Banana Cup', 'Sherbert Land, SHy Guy Beach, Delfino Square, \
and Waluigi Stadium', appx_time = 10)


  
choice = raw_input(">").strip().lower()

if choice in circuits:
    if choice == 'Mushroom Cup':
        print select(MushroomCup)
        
        
        
