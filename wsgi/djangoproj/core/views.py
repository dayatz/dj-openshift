from django.shortcuts import render
from django.http import JsonResponse


def login(request):
    if request.POST:
        u = request.POST.get('username')
        p = request.POST.get('password')

        if (u == 'ela' and p == 'ela'):
            data = {'status': 'success', 'token': 'eladayat'}
            status_code = 200
        else:
            data = {'status': 'failed', 'msg':'invalid username and password.'}
            status_code = 400

        return JsonResponse(data, status=status_code)
           

    return JsonResponse({'msg': 'GET method not allowed.'})


def me(request):
        token = 'eladayat'
	if request.META.get('Authorization') == token:
            return JsonResponse({'status': 'logged_in', 'msg': 'hai ela'})
        return JsonResponse({'msg': 'invalid provided credential'}, status=401)
