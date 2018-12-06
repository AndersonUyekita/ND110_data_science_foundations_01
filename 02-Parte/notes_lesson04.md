# Python Introduction `Lesson04`

#### Tags
* Título: Functions
* Autor: AH Uyekita
* Data início: 06/12/2018
* Cod: nd110

## _Functions_

A função nada mais é que a abstração de uma rotina (ou _script_) encapsulado num simples _call_ de uma função _built-in_ (parece mas não é _built-in_ porque nós que a criamos).

### Conteúdo da aula

Essa lição abordou:

* Defining Functions
* Variable Scope
* Documentation
* Lambda Expressions
* Iterators and Generators

### Estrutura de uma função

A função possui uma estrutura que deve ser seguida para que o devido funcionamento.

* Sempre começa com `def`;
* Deve ser indentada;
* Possui argumento;
* Pode ou não retornar (_return_) algum valor (_None_ se não for retornar nada).

```
def my_function(arg1, arg2)
+---+----------------------------|
|   |                            |
| 1 |           2                |
|   |return                      |  # Note que não é uma exigência que tenha o return
+---+----------------------------|

1: área de indentação
2: área de código
```
Ressalta-se que as funções podem ter variáveis locais, isto é, as variáveis internas à função não afetam o _environment_ externo dela.

Além disso, pode-se declarar variáveis _default_ para cada argumento (igual o R). Outra similaridade com o R é com relação ao uso da função.

* Declarar argumentos por posição: my_function(10,5)
* Declarar argumentos por nomes: my_function(arg2 = 5, arg1 = 10)
