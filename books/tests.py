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
        # Test that the book title is correctly set
        self.assertEqual(self.book.title, "Test Book")

    def test_book_author(self):
         # Test that the book author is correctly set
        self.assertEqual(self.book.author, self.author)

    def test_book_description(self):
        # Test that the book description is correctly set
        self.assertEqual(self.book.description, "This is a test book")

    def test_book_price(self):
        # Test that the book price is correctly set
        self.assertEqual(self.book.price, 19.99)

    def test_book_is_active(self):
        # Test that the book is active by default
        self.assertTrue(self.book.is_active)

    def test_book_image(self):
        # Test that the book image is not set by default
        self.assertFalse(bool(self.book.image))

    def test_book_str(self):
        # Test that the book's string representation is correct
        self.assertEqual(str(self.book), "Test Book")

    def test_book_list_url(self):
        # Test that the book list URL is correctly reversed
        respond = reverse('book_list')
        self.assertEqual(respond, '/')

    def test_book_detail_url(self):
        # Test that the book detail URL is correctly reversed
        respond = reverse('book_detail', kwargs={'pk': 1})
        self.assertEqual(respond, '/1/')

    def test_book_add_url(self):
        # Test that the book add URL is correctly reversed
        respond = reverse('book_add')
        self.assertEqual(respond, '/add/')

    def test_book_update_url(self):
        # Test that the book update URL is correctly reversed
        respond = reverse('book_update', kwargs={'pk': 1})
        self.assertEqual(respond, '/1/update/')

    def test_book_delete_url(self):
        # Test that the book delete URL is correctly reversed
        respond = reverse('book_delete', kwargs={'pk': 1})
        self.assertEqual(respond, '/1/delete/')