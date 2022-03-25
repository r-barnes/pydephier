import unittest

import pydephier

class PyDepHierTests(unittest.TestCase):
  def test_depression_defaults(self) -> None:
    d = pydephier.Depression()
    self.assertEqual(d.out_cell, pydephier.NO_VALUE)
    self.assertEqual(d.pit_cell, pydephier.NO_VALUE)
    self.assertEqual(d.parent, pydephier.NO_PARENT)
    self.assertEqual(d.odep, pydephier.NO_VALUE)
    self.assertEqual(d.geolink, pydephier.NO_VALUE)
    self.assertEqual(d.lchild, pydephier.NO_VALUE)
    self.assertEqual(d.rchild, pydephier.NO_VALUE)
    self.assertEqual(d.ocean_parent, False)
    self.assertEqual(d.dep_label, 0)
    self.assertEqual(d.cell_count, 0)
    self.assertEqual(d.dep_vol, 0)
    self.assertEqual(d.water_vol, 0)
    self.assertEqual(d.total_elevation, 0)