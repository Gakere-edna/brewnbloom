from django.test import TestCase
from django.urls import reverse


class PageTests(TestCase):
    def test_main_pages_render(self):
        pages = (
            ("home", "cafe/index.html"),
            ("menu", "cafe/menu.html"),
            ("about", "cafe/about.html"),
            ("contact", "cafe/contact.html"),
        )

        for url_name, template_name in pages:
            with self.subTest(page=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template_name)

    def test_contact_form_redirects_after_valid_submission(self):
        response = self.client.post(
            reverse("contact"),
            {
                "name": "Ada Lovelace",
                "email": "ada@example.com",
                "message": "Hello!",
            },
        )

        self.assertRedirects(response, f'{reverse("contact")}?submitted=1')

    def test_contact_form_shows_invalid_email(self):
        response = self.client.post(
            reverse("contact"),
            {
                "name": "Ada Lovelace",
                "email": "not-an-email",
                "message": "Hello!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("Enter a valid email address.", response.context["form"].errors["email"])
