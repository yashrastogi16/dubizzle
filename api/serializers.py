from django.forms import widgets
from rest_framework import serializers
from feeds.models import *

class dubizzleSerializer(serializers.ModelSerializer):
	class Meta:
		model = dubizzle
		fields = ('status','type1','subtype','commercialtype','refno','title','description','privateamenities','commercialamenities','sizeunits','rentpriceterm','rentispaid','bedrooms','developer','readyby','lastupdated','contactemail','contactnumber','locationtext','building','photos','view360','geopoint','zoned')
		# fields = ('status','type1','subtype','commercialtype','refno','title','description','privateamenities','commercialamenities','size','sizeunits','price','rentpriceterm','totalclosingfee','annualcommunityfee','agencyfee','rentispaid','furnished','bedrooms','bathrooms','developer','readyby','lastupdated','contactemail','contactnumber','locationtext','building','city','photos','view360','geopoint','freehold','zoned')