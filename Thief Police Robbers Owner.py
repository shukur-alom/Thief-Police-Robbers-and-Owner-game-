import random
player_list = []
ho_play = int(input("\n\n\t\t\t\t\t\t\t\t\tWELCOME TO THE GAME\nHow many time you want to play: "))
ply_1 = 0
ply_2 = 0
ply_3 = 0
ply_4 = 0
for x in range(1,5):
   name = input(f"{x}. player name: ")
   player_list.append(name)
print(player_list)
while ho_play >= 1:  
   print(f'\n{ho_play} round\n')
   win_list = []
   count = ['c1','c2','c3','c4']
   game_contain = ['Thief','Police','Robbers','Owner']
   def rem(x,name):
      if x == 'Thief':
         print(f"\n{name} got Thief point 200\n")
         game_contain.remove('Thief')
         win_list.append(200)
      elif x == 'Police':
         print(f"\n{name} got Police point 800\n")
         game_contain.remove('Police')
         win_list.append(800)
      elif x == 'Robbers':
         print(f"{name} got Robbers point 400\n")
         game_contain.remove('Robbers')
         win_list.append(400)
      elif x == 'Owner':
         print(f"\n{name} got Owner point 900\n")
         game_contain.remove('Owner')
         win_list.append(900)
   for s in range(4):
      contain = random.choice(game_contain)
      player = input(f'{player_list[s]} choose one\n{count}\nInput: ')
      if player == 'c1':
         count.remove('c1')
         rem(contain,player_list[s])            
      elif player == 'c2':
         count.remove('c2')
         rem(contain,player_list[s])
      elif player == 'c3':
         count.remove('c3')
         rem(contain,player_list[s])
      elif player == 'c4':
         count.remove('c4')
         rem(contain,player_list[s])
   try: ply_1 += win_list[0]
   except: pass
   try: ply_2 += win_list[1]
   except: pass
   try: ply_3 += win_list[2]
   except: pass
   try:ply_4 += win_list[3]
   except: pass
   ho_play -=1
if ply_1 > ply_2 and ply_1 > ply_3 and ply_1>ply_4:
   print(f'win the match {player_list[0]} score {ply_1}')
elif ply_2 > ply_1 and ply_2 > ply_3 and ply_2>ply_4:
   print(f'win the match {player_list[1]} score {ply_2}')
elif ply_3 > ply_2 and ply_3 > ply_1 and ply_3>ply_4:
   print(f'win the match {player_list[2]} score {ply_3}')
elif ply_4 > ply_2 and ply_4 > ply_3 and ply_4>ply_1:
   print(f'win the match {player_list[3]} score {ply_4}')
elif ply_4 == ply_2 and ply_4 == ply_3 and ply_4 == ply_1:
   print("Drow the match")