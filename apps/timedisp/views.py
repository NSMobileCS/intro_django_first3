from datetime import datetime
from django.shortcuts import render
# Create your views here.


def index(request):
    now = datetime.now()
    context = {
        'datestring': now.strftime('%b %d, %Y'),
        'timestring': now.strftime('%-I:%M%P'),
    }
    return render(request, 'timedisp/index.html', context=context)
