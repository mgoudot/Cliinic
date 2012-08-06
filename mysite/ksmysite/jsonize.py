import sys, os

sys.path.append('/mysite/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.serializers import serialize
from versus import models

model_names = [Question] # a list of the names of the models you want to export

for model_name in model_names:
    cls = getattr(models, model_name)
    filename = model_name.lower() + ".json"
    file = open(filename, "w")
    file.write(serialize("json", cls.objects.all()))