from django.shortcuts import render
from firstapp.forms import PracticeForm
# Create your views here.
def home(request):
    form = PracticeForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = PracticeForm()
    return render(request, 'home.html', {'form': form})
