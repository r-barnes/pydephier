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
    ; //Ends the class definition above
}