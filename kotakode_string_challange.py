
def ubahString(inputString,N,karakterArray,ubahKarakter):
    masukkan = inputString
    dict_element = {}
    nilai = ""
    for elem in masukkan:
        if elem in dict_element:
            dict_element[elem] += 1
                        
        else:
            dict_element[elem] = 1

        for i in karakterArray:
            if dict_element.get(i) == N:
                if elem == i:
                    elem = ubahKarakter
                    
                else:
                    elem = elem

        nilai += elem
 
    output = print(nilai)
    return output

ubahString('kotakode adalah sebuah situs untuk programmer',3,['k','a','o'],'*')
ubahString('mari kita belajar python',1,['a','r'],'*')