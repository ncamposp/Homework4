import unittest
import average

class TestAverage (unittest.TestCase):
  #
  def test_average(self):
    empty = []
    list1 = [15,5, 7, 4, 9]
    list2 = [-6,-8,-3,-4]
    list3 = [7.6, 8.4, -9.6, 0.3]
    self.assertEqual(average.average(list1), 8)
    self.assertEqual(average.average(empty), "Error")
    self.assertEqual(average.average(list2), -5.25)
    self.assertEqual(average.average(list3), 1.675)
    
if __name__ == '__main__':
  unittest.main()