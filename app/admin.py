from django.contrib import admin

from app.models import Channel, Contract, Countries, Events, Eventstats, Eventtv, Formerteam, Honoursteam, League, \
    Player, Playerteam, Sports, Tables, Team, Teamleague, Timeline

admin.site.register(Channel)
admin.site.register(Contract)
admin.site.register(Countries)
admin.site.register(Events)
admin.site.register(Eventstats)
admin.site.register(Eventtv)
admin.site.register(Formerteam)
admin.site.register(Honoursteam)
admin.site.register(League)
admin.site.register(Player)
admin.site.register(Playerteam)
admin.site.register(Sports)
admin.site.register(Tables)
admin.site.register(Team)
admin.site.register(Teamleague)
admin.site.register(Timeline)