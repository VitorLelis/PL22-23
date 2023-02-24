text = input('Insert text:\n') #Lê do stdin

words = text.strip('\n').split() #Lista com todas as palavras

flag = True #Para controlar o comportamento

total = 0 #Total somado

for w in words:
#Transforma a palavra totalmente em lowercase para comparar
    if w.lower() == 'on':
        flag = True
            
    elif w.lower() == 'off': 
        flag = False
    
    elif w == '=': 
        print(total)
    
    else:
        try:
            #Tenta converter o int para somar ao total
            if flag:
              total += int(w) 
    
        except:
            continue