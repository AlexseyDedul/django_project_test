# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Channel(models.Model):
    idchannel = models.IntegerField(primary_key=True)
    strchannel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'channel'
        app_label = 'thesportdb_data'


class Contract(models.Model):
    idcontract = models.IntegerField(primary_key=True)
    idplayer = models.ForeignKey('Player', models.DO_NOTHING, db_column='idplayer', blank=True, null=True)
    idteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='idteam', blank=True, null=True)
    strsport = models.TextField(blank=True, null=True)
    strplayer = models.TextField(blank=True, null=True)
    strteam = models.TextField(blank=True, null=True)
    strteambadge = models.TextField(blank=True, null=True)
    stryearstart = models.TextField(blank=True, null=True)
    stryearend = models.TextField(blank=True, null=True)
    strwage = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract'
        app_label = 'thesportdb_data'


class Countries(models.Model):
    name_en = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'
        app_label = 'thesportdb_data'


class Team(models.Model):
    idteam = models.IntegerField(primary_key=True)
    strteam = models.TextField(blank=True, null=True)
    stralternate = models.TextField(blank=True, null=True)
    intformedyear = models.IntegerField(blank=True, null=True)
    strsport = models.TextField(blank=True, null=True)
    strleague = models.TextField(blank=True, null=True)
    strdivision = models.TextField(blank=True, null=True)
    strmanager = models.TextField(blank=True, null=True)
    strstadium = models.TextField(blank=True, null=True)
    strrss = models.TextField(blank=True, null=True)
    strstadiumthumb = models.TextField(blank=True, null=True)
    strstadiumdescription = models.TextField(blank=True, null=True)
    strstadiumlocation = models.TextField(blank=True, null=True)
    intstadiumcapacity = models.TextField(blank=True, null=True)
    strwebsite = models.TextField(blank=True, null=True)
    strfacebook = models.TextField(blank=True, null=True)
    strtwitter = models.TextField(blank=True, null=True)
    stryoutube = models.TextField(blank=True, null=True)
    strinstagram = models.TextField(blank=True, null=True)
    strdescriptionen = models.TextField(blank=True, null=True)
    strdescriptionru = models.TextField(blank=True, null=True)
    strgender = models.TextField(blank=True, null=True)
    strcountry = models.TextField(blank=True, null=True)
    strteambadge = models.TextField(blank=True, null=True)
    strteamjersey = models.TextField(blank=True, null=True)
    strteamlogo = models.TextField(blank=True, null=True)
    strteambanner = models.TextField(blank=True, null=True)
    strteamfanart1 = models.TextField(blank=True, null=True)
    strteamfanart2 = models.TextField(blank=True, null=True)
    strteamfanart3 = models.TextField(blank=True, null=True)
    strteamfanart4 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'
        app_label = 'thesportdb_data'


class Events(models.Model):
    idevent = models.IntegerField(primary_key=True)
    idleague = models.ForeignKey('League', models.DO_NOTHING, db_column='idleague', blank=True, null=True)
    strsport = models.TextField(blank=True, null=True)
    strevent = models.TextField(blank=True, null=True)
    streventalternate = models.TextField(blank=True, null=True)
    idhometeam = models.ForeignKey('Team', models.DO_NOTHING, db_column='idhometeam', related_name='idhometeam+', blank=True, null=True)
    idawayteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='idawayteam', blank=True, null=True)
    strfilename = models.TextField(blank=True, null=True)
    strseason = models.TextField(blank=True, null=True)
    strdescriptionen = models.TextField(blank=True, null=True)
    inthomescore = models.IntegerField(blank=True, null=True)
    intround = models.IntegerField(blank=True, null=True)
    intawayscore = models.IntegerField(blank=True, null=True)
    intspectators = models.IntegerField(blank=True, null=True)
    strofficial = models.TextField(blank=True, null=True)
    strtimestamp = models.TextField(blank=True, null=True)
    dateevent = models.TextField(blank=True, null=True)
    dateeventlocal = models.TextField(blank=True, null=True)
    strtime = models.TextField(blank=True, null=True)
    strtimelocal = models.TextField(blank=True, null=True)
    strtvstation = models.TextField(blank=True, null=True)
    strresult = models.TextField(blank=True, null=True)
    strvenue = models.TextField(blank=True, null=True)
    strcountry = models.TextField(blank=True, null=True)
    strcity = models.TextField(blank=True, null=True)
    strposter = models.TextField(blank=True, null=True)
    strsquare = models.TextField(blank=True, null=True)
    strfanart = models.TextField(blank=True, null=True)
    strthumb = models.TextField(blank=True, null=True)
    strbanner = models.TextField(blank=True, null=True)
    strmap = models.TextField(blank=True, null=True)
    strvideo = models.TextField(blank=True, null=True)
    strstatus = models.TextField(blank=True, null=True)
    strpostponed = models.TextField(blank=True, null=True)
    strlocked = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'
        app_label = 'thesportdb_data'


class Eventstats(models.Model):
    idstatistic = models.IntegerField(primary_key=True)
    idevent = models.ForeignKey(Events, models.DO_NOTHING, db_column='idevent', blank=True, null=True)
    strevent = models.TextField(blank=True, null=True)
    strstat = models.TextField(blank=True, null=True)
    inthome = models.IntegerField(blank=True, null=True)
    intaway = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventstats'
        app_label = 'thesportdb_data'


class Eventtv(models.Model):
    id = models.IntegerField(primary_key=True)
    idevent = models.ForeignKey(Events, models.DO_NOTHING, db_column='idevent', blank=True, null=True)
    idchannel = models.ForeignKey(Channel, models.DO_NOTHING, db_column='idchannel', blank=True, null=True)
    strcountry = models.TextField(blank=True, null=True)
    strlogo = models.TextField(blank=True, null=True)
    strseason = models.TextField(blank=True, null=True)
    strtime = models.TextField(blank=True, null=True)
    dateevent = models.TextField(blank=True, null=True)
    strtimestamp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventtv'
        app_label = 'thesportdb_data'


class Formerteam(models.Model):
    idformerteam = models.IntegerField(primary_key=True)
    idplayer = models.ForeignKey('Player', models.DO_NOTHING, db_column='idplayer', blank=True, null=True)
    idteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='idteam', blank=True, null=True)
    strsport = models.TextField(blank=True, null=True)
    strplayer = models.TextField(blank=True, null=True)
    strformerteam = models.TextField(blank=True, null=True)
    strmovetype = models.TextField(blank=True, null=True)
    strteambadge = models.TextField(blank=True, null=True)
    strjoined = models.TextField(blank=True, null=True)
    strdeparted = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formerteam'
        app_label = 'thesportdb_data'


class Honoursteam(models.Model):
    idhonoursteam = models.IntegerField(primary_key=True)
    idplayer = models.ForeignKey('Player', models.DO_NOTHING, db_column='idplayer', blank=True, null=True)
    idteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='idteam', blank=True, null=True)
    strsport = models.TextField(blank=True, null=True)
    strplayer = models.TextField(blank=True, null=True)
    strteam = models.TextField(blank=True, null=True)
    strhonour = models.TextField(blank=True, null=True)
    strseason = models.TextField(blank=True, null=True)
    intchecked = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'honoursteam'
        app_label = 'thesportdb_data'


class League(models.Model):
    idleague = models.IntegerField(primary_key=True)
    strsport = models.TextField(blank=True, null=True)
    strleague = models.TextField(blank=True, null=True)
    strleaguealternate = models.TextField(blank=True, null=True)
    intdivision = models.IntegerField(blank=True, null=True)
    strcurrentseason = models.TextField(blank=True, null=True)
    intformedyear = models.IntegerField(blank=True, null=True)
    datefirstevent = models.TextField(blank=True, null=True)
    strcountry = models.TextField(blank=True, null=True)
    strwebsite = models.TextField(blank=True, null=True)
    strfacebook = models.TextField(blank=True, null=True)
    strtwitter = models.TextField(blank=True, null=True)
    stryoutube = models.TextField(blank=True, null=True)
    strrss = models.TextField(blank=True, null=True)
    strdescriptionen = models.TextField(blank=True, null=True)
    strdescriptionru = models.TextField(blank=True, null=True)
    strtvrights = models.TextField(blank=True, null=True)
    strfanart1 = models.TextField(blank=True, null=True)
    strfanart2 = models.TextField(blank=True, null=True)
    strfanart3 = models.TextField(blank=True, null=True)
    strfanart4 = models.TextField(blank=True, null=True)
    strbanner = models.TextField(blank=True, null=True)
    strbadge = models.TextField(blank=True, null=True)
    strlogo = models.TextField(blank=True, null=True)
    strposter = models.TextField(blank=True, null=True)
    strtrophy = models.TextField(blank=True, null=True)
    strnaming = models.TextField(blank=True, null=True)
    strcomplete = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'league'
        app_label = 'thesportdb_data'


class Lineup(models.Model):
    idlineup = models.IntegerField(primary_key=True)
    idevent = models.ForeignKey(Events, models.DO_NOTHING, db_column='idevent', blank=True, null=True)
    idplayer = models.ForeignKey('Player', models.DO_NOTHING, db_column='idplayer', blank=True, null=True)
    idteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='idteam', blank=True, null=True)
    strevent = models.TextField(blank=True, null=True)
    strposition = models.TextField(blank=True, null=True)
    strpositionshort = models.TextField(blank=True, null=True)
    strformation = models.IntegerField(blank=True, null=True)
    strhome = models.TextField(blank=True, null=True)
    strsubstitute = models.TextField(blank=True, null=True)
    intsquadnumber = models.TextField(blank=True, null=True)
    strcountry = models.TextField(blank=True, null=True)
    strseason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lineup'
        app_label = 'thesportdb_data'


class Player(models.Model):
    idplayer = models.IntegerField(primary_key=True)
    idplayermanager = models.IntegerField(blank=True, null=True)
    strnationality = models.TextField(blank=True, null=True)
    strplayer = models.TextField(blank=True, null=True)
    strteam = models.TextField(blank=True, null=True)
    strsport = models.TextField(blank=True, null=True)
    dateborn = models.TextField(blank=True, null=True)
    strnumber = models.TextField(blank=True, null=True)
    datesigned = models.TextField(blank=True, null=True)
    strsigning = models.TextField(blank=True, null=True)
    strwage = models.TextField(blank=True, null=True)
    stroutfitter = models.TextField(blank=True, null=True)
    strkit = models.TextField(blank=True, null=True)
    stragent = models.TextField(blank=True, null=True)
    strbirthlocation = models.TextField(blank=True, null=True)
    strdescriptionen = models.TextField(blank=True, null=True)
    strdescriptionru = models.TextField(blank=True, null=True)
    strgender = models.TextField(blank=True, null=True)
    strside = models.TextField(blank=True, null=True)
    strposition = models.TextField(blank=True, null=True)
    strfacebook = models.TextField(blank=True, null=True)
    strwebsite = models.TextField(blank=True, null=True)
    strtwitter = models.TextField(blank=True, null=True)
    strinstagram = models.TextField(blank=True, null=True)
    stryoutube = models.TextField(blank=True, null=True)
    strheight = models.TextField(blank=True, null=True)
    strweight = models.TextField(blank=True, null=True)
    strthumb = models.TextField(blank=True, null=True)
    strfanart1 = models.TextField(blank=True, null=True)
    strfanart2 = models.TextField(blank=True, null=True)
    strfanart3 = models.TextField(blank=True, null=True)
    strfanart4 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'
        app_label = 'thesportdb_data'


class Playerteam(models.Model):
    idplayer = models.ForeignKey(Player, models.DO_NOTHING, db_column='idplayer', blank=True, null=True)
    idteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='idteam', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playerteam'
        app_label = 'thesportdb_data'


class Sports(models.Model):
    idsport = models.IntegerField(primary_key=True)
    strsport = models.TextField(blank=True, null=True)
    strformat = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports'
        app_label = 'thesportdb_data'


class Tables(models.Model):
    idstanding = models.IntegerField(primary_key=True)
    intrank = models.IntegerField(blank=True, null=True)
    idteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='idteam', blank=True, null=True)
    idleague = models.ForeignKey(League, models.DO_NOTHING, db_column='idleague', blank=True, null=True)
    strseason = models.TextField(blank=True, null=True)
    strform = models.TextField(blank=True, null=True)
    strdescription = models.TextField(blank=True, null=True)
    intplayed = models.IntegerField(blank=True, null=True)
    intwin = models.IntegerField(blank=True, null=True)
    intloss = models.IntegerField(blank=True, null=True)
    intdraw = models.IntegerField(blank=True, null=True)
    intgoalsfor = models.IntegerField(blank=True, null=True)
    intgoalsagainst = models.IntegerField(blank=True, null=True)
    intgoaldifference = models.IntegerField(blank=True, null=True)
    intpoints = models.IntegerField(blank=True, null=True)
    dateupdated = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tables'
        app_label = 'thesportdb_data'


class Teamleague(models.Model):
    idleague = models.ForeignKey(League, models.DO_NOTHING, db_column='idleague', blank=True, null=True)
    idteam = models.ForeignKey(Team, models.DO_NOTHING, db_column='idteam', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamleague'
        app_label = 'thesportdb_data'


class Timeline(models.Model):
    idtimeline = models.IntegerField(primary_key=True)
    idevent = models.ForeignKey(Events, models.DO_NOTHING, db_column='idevent', blank=True, null=True)
    idplayer = models.ForeignKey(Player, models.DO_NOTHING, db_column='idplayer', blank=True, null=True)
    idteam = models.ForeignKey(Team, models.DO_NOTHING, db_column='idteam', blank=True, null=True)
    strtimeline = models.TextField(blank=True, null=True)
    strtimelinedetail = models.TextField(blank=True, null=True)
    strhome = models.TextField(blank=True, null=True)
    strevent = models.TextField(blank=True, null=True)
    strcountry = models.TextField(blank=True, null=True)
    idassist = models.IntegerField(blank=True, null=True)
    strassist = models.TextField(blank=True, null=True)
    inttime = models.TextField(blank=True, null=True)
    strcomment = models.TextField(blank=True, null=True)
    dateevent = models.TextField(blank=True, null=True)
    strseason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timeline'
        app_label = 'thesportdb_data'
