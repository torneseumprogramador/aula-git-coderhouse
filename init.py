from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    template = request.args.get('template', 'html')
    if template == "html":
        return render_template('home.html')
    
    return jsonify(mensagem="Bem-vindo à minha api com Flask !")

if __name__ == '__main__':
    app.run(debug=True)
