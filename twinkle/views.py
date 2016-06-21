from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from models import Twinkle
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.db.models import Count
from django.contrib.auth import authenticate, login
from forms import LoginForm
from django.http import HttpResponse

def twinkle_list(request, tag_slug=None):
    object_list = Twinkle.published.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        twinkles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        twinkles = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        twinkles = paginator.page(paginator.num_pages)
    return render(request, 'twinkle/Twinkle/list.html', {'page': page,
                                                   'twinkles': twinkles,
                                                         'tag': tag})


class TwinkleListView(ListView):
    queryset = Twinkle.published.all()
    context_object_name = 'twinkles'
    paginate_by = 5
    template_name = 'twinkle/Twinkle/list.html'

def twinkle_detail(request, year, month, day, slug):
    twinkle = get_object_or_404(Twinkle, slug=slug,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day)
    # List of similar posts
    twinkle_tags_ids = twinkle.tags.values_list('id', flat=True)
    similar_twinkles = Twinkle.published.filter(tags__in=twinkle_tags_ids).exclude(id=twinkle.id)
    similar_twinkles = similar_twinkles.annotate(same_tags=Count('tags')).order_by('-same_tags',
                                                                             '-publish')[:4]
    return render(request,'twinkle/Twinkle/detail.html',{'twinkle': twinkle,
                  'similar_twinkles': similar_twinkles})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'twinkle/login/login.html', {'form': form})

from django.contrib.auth.decorators import login_required
@login_required
def dashboard(request):
    return render(request,'twinkle/dashboard.html',{'section': 'dashboard'})
