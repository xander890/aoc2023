#pragma once
#include <vector>
#include <string>
#include <fstream>
#include <filesystem>
using namespace std;

inline vector<string> readFile(const string& filename)
{
    vector<string> res;
    ifstream ifile(filename);
    string arec;
    while (getline(ifile, arec))
    {
        res.push_back(arec);
    }
    ifile.close();
    return res;
}

#define uint unsigned int
#define uint64 size_t