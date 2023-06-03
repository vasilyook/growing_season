from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render, reverse
from .models import Seed
from .forms import SeedForm


def index(request):
    query_dict = request.GET
    print(query_dict)
    saved_seeds = Seed.objects.order_by('-id')
    year = ['я', 'ф', 'м', 'а', 'м', 'и', 'и', 'а', 'с', 'о', 'н', 'д']
    sow_way_emoji = {'into_the_ground': '🪴', 'through_seedlings': '🖼', 'both': '🪴🖼'}
    context = {
        'saved_seeds': saved_seeds,
        'count_l': range(1, 13),
        'count_h': range(2),
        'year': year,
        'sow_way_emoji': sow_way_emoji,
    }
    return render(request, 'index.html', context)


def creation(request):
    return render(request, 'create.html', {})


def save_seed(request):
    s = SeedForm(request.POST)
    s.save()
    return redirect(reverse('timetable:create'))

