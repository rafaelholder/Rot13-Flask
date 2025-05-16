from flask import Flask, render_template, request

app = Flask(__name__)

def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            # Verifica se esta no alfabeto minúsculo
            offset = ord('a')
            result.append(chr((ord(char) - offset + 13) % 26 + offset))
        elif 'A' <= char <= 'Z':
            # Verifica se esta no alfabeto maiúsculo
            offset = ord('A')
            result.append(chr((ord(char) - offset + 13) % 26 + offset))
        else:
            # Não altera outros caracteres
            result.append(char)
    return ''.join(result)

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = ''
    texto_original = ''
    if request.method == 'POST':
        texto_original = request.form.get('texto', '')
        resultado = rot13(texto_original)
    return render_template('index.html', resultado = resultado, texto_original = texto_original)

if __name__ == '__main__':
    app.run(debug=True)
