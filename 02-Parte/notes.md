# Python Introduction

Estas anotações fora feitas no transcurso das aulas, visam firmar o conhecimento ministrado, bem como ter um arquivo digital com as funções aprendidas sempre é útil.
**********************************************************
## Conceitos Gerais

A maior parte do curso destina-se aos conceitos básicos.

* A identação é importante para o Python porque ele define quando termina um _loop_ e começa o outro ou quando termina um _statement_ do _if_;
* Como muitas outras linguagens de programação o Python é _case sensitive_, isto é, maiúsculas e minúsculas definem variáveis diferentes;
* Os comentários dentro do código pode ser feito a partir do uso do `#`.
**********************************************************
## Boas práticas

* Utilizar os espaçamentos de maneira adequada para que as fórmulas fiquem fáceis de ler e consequentemente de entender;
* Comentar as linhas de código, pois o maior beneficiário desses comentários será você daqui 6 meses quando estiver revisando esse código;

**********************************************************
## Configuração

Instalei o [Anaconda](https://www.anaconda.com/download/) e estou rodando o Spyder 3.3.1. para simular/rodar o Python. O [CodeSkulptor 3](https://py3.codeskulptor.org) é um alternativa.

### Classes de Variáveis

Como atribuir um `integer` e um `float` nas variáveis?

```
# Integer
teste_int = 100    # É um inteiro (não colocar o ponto final)
teste_int = 123    # É um inteiro (não colocar o ponto final)

# Float
teste_flo = 100.8  # É um float (só adicionar o ponto final)
teste_flo = 123.   # É um float (só adicionar o ponto final)
```
Note que haverá um conversão (ou _data coercion_ ) de `integer` para `float` caso tenha alguma operação envolvendo os dois tipos de variáveis.

```
# A nova variável será do tipo float
teste_new = teste_int + teste_flo
```
Observe que as variáveis podem ser convertidas para `integer`, `float` etc. Contudo, deve-se ressaltar que para os casos de conversão de `float` para `integer` pode-se ter uma perda de informação significativa.
```
teste = 100.987      # Variável float

teste = int(100.987) # Convertendo para integer

print(teste)         # Note que o valor impresso é 100
                     # perdeu-se tudo o que estava após a vírgula
```

#### Boolean `bool`

Além de `integer` e `float`, também há o `bool` que se refere aos booleanos (`True` e `False`). Observe que para o Python `True` e `False` (1 e 0) devem ser escritos exatamete como está neste texto, em `R` eles são escritos todos em caixa alta.

#### Strings `str`

O `strings` é uma cadeia de letras, um exemplo é o texto que estou escrevendo agora.

```
print("Hello World")  # É a impressão de uma simples string "Hello World", mas poderia
                      # ser bem mais complexa.

meu_texto = "Vamos fazer um teste!111"   # Note que esse exemplo é um pouco mais complexo
print(meu_texto)                         # já que tem espaços, números e caracteres especiais.
```

Surpreenda-se pois no Python pode-se usar os operadores (`+`, `*` etc.) para realizar algumas funções.

* `+` Une/concatena duas `strings`;
* `*` Multiplica a `string`.

**********************************************************
## Operadores

São os operadores matemáticos básicos:

#### `+` Adição

Adiciona dois elementos.

```
print(5 + 3) # Somando dois números inteiros

print("Hello" + " " + "World") # Somando três strings
```

#### `-` Subtração

Subtrai dois elementos.

```
print(5 - 3)
```

#### `*` Multiplicação

Multiplica dois elementos.

```
print(5 * 3)

print("Ha" * 5)  # Terá como saída HaHaHaHaHa
```
#### `/` Divisão

Divide dois elementos.

```
print(5 / 3) # Retorna um float
```
#### `%` Resto da Divisão
Divide dois elementos e retorna o resto da divisão.

```
print(5 % 3) # Retorna 2
```
#### `**` Exponenciação
Eleva o primeiro termo ao segundo (normalmente anotamos como 5^3).

```
print(5 ** 3) # Retorna cinco elevado à terceira potência 5^3
```
#### `//` Retorna o Quociente da Divisão
Divide dois elementos e retorna o quociente da divisão.

```
print(5 // 3) # Retorna 1
```

**********************************************************
## _Assignment Operators_

Conforme abordado em sala de aula, essa forma de notação é para simplificar o código. É muito parecido com o `i++`(que é o mesmo que `i=i+1`) do C++.

#### `+=`

Atualização da variável a partir de soma.

```
teste = teste + 100   # Como eu faço
teste += 100          # Como um programador faz
```

#### `-=`

Atualização da variável a partir de uma subtração.

```
teste = teste - 100   # Como eu faço
teste -= 100          # Como um programador faz
```

#### `*=`

Atualização da variável a partir de uma multiplicação.

```
teste = teste * 100   # Como eu faço
teste *= 100          # Como um programador faz
```

#### `/=`

Atualização da variável a partir de uma divisão.

```
teste = teste / 100   # Como eu faço
teste /= 100          # Como um programador faz
```

#### `//=`

Atualização da variável pelo quociente de uma divisão.

```
teste = teste // 100   # Como eu faço
teste //= 100          # Como um programador faz
```
#### `%=`

Atualização da variável pelo resto de uma divisão.

```
teste = teste % 100   # Como eu faço
teste %= 100          # Como um programador faz
```

#### `**=`

Atualização da variável pelo resto de uma divisão.

```
teste = teste ** 100  # Como eu faço
teste %= 100          # Como um programador faz
```
Há outros mais complicados no site do [Programiz](https://www.programiz.com/python-programming/operators).

**********************************************************
## _Comparison Operators_

Lógica básica de comparação entre dois argumentos, igual a qualquer outra linguagem de programação.

#### `<` Menor
Compara dois elementos e retorna `True` ou `False`.

```
100 < 90  # 100 é menor que 90
False     # Não
```
#### `>` Maior
Compara dois elementos e retorna `True` ou `False`.

```
100 > 90  # 100 é maior que 90
True      # Sim
```
#### `<=` Menor ou igual
Compara dois elementos e retorna `True` ou `False`.

```
100 <= 90  # 100 é menor ou igual a 90
False      # Não
```
#### `>=` Maior ou igual
Compara dois elementos e retorna `True` ou `False`.

```
100 > 90  # 100 é maior ou igual a 90
True      # Sim
```
#### `==` Igual
Compara dois elementos e retorna `True` ou `False`.

```
100 == 90  # 100 é igual (ou idêntico) a 90
False      # Não
```
#### `!=` Diferente (ou _não igual_)
Compara dois elementos e retorna `True` ou `False`.

```
100 != 90  # 100 é differente de 90
True       # Sim
```
**********************************************************
## _Logical Operators_

O Python possui 3 operadores de lógica que são: `and`, `or` e `not`. Eles devem ser escritos necessariamente em letras minúsculas.

#### `and`

Comporta-se conforme a tabela abaixo

|a|b|**s**|
|:-:|:-:|:-:|
|0|0|**0**|
|0|1|**0**|
|1|0|**0**|
|1|1|**1**|

#### `or`

Comporta-se conforme a tabela abaixo

|a|b|**s**|
|:-:|:-:|:-:|
|0|0|**0**|
|0|1|**1**|
|1|0|**1**|
|1|1|**1**|

#### `not`

Retorna o booleano contrário.

|a|**s**|
|:-:|:-:|
|0|**1**|
|1|**0**|

**********************************************************

## Built-in functions

Esta será um lista das funções, operadores e qualquer outra coisa que foi apresentado em sala de aula.

### `print()`
```
print("Hello World")  # Imprime Hello World
```
Imprime a variável.

### `type()`
```
teste = type(100)    # Atribui o resultado da função em teste
print(teste)         # Imprime a classe da variável dentro do type()
                     # que no caso é 100. Logo, será <class 'int'>
```
Retorna o tipo de variável.

### `len()`
```
print(len("Hello World"))  # Retorna 11, pois conta o espaço também.
```
Retorna o comprimento de uma `strings`, isto é, a quantidade de caracteres. E para os casos de um vetor retorna o comprimento.

### `int()`
```
int(43.3)
```
Converte o elemento declarado na função para um `integer`.

### `str()`
```
str(43.3)
```
Converte o elemento declarado na função para um `string`.

### `float()`
```
str(43)
```
Converte o elemento declarado na função para um `float`.


## Methods

Como o Python é uma linguagem orientada a objeto, há alguns `methods` relacionado a alguma `classe`. O funcionamento de um método é similar ao de uma função, contudo o método está ligado a alguma classe e só será útil para essa classe. Isto quer dizer que não há possibilidade de usar o `.title()` num número `integer` ou `float`.

### `.title()`
```
meu_nome = "anderson uyekita"
print(meu_nome.title())
```

O retorno da aplicação do método `.title()` é a substituição das primeiras letras minúsculas do meu nome para maiúsculas, ficando assim " **A**nderson **U**yekita "


### `.islower()`
```
meu_nome = "anderson uyekita"
print(meu_nome.lower())
```

O retorno da aplicação deste método retorna um `booleano` e significa se há ou não alguma letra maiúscula, se sim `False` senão `True`.

### `.format()`
```
# Exemplo 1
print("Eu sou o Hitoshi e tenho {} anos".format(33))

# Examplo 2 (retirado das notas de aula)
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
```
O retorno desse método é a substituição dos `{}` pelo `33`.


## Referências

* [String methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
