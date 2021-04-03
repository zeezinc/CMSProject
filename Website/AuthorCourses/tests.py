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


class AllContentsModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        # Set up non-modified objects used by all test methods
        cat = Category(name="Self Paced")
        cat.save()

        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test2.pdf'
        docy = Document(document=file_mock)
        docy.save()

        self.user = get_user_model().objects.create(username='some_user')

        # entry = AllContents.objects.create(contentName="My entry title", author=user, category=cat, doc=docy)
        self.entry=AllContents.objects.create(contentName="My entry title", author=self.user, category=cat, doc=docy)
        # cls.assertIsNotNone(entry)

    def test_string_representation(self):
        content = AllContents(contentName="My entry title")
        self.assertEqual(str(content), content.contentName)

    def test_verbose_name_plural(self):
        self.assertEqual(str(AllContents._meta.verbose_name_plural), "all contents")

    def test_title_max_length(self):
        ac = AllContents.objects.get(id=1)
        max_length = ac._meta.get_field('contentName').max_length
        self.assertEqual(max_length, 200)

    def test_file_field(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.pdf'
        file_model = Document(document=file_mock)
        self.assertEqual(file_model.document.name, file_mock.name)

    def test_get_absolute_url(self):
        self.assertIsNotNone(self.entry.get_absolute_url())


class AllContentsViewTest(TestCase):

    # def setUp(self):
    #     self.user = get_user_model().objects.create(username='some_user')
    #     self.entry = Entry.objects.create(title='1-title', body='1-body',
    #                                       author=self.user)

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
                                                     # Remove @login_required on home_view and test
    def test_title_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.contentName)

    def test_body_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.contentBody)


class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # 302 since it needs authentication to show homepage should be 200
                                                     # Remove @login_required on home_view and test
