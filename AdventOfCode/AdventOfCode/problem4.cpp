#include <iostream>
#include <ranges>
#include <set>
#include <numeric>
#include <chrono>
#include "utils.h"

void problem4()
{
    auto res = readFile("../../input4.txt");

    chrono::steady_clock::time_point begin = chrono::steady_clock::now();

    uint size = (uint)res.size();
    vector<uint> cardCount(size);
    fill(cardCount.begin(), cardCount.end(), 1);
    uint points = 0;

    for (uint i = 0; i < size; i++)
    {
        const string& line = res[i];
        uint64 sepCol = line.find(':');
        uint64 sepBar = line.find('|');
        uint64 lenFirst = (sepBar - 1) - (sepCol + 1) + 1;
        
        string winstring = line.substr(sepCol + 1, lenFirst);
        string playstring = line.substr(sepBar + 1);
        
        set<uint> win;
        for (const auto word : views::split(winstring, ' '))
        {
            string_view w = string_view(word);
            if (w.length())
            {
                int r;
                std::from_chars(w.data(), w.data() + w.size(), r);
                win.insert(r);
            }
        }
        set<uint> play;
        for (const auto word : views::split(playstring, ' '))
        {
            string_view w = string_view(word);
            if (w.length())
            {
                int r;
                std::from_chars(w.data(), w.data() + w.size(), r);
                play.insert(r);
            }
        }
        set<uint> intersect;
        set_intersection(win.begin(), win.end(), play.begin(), play.end(), inserter(intersect, intersect.begin()));

        uint wins = (uint)intersect.size();
        points += 1 << wins >> 1;
        for (uint n : views::iota(0u, wins))
        {
            cardCount[i + n + 1] += cardCount[i];
        }
    }

    uint sum = 0;
    sum = accumulate(cardCount.begin(), cardCount.end(), sum);

    chrono::steady_clock::time_point end = chrono::steady_clock::now();
    cout << "problem 4" << endl;
    cout << "part1 : " << points << endl;
    cout << "part2 : " << sum << endl;
    cout << "Time = " << chrono::duration_cast<chrono::microseconds>(end - begin).count() / 1000.0f << "[ms]" << endl;
}