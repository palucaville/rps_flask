from flask import Flask, render_template, request
import random

global last_result

def random_choice():
  return random.choice(["rock", "paper", "scissors"])

def winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "Tie!"
  elif user_choice == "rock" and computer_choice == "scissors":
    return "You won!"
  elif user_choice == "scissors" and computer_choice == "paper":
    return "You won!"
  elif user_choice == "paper" and computer_choice == "rock":
    return "You won!"
  else:
    return "You lost!"

app = Flask(__name__)

@app.route("/")
def index():

  last_result = ""
  return render_template("index.html", last_result=last_result)

@app.route("/play", methods=["POST"])
def play():
  user_choice = request.form["choice"]
  computer_choice = random.choice(["rock", "paper", "scissors"])

  if user_choice == computer_choice:
    result = "Tie!"
  elif user_choice == "rock" and computer_choice == "scissors":
    result = "You won!"
  elif user_choice == "scissors" and computer_choice == "paper":
    result = "You won!"
  elif user_choice == "paper" and computer_choice == "rock":
    result = "You won!"
  else:
    result = "You lost!"
  global last_result
  last_result = result
  return render_template("result.html", user_choice=user_choice, computer_choice=computer_choice, result=result)

@app.errorhandler(400)
def not_found_error(error):
    return render_template('400.html'), 400

@app.errorhandler(500)
def not_found_error(error):
    return render_template('500.html'), 500

if __name__ == "__main__":
  app.run(debug=True)
