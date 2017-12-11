def table(size):
    stlp_sk, eil_sk=size.split("x")
    stlp_sk, eil_sk=int(stlp_sk),int(eil_sk)
    
    def sk():
        global sk
        sk = int(sk)
        sk+=1
        if sk<10: sk=str("0"+str(sk))
        return sk

    for i in range (eil_sk):
        for z in range(stlp_sk):
            print(" ----",sep=" ",end="")
        print(" ")
        for j in range(stlp_sk):
            print("| "+str(sk())+"",end=" ")
        print("|")
    print(" ----" * stlp_sk)
sk = 0
size = input("Table size?,(example: 3x5 ")
table(size)
