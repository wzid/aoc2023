from sys import stdin

s = 0
for line in stdin:
    line = line.rstrip()
    digits = []
    sub = ''
    
    i = 0
    while i < len(line):
        if digits:
            break
        c = line[i]
        if c.isdigit():
            digits.append(c)
            i += 1
        else:
            sub3 = line[i:i+3]
            if i + 3 > len(line):
                i += 1
            elif sub3 == 'one':
                digits.append('1')
                i += 3
            elif sub3 == 'two':
                digits.append('2')
                i += 3
            elif sub3 == 'six':
                digits.append('6')
                i += 3
            elif sub3 == 'thr':
                if i+5 <= len(line) and line[i:i+5] == 'three':
                    digits.append('3')
                    i += 5
                else:
                    i += 3
            elif sub3 == 'fou':
                if i+4 <= len(line) and line[i:i+4] == 'four':
                    digits.append('4')
                    i += 4
                else:
                    i += 3
            elif sub3 == 'fiv':
                if i+4 <= len(line) and line[i:i+4] == 'five':
                    digits.append('5')
                    i += 4
                else:
                    i += 3
            elif sub3 == 'sev':
                if i+5 <= len(line) and line[i:i+5] == 'seven':
                    digits.append('7')
                    i += 5
                else:
                    i += 3
            elif sub3 == 'eig':
                if i+5 <= len(line) and line[i:i+5] == 'eight':
                    digits.append('8')
                    i += 5
                else:
                    i += 3
            elif sub3 == 'nin':
                if i+4 <= len(line) and line[i:i+4] == 'nine':
                    digits.append('9')
                    i += 4
                else:
                    i += 3
            else:
                i += 1
    digits2 = []
    i = len(line) - 1
    while i >= 0:
        if digits2:
            break
        c = line[i]
        if c.isdigit():
            digits2.append(c)
            i -= 1
        else:
            sub3 = line[i-2:i+1]
            if i - 3 < 0:
                i -= 1
            elif sub3 == 'one':
                digits2.append('1')
                i -= 3
            elif sub3 == 'two':
                digits2.append('2')
                i -= 3
            elif sub3 == 'six':
                digits2.append('6')
                i -= 3
            elif sub3 == 'ree':
                if i-4 > 0 and line[i-4:i+1] == 'three':
                    digits2.append('3')
                    i -= 5
                else:
                    i -= 3
            elif sub3 == 'our':
                if i-4 > 0 and line[i-3:i+1] == 'four':
                    digits2.append('4')
                    i -= 4
                else:
                    i -= 3
            elif sub3 == 'ive':
                if i-4 > 0 and line[i-3:i+1] == 'five':
                    digits2.append('5')
                    i -= 4
                else:
                    i -= 3
            elif sub3 == 'ven':
                if i-5 > 0 and line[i-4:i+1] == 'seven':
                    digits2.append('7')
                    i -= 5
                else:
                    i -= 3
            elif sub3 == 'ght':
                if i-5 > 0 and line[i-4:i+1] == 'eight':
                    digits2.append('8')
                    i -= 5
                else:
                    i -= 3
            elif sub3 == 'ine':
                if i-4 > 0 and line[i-3:i+1] == 'nine':
                    digits2.append('9')
                    i -= 4
                else:
                    i -= 3
            else:
                i -= 1
    v = int(digits[0] + digits2[0])
    s += v
print(s)