from typing import Mapping
from django.db import models
from django.db.models import Model

from django.core.validators import RegexValidator


from django.contrib.auth.models import User
from django.db.models.fields import CharField, DateTimeField, TextField, IntegerField

from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField




work_preferences = [('server','Server'), ('runner/busser','Runner/Busser'),('barista','Barista'),('bartender','Bartender'),('cashier','Cashier'),('line-cook','Line-cook'),('sous-chef','Sous chef'),('baker','Baker'),('pastry chef','Pastry Chef'), ('kitchen manager','Kitchen Manager'),('head chef','Head Chef'),('prep cook','Prep Cook'),('dishwasher','Dishwasher'),('general manager','General Manager'),('other', 'Other')]

business_type = [('fs-rest','Full-service Restaurant'),('cafe','Cafe'),('commissary','Commissary Kitchen'),('catering','Catering'),('prod mft','Product Manufacturing'),('coff-rst','Coffee Roaster'),('food-cult','Food Cultivation'),('food-science','Food-Science'),('fine-dine','Fine Dining'),('product supply','Product Supplier'),('wholesale','Wholesale'),('other','Other')]

pay_type = [('hourly','Hourly'), ('salary','Salary'), ('other','Other') ]

# === this list could be used within a model itself if the content is specific to it

states = [('AL','Alabama'),('AK','Alaska'),('AZ','Arizona'),('AR','Arkansas'),('CA','California'),('CO','Colorado'), ('CT','Connecticut'), ('DE','Delaware'),('FL','Florida'), ('GA','Georgia'), ('HI','Hawaii'), ('ID','Idaho'), ('IL','Illinois'), ('IN','Indiana'), ('IA','Iowa'), ('KS','Kansas'), ('KY','Kentucky'), ('LA','Louisiana'), ('ME','Maine'), ('MD','Maryland'), ('MA','Massachusetts'), ('MI','Michigan'), ('MN','Minnesota'), ('MS','Mississippi'), ('MO','Missouri'), ('MT','Montana'), ('NE','Nebraska'), ('NV','Nevada'), ('NH','New Hampshire'), ('NJ','New Jersey'), ('NM','New Mexico'), ('NY','New York'), ('NC','North Carolina'), ('ND','North Dakota'), ('OH','Ohio'), ('OK','Oklahoma'), ('OR','Oregon'), ('PA','Pennsylvania'), ('RI','Rhode Island'), ('SC','South Carolina'), ('SD','South Dakota'), ('TN','Tennessee'), ('TX','Texas'), ('UT','Utah'), ('VT','Vermont'), ('VA','Virginia'),  ('WA','Washington'), ('WV','West Virginia'), ('WI','Wisconsin'), ('WY','Wyoming')]

# Create models here

class Individual(Model):
  user = OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=75)
  last_name = models.CharField(max_length=75)
  city = models.CharField(max_length=75)
  state = models.CharField(choices=states, max_length=2)
  zip_code = models.CharField(max_length=5, validators=[RegexValidator(r'^[0-9]{5}$')])
  work_preferences = models.CharField(choices=work_preferences, max_length=50)
  description = models.TextField(max_length=1000)
  image = models.CharField(max_length=400, default="https://www.google.com/search?q=user+icon+for+website+free&tbm=isch&ved=2ahUKEwjindHKh7r0AhVNBzQIHV0nBtMQ2-cCegQIABAA&oq=user+icon+for+website+free&gs_lcp=CgNpbWcQA1DVBFj8CWCvEmgAcAB4AIABVogBgAOSAQE2mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=6u-iYeKAIM2O0PEP3c6YmA0&bih=898&biw=896#imgrc=oOwVdMy4j7n3mM")
  created_at = DateTimeField(auto_now_add=True)
  updated_at = DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return self.username


class Business(Model):
  user = OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=150)
  category = models.CharField(choices=business_type, max_length=75)
  description = models.TextField(max_length=1000, default='business description pending')
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=75)
  state = models.CharField(choices=states, max_length=2)
  zip_code = models.CharField(max_length=5, validators=[RegexValidator(r'^[0-9]{5}$')])
  created_at = DateTimeField(auto_now_add=True)
  updated_at = DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return self.name

class Job_Post(Model):
  business_name = models.CharField(max_length=150)
  title = CharField(max_length=200)
  pay_type = models.CharField(choices=pay_type, max_length=10)
  description = TextField(max_length=4000)
  city = models.CharField(max_length=75)
  state = models.CharField(choices=states, max_length=2)
  created_at = DateTimeField(auto_now_add=True)
  updated_at = DateTimeField(auto_now=True)
  business = ForeignKey(Business, on_delete=models.CASCADE, related_name='job_posts')
  
  def __str__(self) -> str:
    return self.title

class Review(Model):
  title = CharField(max_length=200)
  city = models.CharField(max_length=75)
  state = models.CharField(choices=states, max_length=2)
  review = TextField(max_length=4000)
  created_at = DateTimeField(auto_now_add=True)
  updated_at = DateTimeField(auto_now=True)
  user = ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')

  def __str__(self) -> str:
    return self.title

  
  
  

