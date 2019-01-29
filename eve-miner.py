class Mineral():
    def __init__(self, name):
        self.name = name
        self.volume = 0.01
    def __repr__(self):
        return self.name
################################################################################
class Asteroid():
    def __init__(self, name, minerals, volume):
        """
        var name string: name of Asteroid
        var minerals dictionary: dictionary of Minerals and their quantities composing Asteroid
        """
        self.name = name
        self.minerals = minerals
        self.volume = volume
#minerals
tritanium = Mineral("Tritanium")
pyerite = Mineral("Pyerite")
mexallon = Mineral("Mexallon")
isogen = Mineral("Isogen")
noxium = Mineral("Noxium")
zydrine = Mineral("Zydrine")
megacyte = Mineral("Megacyte")
#asteroids
arkonor = Asteroid("Arkonor", {tritanium:22000, mexallon:2500, megacyte:320}, 16.0)
bistot = Asteroid("Bistot", {pyerite:12000, zydrine:450, megacyte:100}, 16.0)
crokite = Asteroid("Crokite", {tritanium:10000, noxium:120, zydrine:135}, 16.0)
dark_ochre = Asteroid("Dark Ochre", {tritanium:21000, isogen:1600, noxium:760}, 8.0)
gneiss = Asteroid("Gneiss", {pyerite:2200, mexallon:2400, isogen:300}, 5.0)
hedbergite = Asteroid("Hedbergite", {pyerite:1000, isogen:200, noxium:100, zydrine:19}, 3.0)
hemorphite = Asteroid("Hemorphite", {tritanium:2200, isogen:100, noxium:120, zydrine:15}, 3.0)
jaspet = Asteroid("Jaspet", {mexallon:350, noxium:75, zydrine:8}, 2.0)
kernite = Asteroid("Kernite", {tritanium:134, mexallon:267, isogen:134}, 1.2)
omber = Asteroid("Omber", {tritanium:800, pyerite:100, isogen:85}, 0.6)
plagioclase = Asteroid("Plagioclase", {tritanium:107, pyerite:213, mexallon:107}, 0.35)
pyroxeres = Asteroid("Pyroxeres", {tritanium:351, pyerite:25, mexallon:50, noxium:5}, 0.3)
scordite = Asteroid("Scordite", {tritanium:346, pyerite:173}, 0.15)
spodumain = Asteroid("Spodumain", {tritanium:56000, pyerite:12050, mexallon:2100, isogen:450}, 16.0)
veldspar = Asteroid("Veldspar", {tritanium:415}, 0.1)

asteroids = [arkonor,
            bistot,
            crokite,
            dark_ochre,
            gneiss,
            hedbergite,
            hemorphite,
            jaspet,
            kernite,
            omber,
            plagioclase,
            pyroxeres,
            scordite,
            spodumain,
            veldspar]

for asteroid in asteroids:
    print(asteroid.name)
    print(asteroid.minerals)
