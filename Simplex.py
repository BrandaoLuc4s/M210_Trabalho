
#lib
import numpy as np
from utils import *
np.set_printoptions(precision=2,suppress=True)

alfabeto_restricoes = ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfabeto_variaveis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nVar = 0
nRestricoes = 0
nDelta = []


# Entrando com numero de variaveis e restricoes
print("============= Coletando informações de entrada (variáveis e restrições) ===============")
nVar = int(input(f"Entre com o numero de variaveis: "))
nRestricoes = int(input(f"Entre com o numero de restricoes: "))

#DEFININDO MINHAS VARIAVEIS DE DECISÃO
variaveis = alfabeto_variaveis[0:nVar]

#coletando coeficientes das variaveis de decisão
print("============= Coletando coeficientes das variáveis de decisão ===============")
coeficientes_var = []
formula_z = ""
for i in range(0,nVar):
    coeficientes_var.append(int(input(f"Entre com o coeficiente de {variaveis[i]}: ")))
    formula_z += str(coeficientes_var[i])+str(variaveis[i])
    if i != nVar-1:
        formula_z += " + "


#coletando coeficientes das restrições
restricoes = alfabeto_restricoes[0:nRestricoes]
print(f"============= Coletando coeficientes das restrições {restricoes} ===============")
coeficientes_restricoes, string_restricoes = define_coeficientes_restricoes(nRestricoes, nVar, variaveis, restricoes)

print("======= Função de Maximização ========")
print(f'Maximize: Z = {formula_z}')
print("============= Sujeito à ===============")
print(string_restricoes)
#montando matriz
# a matriz deve possuir
matriz_linha = 1 + nRestricoes
matriz_coluna = nVar + nRestricoes + 1

#definindo primeira matriz
matriz = define_matriz_primaria(matriz_linha,matriz_coluna,coeficientes_var,coeficientes_restricoes,variaveis,nVar)

print("============= Matriz Primária ===============")
print(matriz)

continuar = True
valores_otimos = {}
#definindo novas matrizes
print("============= Matrizes Secundárias ===============")
indice_matriz = 1
while continuar:
    # define culuna pivo e linha de referencia
    coluna_pivo = define_coluna_pivo(matriz, matriz_linha, matriz_coluna)
    linha_referencia = define_linha_referencia(matriz, matriz_linha, matriz_coluna, coluna_pivo)

    # define linhas dos valores ótimos
    for k, v in valores_otimos.items():
        if v == linha_referencia:
            valores_otimos.pop(k)
            break
    if(len(valores_otimos) < nVar):
        valores_otimos[variaveis[coluna_pivo]] = linha_referencia

    #definindo nova matriz zerada
    nova_matriz = np.zeros((matriz_linha,matriz_coluna),dtype='float')

    #calculando linha de referencia
    for j in range(0,matriz_coluna):
        nova_matriz[linha_referencia][j] = matriz[linha_referencia][j]/matriz[linha_referencia][coluna_pivo]

    #calculando restante da nova matriz
    for i in range(0,matriz_linha):
        if i != linha_referencia:
            for j in range(0,matriz_coluna):
                nova_matriz[i][j] = matriz[i][j] + (matriz[i][coluna_pivo]*-1)*nova_matriz[linha_referencia][j]
    matriz = nova_matriz
    #verificando as condições de parada
    continuar = False
    for sk in range(0,matriz_coluna):
        if matriz[0][sk] < 0:
            continuar = True
    #mostrando matriz
    print(f"Matriz {indice_matriz}: ")
    indice_matriz += 1
    print(matriz)


#valores ótimos
print("============= Valores Ótimos ===============")
for k, v in valores_otimos.items():
    valores_otimos[k] = matriz[v][matriz_coluna-1]
valores_otimos['Z'] = matriz[0][matriz_coluna-1]
for k, v in sorted(valores_otimos.items()):
    if k != 'Z':
        print(f'Valor ótimo de {k} = {v}')
    else:
        print(f'Lucro ótimo [Z] = {v}')
        lucro_primario = v

# preço sombra
print("============= Preço sombra ===============")
for s in range(nVar,matriz_coluna-1):
    print(f'Preço sombra da restrição {restricoes[s-nVar]} = {matriz[0][s]}')


#coletando coeficientes dos Deltas das restrições: Calcular delta?
print("============= Verificando Delta para restrições ===============")
calcular = str(input("Deseja calcular o delta? (s/n): ")).lower()

if calcular == "s":
    print(f"============= Coletando Deltas das restrições {restricoes} ===============")
    for d in range(0,nRestricoes):
        nDelta.append(int(input(f"Entre com o delta de {alfabeto_restricoes[d]}: ")))

    valido = True
    #valida deltas
    print("============= Calculando Delta ===============")
    for x, d in enumerate(restricoes):
        print(f'Delta linha {x+1}...')
        linha = x+1
        soma = 0
        indice_delta = 0
        for coluna in range(nVar,matriz_coluna-1):
            soma += nDelta[indice_delta]*matriz[linha][coluna]
            indice_delta += 1
        soma += matriz[linha][matriz_coluna-1]
        if soma <= 0:
            print(f'Resultado = {soma} --> Não Valido!')
            valido = False
        else:
            print(f'Resultado = {soma} --> Valido!')

    #novo lucro ótimo se delta valido
    if valido:
        print(f'Daltas validados! Calculando novo lucro ótimo...')
        linha = 0
        indice_delta = 0
        soma = valores_otimos['Z']
        for coluna in range(nVar,matriz_coluna-1):
            soma += nDelta[indice_delta]*matriz[linha][coluna]
            indice_delta += 1
        print(f'Novo lucro ótimo [Z] = {soma}')
        print(f'O lucro subiu {soma-lucro_primario}')
    else:
        print(f'Não é viável alterar as disponibilidades das restrições!')
else:
    print(f'Calculo de delta não necessário. Programa finalizado!')