//
// Created by mhaponiu on 01.04.16.
//
#include "kmp.h"
#include <boost/python.hpp>

BOOST_PYTHON_MODULE(calc)
{
    using namespace boost::python;
    def("kmp", kmp);
}
