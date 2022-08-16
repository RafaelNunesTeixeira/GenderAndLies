from otree.api import *

doc = ""

class Constants(BaseConstants):
    name_in_url = 'Beliefs'
    players_per_group = None
    num_rounds = 1
    instructions_template =  'Receiver/instructions.html'
    # """Amount allocated to each player"""
    rounds = 1
    contact =  'Receiver/contact.html'
    papercups_template = 'Receiver/papercups.html'
    match =  __name__ + '/match.html'
    role = 'Participant 2'
    nationality = 'U.S.'
    age = '20-30'



class Subsession(BaseSubsession):
    pass

def creating_session(subsession):

    for player in subsession.get_players():
        if player.id_in_group % 2 == 0:
            player.gender = 'Male'
        else:
            player.gender = 'Female'


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    gender = models.StringField()

    """"empirical"""
    expblue = models.IntegerField(min=0,max=100)
    expgreen = models.IntegerField(min=0,max=100)
    punblue = models.IntegerField(min=0,max=100)
    pungreen = models.IntegerField(min=0,max=100)



    """"normative"""

    normsblue1 = models.IntegerField()
    normsgreen1 = models.IntegerField()
    normsblue2 = models.IntegerField()
    normsgreen2 = models.IntegerField()

    normsblue1p = models.IntegerField()
    normsgreen1p = models.IntegerField()
    normsblue2p = models.IntegerField()
    normsgreen2p = models.IntegerField()


    """normative b-xiao"""
    bnormsblue1 = models.IntegerField()
    bnormsgreen1 = models.IntegerField()
    bnormsblue2 = models.IntegerField()
    bnormsgreen2 = models.IntegerField()

    bnormsblue1p = models.IntegerField()
    bnormsgreen1p = models.IntegerField()
    bnormsblue2p = models.IntegerField()
    bnormsgreen2p = models.IntegerField()

    """"perception"""
    perblue1 = models.IntegerField()
    perblue2 = models.IntegerField()
    perblue3 = models.IntegerField()
    perblue4 = models.IntegerField()
    perblue5 = models.IntegerField()

    perblue1p = models.IntegerField()
    perblue2p = models.IntegerField()
    perblue3p = models.IntegerField()
    perblue4p = models.IntegerField()
    perblue5p = models.IntegerField()


class empinst(Page):
    pass

class emp1(Page):
    form_model = 'player'
    form_fields = ['expblue', 'expgreen']

class emp2(Page):
    form_model = 'player'
    form_fields = ['punblue', 'pungreen']



class norminst(Page):
    pass


class norm1(Page):
    form_model = 'player'
    form_fields = [ 'normsblue1','normsblue2', 'normsgreen1','normsgreen2']

class norm2(Page):
    form_model = 'player'
    form_fields = [ 'normsblue1p','normsblue2p', 'normsgreen1p','normsgreen2p']

class norm3(Page):
    form_model = 'player'
    form_fields = [ 'bnormsblue1','bnormsblue2', 'bnormsgreen1','bnormsgreen2']

class norm4(Page):
        form_model = 'player'
        form_fields = ['bnormsblue1p', 'bnormsblue2p', 'bnormsgreen1p', 'bnormsgreen2p']


class perception1(Page):
    form_model = 'player'
    form_fields = ['perblue1', 'perblue2', 'perblue3', 'perblue4', 'perblue5']


class perception2(Page):
    form_model = 'player'
    form_fields = ['perblue1p', 'perblue2p', 'perblue3p', 'perblue4p', 'perblue5p']

page_sequence = [empinst,emp1, norm3,norm1,perception1]

