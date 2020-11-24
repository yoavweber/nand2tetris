
// push constant 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop temp StaticTest.8


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@StaticTest.8
M=D

// pop temp StaticTest.3


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@StaticTest.3
M=D

// pop temp StaticTest.1


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@StaticTest.1
M=D

// push temp StaticTest.3
@StaticTest.3
D=M

@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1


// push temp StaticTest.1
@StaticTest.1
D=M

@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1


// sub
@SP
A=M
A=A-1
D=M
A=A-1

D=-D
M=D+M
        
@SP
M=M-1
        
// push temp StaticTest.8
@StaticTest.8
D=M

@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1


// add
@SP
A=M
A=A-1
D=M
A=A-1
M=D+M
@SP
M=M-1
        
(INFINIELOOP)
@INFINIELOOP
0;JMP
        