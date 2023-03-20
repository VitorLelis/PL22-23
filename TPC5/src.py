from re import compile
from math import floor

def value_convert(value: int) -> str:
    euro = floor(value/100)
    cents = value % 100

    if euro > 0:
        result = f'{euro}e{cents}c'
    else:
        result = f'{cents}c'
    
    return result

def coin_convert(coin:str)-> int:
    if 'e' in coin:
        result = int(coin.strip('e')) * 100
    else:
        result = int(coin.strip('c'))

    return result

lev_rgx  = compile(r'LEVANTAR',flags=0)
stop_rgx = compile(r'^[POUSAR|ABORTAR]+',flags=0)
moe_rgx  = compile(r'[\d|c|e]+', flags=0)
tel_rgx  = compile(r'^T=\d+', flags=0)

coins = ['1c', '2c', '5c', '10c', '20c', '50c', '1e', '2e']
value = 0

control = True
while(control):
    comando = input()
    if lev_rgx.search(comando):
        print('maq: \"Introduza moedas.\"\n')

    elif tel_rgx.search(comando):
        number = comando.strip('T=')

        if number.startswith('601') or number.startswith('641'):
            print('maq: \"Esse número não é permitido neste telefone. Queira discar novo número!\"\n')
        
        elif number.startswith('00'):
            if value < 150:
                print('maq: \"Saldo insuficiente!\"\n')
            else:
                value -= 150
                print(f'maq: \"saldo = {value_convert(value)}\"\n')
        
        elif number.startswith('2'):
            if value < 25:
                print('maq: \"Saldo insuficiente!\"\n')
            else:
                value -= 25
                print(f'maq: \"saldo = {value_convert(value)}\"\n')

        elif number.startswith('808'):
            if value < 10:
                print('maq: \"Saldo insuficiente!\"\n')
            else:
                value -= 10
                print(f'maq: \"saldo = {value_convert(value)}\"\n')
        
        elif number.startswith('800'):
                print(f'maq: \"saldo = {value_convert(value)}\"\n')


    elif moe_rgx.search(comando):
        inserted_coin = moe_rgx.findall(comando)
        message = 'maq: \"'
        for ic in inserted_coin:
            if ic in coins:
                value += coin_convert(ic)
            else:
                message += f'{ic} - moeda inválida; '
        
        message += f'saldo = {value_convert(value)}\"\n'
        print(message)

    elif stop_rgx.search(comando):
        print(f'maq: \"troco={value_convert(value)}; Volte sempre!\"\n')
        control = False