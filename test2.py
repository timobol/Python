import random

print('じゃんけんスタート')

print('自分の手を入力してください')
my_hand = int(input('0:グー, 1:チョキ, 2:パー'))
you_hand = random.randint(0, 2)

if my_hand == you_hand:    
  print('あいこ')
elif my_hand - you_hand == -1 or my_hand - you_hand == 2:
  print('勝ち')
else:
  print('負け')