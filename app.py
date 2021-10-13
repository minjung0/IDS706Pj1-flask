from flask import Flask
from flask import jsonify
app = Flask(__name__)

def outputAssignment(name):
    res = ""
    if name == "IDS702":
#        res = "Data Analysis Assignment 2 (~Sep 14)"
#        res = "Data Analysis Assignment 3 (~9/22)"
        res = "Team Project 2 (~10/24)"
    elif name == "IDS703":
#        res = "Markov Text Generation (~Sep 15)"
#        res = "Part-of-Speech Tagging (~9/22)"
        res = "Feed-forward neural networks (~10/18)"
    elif name == "IDS706":
#        res = "Module Four Discussion (~Sep 15), Demo Video Assignment (~Sep 17)"
#        res = "Module Four Discussion (~9/22), Demo Video Assignment (~9/24)"
        res = "Module Eight Discussion (~10/13), Demo Video Assignment (~10/15)"
    elif name == "IDS720":
#        res = "Pandas Series (~Sep 14), Dataframe Exercises (~Sep 16)"
#        res = "Missing Values Exercises (~9/21), Github Exercises 1 (~9/21)"
        res = "Big Data Exercises (~10/19)"
    elif name == "IDS898":
#        res = "Modifiy your resume using check lists. (~ASAP)"
#        res = "Modifiy your resume using check lists. (~9/23)"
        res = "There is no assignment for this week! :)"
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
