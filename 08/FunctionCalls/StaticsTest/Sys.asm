
//--------function decleration -------
(Class2.set)
@0
D=A
@LCL
A=M
@EXIT_INITALIZIE_Class2.set
D;JEQ
(INITALIZIE_Class2.set)
M=0
A=A+1
D=D-1
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
//assign the stack pzointer to the new location
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
//assign the stack pzointer to the new location
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
(Class2.get)
@0
D=A
@LCL
A=M
@EXIT_INITALIZIE_Class2.get
D;JEQ
(INITALIZIE_Class2.get)
M=0
A=A+1
D=D-1
@INITALIZIE_Class2.get
D;JNE
(EXIT_INITALIZIE_Class2.get)

        
// push temp 0
@0
D=M

@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1


// push temp 1
@1
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
(Class2.set)
@0
D=A
@LCL
A=M
@EXIT_INITALIZIE_Class2.set
D;JEQ
(INITALIZIE_Class2.set)
M=0
A=A+1
D=D-1
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
//assign the stack pzointer to the new location
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
//assign the stack pzointer to the new location
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
(Class2.get)
@0
D=A
@LCL
A=M
@EXIT_INITALIZIE_Class2.get
D;JEQ
(INITALIZIE_Class2.get)
M=0
A=A+1
D=D-1
@INITALIZIE_Class2.get
D;JNE
(EXIT_INITALIZIE_Class2.get)

        
// push temp 0
@0
D=M

@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1


// push temp 1
@1
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
(Class2.set)
@0
D=A
@LCL
A=M
@EXIT_INITALIZIE_Class2.set
D;JEQ
(INITALIZIE_Class2.set)
M=0
A=A+1
D=D-1
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
//assign the stack pzointer to the new location
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
//assign the stack pzointer to the new location
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
(Class2.get)
@0
D=A
@LCL
A=M
@EXIT_INITALIZIE_Class2.get
D;JEQ
(INITALIZIE_Class2.get)
M=0
A=A+1
D=D-1
@INITALIZIE_Class2.get
D;JNE
(EXIT_INITALIZIE_Class2.get)

        
// push temp 0
@0
D=M

@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1


// push temp 1
@1
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
    