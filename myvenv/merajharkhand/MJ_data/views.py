from django.shortcuts import render
from .models import Data
from .forms import DataForm


def index(request):
	if request.method == "POST":
		form = DataForm(request.POST)
		if form.is_valid():
			data=form.save(commit=False)
			data.save()
			return render(request, 'MJ_data/success.html',{'data':data})
	else:
		form=DataForm()
	return render(request,'MJ_data/index.html',{'form':form})

