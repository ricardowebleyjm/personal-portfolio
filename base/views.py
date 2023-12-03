from django.views.decorators.cache import cache_page
from django.shortcuts import render

from base.models import PageVisits

@cache_page(60 * 15)  # Cache for 15 minutes (in seconds)
def index(request):
    view_name = request.resolver_match.view_name
    page, created = PageVisits.objects.get_or_create(page_name=view_name)
    page.total_count += 1
    page.save()
    total_page_count = page.total_count #PageVisits.objects.filter(page_name=view_name).aggregate(total_count=Sum('total_count'))['total_count'] or 0
    
    context = {
        'total_page_count': total_page_count,
    }

    return render(request, 'base/base_template.html', context)
