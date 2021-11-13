import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

print("hey")
# Import our flight model
from portalAR.models import componente, scena

import pandas as pd
df = pd.read_excel(r"urls.xlsx")

scene = scena.objects.all()
ceccato = scene.first()

for x in df.values:
    f = componente(scena= ceccato, codice=x[1], modello="<modello>", url= x[0])
    f.save()