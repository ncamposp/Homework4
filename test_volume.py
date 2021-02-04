import unittest
import volume

class TestCalculator (unittest.TestCase):
  def test_volume(self):
    self.assertEqual(volume.volume(5, 6, 1), 30)
    

  

if __name__ == '__main__':
  unittest.main()