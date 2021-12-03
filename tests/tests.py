import unittest

import pydephier

class PyDepHierTests(unittest.TestCase):
  def test_depression_defaults(self) -> None:
    d = pydephier.Depression()
    self.assertEqual(d.out_cell, 4294967295)
    self.assertEqual(d.pit_cell, 4294967295)