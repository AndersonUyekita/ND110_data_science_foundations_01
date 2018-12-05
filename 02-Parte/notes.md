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
**********************************************************
## Operadores

São os operadores matemáticos básicos:

#### `+` Adição

Adiciona dois elementos.

```
print(5 + 3)
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

#### +=

Atualização da variável a partir de soma.

```
teste = teste + 100   # Como eu faço
teste += 100          # Como um programador faz
```

#### -=

Atualização da variável a partir de uma subtração.

```
teste = teste - 100   # Como eu faço
teste -= 100          # Como um programador faz
```

#### *=

Atualização da variável a partir de uma multiplicação.

```
teste = teste * 100   # Como eu faço
teste *= 100          # Como um programador faz
```

#### /=

Atualização da variável a partir de uma divisão.

```
teste = teste / 100   # Como eu faço
teste /= 100          # Como um programador faz
```

#### //=

Atualização da variável pelo quociente de uma divisão.

```
teste = teste // 100   # Como eu faço
teste //= 100          # Como um programador faz
```
#### %=

Atualização da variável pelo resto de uma divisão.

```
teste = teste % 100   # Como eu faço
teste %= 100          # Como um programador faz
```

#### **=

Atualização da variável pelo resto de uma divisão.

```
teste = teste ** 100  # Como eu faço
teste %= 100          # Como um programador faz
```


Há outros mais complicados no site do [Programiz](https://www.programiz.com/python-programming/operators).

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
teste = type(100)   # Atribui o resultado da função em teste
print(teste)         # Imprime a classe da variável dentro do type()
                     # que no caso é 100. Logo, será <class 'int'>
```
