import unittest
import volume

class TestCalculator (unittest.TestCase):
  def test_volume(self):
    self.assertEqual(volume.volume(5, 6, 1), 30)
    self.assertEqual(volume.volume(5, 0, 1), 0)

    self.assertEqual(volume.volume(5, -6, 1), -30)
    self.assertEqual(volume.volume(5, -6, -1), 30)
    self.assertEqual(volume.volume(-5, -6, -1), -30)

    #As far as I know, almost equal is the only way to compare floats
    self.assertAlmostEqual(volume.volume(5.2, 6.5, 1.8), 60.84)
    self.assertAlmostEqual(volume.volume(5.45, -6.80, 1.78), -65.9668)

if __name__ == '__main__':
  unittest.main()