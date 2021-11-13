import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

print("hey")
# Import our flight model
from portalAR.models import stabile

# Create a new flight
f = stabile(facility_manager="Nome", nome_stabile="Ceccato", indirizzo="Via Soastene, 34, 36040 Brendola VI, Italy")

# Instert that flight into our database
f.save()