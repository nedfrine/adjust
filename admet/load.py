import models.py
from .models import Click
from .serializers import ClickSerializer
import csv
import time

def setUp(self):
    with open("/home/ubuntu/adjust/admet/data.csv","r") as dfile:
        reader = csv.reader(dfile)
        for row in reader:
            if row[0] != "" and row[1] != "":
                Click.objects.create(date=row[0],channel=row[1],country=row[2],os=row[3],impressions=row[4],clicks=row[5],installs=row[6],spend=row[7],revenue=row[8])

