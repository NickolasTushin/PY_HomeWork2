""""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""

print ("Введите первую подсказку")
s = int(input())
print ("Введите вторую подсказку")
p = int(input())
c = 0
for i in range(s + p):

    for j in range(s + p):
        if i + j == s and i * j == p:
            c = 1
            print(*sorted([i, j]))
            


