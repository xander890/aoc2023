#include <iostream>
#include <ranges>
#include <set>
#include <numeric>
#include <chrono>
#include <unordered_map>
#include <regex>
#include "utils.h"

/*import regex
file1 = open('input1.txt', 'r')
Lines = file1.readlines()
nums = { "zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", \
        "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9" }

    def solve(regexVal) :
    total = 0
    for line in Lines :
res = regex.findall(regexVal, line, overlapped = True)
res = [nums[x] if x in nums else x for x in res]
value = int(res[0] + res[-1])
total = total + value
return total

print("part1", solve(r'([1-9])'))
print("part2", solve(r'([1-9]|' + '|'.join(nums.keys()) + ')'))*/

unordered_map<string, string> nums = { {"zero" , "0"} , { "one" , "1"} , { "two" , "2"} , { "three" , "3"} , { "four" , "4"} , {
        "five" , "5"} , { "six" , "6"} , { "seven" , "7"} , { "eight" , "8"} , { "nine" , "9" } };

const char* rgx1 = "([1-9])";
const char* rgx2 = "(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))";

uint solve(const vector<string>& vec, const char* regex)
{
    uint total = 0;
    std::regex re(regex);
    for (const string& line : vec)
    {
        std::sregex_iterator next(line.begin(), line.end(), re);
        std::sregex_iterator end;
        string first = next->str(1);
        string last = "";
        while (next != end) {
            last = next->str(1);
            next++;
        }

        first = nums.contains(first) ? nums[first] : first;
        last = nums.contains(last) ? nums[last] : last;
        string combined = first + last;
        uint val = atoi(combined.c_str());
        total += val;
    }
    return total;
}


void problem1()
{
    auto res = readFile("../../input1.txt");
    chrono::steady_clock::time_point begin = chrono::steady_clock::now();
    cout << "problem 1" << endl;
    cout << "part1 : " << solve(res, rgx1) << endl;
    chrono::steady_clock::time_point end = chrono::steady_clock::now();
    cout << "Time = " << chrono::duration_cast<chrono::microseconds>(end - begin).count() / 1000.0f << "[ms]" << endl;
    begin = chrono::steady_clock::now();
    cout << "part2 : " << solve(res, rgx2) << endl;
    end = chrono::steady_clock::now();
    cout << "Time = " << chrono::duration_cast<chrono::microseconds>(end - begin).count() / 1000.0f << "[ms]" << endl;
}