
@256
D=A
@SP
M=D
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
A=M-1
A=A+D
D=D-1
M=0
@INITALIZIE_Sys.init
D;JNE
(EXIT_INITALIZIE_Sys.init)

        
// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// -----calling function Main.fibonacci

//--------saving the old values------------
// saving the return address
@Main.fibonacci1
D=A
@SP
A=M
M=D
//save the old LCL
@LCL
D=M
@SP
A=M
A=A+1
M=D
//save the old ARG
@ARG
D=M
@SP
A=M+1
A=A+1
M=D
//save the old THIS
@THIS
D=M
@SP
A=M+1
A=A+1
A=A+1
M=D
//save the old THAT
@THAT
D=M
@SP
A=M+1
A=A+1
A=A+1
A=A+1
M=D
//------------assigning the new values----------------------
//asign new LCL
A=A+1
D=A
@LCL
M=D
//assign new ARG pointer
@1
D=A
@SP
A=M
D=A-D
@ARG
M=D
//assign new SP
//@1
//D=A
@LCL
A=M
D=A
@SP
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci1)
        
(WHILE)
        
@WHILE
0;JMP
        
//--------function decleration -------
(Main.fibonacci)
@0
D=A
@SP
M=D+M
@EXIT_INITALIZIE_Main.fibonacci
D;JEQ
(INITALIZIE_Main.fibonacci)
@LCL
A=M-1
A=A+D
D=D-1
M=0
@INITALIZIE_Main.fibonacci
D;JNE
(EXIT_INITALIZIE_Main.fibonacci)

        
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
//assign the stack pointer to the new location
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
        
// lt
@SP
M=M-1
A=M
D=M
A=A-1
D=D-M
@lxonzlbeob
D;JGT
@SP
A=M-1
M=0
@basasplrvc
D;JMP
(lxonzlbeob)
@SP
A=M-1
M=-1
(basasplrvc)

@SP
M=M-1
A=M
D=M
@IF_TRUE
D;JNE
        
@IF_FALSE
0;JMP
        
(IF_TRUE)
        
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
//assign the stack pointer to the new location
@SP
M=M+1

            
// -------------- return function
//assign the return value to the global stack?

// get the old return value
@LCL
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@xqgonpuyny
M=D

//assning the return value to the preivous stack
@SP
A=M
A=A-1
D=M
@ARG
A=M
M=D

//assigning the old stack pointer location
@ARG
D=M+1
@SP
M=D



// getting the prevoius that
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

// jump to the return address
@xqgonpuyny
D=M
A=D
0;JMP

        
(IF_FALSE)
        
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
//assign the stack pointer to the new location
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
        
// -----calling function Main.fibonacci

//--------saving the old values------------
// saving the return address
@Main.fibonacci1
D=A
@SP
A=M
M=D
//save the old LCL
@LCL
D=M
@SP
A=M
A=A+1
M=D
//save the old ARG
@ARG
D=M
@SP
A=M+1
A=A+1
M=D
//save the old THIS
@THIS
D=M
@SP
A=M+1
A=A+1
A=A+1
M=D
//save the old THAT
@THAT
D=M
@SP
A=M+1
A=A+1
A=A+1
A=A+1
M=D
//------------assigning the new values----------------------
//asign new LCL
A=A+1
D=A
@LCL
M=D
//assign new ARG pointer
@1
D=A
@SP
A=M
D=A-D
@ARG
M=D
//assign new SP
//@1
//D=A
@LCL
A=M
D=A
@SP
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci1)
        
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
//assign the stack pointer to the new location
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
        
// -----calling function Main.fibonacci

//--------saving the old values------------
// saving the return address
@Main.fibonacci1
D=A
@SP
A=M
M=D
//save the old LCL
@LCL
D=M
@SP
A=M
A=A+1
M=D
//save the old ARG
@ARG
D=M
@SP
A=M+1
A=A+1
M=D
//save the old THIS
@THIS
D=M
@SP
A=M+1
A=A+1
A=A+1
M=D
//save the old THAT
@THAT
D=M
@SP
A=M+1
A=A+1
A=A+1
A=A+1
M=D
//------------assigning the new values----------------------
//asign new LCL
A=A+1
D=A
@LCL
M=D
//assign new ARG pointer
@1
D=A
@SP
A=M
D=A-D
@ARG
M=D
//assign new SP
//@1
//D=A
@LCL
A=M
D=A
@SP
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci1)
        
// add
@SP
A=M
A=A-1
D=M
A=A-1
M=D+M
@SP
M=M-1
        
// -------------- return function
//assign the return value to the global stack?

// get the old return value
@LCL
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@yllhdrzsyy
M=D

//assning the return value to the preivous stack
@SP
A=M
A=A-1
D=M
@ARG
A=M
M=D

//assigning the old stack pointer location
@ARG
D=M+1
@SP
M=D



// getting the prevoius that
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

// jump to the return address
@yllhdrzsyy
D=M
A=D
0;JMP

        
(INFINIELOOP)
@INFINIELOOP
0;JMP
    