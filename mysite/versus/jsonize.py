from django.core import serializers
from versus import models
data = serializers.serialize("json", models.versus.objects.all())
out = open("versus.json", "w")
out.write(data)
out.close()