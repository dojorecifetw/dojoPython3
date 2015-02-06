def romanToArabic(number):
    roman = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100}
    
    if (len(number) == 1):
        return roman[number]
    
    nextValue = romanToArabic(number[1:])
    curr = romanToArabic(number[0])
    
    bla = nextValue <= curr
    
    return (nextValue + curr) if bla else (nextValue - curr)