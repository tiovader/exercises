# Raspagem de Exercícios
Este repositório tem como finalidade armazenar os desafios de programação resolvidos das várias plataformas de desafio, tipo [Exercism](https://exercism.org/) e [Beecrowd](https://www.beecrowd.com.br/judge/), o objetivo é raspar esses exercícios das plataformas usando **Selenium** e talvez **BS4**.

## Como usar
Para configurar o scrapping, é so criar um arquivo `.config` na pasta `scr`. Dento do arquivo deve ser especificado `user` e `password` da seguinte forma:
```
user=some.cool.email@something.com
password=pls_do_not_hack_me123
```
E para os parâmetros do scrapper do `Exercism`, deve-se adicionar as tracks (em forma de lista/tupla/set) e definir se o login é feito por meio do github ou não. 

> vale lembrar que é necessário o download do GeckoDriver, caso não esteja no `C:\bin\`, baixe-o e coloque nesse pathing, ou coloque o pathing correto.

## Exercism
Alguns exercícios podem estar falhando nos testes porque ainda precisam ser atualizados pra versões mais recentes, na época que eu upei estavam passando em todos.

## TODO
- adicionar parâmetros pra tipos diferentes de exercícios do Exercism
- adicionar ferramenta de CLI pro `main.py`, para poder chamar o programa pelo terminal!!!
- raspar os exercícios do `Beecrowd`
- melhorar a modularização do repositório
- otimizar o código (reescrever boa parte)...
- adicionar **Threading** pra baixar os exercícios do Exercism mais rápido
- ajeitar o main.py pra incrementar outras plataformas (pelo menos o Beecrowd)