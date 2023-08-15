from flask import Flask
import random

random_number = random.randint(1, 10)
app = Flask(__name__)


@app.route('/')
def adivinhe_o_numero():
    return '<h1>Adivinhe o número</h1>'


@app.route('/<int:number>')
def greetings(number):
    if number < random_number:
        return '<h1>Too low</h1>'
    if number > random_number:
        return '<h1>Too high</h1>'
    if number == random_number:
        return '<h1>You are correct!</h1>'


print(random_number)
