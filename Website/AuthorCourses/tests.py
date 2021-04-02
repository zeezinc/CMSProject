from unittest import mock

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.files import File
from django.test import TestCase
from .models import AllContents, Category, Document


# Create your tests here.


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'email': 'email',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)


class FileModelTestCase(TestCase):
    def test_file_field(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.pdf'
        file_model = Document(document=file_mock)
        self.assertEqual(file_model.document.name, file_mock.name)


class AllContentsModelTest(TestCase):

    def test_string_representation(self):
        content = AllContents(contentName="My entry title")
        self.assertEqual(str(content), content.contentName)

    def test_verbose_name_plural(self):
        self.assertEqual(str(AllContents._meta.verbose_name_plural), "all contents")

    # def test_fields_author_name(self):
    #     cat = Category(name="Self Paced")
    #     cat.save()
    #
    #     file_mock = mock.MagicMock(spec=File)
    #     file_mock.name = 'test2.pdf'
    #     docy = Document(document=file_mock)
    #     docy.save()
    #
    #     con = AllContents(contentName="Zen Training", category=cat, doc=docy)
    #     con.save()
    #
    #     # assertion example ...
    #     record = AllContents.objects.get(id=1)
    #     self.assertEqual(record.contentName, "Zen Training")
    #     # self.assertEqual(record.category.name, cat.name)
    #     self.assertEqual(record.doc.description.name, file_mock.name)


class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # 302 since it needs authentication to show homepage should be 200
