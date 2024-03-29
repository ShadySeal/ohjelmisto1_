from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<num>')
def summa(num):
    num = int(num)

    flag = True
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break

        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")

    vastaus = {
        "Number" : num,
        "isPrime" : flag,
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)