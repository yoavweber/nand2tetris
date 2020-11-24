
// push ARG 1
@1
D=A
@ARG
A=M+D
D=M
//get the last value in the stack 

@SP
A=M
M=D
//assign the stack pzointer to the new location
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

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop THAT 0
@0
D=A
@THAT
A=M+D
D=A
@gddnepgsox
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@gddnepgsox
A=M
M=D
            
// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop THAT 1
@1
D=A
@THAT
A=M+D
D=A
@hsqjgcuihm
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@hsqjgcuihm
A=M
M=D
            
// push ARG 0
@0
D=A
@ARG
A=M+D
D=M
//get the last value in the stack 

@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1

            
// push constant 2
@2
D=A
@SP
A=M
M=D
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
        
// pop ARG 0
@0
D=A
@ARG
A=M+D
D=A
@fwrpfwwgdf
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@fwrpfwwgdf
A=M
M=D
            
(MAIN_LOOP_START)
        
// push ARG 0
@0
D=A
@ARG
A=M+D
D=M
//get the last value in the stack 

@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1

            
@SP
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JNE
        
@END_PROGRAM
0;JMP
        
(COMPUTE_ELEMENT)
        
// push THAT 0
@0
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

            
// push THAT 1
@1
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
        
// pop THAT 2
@2
D=A
@THAT
A=M+D
D=A
@wozurwjahe
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@wozurwjahe
A=M
M=D
            
// push temp THAT
@THAT
D=M

@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1


// push constant 1
@1
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
        
// pop temp THAT


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@THAT
M=D

// push ARG 0
@0
D=A
@ARG
A=M+D
D=M
//get the last value in the stack 

@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1

            
// push constant 1
@1
D=A
@SP
A=M
M=D
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
        
// pop ARG 0
@0
D=A
@ARG
A=M+D
D=A
@ixrikaplds
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@ixrikaplds
A=M
M=D
            
@MAIN_LOOP_START
0;JMP
        
(END_PROGRAM)
        
(INFINIELOOP)
@INFINIELOOP
0;JMP
        