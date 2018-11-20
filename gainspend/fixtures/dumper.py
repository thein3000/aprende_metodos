from django.core import serializers
from gainspend import models

data = serializers.serialize("json", UserMethod.objects.all())
out = open("mymodel.json", "w")
out.write(data)
out.close()
