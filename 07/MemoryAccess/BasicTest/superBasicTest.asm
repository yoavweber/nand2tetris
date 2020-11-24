
// push constant 36
@36
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop argument 2
@2
D=A
@ARG
A=A+D
D=A
@jothohurmy
M=D
//get the last value in the stack
@SP
A=M
A=A-1
D=M
//store it in the segment
@jothohurmy
A=M
M=D

@SP
M=M-1
            
            
// push argument 1
@1
D=A
@ARG
A=A+D
D=M
//get the last value in the stack
@SP
A=M
M=D

@SP
M=M+1
            
            
// push constant 42
@42
D=A
@SP
A=M
M=D
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
        