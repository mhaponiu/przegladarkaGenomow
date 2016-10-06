//
// Created by mhaponiu on 01.04.16.
//

#ifndef CALC_KMP_H
#define CALC_KMP_H

#include <string>
#include <boost/python/list.hpp>

namespace bp = boost::python;

bp::list kmp(const std::string &target, const std::string &pattern);

#endif //CALC_KMP_H

