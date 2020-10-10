def minimumTekan(perintah):
    x = perintah[0]
    y = perintah [1] 
    
    if x<1 or x>1000 or y<0 or y>1000:
        return 0
    
    if x > y:
        output = x - y

    if x < y:
        hitung_1 = 0
        x1 = x
        y1 = y
        while x1 < y1 : 
            x1 = x1 * 2
            hitung_1 += 1
        hitung_1 = hitung_1 + (x1 - y1)
    
        # Scenario 2
        x2 = x
        y2 = y
        hitung_2 = 0

        if y2 % 2 == 1:
            while y2 % 2 == 1 and x2 < y2:
                y2 = y2 + 1
                hitung_2 += 1

            while y2 % 2 == 0 and x2 < y2:
                y2 = y2//2
                hitung_2 += 1

            hitung_2 = hitung_2 + (x2 - y2)
            output = min(hitung_1, hitung_2)

        # Scenario 2.2
        else:
            while y2 % 2 == 0 and x2 < y2:
                y2 = y2//2
                hitung_2 += 1

            while y2 % 2 == 1 and x2 < y2:
                y2 = y2 + 1
                hitung_2 += 1

            hitung_2 = hitung_2 + (x2 - y2)
            output = min(hitung_1, hitung_2)

  # Output
    print(output)
    return output

#masukan = input()
minimumTekan([0,40])
minimumTekan([9,20])
minimumTekan([40,65])