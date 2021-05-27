from django.shortcuts import render

def index(request):
    from datetime import datetime
    from .libs import test

    context = dict()
    
    time = dict()
    time['time'] = datetime.now().strftime("%H:%M")
    time['date'] = datetime.now().strftime('%d/%m/%Y')
    context['time'] = time

    status = dict()
    status['pihole'] = test.check_pihole()
    status['cups'] = test.check_cups()
    context['status'] = status

    return render(request, 'dashboard/index2.html', context=context)