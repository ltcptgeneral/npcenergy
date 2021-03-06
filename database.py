class database:

    def __init__(self):

        self.skills = {
            "Thick Skin":"Nothing gets under your skin. Not words nor spearheads. Increases HP by 2.",
            "Power Strike":"You've never skipped arm day, and it shows. Increases melee damage by 8%.",
            "Power Draw":"You're biceps are toned perfectly to pulling bowstrings or throwing tables. Increases ranged damage by 10%.",
            "Power Cast":"Mind over matter amirite? Your cranium is bursting at the seams with magical knowledge. Increase magic damage by 10%.",
            "Weapons Master":"You are America's next ninja warrior. Adds 40 weapon proficiency points.",
            "Self Motivation":"Something you've never had before. Increases EXP gain by 2%.",
            "Sneak":"You don your sneakers and head out for a life of stealth. Increases chance of success in sneak related actions.",
            "Profitable":"Having spent your earlier years squandering your money, you now know how to make a profit. Increases money gained from interactions.",
            "Scavenger": "A veteran of the frontier, you know how to repurpose anything for you benefit. Increases drop rate of items by 1% and increases drop quality.",
            "Tactician":"You are Napolean's prodigy. Increases critical hit chance by 1% and increases battle retreat chance by 5%.",
            "Light Packer":"You pack just the bare essentials and are always ready for action. Increases movement speed by 1% only when below maximum carrying capacity.",
            "Heavy Packer":"Let's be honest, most of what you pack wont see the light of day. Increases maximum carrying capacity and increases armor by 1 point when over maximum carrying capacity.",
            "First Aid":"You're stuck on bandaids because bandaids stick on you. Increases effectiveness of healing items by 10%.",
            "MEDIC!":"Like a [ certain red clad regerating superhero] (except without the cancer) you can slowly but surely defy ",
            "Mechanical Engineer":"Like a true newtonian, you live by old world values. Increases chances of succeeding in mechanical engineering tasks.",
            "Software Engineer":"Oh shit I misspelled magic. Increases chances of succeeding in software engineering tasks.",
            "Speech":"It was overpowered in Falldown 3 and New Vegas so it must be overpowered here too. Increases chances of succeeding in speech related tasks.",
            "Dealer":"Not of cards, but of trade. They call it an art. Increases selling price by 10% and decreases buying price by 5%.",
            "Ultra Instinct":"It's not a skill, it's a godly power. Does something..."
            }

        self.skills_max = {
            "Thick Skin":10,
            "Power Strike":10,
            "Power Draw":10,
            "Power Cast":10,
            "Weapons Master":10,
            "Self Motivation":10,
            "Sneak":10,
            "Profitable":10,
            "Scavenger": 10,
            "Tactician":10,
            "Light Packer": 10,
            "Heavy Packer":10,
            "First Aid":10,
            "MEDIC!":10,
            "Engineer":10,
            "Software Engineer":10,
            "Speech":100,
            "Dealer":10,
            "Ultra Instinct":1
            }

        self.families = {
            "1":{
                "Thick Skin":0,
                "Power Strike":0,
                "Power Draw":0,
                "Power Cast":0,
                "Weapons Master":0,
                "Self Motivation":1,
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
                "Speech":2,
                "Dealer":0,
                "Ultra Instinct":0
                },
            "2":{
                "Thick Skin":0,
                "Power Strike":0,
                "Power Draw":0,
                "Power Cast":0,
                "Weapons Master":0,
                "Self Motivation":0,
                "Sneak":0,
                "Profitable":1,
                "Scavenger":0,
                "Tactician":0,
                "Light Packer":0,
                "Heavy Packer":1,
                "First Aid":0,
                "MEDIC!":0,
                "Engineer":0,
                "Software Engineer":0,
                "Speech":0,
                "Dealer":1,
                "Ultra Instinct":0
                },
            "3":{
                "Thick Skin":1,
                "Power Strike":0,
                "Power Draw":0,
                "Power Cast":0,
                "Weapons Master":1,
                "Self Motivation":1,
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
                },
            "4":{
                "Thick Skin":0,
                "Power Strike":0,
                "Power Draw":1,
                "Power Cast":0,
                "Weapons Master":1,
                "Self Motivation":0,
                "Sneak":0,
                "Profitable":0,
                "Scavenger":1,
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
                },
            "5":{
                "Thick Skin":0,
                "Power Strike":0,
                "Power Draw":0,
                "Power Cast":0,
                "Weapons Master":0,
                "Self Motivation":0,
                "Sneak":0,
                "Profitable":0,
                "Scavenger":1,
                "Tactician":0,
                "Light Packer":1,
                "Heavy Packer":0,
                "First Aid":1,
                "MEDIC!":0,
                "Engineer":0,
                "Software Engineer":0,
                "Speech":0,
                "Dealer":0,
                "Ultra Instinct":0
                },
            "6":{
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
                "Ultra Instinct":1
                }
            }

        self.childhoods = {
            "1":{
                "Thick Skin":0,
                "Power Strike":0,
                "Power Draw":0,
                "Power Cast":0,
                "Weapons Master":0,
                "Self Motivation":0,
                "Sneak":0,
                "Profitable":1,
                "Scavenger":0,
                "Tactician":0,
                "Light Packer":0,
                "Heavy Packer":0,
                "First Aid":0,
                "MEDIC!":0,
                "Engineer":1,
                "Software Engineer":0,
                "Speech":1,
                "Dealer":0,
                "Ultra Instinct":0
                },
            "2":{
                "Thick Skin":0,
                "Power Strike":0,
                "Power Draw":0,
                "Power Cast":0,
                "Weapons Master":0,
                "Self Motivation":1,
                "Sneak":0,
                "Profitable":0,
                "Scavenger":0,
                "Tactician":0,
                "Light Packer":0,
                "Heavy Packer":0,
                "First Aid":0,
                "MEDIC!":0,
                "Engineer":2,
                "Software Engineer":0,
                "Speech":0,
                "Dealer":0,
                "Ultra Instinct":0
                },
            "3":{
                "Thick Skin":0,
                "Power Strike":0,
                "Power Draw":0,
                "Power Cast":0,
                "Weapons Master":0,
                "Self Motivation":1,
                "Sneak":0,
                "Profitable":0,
                "Scavenger":0,
                "Tactician":0,
                "Light Packer":0,
                "Heavy Packer":0,
                "First Aid":0,
                "MEDIC!":0,
                "Engineer":0,
                "Software Engineer":2,
                "Speech":0,
                "Dealer":0,
                "Ultra Instinct":0
                },
            "4":{
                "Thick Skin":1,
                "Power Strike":0,
                "Power Draw":0,
                "Power Cast":0,
                "Weapons Master":0,
                "Self Motivation":0,
                "Sneak":1,
                "Profitable":0,
                "Scavenger":1,
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
                },
            "5":{
                "Thick Skin":1,
                "Power Strike":0,
                "Power Draw":0,
                "Power Cast":0,
                "Weapons Master":0,
                "Self Motivation":0,
                "Sneak":0,
                "Profitable":0,
                "Scavenger":1,
                "Tactician":0,
                "Light Packer":0,
                "Heavy Packer":0,
                "First Aid":0,
                "MEDIC!":0,
                "Engineer":1,
                "Software Engineer":0,
                "Speech":0,
                "Dealer":0,
                "Ultra Instinct":0
                }
            }

        self.jobs = {
            "1":{
                "Thick Skin":1,
                "Power Strike":2,
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
                },
            "2":{
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
                "Speech":5,
                "Dealer":0,
                "Ultra Instinct":0
                },
            "3":{
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
                "Engineer":3,
                "Software Engineer":0,
                "Speech":0,
                "Dealer":0,
                "Ultra Instinct":0
                },
            "4":{
                "Thick Skin":0,
                "Power Strike":0,
                "Power Draw":0,
                "Power Cast":0,
                "Weapons Master":0,
                "Self Motivation":0,
                "Sneak":0,
                "Profitable":2,
                "Scavenger":0,
                "Tactician":0,
                "Light Packer":0,
                "Heavy Packer":1,
                "First Aid":0,
                "MEDIC!":0,
                "Engineer":0,
                "Software Engineer":0,
                "Speech":0,
                "Dealer":0,
                "Ultra Instinct":0
                },
            "5":{
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
                "Engineer":3,
                "Software Engineer":0,
                "Speech":0,
                "Dealer":0,
                "Ultra Instinct":0
                },
            "6":{
                "Thick Skin":0,
                "Power Strike":0,
                "Power Draw":2,
                "Power Cast":0,
                "Weapons Master":0,
                "Self Motivation":0,
                "Sneak":0,
                "Profitable":0,
                "Scavenger":1,
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
                },
            "7":{
                "Thick Skin":0,
                "Power Strike":0,
                "Power Draw":0,
                "Power Cast":0,
                "Weapons Master":0,
                "Self Motivation":0,
                "Sneak":2,
                "Profitable":0,
                "Scavenger":0,
                "Tactician":1,
                "Light Packer":0,
                "Heavy Packer":0,
                "First Aid":0,
                "MEDIC!":0,
                "Engineer":0,
                "Software Engineer":0,
                "Speech":0,
                "Dealer":0,
                "Ultra Instinct":0
                },
            "8":{
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
                "Software Engineer":3,
                "Speech":0,
                "Dealer":0,
                "Ultra Instinct":0
                }
            }

    def getskills(self):

        return self.skills

    def getmaxskills(self):

        return self.skills_max

    def getfamilies(self):

        return self.families

    def getchildhoods(self):

        return self.childhoods

    def getjobs(self):

        return self.jobs
