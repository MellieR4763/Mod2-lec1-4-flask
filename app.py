from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "app": "Capstone Task Manager",
        "version": "1.0",
        "author": "Your Name"
    })

@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json()
    if not data or 'mensaje' not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data['mensaje']
    response_text = f"Recibí tu mensaje: '{user_message}'. ¡Gracias por escribirnos!"
    return jsonify({"respuesta": response_text})

if __name__ == '__main__':
    app.run(debug=True)