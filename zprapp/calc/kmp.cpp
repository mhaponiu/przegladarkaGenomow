//
// Created by mhaponiu on 01.04.16.
//

//#include <string>
//#include <boost/python/list.hpp>
#include "kmp.h"

namespace bp = boost::python;
using namespace std;

void Pref( vector<int> &P, string &S )
{
    unsigned int t = 0, i, n = S.size();
    P.resize(n+1, 0);

    for( i = 2; i < n; i++ )
    {
        while (t > 0 && S[t + 1] != S[i]) t = P[t];
        if( S[t+1] == S[i] ) t++;
        P[i] = t;
    }
}

bp::list kmp(const std::string &T, const std::string &W){
//    bp::list ret_list;
//    ret_list.append(target.length());
//    ret_list.append(pattern.length());
//    return ret_list;
    bp::list ret_list;

    string S = "#" + W + "#" + T;
    vector<int> P;
    Pref(P, S);

    unsigned int i, ws = W.size();

    for( i = ws + 2; i < S.size(); i++ )
    {
//wypisz pozycje wzorca w tekscie
        if( P[i] == ws ) ret_list.append(i-ws-ws-1);
    }

    return ret_list;
}

//void KMP( string &T, string &W )
//{
//    string S = "#" + W + "#" + T;
//    vector<int> P;
//    Pref(P, S);
//
//    unsigned int i, ws = W.size();
//
//    for( i = ws + 2; i < S.size(); i++ )
//    {
////wypisz pozycje wzorca w tekscie
//        if( P[i] == ws ) printf("%d\n", i-ws-ws);
//    }
//}
