cInstructorsComp = {}
cInstructorsDest = {}
cInstructorsJump = {}
#------------------COMP-----------------------------
cInstructorsComp["0"] = "0101010"
cInstructorsComp["1"] = "0111111"
cInstructorsComp["-1"] = "0111010"
cInstructorsComp["D"] = "0001100"
cInstructorsComp["A"] = "0110000"
cInstructorsComp["M"] = "1110000"
cInstructorsComp["!D"] = "0001101"
cInstructorsComp["!A"] = "0110001"
cInstructorsComp["!M"] = "1110001"
cInstructorsComp["-D"] = "0001111"
cInstructorsComp["-A"] = "0110011"
cInstructorsComp["-M"] = "1110011"
cInstructorsComp["D+1"] = "0011111"
cInstructorsComp["A+1"] = "0110111"
cInstructorsComp["M+1"] = "1110111"
cInstructorsComp["D-1"] = "0001110"
cInstructorsComp["A-1"] = "0110010"
cInstructorsComp["M-1"] = "1110010"
cInstructorsComp["D+A"] = "0000010"
cInstructorsComp["D+M"] = "1000010"
cInstructorsComp["D-A"] = "0010011"
cInstructorsComp["D-M"] = "1010011"
cInstructorsComp["A-D"] = "0000111"
cInstructorsComp["M-D"] = "1000111"
cInstructorsComp["D&A"] = "0000000"
cInstructorsComp["D&M"] = "1000000"
cInstructorsComp["D|A"] = "0010101"
cInstructorsComp["D|M"] = "1010101"

#------------------DEST-----------------------------
cInstructorsDest[""] = "000"
cInstructorsDest["M"] = "001"
cInstructorsDest["D"] = "010"
cInstructorsDest["MD"] = "011"
cInstructorsDest["A"] = "100"
cInstructorsDest["AM"] = "101"
cInstructorsDest["AD"] = "110"
cInstructorsDest["AMD"] = "111"
#------------------JUMP-----------------------------
cInstructorsJump[""] = "000"
cInstructorsJump["JGT"] = "001"
cInstructorsJump["JEQ"] = "010"
cInstructorsJump["JGE"] = "011"
cInstructorsJump["JLT"] = "100"
cInstructorsJump["JNE"] = "101"
cInstructorsJump["JLE"] = "110"
cInstructorsJump["JMP"] = "111"

#---------------------SYMBOLS-----------------------
symbols = {
    'R0': 0,
    'R1': 1,
    'R2': 2,
    'R3': 3,
    'R4': 4,
    'R5': 5,
    'R6': 6,
    'R7': 7,
    'R8': 8,
    'R9': 9,
    'R1O': 10,
    'R11': 11,
    'R12': 12,
    'R13': 13,
    'R14': 14,
    'R15': 15,
    'SCREEN': 16384,
    'KBD': 24576,
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4
}

memoryLocation = 16