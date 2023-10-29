from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from user_profile_page.models import Member
from landingPage.models import Books
from wishlist_page.models import WishlistItem
from json import loads



class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.member = Member.objects.create(user=self.user, bio='This is a bio')
        self.book1 = Books.objects.create(title='Book1', borrowed_by=self.user)
        self.book2 = Books.objects.create(title='Book2')
        self.wishlist_item = WishlistItem.objects.create(user=self.user, title='WishBook1')

    def test_user_dashboard(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user_profile_page:user_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_info', response.context)
        self.assertIn('user_bio', response.context)
        self.assertIn('borrowed_books', response.context)
        self.assertIn('wishlisted_books', response.context)

    def test_load_wishlist(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user_profile_page:load_wishlist'))
        data = loads(response.content)
        self.assertIn('WishBook1', [item['title'] for item in data['wishlist']])

    def test_load_borrowed_book(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user_profile_page:load_borrowed_book'))
        data = loads(response.content)
        self.assertIn('Book1', [item['title'] for item in data['books']])
        
    def test_update_bio_ajax(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('user_profile_page:update_bio_ajax'), {'bio': 'New bio'})
        self.assertEqual(response.status_code, 201)
        updated_member = Member.objects.get(user=self.user)
        self.assertEqual(updated_member.bio, 'New bio')

    def test_return_book(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('user_profile_page:return_book', args=[self.book1.id]))
        data = loads(response.content)
        self.assertEqual(data['status'], 'success')
        updated_book = Books.objects.get(pk=self.book1.id)
        self.assertIsNone(updated_book.borrowed_by)

    # More test methods can go here to cover other functionalities

