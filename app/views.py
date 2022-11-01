from django.db.models import OuterRef
from django.http import JsonResponse

from app.models import Countries, Events, Contract, Player, League, Teamleague, Team


def countries(request):
    countr = Countries.objects.values('name_en')
    for c in countr:
        print(c)
    return JsonResponse({'countries': list(countr)})


def league(request):
    # tmp = League.objects.filter(
    #     idleague=4328
    # ).values('idleague')
    # print(tmp[0]['idleague'])
    # tl = Teamleague.objects.filter(idleague=tmp[0]['idleague']).values_list('idteam', flat=True)
    # print(tl)
    # for t in tl:
    #     team = Team.objects.filter(idteam=t).values('idteam', 'strteam')
    # print(team)
    team = League.objects.raw(
                            '''
                            select league.idleague, league.strleague, team.idteam, team.strteam from league left join teamleague on league.idleague=teamleague.idleague
                            left join team on team.idteam=teamleague.idteam
                            ''')
    d = []
    for t in team:
        d.append(t.idleague)
    s = set(d)
    arr = []
    for i in s:
        tmp = []
        for j in team:
            if i == j.idleague:
                tmp.append({
                    'idteam': j.idteam,
                    'strteam': j.strteam
                })

        arr.append({
            'idleague': i,
            'teams': tmp
        })

        # arr.append({
        #     'idleague': t.idleague,
        #     'strleague': t.strleague,
        #     'teams': [
        #         {
        #             'idteam': t.idteam,
        #             'strteam': t.strteam
        #         }
        #
        #     ]
        # })
    print({'t': arr})
    return JsonResponse({'t': arr})


def events(request):
    events = Events.objects.filter(strsport='Soccer').values('idevent', 'idleague_id', 'strsport', 'strdescriptionen', 'idhometeam_id', 'idawayteam_id')
    # events = Events.objects.filter(strsport='Soccer').values()
    for e in events:
        print(e)
    return JsonResponse({'events': list(events)})
