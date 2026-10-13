import unittest
from io import BytesIO
from unittest.mock import patch
import urllib.error
from scripts.refresh_scryfall_metadata import request

def http_error(code):
    return urllib.error.HTTPError("https://api.scryfall.com/bulk-data", code, "test failure",
                                  {"Retry-After": "0.01"}, BytesIO(b""))

class ScryfallRequestRetryTests(unittest.TestCase):
    @patch("scripts.refresh_scryfall_metadata.time.sleep")
    @patch("scripts.refresh_scryfall_metadata.urllib.request.urlopen")
    def test_transient_503_retries_then_succeeds(self, mocked_urlopen, mocked_sleep):
        response = object()
        mocked_urlopen.side_effect = [http_error(503), response]
        self.assertIs(request("https://api.scryfall.com/bulk-data"), response)
        self.assertEqual(mocked_urlopen.call_count, 2)
        mocked_sleep.assert_called_once()

    @patch("scripts.refresh_scryfall_metadata.time.sleep")
    @patch("scripts.refresh_scryfall_metadata.urllib.request.urlopen")
    def test_403_fails_fast_without_retries(self, mocked_urlopen, mocked_sleep):
        mocked_urlopen.side_effect = http_error(403)
        with self.assertRaisesRegex(RuntimeError, "HTTP 403"):
            request("https://api.scryfall.com/bulk-data")
        mocked_urlopen.assert_called_once()
        mocked_sleep.assert_not_called()

if __name__ == "__main__":
    unittest.main()
