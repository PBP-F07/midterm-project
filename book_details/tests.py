from django.test import TestCase
from .models import discussion, reply
from landingPage.models import Books


class mainTest(TestCase):

    def setUp_discussion(self):
        book1 = Books.objects.create(
            title="pbp",
            author="pbp",
            description="pbp",
            image="http://books.google.com/books/content?id=aJQILlLxRmAC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
            year_of_release=2005,
            amount=5
        )
        self.item = discussion.objects.create(
            book = book1,
            comment = "halo semua",
            user = "halo",
        )
        
    def test_discussion_creation(self):
        self.assertEqual(self.item.comment, "halo semua")
        self.assertEqual(self.item.user,"halo")

