def convertToRoman(num):
    try:
        if num <= 0 or num > 3999:
            raise Exception("Invalid Number")
    except ValueError:
        raise Exception("Invalid Number")
    roman = (("I", 1), ("V", 5), ("X", 10), ("L", 50),
             ("C", 100), ("D", 500), ("M", 1000))
    converted=""
    i=0
    while num>0:
        n=pow(10, i+1)
        temp=int(num / n)*n
        div=num-temp
        num=temp
        
        i+=1
        r=0
        rIndex=0
        t=0
        for t in range(len(roman)):
            if roman[t][1]<=div:
                r=roman[t][1]
                rIndex=t
        
        if div-roman[rIndex][1]>=0:
            converted+=roman[rIndex][0]
            div-=roman[rIndex][1]
            print("%d %d"%(div, (roman[rIndex][1])))
        if div-(roman[rIndex+1][1]-roman[rIndex][1])==0:
            print("%d %d"%(div, (roman[rIndex+1][1]-roman[rIndex][1])))
            converted+=roman[rIndex][0]+roman[rIndex+1][1]
        else:
            for j in range(1,3):
                if div-roman[rIndex][1]>=0:
                    converted+=roman[rIndex][0]
                    div-=roman[rIndex][1]
        
    return converted

print(convertToRoman(812))