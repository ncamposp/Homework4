import unittest
import fullname

class Testfullname (unittest.TestCase):
  def test_fullname(self):
    self.assertEqual(fullname.fullname("John", "Smith"), "John Smith")
    self.assertEqual(fullname.fullname("John", ""), "John ")
    self.assertEqual(fullname.fullname("", "Smith"), " Smith")
    self.assertEqual(fullname.fullname("", ""), " ")
    

if __name__ == '__main__':
  unittest.main()