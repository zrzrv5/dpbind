#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include "deepmd/DeepPot.h"

namespace py = pybind11;

PYBIND11_MODULE(deepmd_pybind, m) {
    py::class_<deepmd::DeepPot>(m, "DeepPot")
        .def(py::init<const std::string &>())
        .def("compute", [](deepmd::DeepPot &self,
                           const std::vector<double> &coord,
                           const std::vector<int> &atype,
                           const std::vector<double> &cell) {
            double e;
            std::vector<double> f;
            std::vector<double> v;
            self.compute(e, f, v, coord, atype, cell);
            return py::make_tuple(e, f, v);
        });
