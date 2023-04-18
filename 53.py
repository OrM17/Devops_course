from flask import Flask, request

app = Flask("something")


@app.route('/cars', methods=['GET'])
def car_list():
   with open("names.txt") as f:
       result = f.read()
       return result

@app.route('/cars', methods=['POST'])
def update_car():
    if request.method == 'POST':
        return "saved new car"


@app.route('/')
def my_func():
    return "hello and welcome to the world of games"


app.run(host="0.0.0.0", port=5001, debug=False)