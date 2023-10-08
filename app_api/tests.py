from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.utils.formatting import dedent

from .models import DataFile


# Create your tests here.
class DataFileViewSetTestCase(APITestCase):

    def setUp(self):
        file_content = dedent("""name,age
            John,23
            Jane,24
            Doe,30
            """)
        self.data_file = SimpleUploadedFile("test.csv", file_content.encode('utf-8'))
        self.data_file_obj = DataFile.objects.create(file=self.data_file)

    def test_list_files(self):
        url = reverse('datafile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], "test.csv")

    def test_retrieve_file(self):
        url = reverse('datafile-detail', args=[self.data_file_obj.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "test.csv")

    def test_get_data(self):
        url = reverse('datafile-get-data', args=[self.data_file_obj.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_data_with_filtering(self):
        url = reverse('datafile-get-data', args=[self.data_file_obj.id])
        response = self.client.get(url + '?filter_by=name&filter_value=John')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'John')

    def test_get_data_with_sorting(self):
        url = reverse('datafile-get-data', args=[self.data_file_obj.id])
        response = self.client.get(url, {'sort_by': 'age'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0]['age'], 23)
        self.assertEqual(response.data[1]['age'], 24)
        self.assertEqual(response.data[2]['age'], 30)

    def tearDown(self):
        self.data_file_obj.file.delete()
