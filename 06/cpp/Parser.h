#include <iostream>
#include <string>
#include <unordered_map>

class Parser
{
public:
    static std::unordered_map<const char *, std::string> cInct;
    cInct["0"] = "0101010";
    cInct["1"] = "0111111";
    cInct["-1"] = "0111010";
    cInct["D"] = "0001100";
    cInct["A"] = "0110000";
    cInct["M"] = "1110000";
    cInct["!D"] = "0001101";
    cInct["!A"] = "0110001";
    cInct["!M"] = "1110001";
    cInct["-D"] = "0001111";
    cInct["-A"] = "0110011";
    cInct["-M"] = "1110011";
    cInct["D+1"] = "0011111";
    cInct["A+1"] = "0110111";
    cInct["M+1"] = "1110111";
    cInct["D-1"] = "0001110";
    cInct["A-1"] = "0110010";
    cInct["M-1"] = "1110010";
};

//class Cparser {

//}