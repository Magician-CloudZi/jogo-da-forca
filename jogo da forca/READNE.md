# Hangman

Um projeto prático utilizando conceitos de Redes de computadores
para desenvolvimento de um game entre 2 pessoas

## Objetivo

criar um jogo da forca utilizando conceitos de
sockets, TCP/IP e comunicação cliente-servidor

## Ferramentas
python
github
git
vscode

## Estrutura do  projeto

### Fluxo game
- Cliente diz "quero me conectar"
- connect()
- Servidor diz "conexão aceita ent"
- accept()
- Servidor inicia palavra = "PATO"
- Servidor envia _ _ _ _
- Cliente envia "P"
- Servidor verifica
- Servidor envia _ _ _ _
- Cliente envia "U"
- Servidor verifica
- Servidor envia "errou, tentativas: 5"
- segue o jogo...

### Cliente
Responsavel por:
- se conectar com o servidor
- enviar uma letra por vez
- recebe a resposta
- exibir informações 

### Servidor
Responsavel por:
- cria o socket
- associa ip e porta
- guarda a conexão
- valida letra
- envia atualização pro cliente
## Integrantes
João Pedro Ximenes
Artur Melo
