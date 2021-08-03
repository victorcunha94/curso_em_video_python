times = 'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Atlético-PA', 'Cruzeiro', 'Bota-Fogo', 'Santos', 'Bahia', 'Fluminese', 'Corinthinas', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG-', 'Vitória', 'Paraná'
print(f'Os 5 primeiros colocados foram {times[:5]}')
print(f'Os times rebaixados serão: {times[-4:]}')
print(f'Em ordem alfabética os times são {sorted(times)}')
print(f'A chapecoense está na posição {times.index("Chapecoense")+1}')