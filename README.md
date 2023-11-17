<h1 align='center'>Optimization Simplex Method using Python 🐍</h1>
<p align="left">Repositório destinado ao trabalho de otimização por método simple utilizando Python.</p>

<div align="center">

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

</div>

# 📜 Passo a passo

<h3> VS Code</h3>
🚨 Para instalar a biblioteca necessária, rode o seguinte comando:

```
pip install numpy
```
🚨 Rodar a aplicação na IDE utilizada com o run nativo ou com o comando abaixo:

```
python Simplex.py
```

#
## A aplicação deve receber como entrada: 📥🚀

#
> Número de variáveis de decisão. *Quantidade de parâmetros analisados*

> Número de restrições. *Quantas formulas serão analisadas para se chegar ao valor ótimo*
```
============= Coletando informações de entrada (variáveis e restrições) ===============
Entre com o numero de variaveis: 2
Entre com o numero de restricoes: 3
```

#
> Coeficientes das variáveis da decisão --> Z no formato: x1A + x2B, deve-se entrar com as variáveis x1 e x2;
```
============= Coletando coeficientes das variáveis de decisão ===============
Entre com o coeficiente de A: 5
Entre com o coeficiente de B: 7

# Resultando em:
Maximize: Z = 5A + 7B
```
#### O programa atribui automaticamente letras as variaveis de decisão, no exemplo A e B.

#
> Coeficientes das restrições --> No formado Ax1 + Bx2 <= LD, deve-se entrar com A,B e LD ;
```
============= Coletando coeficientes das restrições ['M', 'N', 'O'] ===============
Entrar com as restrições de M:
Entre com o valor do coeficiente de A: 3
Entre com o valor do coeficiente de B: 0
Entre com o valor do lado direito: 250
...
#Resultando em:
3.0A + 0.0B <= 250.0 [M]
```
O programa atribui automaticamente letras as restrições, no exemplo M, N e O.
#
> Deve-se verificar se o cálculo do Delta será feito e aceito (s/n) na entrada;
```
============= Verificando Delta para restrições ===============
Deseja calcular o delta? (s/n): s
```
> Caso o Delta for calculado, informar o Delta de cada uma das restições;🥏
```
============= Coletando Deltas das restrições ['M', 'N', 'O'] ===============
Entre com o delta de M: 50
Entre com o delta de N: 0
Entre com o delta de O: 3
```
#
# A aplicação calculará e informará a saída:📤 🎯


> A função de Maximização (Z): Z = Ax1 + Bx2, por exemplo;

> As funções de restrições em sua forma de função;
```
======= Função de Maximização ========
Maximize: Z = 5A + 7B
============= Sujeito à ===============
3.0A + 0.0B <= 250.0 [M]
0.0A + 1.5B <= 100.0 [N]
0.25A + 0.5B <= 50.0 [O]
```
> Matriz primária e Matrizes secundárias. Caso exista mais de uma, já enumeradas e calculadas;
```
============= Matriz Primária ===============
[[ -5.    -7.     0.     0.     0.     0.  ]
 [  3.     0.     1.     0.     0.   250.  ]
 [  0.     1.5    0.     1.     0.   100.  ]
 [  0.25   0.5    0.     0.     1.    50.  ]]
============= Matrizes Secundárias ===============
Matriz 1:
[[ -5.     0.     0.     4.67   0.   466.67]
 [  3.     0.     1.     0.     0.   250.  ]
 [  0.     1.     0.     0.67   0.    66.67]
 [  0.25   0.     0.    -0.33   1.    16.67]]
Matriz 2:
[[  0.     0.     0.    -2.    20.   800.  ]
 [  0.     0.     1.     4.   -12.    50.  ]
 [  0.     1.     0.     0.67   0.    66.67]
 [  1.     0.     0.    -1.33   4.    66.67]]
Matriz 3:
[[  0.     0.     0.5    0.    14.   825.  ]
 [  0.     0.     0.25   1.    -3.    12.5 ]
 [  0.     1.    -0.17   0.     2.    58.33]
```
> Os valores ótimos para cada parâmetro;
```
============= Valores Ótimos ===============
Valor ótimo de A = 83.33333333333333
Valor ótimo de B = 58.333333333333336
Lucro ótimo [Z] = 825.0
```
> Preço Sombra de cada restrição;
```
============= Preço sombra ===============
Preço sombra da restrição M = 0.5
Preço sombra da restrição N = 0.0
Preço sombra da restrição O = 14.0
```
> Se o Delta for calculado, informa o resultado obtido e se é válido; 🧮

> Finalmente, gera o resultado do novo Lucro ótimizado. 💰 💸
```
============= Calculando Delta ===============
Delta linha 1...
Resultado = 16.000000000000007 --> Valido!
Delta linha 2...
Resultado = 56.0 --> Valido!
Delta linha 3...
Resultado = 100.0 --> Valido!
Daltas validados! Calculando novo lucro ótimo...
Novo lucro ótimo = 892.0
```
## Lib utilizada no projeto 🕋 🗳️

- numpy
