import numpy as np

## Função que está recebendo nRestricoes, nVar, variaveis, restricoes
def define_coeficientes_restricoes(nRestricoes,nVar,variaveis,restricoes):
    coeficientes_restricoes = []
    ##Pede pro usuário entrar com as restrições de acordo com os valores das var de decisão
    for i in range(0,nRestricoes):
        print(f'Entrar com as restrições de {restricoes[i]}:')
        restri_dict = {}
        for j in range(0,nVar):
            restri_dict[variaveis[j]] = float(input(f"Entre com o valor do coeficiente de {variaveis[j]}: "))

        ## Entrando com lado direito da restrição
        restri_dict["LD"] = float(input(f"Entre com o valor do lado direito: "))
        coeficientes_restricoes.append(restri_dict)
    
    string_restricoes = ''

    #Definindo as variáveis auxiliares de cada restrição
    for i, item in enumerate(coeficientes_restricoes):
        for k, v in item.items():
            if k != 'LD': 
                string_restricoes += f'{v}{k} '
                if list(item.items())[-2][0] != k:
                    string_restricoes += '+ '
            else:
                string_restricoes += f'<= {v} [{restricoes[i]}] \n'  
    
    #Retornando as equações formadas das restrições e os coeficientes 
    return coeficientes_restricoes, string_restricoes

## Definindo a matriz primária (primeira tabela simplex)
def define_matriz_primaria(matriz_linha,matriz_coluna,coeficientes_var,coeficientes_restricoes,variaveis,nVar):
    matriz = np.zeros((matriz_linha,matriz_coluna),dtype='float')
    for i in range(0,matriz_linha):
        ##loop de colunas
        for j in range(0,matriz_coluna):
            ##Definindo linha Z
            if i == 0:
                if j < nVar:
                    matriz[i][j] = coeficientes_var[j] * -1
                else:
                    matriz[i][j] = 0
            ##Definindo a linha das restricoes
            else:
                if j < nVar:
                    matriz[i][j] = coeficientes_restricoes[i-1][variaveis[j]]
                elif j == nVar + i - 1:
                    matriz[i][j] = 1
                elif j == matriz_coluna-1:
                    matriz[i][j] = coeficientes_restricoes[i-1]['LD']
                else:
                    matriz[i][j] = 0
    return matriz

## Definindo coluna do pivo
def define_coluna_pivo(matriz,matriz_linha,matriz_coluna):
    i = 0
    menor = 0
    for j in range(0,matriz_coluna):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            coluna_pivo = j
    return coluna_pivo

## Definindo a linha de referencia
def define_linha_referencia(matriz,matriz_linha,matriz_coluna,coluna_pivo):
    menor_impacto = 999999999999999
    for i in range(1,matriz_linha):
        if matriz[i][coluna_pivo] > 0:
            impacto = float(matriz[i][matriz_coluna-1]) / float(matriz[i][coluna_pivo])
            if impacto < menor_impacto:
                menor_impacto = impacto
                linha_referencia = i
    return linha_referencia