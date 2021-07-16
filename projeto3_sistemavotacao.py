
def autoriza_voto(nasc):
    if nasc >= 2007:
        return 'VOTO NEGADO!'
    elif nasc <= 2004 and nasc >= 1952:
        return 'VOTO OBRIGATÓRIO!'
    elif nasc >= 2005 or nasc <= 1952:
        return 'VOTO OPCIONAL!' 
    
voto = ('Nebulosa', 'Hades', 'Chapolin', 'Branco','Nulo')
votos = {voto[0]: 0, voto[1]: 0, voto[2]: 0, voto[3]: 0, voto[4]:0}
iniciar = input('Seja bem vindo(a) as eleições de 2022!\nDeseja iniciar a votação?[S/N]').upper()
while iniciar =='S':
    nasc = int(input('Em qual ano você nasceu?[AAAA]'))
    autoriza = autoriza_voto(nasc)
    print(autoriza)
    if autoriza == 'VOTO OBRIGATÓRIO!' or autoriza == 'VOTO OPCIONAL!':
        titulo = input(f'Em quem você deseja votar: \n[1]{voto[0]}\n[2]{voto[1]}\n[3]{voto[2]}\n[4]{voto[3]}\n[5]{voto[4]}\n')
        if titulo == '1':
            votos[voto[0]] += 1
        elif titulo == '2':
            votos[voto[1]] += 1
        elif titulo == '3':
            votos[voto[2]] += 1
        elif titulo == '4':
            votos[voto[3]] += 1
        elif titulo == '5':
            votos[voto[4]] += 1
    elif autoriza == 'VOTO NEGADO!':
        print('Você não pode votar!')
    iniciar = input('Deseja iniciar a votação?[S/N]').upper()    
    
        
total = votos[voto[4]] + votos[voto[3]] + votos[voto[2]] + votos[voto[1]] + votos[voto[0]]
total_invalido = votos[voto[4]] + votos[voto[3]]
print('-='*20)
print(f'Total de votos para cada candidato:\nCandidato {voto[0]} teve um total de {votos[voto[0]]}\nCandidato {voto[1]} teve um total de {votos[voto[1]]}\nCandidato {voto[2]} teve um total de {votos[voto[2]]}\nCandidato {voto[3]} teve um total de {votos[voto[3]]}\nCandidato {voto[4]} teve um total de {votos[voto[4]]}')
print('-='*20)
print(f'Total de votos:{total}')
print('-='*20)
print(f'Total de votos inválidos:{total_invalido}')
print('-='*20)
print(f'O nomeado desta votação foi:{max(votos, key = votos.get)}. Parabéns!')




    
