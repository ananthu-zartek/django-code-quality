from django.test import TestCase


class HealthEndpointTests(TestCase):
    def test_health_endpoint_returns_status(self):
        response = self.client.get("/api/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})


class ChecksEndpointTests(TestCase):
    def test_checks_endpoint_returns_count(self):
        response = self.client.get("/api/checks/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok", "checks": 1})
