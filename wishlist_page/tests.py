from django.test import TestCase, SimpleTestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from .views import search_books, add_to_wishlist, load_wishlist, delete_item_ajax, show_json, add_book_ajax, create_notes

class TestUrls(SimpleTestCase):
    def test_search_books_url_resolves(self):
        url = reverse('wishlist_page:search_books')
        self.assertEquals(resolve(url).func, search_books)

    def test_add_to_wishlist_url_resolves(self):
        url = reverse('wishlist_page:add_to_wishlist')
        self.assertEquals(resolve(url).func, add_to_wishlist)

    def test_load_wishlist_url_resolves(self):
        url = reverse('wishlist_page:load_wishlist')
        self.assertEquals(resolve(url).func, load_wishlist)

    def test_show_json_url_resolves(self):
        url = reverse('wishlist_page:show_json')
        self.assertEquals(resolve(url).func, show_json)

    def test_add_book_ajax_url_resolves(self):
        url = reverse('wishlist_page:add_book_ajax')
        self.assertEquals(resolve(url).func, add_book_ajax)

    def test_create_notes_url_resolves(self):
        url = reverse('wishlist_page:create_notes')
        self.assertEquals(resolve(url).func, create_notes)


class WishlistPageViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_search_books_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('wishlist_page:search_books'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('wishlist_page:search_books'), {'search': 'Harry Potter'})
        self.assertEqual(response.status_code, 200)
