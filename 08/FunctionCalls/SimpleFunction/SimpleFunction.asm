
(SimpleFunction.test)
@2
D=A
@arguments
M=D

        
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

            
// push LCL 1
@1
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
        
// not
@SP
A=M
A=A-1
M=!M
    
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

            
// add
@SP
A=M
A=A-1
D=M
A=A-1
M=D+M
@SP
M=M-1
        
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
        


//assign the return value to the global stack
@SP
A=M
A=A-1
D=M
@ARG
A=M
M=D

//assigning the old stack location
@ARG
D=M+1
@SP
M=D

// getting the prevouse that
@LCL
A=M
A=A-1
D=M
@THAT
M=D
// getting to the prevoius this
@LCL
A=M
A=A-1
A=A-1
D=M
@THIS
M=D
// getting previous ARG
@LCL
A=M
A=A-1
A=A-1
A=A-1
D=M
@ARG
M=D
// getting previous LCL
@LCL
A=M
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@LCL
M=D
        
(INFINIELOOP)
@INFINIELOOP
0;JMP
        