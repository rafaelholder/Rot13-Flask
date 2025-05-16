# ROT13 - Rholder

Este é um projeto simples feito com **Flask** que demonstra o funcionamento do algoritmo de cifra **ROT13**, uma variação da cifra de César. A aplicação permite ao usuário digitar um texto e visualizar sua versão cifrada usando ROT13 diretamente no navegador.

## O que é ROT13?

ROT13 (abreviação de "rotate by 13 places") é um algoritmo de substituição no qual cada letra do alfabeto é trocada pela letra 13 posições à frente. Por exemplo, a letra **A** vira **N**, **B** vira **O**, e assim por diante.

Aplicar ROT13 duas vezes retorna o texto original, o que o torna uma cifra simétrica e interessante para estudos básicos de criptografia.

## Funcionalidades

- Interface web simples com HTML e CSS
- Campo de entrada para texto
- Resultado cifrado exibido dinamicamente na tela
- Implementado 100% em Python com Flask

## 🛠️ Tecnologias usadas

- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- HTML5 + CSS3

## 💻 Como rodar localmente

1. Clone este repositório:
    ```bash
    git clone https://github.com/rafaelholder/rot13-flask.git
    cd rot13-flask
    ```

2. Crie um ambiente virtual e ative:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Inicie o servidor Flask:
    ```bash
    python app.py
    ```

5. Acesse no navegador:
    ```
    http://127.0.0.1:5000/
    ```

## 🌐 Deploy na Web

Você pode publicar este projeto facilmente usando o Heroku. Veja as instruções na seção "Como subir num servidor" ou [clique aqui](https://devcenter.heroku.com/articles/getting-started-with-python) para o guia oficial.

---

