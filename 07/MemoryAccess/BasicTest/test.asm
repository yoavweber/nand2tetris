// //pop argument 2
// 
// @2
// D=A
// @30 //ARG(at 30)
// A=A+D
// D=A
// @verible
// M=D
// //get the last value in the stack
// @4 //SP
// A=M
// A=A-1
// D=M
// //store it in the segment
// @verible
// A=M
// M=D
// 



//push argument 1
@1
D=A
@30 //ARG(at 30)
A=A+D
D=M
//get the last value in the stack
@4 //SP
A=M
M=D
@4 //SP
M=M+1

// expected 10 to be 10