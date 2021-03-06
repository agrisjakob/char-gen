import random
from flask import Flask, Response, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_weapon():
    weapons= ["1 Axe", "2 Dagger", "3 Staff", "4 Bow", "5 Wand", "6 Mace", "7 Spear", "8 Sword", "9 Shield", "a Crossbow", "b Flintlock", "c Claws"]
    final_weapon= random.choice(weapons)

    return Response(final_weapon, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True,port=5001, host='0.0.0.0')
