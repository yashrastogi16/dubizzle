from django.db import models
from django.utils.encoding import smart_unicode
from django.utils import timezone
from datetime import datetime

# Create your models here.
CITY_CHOICE = (
	(2,'DUBAI'),
	(3,'Abu Dhabi'),
	(11,'Ras al Khaimeh'),
	(12,'Sharjah'),
	(13,'Fujeirah'),
	(14,'Ajman'),
	(15,'Umm al Quwain'),
	(39,'Al Ain'),
	)

class dubizzle(models.Model):
	status = models.CharField('Status',max_length=20,null=False)
	type1 = models.CharField('Type',max_length=20,null=False)
	subtype = models.CharField('Sub Type', max_length=20,null=False)
	commercialtype = models.CharField('Commercial Type', max_length=50)
	refno = models.CharField('Refno', max_length=50,null=False)
	title = models.CharField('Title', max_length=50,null=False)
	description = models.TextField('Description',null=False)
	privateamenities = models.CharField('Private Amenities', max_length=50,blank=True)
	commercialamenities = models.CharField('Commercial Amenities', max_length=50, blank=True)
	size = models.IntegerField('Size',max_length=20,null=False)
	sizeunits = models.CharField('Size Units',max_length=50,blank=True)
	price = models.IntegerField('Price',null=False)
	rentpriceterm = models.CharField('Rent Price Term', max_length=30,blank = True)
	totalclosingfee = models.IntegerField('Total Closing Fees', max_length=30,blank=True)
	annualcommunityfee = models.IntegerField('Annual Community Fee', max_length=50,blank=True)
	agencyfee = models.IntegerField('Agency Fee',max_length=30,blank=True)
	rentispaid = models.CharField('Rent is Paid', max_length=30,blank=True)
	furnished = models.IntegerField('Furnished',blank=True)
	bedrooms = models.CharField('Bedrooms', max_length=30)
	bathrooms = models.IntegerField('Bathrooms', max_length=5, blank=True)
	developer = models.CharField('Developer', max_length=50,blank=True)
	readyby = models.DateField('Read By',null=True)
	lastupdated = models.DateTimeField('Last Updated',null=False)
	contactemail = models.EmailField('Contact Email',blank=True)
	contactnumber = models.CharField('Contact Number', max_length=20,blank=True)
	locationtext = models.CharField('Location Text', max_length=30,null=False)
	building = models.CharField('Building', max_length=30,blank=True)
	city = models.IntegerField('City', max_length=50,choices=CITY_CHOICE)
	photos = models.CharField('Photos', max_length=500,blank=True)
	view360 = models.CharField('View360', max_length=200,blank=True)
	geopoint = models.CharField('Geopoint',max_length=100,blank=True)
	freehold = models.IntegerField('Freehold',blank=True)
	zoned = models.CharField('Zonedfor', max_length=200,blank=True)
	def __unicode__(self):
		return smart_unicode(self.id)