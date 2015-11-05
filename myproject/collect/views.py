from django.shortcuts import render
from .forms import CollectForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return register(request)
        else:
            print form.errors
    else:
        form = PageForm()
    return render(request, 'collect/add_page.html', {'form': form})
