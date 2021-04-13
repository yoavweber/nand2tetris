
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

        
// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// -----calling function Class1.set

//--------saving the old values------------
// saving the return address
@Class1.set1
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
@2
D=A
@SP
A=M
D=A-D
@ARG
M=D
//assign new SP
//@2
//D=A
@LCL
A=M
D=A
@SP
M=D
@Class1.set
0;JMP
(Class1.set1)
        
// pop temp 5


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@5
M=D

// push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// -----calling function Class2.set

//--------saving the old values------------
// saving the return address
@Class2.set1
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
@2
D=A
@SP
A=M
D=A-D
@ARG
M=D
//assign new SP
//@2
//D=A
@LCL
A=M
D=A
@SP
M=D
@Class2.set
0;JMP
(Class2.set1)
        
// pop temp 5


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@5
M=D

// -----calling function Class1.get

//--------saving the old values------------
// saving the return address
@Class1.get1
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
@0
D=A
@SP
A=M
D=A-D
@ARG
M=D
//assign new SP
//@0
//D=A
@LCL
A=M
D=A
@SP
M=D
@Class1.get
0;JMP
(Class1.get1)
        
// -----calling function Class2.get

//--------saving the old values------------
// saving the return address
@Class2.get1
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
@0
D=A
@SP
A=M
D=A-D
@ARG
M=D
//assign new SP
//@0
//D=A
@LCL
A=M
D=A
@SP
M=D
@Class2.get
0;JMP
(Class2.get1)
        
(WHILE)
        
@WHILE
0;JMP
        
//--------function decleration -------
(Class2.set)
@0
D=A
@SP
M=D+M
@EXIT_INITALIZIE_Class2.set
D;JEQ
(INITALIZIE_Class2.set)
@LCL
A=M-1
A=A+D
D=D-1
M=0
@INITALIZIE_Class2.set
D;JNE
(EXIT_INITALIZIE_Class2.set)

        
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

            
// pop temp 0


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@0
M=D

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
//assign the stack pointer to the new location
@SP
M=M+1

            
// pop temp 1


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@1
M=D

// push constant 0
@0
D=A
@SP
A=M
M=D
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
@cmqwdytxas
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
@cmqwdytxas
D=M
A=D
0;JMP

        
//--------function decleration -------
(Class2.get)
@0
D=A
@SP
M=D+M
@EXIT_INITALIZIE_Class2.get
D;JEQ
(INITALIZIE_Class2.get)
@LCL
A=M-1
A=A+D
D=D-1
M=0
@INITALIZIE_Class2.get
D;JNE
(EXIT_INITALIZIE_Class2.get)

        
// push temp 0
@0
D=M

@SP
A=M
M=D
//assign the stack pointer to the new location
@SP
M=M+1


// push temp 1
@1
D=M

@SP
A=M
M=D
//assign the stack pointer to the new location
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
@leylbizsck
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
@leylbizsck
D=M
A=D
0;JMP

        
//--------function decleration -------
(Class1.set)
@0
D=A
@SP
M=D+M
@EXIT_INITALIZIE_Class1.set
D;JEQ
(INITALIZIE_Class1.set)
@LCL
A=M-1
A=A+D
D=D-1
M=0
@INITALIZIE_Class1.set
D;JNE
(EXIT_INITALIZIE_Class1.set)

        
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

            
// pop temp 0


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@0
M=D

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
//assign the stack pointer to the new location
@SP
M=M+1

            
// pop temp 1


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@1
M=D

// push constant 0
@0
D=A
@SP
A=M
M=D
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
@ginhnqnqap
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
@ginhnqnqap
D=M
A=D
0;JMP

        
//--------function decleration -------
(Class1.get)
@0
D=A
@SP
M=D+M
@EXIT_INITALIZIE_Class1.get
D;JEQ
(INITALIZIE_Class1.get)
@LCL
A=M-1
A=A+D
D=D-1
M=0
@INITALIZIE_Class1.get
D;JNE
(EXIT_INITALIZIE_Class1.get)

        
// push temp 0
@0
D=M

@SP
A=M
M=D
//assign the stack pointer to the new location
@SP
M=M+1


// push temp 1
@1
D=M

@SP
A=M
M=D
//assign the stack pointer to the new location
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
@puymvryyyz
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
@puymvryyyz
D=M
A=D
0;JMP

        
(INFINIELOOP)
@INFINIELOOP
0;JMP
    