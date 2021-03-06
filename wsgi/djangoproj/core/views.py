from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from data_mock import token, heroes


@csrf_exempt
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
    if request.META.get('HTTP_AUTHORIZATION') == token:
        return JsonResponse({'status': 'logged_in', 'msg': 'hai ela'})
    return JsonResponse({'msg': 'unauthorized'}, status=401)


def get_hero(pk):
    try:
        return [i for i in heroes if i.get('id') == int(pk)][0]
    except Exception, e:
        print e
        return None


def heroes_list(request):
    if request.META.get('HTTP_AUTHORIZATION') == token:
        print token, request.META.get('HTTP_AUTHORIZATION')
        return JsonResponse(heroes, safe=False)
    return JsonResponse({'msg': 'unauthorized'}, status=401)


def hero(request, pk):
    print pk
    if request.META.get('HTTP_AUTHORIZATION') == token:

        hero = get_hero(pk)
        if not hero:
            hero = {'msg': 'not found'}
            status_code = 404
        else:
            status_code = 200

        return JsonResponse(hero, status=status_code)
    return JsonResponse({'msg': 'unauthorized'}, status=401)
