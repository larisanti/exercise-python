score_total = []
qtd_atividade = int(input("Quantidade de atividades:"))

for i in range(1, qtd_atividade + 1):
    entrada = input(f"Atividade {i} (acerto/total): ")
    
    a, t = map(int, entrada.split('/'))
    score_parcial = (a * 100) / t
    
    score_total.append(score_parcial)
    print(f"Atividade {i}: {score_parcial:.2f}%")

if score_total:
    media_final = sum(score_total) / len(score_total)
    print(f"Score: {media_final:.2f}%")