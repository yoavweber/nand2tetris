@R2
M=0
@R1
D=M // D is 3 now
M=D-1 // M is 2 now
@R13
D;JLE
@R0
D=M // D is 5 now
@R2
M=D+M
@R2
A;JMP

@R2
M=M-D
(END)
@END
0; JMP
 









// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// loop over R0 R1 times and each time add R0

// @R3
// D=M
// @5
// D=D-A
// @100
// D;JEQ
// M=A
// @200
// 0;JMP







// @R0
// D=M
// @R1
// A=M
// D=A-1
// @R2
// D=A
// @R3
// M=D


// @R3
// M=D+M
// @R5
// A;JEQ
// M=A