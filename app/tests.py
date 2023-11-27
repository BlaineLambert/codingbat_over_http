# Create your tests here.
from django.test import SimpleTestCase


class Testnear_hundred(SimpleTestCase):
    def test_89(self):
        response = self.client.get("/warmup-1/near-hundred/89/")
        self.assertContains(response, False)

    def test_100(self):
        response = self.client.get("/warmup-1/near-hundred/93/")
        self.assertContains(response, True)

    def test_90(self):
        response = self.client.get("/warmup-1/near-hundred/90/")
        self.assertContains(response, True)

class Testcat_dog(SimpleTestCase):
    def test_cadog(self):
        response = self.client.get("/string-2/cat-dog/1cat1cadodog/")
        self.assertContains(response, True)

    def test_catdo(self):
        response = self.client.get("/string-2/cat-dog/catcat/")
        self.assertContains(response, False)

    def test_catdog(self):
        response = self.client.get("/string-2/cat-dog/catdog/")
        self.assertContains(response, True)


class Testnumbers(SimpleTestCase):
    def test_121(self):
        response = self.client.get("/logic-2/lone-sum/3/2/3/")
        self.assertContains(response, 2)

    def test_111(self):
        response = self.client.get("/logic-2/lone-sum/1/1/1/")
        self.assertContains(response, 0)

    def test_123(self):
        response = self.client.get("/logic-2/lone-sum/1/2/3/")
        self.assertContains(response, 6)


class Teststring(SimpleTestCase):
    def test_Code(self):
        response = self.client.get("/warmup-2/string-splosion/Code/")
        self.assertContains(response, "CCoCodCode")

    def test_ab(self):
        response = self.client.get("/warmup-2/string-splosion/ab/")
        self.assertContains(response, "aab")

    def test_hi(self):
        response = self.client.get("/warmup-2/string-splosion/abc/")
        self.assertContains(response, "aababc")
