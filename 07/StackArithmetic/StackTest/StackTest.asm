
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=D-M
@qtleqwwwqn
D;JEQ
@SP
A=M-1
M=0
@dbeamhgmzk
D;JMP
(qtleqwwwqn)
@SP
A=M-1
M=-1
(dbeamhgmzk)

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=D-M
@tpdrctkgek
D;JEQ
@SP
A=M-1
M=0
@kveoprezpn
D;JMP
(tpdrctkgek)
@SP
A=M-1
M=-1
(kveoprezpn)

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=D-M
@fdpqakfbti
D;JEQ
@SP
A=M-1
M=0
@buvdcjrjcd
D;JMP
(fdpqakfbti)
@SP
A=M-1
M=-1
(buvdcjrjcd)

// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 891
@891
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
@zdvscapjss
D;JGT
@SP
A=M-1
M=0
@nqopznlhvh
D;JMP
(zdvscapjss)
@SP
A=M-1
M=-1
(nqopznlhvh)

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 892
@892
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
@pcebxdsxeb
D;JGT
@SP
A=M-1
M=0
@cbqrsxwdbh
D;JMP
(pcebxdsxeb)
@SP
A=M-1
M=-1
(cbqrsxwdbh)

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 891
@891
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
@zxfzbpquui
D;JGT
@SP
A=M-1
M=0
@fmyenotmyj
D;JMP
(zxfzbpquui)
@SP
A=M-1
M=-1
(fmyenotmyj)

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// gt
@SP
M=M-1
A=M
D=M
A=A-1
D=D-M
@hezjkewuqr
D;JLT
@SP
A=M-1
M=0
@klasxflmkt
D;JMP
(hezjkewuqr)
@SP
A=M-1
M=-1
(klasxflmkt)

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// gt
@SP
M=M-1
A=M
D=M
A=A-1
D=D-M
@qhyalsspzl
D;JLT
@SP
A=M-1
M=0
@ravtvyfvej
D;JMP
(qhyalsspzl)
@SP
A=M-1
M=-1
(ravtvyfvej)

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// gt
@SP
M=M-1
A=M
D=M
A=A-1
D=D-M
@lespiftcbc
D;JLT
@SP
A=M-1
M=0
@rboifajans
D;JMP
(lespiftcbc)
@SP
A=M-1
M=-1
(rboifajans)

// push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// push constant 53
@53
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
        
// push constant 112
@112
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
        
// neg
@SP
A=M
A=A-1
M=-M
    
// or
@SP
A=M
A=A-1
D=M
A=A-1
M=D&M
@SP
M=M-1
        
// push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
        
// or
@SP
A=M
A=A-1
D=M
A=A-1
M=D|M
@SP
M=M-1
        
// not
@SP
A=M
A=A-1
M=!M
    
(INFINIELOOP)
@INFINIELOOP
0;JMP
        