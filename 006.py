#Leia uma quantidade de segundos e mostre a quantas horas, minutos e segundos ela
#corresponde. Ex.: 3760 → 1h 2min 40s
#DICA divisão inteira // separa a parte cheia; % devolve o que sobrou para a próxima unidade.

segundos = int(input('Digite os segundo: '))
horas = segundos // 3600
resto = segundos % 3600

minutos = resto // 60
segundos = resto % 60

print(f' {horas} Horas {minutos} Minutos {segundos} Segundos ')