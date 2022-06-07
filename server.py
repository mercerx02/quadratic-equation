from flask import Flask
from math import sqrt
app = Flask(__name__)

def find_roots(a,b,c):
    """ Решает квадратное уравнение и выводит отформатированный ответ """
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        return {"x1":x1,"x2":x2}

    return "This equation has no solutions"

@app.route("/quadratic_equation/<a>/<b>/<c>",methods=["GET"])
def show_roots(a,b,c):
    return find_roots(int(a),int(b),int(c))


if __name__ == "__main__":
    app.run()