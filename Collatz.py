def Collatz_Maker(num) :
    numlist.append([num,len(numlist) + 1])

    # 종료          
    if num == 1 : 
        dictionary_Maker(numlist)
       
    # 짝수일 때
    elif num % 2 == 0 : 
        Nextnum = num // 2

        try :
            existed_count = CollatzDict[Nextnum]   # Nextnum이 이미 기록되어있는 시퀀스일 경우 함수종료 
            for a in range(len(numlist)) :
                numlist[a][1] += existed_count
            dictionary_Maker(numlist)   # 함수를 종료하면서 데이터를 CollatzDict에 딕션형태로 저장   (key: ColatzNum , Value: Sequence)         
            
        except :         
            Collatz_Maker(Nextnum)
        
    # 홀수일 때
    else : 
        Nextnum = (num * 3) + 1

        try :
            existed_count = CollatzDict[Nextnum]   # Nextnum이 이미 기록되어있는 시퀀스일 경우 함수종료 
            for a in range(len(numlist)) :
                numlist[a][1] += existed_count
            dictionary_Maker(numlist)   # 함수를 종료하면서 데이터를 CollatzDict에 딕션형태로 저장   (key: ColatzNum , Value: Sequence) 
                        
        except :
            Collatz_Maker(Nextnum)


def dictionary_Maker(numlist) :
    for a in range(len(numlist)) :
        dic_keys = numlist[a][0]
        dic_values = numlist[-(a+1)][1]
        CollatzDict[dic_keys] = dic_values


def What_is_best(CollatzDict) :
    bestnum = list(CollatzDict.values())
    bestnum.sort(reverse = True)
    bestnum = bestnum[0]
    for num_keys, num_values in list(CollatzDict.items()) :
        if num_values == bestnum :
            return num_keys

        
def print_everythings(num_keys) :
    printCollatz = []
    Collatz_Maker(num_keys)
    Returned = numlist
    for a in range(len(Returned)) :
        printCollatz.append(Returned[a][0])

    print(''' 
1. Number up to %d , 

2. The longest Collatz sequence : %s 

3. How long is : %d

4. Sequence Details 

==> %s
'''%(Upto, num_keys, how_long, printCollatz ))


CollatzDict = {}
Upto = 1000001
randomBox = range(1, Upto)


for num in randomBox :
    #if not num in list(CollatzDict.keys()) :
    numlist = []
    Collatz_Maker(num)


highest = What_is_best(CollatzDict)
how_long = CollatzDict[highest]
CollatzDict = {}
numlist = []

print_everythings(highest)


print("\n" ,(end - start),"초") 
