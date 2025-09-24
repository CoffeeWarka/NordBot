from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PriceList, Promotion


@login_required
def dashboard(request):
    price_list_count = PriceList.objects.count()
    promotion_count = Promotion.objects.count()

    context = {
        'price_list_count' : price_list_count,
        'promotion_count' : promotion_count
    }
    return render(request, 'bot_dashboard/dashboard.html', context)