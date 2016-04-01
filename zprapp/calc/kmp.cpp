//
// Created by mhaponiu on 01.04.16.
//

//#include <string>
//#include <boost/python/list.hpp>
#include "kmp.h"

namespace bp = boost::python;

bp::list kmp(const std::string &target, const std::string &pattern){
    bp::list ret_list;
    ret_list.append(target.length());
    ret_list.append(pattern.length());
    return ret_list;
}
