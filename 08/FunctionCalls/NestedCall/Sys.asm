
//--------function decleration -------
(Sys.init)
@0
D=A
@SP
M=D+M
@EXIT_INITALIZIE_Sys.init
D;JEQ
(INITALIZIE_Sys.init)
@LCL
A=M
A=A+D
M=0
D=D-1
@INITALIZIE_Sys.init
D;JNE
(EXIT_INITALIZIE_Sys.init)

        
// push constant 4000	
@4000	
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

// push constant 5000
@5000
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

// -----calling function Sys.main

//--------saving the old values------------
//save the old LCL
@LCL
D=M
@SP
A=M
M=D
//save the old ARG
@ARG
D=M
@SP
A=M+1
M=D
//save the old THIS
@THIS
D=M
@SP
A=M+1
A=A+1
M=D
//save the old THAT
@THAT
D=M
@SP
A=M+1
A=A+1
A=A+1
M=D
//------------assigning the new values----------------------
//asign new LCL
A=A+1
A=A+1
D=A
@LCL
M=D
//assign new ARG
@0
D=A
@SP
A=M
D=A-D
@ARG
M=D
//assign new SP
@0
D=A
@LCL
A=M
A=A+1
D=A+D
@SP
M=D+1
@Sys.main
0;JMP
        
// pop temp 6


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@6
M=D

(LOOP)
        
@LOOP
0;JMP
        
//--------function decleration -------
(Sys.main)
@5
D=A
@SP
M=D+M
@EXIT_INITALIZIE_Sys.main
D;JEQ
(INITALIZIE_Sys.main)
@LCL
A=M
A=A+D
M=0
D=D-1
@INITALIZIE_Sys.main
D;JNE
(EXIT_INITALIZIE_Sys.main)

        
// push constant 4001
@4001
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

// push constant 5001
@5001
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

// push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop LCL 1
@1
D=A
@LCL
A=M+D
D=A
@kyfyfytvme
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@kyfyfytvme
A=M
M=D
            
// push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop LCL 2
@2
D=A
@LCL
A=M+D
D=A
@cqfbvcjtoh
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@cqfbvcjtoh
A=M
M=D
            
// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop LCL 3
@3
D=A
@LCL
A=M+D
D=A
@nwhwpewikz
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@nwhwpewikz
A=M
M=D
            
// push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// -----calling function Sys.add12

//--------saving the old values------------
//save the old LCL
@LCL
D=M
@SP
A=M
M=D
//save the old ARG
@ARG
D=M
@SP
A=M+1
M=D
//save the old THIS
@THIS
D=M
@SP
A=M+1
A=A+1
M=D
//save the old THAT
@THAT
D=M
@SP
A=M+1
A=A+1
A=A+1
M=D
//------------assigning the new values----------------------
//asign new LCL
A=A+1
A=A+1
D=A
@LCL
M=D
//assign new ARG
@1
D=A
@SP
A=M
D=A-D
@ARG
M=D
//assign new SP
@1
D=A
@LCL
A=M
A=A+1
D=A+D
@SP
M=D+1
@Sys.add12
0;JMP
        
// pop temp 5


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@5
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

            
// push LCL 2
@2
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

            
// push LCL 3
@3
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

            
// push LCL 4
@4
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
        
// add
@SP
A=M
A=A-1
D=M
A=A-1
M=D+M
@SP
M=M-1
        
// add
@SP
A=M
A=A-1
D=M
A=A-1
M=D+M
@SP
M=M-1
        
// add
@SP
A=M
A=A-1
D=M
A=A-1
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
        
//--------function decleration -------
(Sys.add12)
@0
D=A
@SP
M=D+M
@EXIT_INITALIZIE_Sys.add12
D;JEQ
(INITALIZIE_Sys.add12)
@LCL
A=M
A=A+D
M=0
D=D-1
@INITALIZIE_Sys.add12
D;JNE
(EXIT_INITALIZIE_Sys.add12)

        
// push constant 4002
@4002
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

// push constant 5002
@5002
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

            
// push constant 12
@12
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
    