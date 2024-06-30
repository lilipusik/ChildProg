from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'InfinitySchool/main_page.html')


# class CoursesListViewTestCase(TestCase):
#     fixtures = ['courses.json']
#     def test_list(self):
#         path = reverse('catalog')
#         response = self.client.get(path)
#
#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertTemplateUsed(response, 'InfinitySchool/catalog.html')

