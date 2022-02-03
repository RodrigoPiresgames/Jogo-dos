import random
import pygame

#numero de colunas e linhas de jogo
r = 5
c = 5

#matriz de jogo
m = []

#variavél que vê se perdemos ou não
d = False

#variavél que uso para a bola
b = 0

#Variavél que ajuda nas contas
t = c * r

screen = pygame.display.set_mode((40 * c, 40 * r))

#iniciar a matriz de jogo
def matriz(m, r, c):

  for x in range(0, c):
    for y in range(0, r):
      m.append (0)
  return m 

#a primeira peça que aparece no começo do jogo
def ball_spawn(m, c):

  global d
  global b

  ball = random.randint(1,4)
  spawn = random.randint(0,c - 1)
  b = spawn
  if m[b] != 0:
    d = True
  else:
    m[b] = ball
  return m

#verificação no final de um ciclo de jogo se fizemos uma linha
def linha(c, r):

  global t
  global m

  for x in range(0, t):
      if m[x] == 0:
        pass
      else:
        if m[x] == m[x + 1]:
          if m[x + 1] == m[x + 2]:
            if m[x + 2] < c:
              m[x] = 0
              m[x + 1] = 0
              m[x + 2] = 0
            else:
              m[x] = m[x - c]
              m[x + 1] = m[(x + 1) - c]
              m[x + 2] = m[(x + 2) - c]
          else:
            pass
        elif m[x] == m[x + c]:
          if m[x + c] == m[x + (2 * c)]:
            m[x] = 0
            m[x + c] = 0
            m[x + (c * 2)] = 0
          else:
            pass
  return m

#faz a bola descer
def ball_update(m, c):

  global b

  m[b + c] = m [b]
  m[b] =  0
  b = b + c

#função que recebe imput do pl e mexe a bola
def move (m, i, c):

  global b
  MovKeyARest = b % c
  MovKeyDRest = b+1 % c
      
  if b==0 or b==c+1 or b==(c*2)+1 or b==(c*3)+1 or b==(c*4)+1 or b==(c*5)+1 or b==(c*6)+1 or b==(c*7)+1 or b==(c*8)+1  or b==(c*9)+1 or b==(c*10)+1:
    MovKeyARest = 0    
    
  if b==c-1 or b==(c*2)-1 or b==(c*3)-1 or b==(c*4)-1 or b==(c*5)-1 or b==(c*6)-1 or b==(c*7)-1 or b==(c*8)-1 or b==(c*9)-1 or b==(c*10)-1:
    MovKeyDRest = 0    

  if i == "d":
   if m[b + 1] == 0:
     if MovKeyDRest == 0:
      pass
     else:
      m[b + 1] = m[b]
      m[b] =  0
      b = b + 1
   else:
      pass
  elif i == "a":
    if m[b - 1] == 0:
      if MovKeyARest == 0 or b == 0:
        pass
      else:
        m[b - 1] = m[b]
        m[b] =  0
      b = b - 1
    else:
      pass
  else:
    pass

#função que faz todo do pygame
def display_game ():
  
  global m
  global screen
  global t

  screen.fill((0, 0, 0))

  k = 0

  j = 20

  for x in range(0, r):
    i = 20
    for y in range(0, c):
      
      if m[k] == 0:
        pygame.draw.circle(screen,(255, 255, 255), (i,j), 20, 5)
      else:
        if m[k] == 1:
          pygame.draw.circle(screen,(0, 255, 0), (i,j), 20, 5)
        elif m[k] == 2:
          pygame.draw.circle(screen,(0, 0, 255), (i,j), 20, 5)
        elif m[k] == 3:
          pygame.draw.circle(screen,(179, 0, 255), (i,j), 20, 5)
        elif m[k] == 4:
          pygame.draw.circle(screen,(255, 255, 0), (i,j), 20, 5)

      i = i + 40
      
      k = k + 1
    
    j = j + 40

  pygame.display.flip()

#ciclo principal que junta tudo
print(matriz(m, r, c))
while True:
  print()
  if d == False:
    ball_spawn(m, c)
    print(m)
    display_game()
    print()
    while m[b + c] == 0:
      i = input()
      move(m, i, c)
      ball_update(m, c)
      print(m)
      display_game()
      #linha(c, r)
      #print()
      #print(m)
      if b >= t - c:
        break
      else:
        pass
  else:
    print("You lost")
    break