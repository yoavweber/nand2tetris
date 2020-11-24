
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop LCL 0
@0
D=A
@LCL
A=M+D
D=A
@agmraytagq
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@agmraytagq
A=M
M=D
            
(LOOP_START)
        
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

            
// push LCL 0
@0
D=A
@LCL
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
        
// pop LCL 0	
@0	
D=A
@LCL
A=M+D
D=A
@xhuveezlba
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@xhuveezlba
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
@ywkjfgkchl
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@ywkjfgkchl
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

            
@SP
M=M-1
A=M
D=M
@LOOP_START
D;JNE
        
// push LCL 0
@0
D=A
@LCL
A=M+D
D=M
//get the last value in the stack 

@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1

            
(INFINIELOOP)
@INFINIELOOP
0;JMP
        