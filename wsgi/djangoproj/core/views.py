from django.http import JsonResponse
from data_mock import token, heroes


def login(request):
    if request.POST:
        u = request.POST.get('username')
        p = request.POST.get('password')

        if (u == 'ela' and p == 'ela'):
            data = {'status': 'success', 'token': token}
            status_code = 200
        else:
            data = {
                'status': 'failed', 'msg': 'invalid username and password.'}
            status_code = 400

        return JsonResponse(data, status=status_code)

    return JsonResponse({'msg': 'GET method not allowed.'})


def me(request):
    if request.META.get('AUTHORIZATION') == token:
        return JsonResponse({'status': 'logged_in', 'msg': 'hai ela'})
    return JsonResponse({'msg': 'unauthorized'}, status=401)


def get_hero(pk):
    try:
        return [i for i in heroes if i.get('id') == pk][0]
    except:
        return None


def heroes_list(request):
    if request.META.get('AUTHORIZATION') == token:
        return JsonResponse(heroes)
    return JsonResponse({'msg': 'unauthorized'}, status=401)


def hero(request, pk):
    if request.META.get('AUTHORIZATION') == token:

        hero = get_hero(pk)
        if not hero:
            hero = {'msg': 'not found'}
            status_code = 404
        else:
            status_code = 200

        return JsonResponse(hero, status=status_code)
    return JsonResponse({'msg': 'unauthorized'}, status=401)
