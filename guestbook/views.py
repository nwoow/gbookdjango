from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Person
from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.
def index(request):
    pname = Person.objects.order_by('-pub_date')[:5]
    context = {'pname': pname}
    return render(request, 'guestbook/index.html', context)

def detail(request, person_id):
    pname = get_object_or_404(Person, id=person_id)
    return render(request, 'guestbook/detail.html', {'pname': pname})

def guestbook_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.pub_date = timezone.now()
            person.save()
            return redirect('detail', person_id=person.id)
    else:
        form = PostForm()
    return render(request, 'guestbook/guestbook_new.html', {'form': form})
