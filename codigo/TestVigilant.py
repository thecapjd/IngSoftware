import unittest
from Vigilant import parse_log_line

class TestLogParser(unittest.TestCase):
    def test_parse_valid_line(self):
        line = "2025-04-11 15:37:12, IP: 192.168.1.10, Bytes: 6000"
        ip, bytes_transferred = parse_log_line(line)
        self.assertEqual(ip, "192.168.1.10")
        self.assertEqual(bytes_transferred, 6000)

    def test_parse_invalid_line(self):
        line = "invalid line without expected format"
        ip, bytes_transferred = parse_log_line(line)
        self.assertIsNone(ip)
        self.assertEqual(bytes_transferred, 0)

if __name__ == '__main__':
    unittest.main()
