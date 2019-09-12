# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Click
from .serializers import ClickSerializer
import csv
import time

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_entry(row):
        if row[0] != "" and row[1] != "":
            Click.objects.create(date=row[0],channel=row[1],country=row[2],os=row[3],impressions=row[4],clicks=row[5],installs=row[6],spend=row[7],revenue=row[8])

    def setUp(self):
        # add test data
        with open("/home/ubuntu/adjust/admet/data.csv","r") as dfile:
            reader = csv.reader(dfile)
            for row in reader:
                self.create_entry(row)
    

class GetAllClickTest(BaseViewTest):

    def test_get_all_entries(self):
        """
        This test ensures that all entries added in the setUp method
        exist when we make a GET request to the metrics/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("metric-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Click.objects.all()
        serialized = ClickSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #time.sleep(500)
