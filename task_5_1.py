# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'Съешь ещёабв этих мягабвких французских булок абв'
my_list = list(filter(lambda x: 'абв' not in x , text.split()))
print(' '.join(my_list))





# a= filter(lambda x: ('абв' not in x),  ('dabvf abvlj abv kjkdabv'))
# print(list(a))
