import ply.lex as lex

tokens = (
    'TIMES',
    'MINUS',
    'LESS',
    'GREAT',
    'COMMENT'
)

def t_TIMES(t):
    r'*'
    return t

def t_MINUS(t):
    r'-'
    return t

def t_LESS(t):
    r'<'
    return t

def t_GREAT(t):
    r'>'
    return t

def t_COMMENT(t):
    r'\\'
    return t


lexer = lex.lex()

data1 = """
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""

data2 = """
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
"""

lexer.input(data2)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)