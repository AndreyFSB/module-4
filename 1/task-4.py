from random import randint
 
secret = randint(0, 100)
 
print ('Число загадано! Попытка №1:')
user_number = int(input())
for i in range(2, 9):
    if user_number == secret:
        print ("Вы победили!")
        break
    word = 'меньше' if user_number > secret else 'больше'
    print(f'Не правильно! Загаданное число {word}!')
    print(f'Попытка №{i}')
    user_number = int(input())
else:
    print ('Вы проиграли!')
