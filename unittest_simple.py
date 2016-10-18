import unittest
from app import name

class SimpleTest(unittest.TestCase):
	
	def test_name(self):
		self.assertEqual(name(), "Tessa and Julia!!!!!")

if __name__ == '__main__':
	unittest.main()
