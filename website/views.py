from django.shortcuts import render

# Create your views here.
def index(request):
    import datetime
    agora = datetime.datetime.now()
    context = {
        'hora': agora.hour,
        'minuto': agora.minute,
        'segundo': agora.second,
        'amigos': [
            'Mickey',
            'Pluto',
            'Donald'
        ]
    }

    return render(request, 'website/index.html', context)

def about(request):
    return render(request, 'website/about.html')