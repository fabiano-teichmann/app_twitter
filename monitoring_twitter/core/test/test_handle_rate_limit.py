import time
from datetime import datetime, timedelta
from unittest import skip

from django.test import TestCase

from core.manage_request_twitter import ManagerRequestApiTwitter
from core.models import RequestAPI


class TestHandleRateLimit(TestCase):

    @skip('Too Slow')
    def test_sleep_request(self):
        """Must be sleep 5 seconds and request total in window current is equal 1"""
        date = datetime.now() - timedelta(minutes=14)
        RequestAPI.objects.create(total_request=450, date=date)
        start = time.time()
        ManagerRequestApiTwitter().handle_rate_limit()
        stop = time.time()
        total_time = stop - start
        self.assertGreater(total_time, 60)

    def test_new_window_request(self):
        date = datetime.now() - timedelta(minutes=15)
        RequestAPI.objects.create(total_request=4, date=date)
        ManagerRequestApiTwitter().handle_rate_limit()
        request = RequestAPI.objects.last()
        self.assertEqual(request.total_request, 1)

    def test_add_request_in_window(self):
        date = datetime.now() - timedelta(minutes=14)
        RequestAPI.objects.create(total_request=449, date=date)
        ManagerRequestApiTwitter().handle_rate_limit()
        request = RequestAPI.objects.last()
        self.assertEqual(request.total_request, 450)
