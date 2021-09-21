'''
from flask import Flask
from flask import jsonify
app = Flask(__name__)

def change(amount):
    # calculate the resultant change and store the result (res)
    res = []
    coins = [1,5,10,25] # value of pennies, nickels, dimes, quarters
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    # divide the amount*100 (the amount in cents) by a coin value
    # record the number of coins that evenly divide and the remainder
    coin = coins.pop()
    num, rem  = divmod(int(amount*100), coin)
    # append the coin type and number of coins that had no remainder
    res.append({num:coin_lookup[coin]})

    # while there is still some remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})
    return res


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'

@app.route('/change/<dollar>/<cents>')
def changeroute(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
'''

from flask import Flask
from flask import jsonify
app = Flask(__name__)

def outputAssignment(name):
    res = ""
    if name == "IDS702":
        res = "Data Analysis Assignment 2 (~Sep 14)"
    elif name == "IDS703":
        res = "Markov Text Generation (~Sep 15)"
    elif name == "IDS706":
        res = "Module Four Discussion (~Sep 15), Demo Video Assignment (~Sep 17)"
    elif name == "IDS720":
        res = "Pandas Series (~Sep 14), Dataframe Exercises (~Sep 16)"
    elif name == "IDS898":
        res = "Modifiy your resume using check lists. (~ASAP)"
    elif name == "IDS791":
        res = "There is no assignment for this week! :)"
    else:
        res = "Oops, I think it's not a classic MIDS class."
    return res


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello! Input your class ID : /ID'

@app.route('/<name>')
def changeClass(name):
    print(f"Assignments for {name}")
    result = outputAssignment(name)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)