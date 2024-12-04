def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
    
    if n == 1000:
        return "one thousand"
    
    word = ""
    
    if n >= 100:
        word += hundreds[n // 100]
        n %= 100
        if n > 0:
            word += " and "
    
    if 0 < n < 20:
        word += ones[n]
    elif n >= 20:
        word += tens[n // 10]
        if n % 10 > 0:
            word += ones[n % 10]
    
    return word

def letter_count():
    total = 0
    for i in range(1, 1001):
        total += len(number_to_words(i).replace(" ", "").replace("-", ""))
    return total

result = letter_count()
print(result)