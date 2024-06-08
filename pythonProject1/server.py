# Код для Flask сервера
from flask import Flask, request

app = Flask(__name__)

@app.route('/get_hint', methods=['POST'])
def hint():
    data = request.json
    guessed_letters = data.get('guessed_letters', '')
    possible_words = [word for word in words if all(letter not in word for letter in guessed_letters)]
    return {"hint": random.choice(possible_words)}

if __name__ == '__main__':
    app.run(debug=True)