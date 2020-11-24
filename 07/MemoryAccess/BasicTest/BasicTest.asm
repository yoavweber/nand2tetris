
// push constant 10
@10
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
@dkztsetoxb
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@dkztsetoxb
A=M
M=D
            
// push constant 21
@21
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 22
@22
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop ARG 2
@2
D=A
@ARG
A=M+D
D=A
@wqfgqphrcn
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@wqfgqphrcn
A=M
M=D
            
// pop ARG 1
@1
D=A
@ARG
A=M+D
D=A
@cqxbltviez
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@cqxbltviez
A=M
M=D
            
// push constant 36
@36
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop THIS 6
@6
D=A
@THIS
A=M+D
D=A
@pcwmhzaboa
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@pcwmhzaboa
A=M
M=D
            
// push constant 42
@42
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 45
@45
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop THAT 5
@5
D=A
@THAT
A=M+D
D=A
@qolzioykmm
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@qolzioykmm
A=M
M=D
            
// pop THAT 2
@2
D=A
@THAT
A=M+D
D=A
@bczeymlinr
//get the last value in the stack and assign the stack pointer to the right location
M=D


@SP
A=M
A=A-1
D=M
@SP
M=M-1

//store it in the segment
@bczeymlinr
A=M
M=D
            
// push constant 510
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// pop temp 11


@SP
A=M
A=A-1
D=M
@SP
M=M-1

@11
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

            
// push THAT 5
@5
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
        
// push THIS 6
@6
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

            
// push THIS 6
@6
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

            
// add
@SP
A=M
A=A-1
D=M
A=A-1
M=D+M
@SP
M=M-1
        
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
        
// push temp 11
@11
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
        