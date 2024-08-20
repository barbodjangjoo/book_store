from django.test import TestCase
from django.urls import reverse

from .models import Book
from authors.models import Author


class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="John Doe" ,birth_date="1990-01-01")
        self.book = Book.objects.create(
            id=1,
            title="Test Book",
            author=self.author,
            description="This is a test book",
            price=19.99,
        )

    def test_book_title(self):
        self.assertEqual(self.book.title, "Test Book")

    def test_book_author(self):
        self.assertEqual(self.book.author, self.author)

    def test_book_description(self):
        self.assertEqual(self.book.description, "This is a test book")

    def test_book_price(self):
        self.assertEqual(self.book.price, 19.99)

    def test_book_is_active(self):
        self.assertTrue(self.book.is_active)

    def test_book_image(self):
        self.assertFalse(bool(self.book.image))

    def test_book_str(self):
        self.assertEqual(str(self.book), "Test Book")

    def test_book_list_url(self):
        respond = reverse('book_list')
        self.assertEqual(respond, '/')

    def test_book_detail_url(self):
        respond = reverse('book_detail', kwargs={'pk': 1})
        self.assertEqual(respond, '/1/')

    def test_book_add_url(self):
        respond = reverse('book_add')
        self.assertEqual(respond, '/add/')

    def test_book_update_url(self):
        respond = reverse('book_update', kwargs={'pk': 1})
        self.assertEqual(respond, '/1/update/')

    def test_book_delete_url(self):
        respond = reverse('book_delete', kwargs={'pk': 1})
        self.assertEqual(respond, '/1/delete/')