from re import split as splt, search

#alinea A
#Calcula a frequência de processos por ano (primeiro elemento da data);
def a_line()-> dict:
    file_handle = open('processos.txt', 'r')

    res = dict()

    for line in file_handle:
        l = list(filter(lambda x: x != '', splt('::|-|\n', line)))
        if l:
            year = l[1]
            process = int(l[0])
            current = res.get(year,0)
            res[year] = process + current

    return res

#alinea B
#Calcula a frequência de nomes próprios (o primeiro em cada nome) 
# e apelidos (o ultimo em cada nome) por séculos e apresenta os 5 mais usados;

#alinea C
#Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.;
def c_line()-> dict:
    file_handle = open('processos.txt', 'r')

    res = dict()

    for line in file_handle:
        if search(',Ti(a|o)\s', line):
            count = res.get('Sobrinho',0)
            res['Sobrinho'] = count + 1
        elif search(',Avo\s', line):
            count = res.get('Neto',0)
            res['Neto'] = count + 1
        elif search(',Irma(o)?\s', line):
            count = res.get('Irmao',0)
            res['Irmao'] = count + 1
        elif search(',Pai|Mae\s', line):
            count = res.get('Filho',0)
            res['Filho'] = count + 1

    return res        

#alinea D
#Converta os 20 primeiros registos num novo ficheiro de output mas em formato Json.