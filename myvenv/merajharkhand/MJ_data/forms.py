from django import forms
from .models import Data


class DataForm(forms.ModelForm):

	class Meta:
		model= Data
		fields = ('author','location','sub_location','lon','lat','status','shop_name','owner_name')
