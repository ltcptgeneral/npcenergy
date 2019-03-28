class enemy:

    def __init__(self, nname, ntitle, nstats, nstatus, nitems):

        self.name = nname
        self.title = ntitle #for special enemies
        self.stats = nstats
        self.status = nstatus
        self.items = nitems
        """
        self.stats = {
            "hp":0,
            "attk":0,
            "defence":0
            }
        self.status = {
            "hp":0,
            "attk":0,
            "defence":0,
            "effects":[]
            }
        self.items = []
        """

    def getname(self):

        return name

    def gettitle(self):

        return title

    def getstats(self):

        return stats

    def getstatus(self):

        return status

    def getitems(self):

        return items

    def setname(self, nname):

        self.name = nname

    def settitle(self, ntitle):

        self.title = ntitle

    def setstats(self, nstats):

        self.stats = nstats

    def setstatus(self, nstatus):

        self.status = nstatus

    def setitems(self, nitems):

        self.items = nitems
