from html.parser import HTMLParser
from pathlib import Path
import unittest


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.form_found = False
        self.inputs = {}
        self.submit_found = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.form_found = True

        if tag == "input" and attrs.get("name"):
            self.inputs[attrs["name"]] = attrs

        if tag == "button" and attrs.get("type") == "submit":
            self.submit_found = True


class TestContactForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html = Path("index.html").read_text(encoding="utf-8")
        cls.parser = FormParser()
        cls.parser.feed(html)

    def test_form(self):
        self.assertTrue(self.parser.form_found)

    def test_name(self):
        self.assertIn("name", self.parser.inputs)
        self.assertEqual(self.parser.inputs["name"]["type"], "text")
        self.assertIn("required", self.parser.inputs["name"])

    def test_email(self):
        self.assertIn("email", self.parser.inputs)
        self.assertEqual(self.parser.inputs["email"]["type"], "email")
        self.assertIn("required", self.parser.inputs["email"])

    def test_contact(self):
        self.assertIn("contact", self.parser.inputs)
        self.assertEqual(self.parser.inputs["contact"]["type"], "tel")
        self.assertIn("required", self.parser.inputs["contact"])

    def test_submit(self):
        self.assertTrue(self.parser.submit_found)


if __name__ == "__main__":
    unittest.main(verbosity=2)