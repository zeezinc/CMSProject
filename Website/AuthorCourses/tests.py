from unittest import mock

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.files import File
from django.test import TestCase
import re

from django_webtest import WebTest

from .forms import ContentForm
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


class HomePageTest(TestCase):

    def test_homepage(self):  # tests homepage working correctly
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # 302 since it needs authentication to show homepage should be 200
        # Remove @login_required on home_view and test


class CategoryModelTest(TestCase):
    def setUp(self):
        cat = Category(name="Self Paced")
        cat.save()

    def test_string_representation(self):
        content = Category(name="Self Paced")
        self.assertEqual(str(content), content.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), "categories")

    def test_name_max_length(self):
        c = Category.objects.get(id=1)
        max_length = c._meta.get_field('name').max_length
        self.assertEqual(max_length, 32)


class DocumentModelTest(TestCase):
    def setUp(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.pdf'
        self.docy = Document(document=file_mock)
        self.docy.save()

    def test_string_representation(self):
        content = Document(description="My resume")
        self.assertEqual(str(content.description), content.description)

    def test_name_max_length(self):
        d = Document.objects.get(id=1)
        max_length = d._meta.get_field('description').max_length
        self.assertEqual(max_length, 255)

    def test_file_field(self):
        self.assertIsNotNone(re.search(r'^documents/test_?[a-zA-Z0-9]*\.pdf$', str(
            self.docy.document)))  # regular expression to check for instance of magicmock


class AllContentsModelTest(TestCase):

    def setUp(self):        # Set up non-modified objects used by all test methods
        cat = Category(name="Self Paced")
        cat.save()

        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.pdf'
        self.docy = Document(document=file_mock)
        self.docy.save()

        self.user = get_user_model().objects.create(username='some_user')

        self.entry = AllContents.objects.create(contentName="My entry title", author=self.user, category=cat,
                                                doc=self.docy)

    def test_string_representation(self):
        content = AllContents(contentName="My entry title")
        self.assertEqual(str(content), content.contentName)

    def test_verbose_name_plural(self):
        self.assertEqual(str(AllContents._meta.verbose_name_plural), "all contents")

    def test_title_max_length(self):
        ac = AllContents.objects.get(id=1)

        max_length_title = ac._meta.get_field('contentName').max_length
        self.assertEqual(max_length_title, 200)

        max_length_body = ac._meta.get_field('contentBody').max_length
        self.assertEqual(max_length_body, 100)

        max_length_summary = ac._meta.get_field('contentSummary').max_length
        self.assertEqual(max_length_summary, 60)

    def test_get_absolute_url(self):
        self.assertIsNotNone(self.entry.get_absolute_url())


class AllContentsViewTest(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        cat = Category(name="Self Paced")
        cat.save()

        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test2.pdf'
        docy = Document(document=file_mock)
        docy.save()

        self.user = get_user_model().objects.create(username='some_user')
        self.entry = AllContents.objects.create(contentName="My entry title", author=self.user, category=cat, doc=docy)

    def test_basic_view(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertEqual(response.status_code, 200)  # 302 since it needs authentication to show homepage should be 200
        # Remove @login_required and test

    def test_title_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.contentName)

    def test_body_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.contentBody)

    # def tearDown(self):


class AllContentsFormTest(WebTest):

    def setUp(self):
        self.cat = Category(name="Self Paced")
        self.cat.save()

        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test2.pdf'
        self.docy = Document(document=file_mock)
        self.docy.save()

        self.user = get_user_model().objects.create_user('Henderson')
        self.entry = AllContents.objects.create(contentName="My entry title", author=self.user, category=self.cat,
                                                doc=self.docy)

    def test_init(self):  # checks if form takes an _init entry keyword argument
        ContentForm(entry=self.entry)

    def test_init_without_entry(self):  # raises exception if no entry keyword found
        with self.assertRaises(KeyError):
            ContentForm()

    def test_valid_data(self):  # tests if form takes valid data
        form = ContentForm({
            'contentName': "Elon Musk",
            'contentBody': "Hi there",
            'contentSummary': "Selfie",
            'category': self.cat,
            'doc': self.docy,
            'author': self.user,
        }, entry=self.entry)

        self.assertTrue(form.is_valid())
        cont = form.save()
        self.assertEqual(cont.contentName, "Elon Musk")
        self.assertEqual(cont.contentBody, "Hi there")
        self.assertEqual(cont.contentSummary, "Selfie")
        self.assertEqual(cont.category.name, "Self Paced")
        self.assertEqual(cont.entry, self.entry)

    def test_blank_data(self):  # tests form with no data and matches errors with required fields
        form = ContentForm({}, entry=self.entry)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'contentName': ['This field is required.'],
            'contentBody': ['This field is required.'],
            'contentSummary': ['This field is required.'],
            'category': ['This field is required.'],
            'doc': ['This field is required.'],
            'author': ['This field is required.'],
        })
