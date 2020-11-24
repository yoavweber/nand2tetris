
// push constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop temp THIS


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@THIS
M=D

// push constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop temp THAT


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@THAT
M=D

// push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop THIS 2
@2
D=A
@THIS
A=M+D
D=A
@dqjvbglwbg
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@dqjvbglwbg
A=M
M=D
            
// push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop THAT 6
@6
D=A
@THAT
A=M+D
D=A
@ngvxgmkxzd
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@ngvxgmkxzd
A=M
M=D
            
// push temp THIS
@THIS
D=M

@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1


// push temp THAT
@THAT
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
        
// push THIS 2
@2
D=A
@THIS
A=M+D
D=M
//get the last value in the stack 

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
        
// push THAT 6
@6
D=A
@THAT
A=M+D
D=M
//get the last value in the stack 

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
        