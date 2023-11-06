
# Create your tests here.
from django.test import SimpleTestCase


class Testnear_hundred(SimpleTestCase):
    def test_89(self):
        response = self.client.get("/hundred/89")
        self.assertContains(response, False)

    def test_100(self):
        response = self.client.get("/hundred/93")
        self.assertContains(response, True)

    def test_90(self):
        response = self.client.get("/hundred/90")
        self.assertContains(response, True)

class Testcat_dog(SimpleTestCase):
    def test_cadog(self):
        response = self.client.get("/catdogcheck/1cat1cadodog")
        self.assertContains(response, False)
    
    def test_catdo(self):
        response = self.client.get("/catdogcheck/catcat")
        self.assertContains(response, False)

    def test_catdog(self):
        response = self.client.get("/catdogcheck/catdog")
        self.assertContains(response, True)

class Testnumbers(SimpleTestCase):
    def test_121(self):
        response = self.client.get("/numbers/3/2/3")
        self.assertContains(response, 2)
    
    def test_111(self):
        response = self.client.get("/numbers/3/3/3")
        self.assertContains(response, 0)

    def test_123(self):
        response = self.client.get("/numbers/1/2/3")
        self.assertContains(response, 6)

class Teststring(SimpleTestCase):
    def test_Code(self):
        response = self.client.get("/string/Code")
        self.assertContains(response, "CCoCodCode")

    def test_ab(self):
        response = self.client.get("/string/ab")
        self.assertContains(response, "aab")

    def test_hi(self):
        response = self.client.get("/string/abc")
        self.assertContains(response, "aababc")
