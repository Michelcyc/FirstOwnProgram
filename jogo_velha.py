# -*- coding: cp1252 -*-
a = ' '
b = ' '
c = ' '
d = ' '
e = ' '
f = ' '
g = ' '
h = ' '
i = ' '
velha = 1

import random
def jogo_velha(a,b,c,d,e,f,g,h,i):
    print(" %s | %s | %s " %(a,b,c)),("    1 | 2 | 3 ")
    print("___|___|___"), ("   ___|___|___")
    print(" %s | %s | %s  ") %(d,e,f), ("   4 | 5 | 6 ")
    print("___|___|___"), ("   ___|___|___")
    print(" %s | %s | %s  ") %(g,h,i), ("   7 | 8 | 9 ")
    print("   |   |   "), ("      |   |   ")

    
def multiplayer(a,b,c,d,e,f,g,h,i,velha):
    nome1 = raw_input("Jogador 1 digite seu nome ")
    nome2 = raw_input("Jogador 2 digite seu nome ")
    print
    print
    benzocriol = random.randrange(1,3)     
    fim_loop = benzocriol + 9   
    if benzocriol == 1 :
        print("%s" %(nome1), " vc eh o primeiro!!")
    else:
        print("%s" %(nome2), " vc eh o primeiro!!")  
    print("Esta é sua lista de escolhas")
    print(" 1 | 2 | 3 ")
    print("___|___|___")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print(" 7 | 8 | 9 ")
    print("   |   |   ")    
    while benzocriol < fim_loop : 
        if benzocriol%2 <> 0:
            print('%s' %(nome1), 'escreva sua escolha' )
            escolha = input()
            if escolha == 1 and a == ' ' :  
                a = 'O'   
                jogo_velha(a,b,c,d,e,f,g,h,i) 
            elif escolha == 2 and b == ' ' :
                b = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 3 and c == ' ' :
                c = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 4 and d == ' ' :
                d = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 5 and e == ' ' :
                e = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 6 and f == ' ' :
                f = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 7 and g == ' ' :
                g = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 8 and h == ' ' :
                h = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 9 and i == ' ' :
                i = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            else:  
                print("Escolha incorreta ou escolha já feita !! Escolha novamente !")
                benzocriol = benzocriol - 1
        elif benzocriol%2 == 0: 
              print('%s' %(nome2), 'escreva sua escolha' )
              escolha = input()
              if escolha == 1 and a == ' ' :
                  a = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif escolha == 2 and b == ' ' :
                  b = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif escolha == 3 and c == ' ' :
                  c = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif escolha == 4 and d == ' ' :
                  d = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif escolha == 5 and e == ' ' :
                  e = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif escolha == 6 and f == ' ' :
                  f = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif escolha == 7 and g == ' ' :
                  g = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif escolha == 8 and h == ' ' :
                  h = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif escolha == 9 and i == ' ' :
                  i = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              else:
                  print("Escolha incorreta ou escolha já feita !! Escolha novamente !")
                  benzocriol = benzocriol - 1
        if ((a==b)and(a==c) and (a == 'O')) or ((d==e)and(d==f)and (d == 'O')) or ((g==h)and(g==i)and (g == 'O')) or ((a==d)and(a==g)and (a == 'O')) or ((b==e)and(b==h)and (b == 'O')) or ((c==f)and(c==i)and (c == 'O')) or ((a==e)and(a==i)and (a == 'O')) or ((c==e)and(c==g)and (c == 'O')) :
            print("%s eh o vencedor") %(nome1)
            velha = 0
            break
        elif ((a==b)and(a==c) and (a == 'X')) or ((d==e)and(d==f)and (d == 'X')) or ((g==h)and(g==i)and (g == 'X')) or ((a==d)and(a==g)and (a == 'X')) or ((b==e)and(b==h)and (b == 'X')) or ((c==f)and(c==i)and (c == 'X')) or ((a==e)and(a==i)and (a == 'X')) or ((c==e)and(c==g)and (c == 'X')) :
            print("%s eh o vencedor") %(nome2)
            velha = 0
            break  
        benzocriol = benzocriol + 1
    if velha <> 0:
        print("Velha")

def singleplayer(a,b,c,d,e,f,g,h,i,velha):
    nome1 = raw_input("Digite seu nome ")
    print
    print
    benzocriol = random.randrange(1,3)
    fim_loop = benzocriol + 9
    if benzocriol == 1 :
        print("%s" %(nome1), " vc eh o primeiro!!")
    else:
        print("A maquina comecou jogando...")
    print("Esta é sua lista de escolhas")
    print(" 1 | 2 | 3 ")
    print("___|___|___")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print(" 7 | 8 | 9 ")
    print("   |   |   ")
    while benzocriol < fim_loop :
        if benzocriol%2 <> 0:
            print('%s' %(nome1), 'escreva sua escolha' )
            escolha = input()
            if escolha == 1 and a == ' ' :
                a = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 2 and b == ' ' :
                b = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 3 and c == ' ' :
                c = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 4 and d == ' ' :
                d = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 5 and e == ' ' :
                e = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 6 and f == ' ' :
                f = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 7 and g == ' ' :
                g = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 8 and h == ' ' :
                h = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            elif escolha == 9 and i == ' ' :
                i = 'O'
                jogo_velha(a,b,c,d,e,f,g,h,i)
            else:
                print("Escolha incorreta ou escolha já feita !! Escolha novamente !")
                benzocriol = benzocriol - 1
        elif benzocriol%2 == 0:
              print("Maquina jogou !!")
              if ((b==c) and (a == ' ') and (b == 'X')) or ((e==i)and (a == ' ') and (e == 'X')) or ((d==g)and (a == ' ') and (d == 'X')) :
                  a = 'X' 
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((a==c) and (b == ' ') and (a == 'X')) or ((e==h)and (b == ' ') and (e == 'X')) :
                  b = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((a==b) and (c == ' ') and (a == 'X')) or ((g==e) and (c == ' ') and (g == 'X')) or ((f==i) and (c == ' ') and (f == 'X')) :
                  c = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((e==f) and (d == ' ') and (e == 'X')) or ((a==g) and (d == ' ') and (a == 'X')) :
                  d = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((a==i) and (e == ' ') and (a == 'X')) or ((b==h) and (e == ' ') and (b == 'X')) or ((c==g) and (e == ' ') and (c == 'X')) or ((d==f) and (e == ' ') and (d == 'X')) :
                  e = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((d==e) and (f == ' ') and (d == 'X')) or ((c==i) and (f == ' ') and (c == 'X')) :
                  f = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((a==d) and (g == ' ') and (a == 'X')) or ((e==c) and (g == ' ') and (e == 'X')) or ((h==i) and (g == ' ') and (h == 'X')) :
                  g = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((g==i) and (h == ' ') and (g == 'X')) or ((b==e) and (h == ' ') and (b == 'X')) :
                  h = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((g==h) and (i == ' ') and (g == 'X')) or ((a==e) and (i == ' ') and (a == 'X')) or ((c==f) and (i == ' ') and (c == 'X')) :
                  i = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((b==c) and (a == ' ') and (b == 'O')) or ((e==i)and (a == ' ') and (e == 'O')) or ((d==g)and (a == ' ') and (d == 'O')) :
                  a = 'X' 
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((a==c) and (b == ' ') and (a == 'O')) or ((e==h)and (b == ' ') and (e == 'O')) :
                  b = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((a==b) and (c == ' ') and (a == 'O')) or ((g==e) and (c == ' ') and (g == 'O')) or ((f==i) and (c == ' ') and (f == 'O')) :
                  c = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((e==f) and (d == ' ') and (e == 'O')) or ((a==g) and (d == ' ') and (a == 'O')) :
                  d = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((a==i) and (e == ' ') and (a == 'O')) or ((b==h) and (e == ' ') and (b == 'O')) or ((c==g) and (e == ' ') and (c == 'O')) or ((d==f) and (e == ' ') and (d == 'O')) :
                  e = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((d==e) and (f == ' ') and (d == 'O')) or ((c==i) and (f == ' ') and (c == 'O')) :
                  f = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((a==d) and (g == ' ') and (a == 'O')) or ((e==c) and (g == ' ') and (e == 'O')) or ((h==i) and (g == ' ') and (h == 'O')) :
                  g = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((g==i) and (h == ' ') and (g == 'O')) or ((b==e) and (h == ' ') and (b == 'O')) :
                  h = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              elif ((g==h) and (i == ' ') and (g == 'O')) or ((a==e) and (i == ' ') and (a == 'O')) or ((c==f) and (i == ' ') and (c == 'O')) :
                  i = 'X'
                  jogo_velha(a,b,c,d,e,f,g,h,i)
              else:
                  while True : 
                      escolha = random.randrange(1,10)
                      if escolha == 1 and a == ' ' :
                          a = 'X'
                          jogo_velha(a,b,c,d,e,f,g,h,i)
                          break 
                      if escolha == 2 and b == ' ' :
                          b = 'X'
                          jogo_velha(a,b,c,d,e,f,g,h,i)
                          break
                      if escolha == 3 and c == ' ' :
                          c = 'X'
                          jogo_velha(a,b,c,d,e,f,g,h,i)
                          break
                      if escolha == 4 and d == ' ' :
                          d = 'X'
                          jogo_velha(a,b,c,d,e,f,g,h,i)
                          break
                      if escolha == 5 and e == ' ' :
                          e = 'X'
                          jogo_velha(a,b,c,d,e,f,g,h,i)
                          break
                      if escolha == 6 and f == ' ' :
                          f = 'X'
                          jogo_velha(a,b,c,d,e,f,g,h,i)
                          break
                      if escolha == 7 and g == ' ' :
                          g = 'X'
                          jogo_velha(a,b,c,d,e,f,g,h,i)
                          break
                      if escolha == 8 and h == ' ' :
                          h = 'X'
                          jogo_velha(a,b,c,d,e,f,g,h,i)
                          break
                      if escolha == 9 and i == ' ' :
                          i = 'X'
                          jogo_velha(a,b,c,d,e,f,g,h,i)
                          break
        if ((a==b)and(a==c) and (a == 'O')) or ((d==e)and(d==f)and (d == 'O')) or ((g==h)and(g==i)and (g == 'O')) or ((a==d)and(a==g)and (a == 'O')) or ((b==e)and(b==h)and (b == 'O')) or ((c==f)and(c==i)and (c == 'O')) or ((a==e)and(a==i)and (a == 'O')) or ((c==e)and(c==g)and (c == 'O')) :
            print("%s eh o vencedor") %(nome1)
            velha = 0
            break
        elif ((a==b)and(a==c) and (a == 'X')) or ((d==e)and(d==f)and (d == 'X')) or ((g==h)and(g==i)and (g == 'X')) or ((a==d)and(a==g)and (a == 'X')) or ((b==e)and(b==h)and (b == 'X')) or ((c==f)and(c==i)and (c == 'X')) or ((a==e)and(a==i)and (a == 'X')) or ((c==e)and(c==g)and (c == 'X')) :
            print("Maquina venceu!! Ai que burrico...Kkkk....")
            velha = 0
            break
        benzocriol = benzocriol + 1
    if velha <> 0:
        print("Velha")

print("Modo de jogo :")
print("1 - Single Player")
print("2 - Multiplayer")
modo_jogo = input()
if modo_jogo == 1 :
    singleplayer(a,b,c,d,e,f,g,h,i,velha)
elif modo_jogo == 2 :
    multiplayer(a,b,c,d,e,f,g,h,i,velha)

