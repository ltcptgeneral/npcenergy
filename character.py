class character:

    def __init__(self):

        self.name = ""
        self.gender = ""
        self.exp = 0
        self.money = 0
        
        self.base_stats = {
            "hp":0,
            "attk": 0,
            "defence":0,
            "intellect":0
            } #max hp, attk, def, int
        self.attributes = {
            "hp":0,
            "attk": 0,
            "defence":0,
            "intellect":0
            } #hp, strength, defense, int
        self.adjusted_stats = {
            "hp":0,
            "attk": 0,
            "defence":0,
            "intellect":0
            } #max hp, attk, def, int

        self.status = {
            "hp":0,
            "effects":[]
            } #current hp, [buffs/debuffs]
        
        self.skills = {
            "Thick Skin":0,
            "Power Strike":0,
            "Power Draw":0,
            "Power Cast":0,
            "Weapons Master":0,
            "Self Motivation":0,
            "Sneak":0,
            "Profitable":0,
            "Scavenger":0,
            "Tactician":0,
            "Light Packer":0,
            "Heavy Packer":0,
            "First Aid":0,
            "MEDIC!":0,
            "Engineer":0,
            "Software Engineer":0,
            "Speech":0,
            "Dealer":0,
            "Ultra Instinct":0
            }

        self.loadout = {
            "head":None,
            "shoulders":None,
            "knees":None,
            "toes":None,
            "melee":None,
            "ranged":None,
            "magic":None
            }

        self.inventory = []

        self.magic_inventory = []
        
    def getname(self):

        return self.name

    def getgender(self):

        return self.gender

    def getexp(self):

        return self.exp

    def getmoney(self):

        return self.money

    def getbasestats(self):

        return self.base_stats

    def getattributes(self):

        return self.attributes

    def getadjustedstats(self):

        return self.adjusted_stats

    def getstatus(self):

        return self.status

    def getskills(self):

        return self.skills

    def getloadout(self):

        return self.loadout

    def getinventory(self):

        return self.inventory

    def getmagicinventory(self):

        return self.magic_inventory

    def setname(self, nname):

        self.name = nname

    def setgender(self, ngender):

        self.gender = ngender

    def setexp(self, nexp):

        self.exp = nexp

    def setmoney(self, nmoney):

        self.money = nmoney

    def setbasestats(self, nbase_stats):

        self.base_stats = nbase_stats

    def setattributes(self, nattributes):

        self.attributes = nattributes

    def setadjustedstats(self, nadjusted_stats):

        self.adjusted_stats = nadjusted_stats

    def setstatus(self, nstatus):

        self.status = status

    def setskills(self, nskills):

        self.skills = nskills

    def setloadout(self, nloadout):

        self.loadout = nloadout

    def setinventory(self, ninventory):

        self.inventory = ninventory

    def setmagicinventory(self, nmagic_inventory):

        self.magic_inventory = nmagic_inventory
