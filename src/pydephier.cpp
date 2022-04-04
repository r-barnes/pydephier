#include <dephier/dephier.hpp>

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl_bind.h>
#include <pybind11/stl.h>

namespace py = pybind11;

using namespace richdem;
using namespace richdem::dephier;

PYBIND11_MODULE(pydephier, m) {
  m.doc() = "Depression Hierarchies for Python";

  // Kludgy way of exposing global variables
  m.attr("NO_PARENT") = &NO_PARENT;
  m.attr("NO_VALUE") = &NO_VALUE;

  py::class_<Depression<double>>(m, "Depression")
    .def(py::init<>())
    .def_readwrite("pit_cell", &Depression<double>::pit_cell, "Flat index of the pit cell, the lowest cell in the depression. If more than one cell shares this lowest elevation, then one is arbitrarily chosen.")
    .def_readwrite("out_cell", &Depression<double>::out_cell, "Flat index of the outlet cell. If there is more than one outlet cell at this cell's elevation, then one is arbitrarily chosen.")
    .def_readwrite("parent", &Depression<double>::parent, "Parent depression. If both this depression and its neighbour fill up, this parent depression is the one which will contain the overflow.")
    .def_readwrite("odep", &Depression<double>::odep, "Outlet depression. The metadepression into which this one overflows. Usually its neighbour depression, but sometimes the ocean.")
    .def_readwrite("geolink", &Depression<double>::geolink, "When a metadepression overflows it does so into the metadepression indicated by `odep`. However, odep must flood from the bottom up. Therefore, we keep track of the `geolink`, which indicates what leaf depression the overflow is initially routed into.")
    .def_readwrite("pit_elev", &Depression<double>::pit_elev, "Elevation of the pit cell. Since the pit cell has the lowest elevation of any cell in the depression, we initialize this to infinity.")
    .def_readwrite("out_elev", &Depression<double>::out_elev, "Elevation of the outlet cell. Since the outlet cell has the lowest elevation of any path leading from a depression, we initialize this to infinity.")
    .def_readwrite("lchild", &Depression<double>::lchild, "The depressions form a binary tree. Each depression has two child depressions: one left and one right.")
    .def_readwrite("rchild", &Depression<double>::rchild, "The depressions form a binary tree. Each depression has two child depressions: one left and one right.")
    .def_readwrite("ocean_parent", &Depression<double>::ocean_parent, "Indicates whether the parent link is to either the ocean or a depression that links to the ocean.")
    .def_readwrite("ocean_linked", &Depression<double>::ocean_linked, "Indicates depressions which link to the ocean through this depression, but are not subdepressions. That is, these ocean-linked depressions may be at the top of high cliffs and spilling into this depression.")
    .def_readwrite("dep_label", &Depression<double>::dep_label, "The label of the depression, for calling it up again.")
    .def_readwrite("cell_count", &Depression<double>::cell_count, "Number of cells contained within the depression and its children.")
    .def_readwrite("dep_vol", &Depression<double>::dep_vol, "Volume of the depression and its children. Used in the Water Level Equation (see below).")
    .def_readwrite("water_vol", &Depression<double>::water_vol, "Water currently contained within the depression. Used in the Water Level Equation (see below).")
    .def_readwrite("total_elevation", &Depression<double>::total_elevation, "Total elevation of cells contained with the depression and its children.")


    ; //Ends the class definition above

  m.def("GetDepressionHierarchy", &GetDepressionHierarchy<double, Topology::D8>, "Calculate the hierarchy of depressions. Takes as input a digital elevation model and a set of labels. The labels should have `OCEAN` for cells");
}
