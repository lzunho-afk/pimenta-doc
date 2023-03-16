# Pimenta Doc

O Pimenta Doc é um projeto simples mas extremamente funcional para quem não tem paciência e/ou está insatisfeito com a atual organização posta pelos programas
de edição de texto.
Ele funciona apenas como uma camada de abstração dos dados para os editores. Então, boa noticia! Você vai poder utilizar seu Vim, seu Emacs e até mesmo seu Writer para edição de texto de maneira muito mais organizada agora.

## Funcionamento

Todo o programa se alinha da seguinte forma:

- O usuário da entrada com o pedido de dados por **linha de comando** ou por algum **aplicativo externo** (Vim, Emacs, etc..);
- A API de Entrada/Saída faz uma requisição de token com os dados de autenticação do usuário;
- A API recebe o token de autenticação e, junto dele, faz a requisição dos dados;
- Caso o token seja compativel com os dados requisitados, a API envia as informações para o usuário.

![abstracao_comunicacao_pimentadoc](https://user-images.githubusercontent.com/76849605/225711640-d6c62f6c-9c8e-46f1-975d-85a167b2a3c0.svg)
