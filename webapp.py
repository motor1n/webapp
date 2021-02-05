import os
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    message = 'Каждый человек — кузнец своего счастья, ' \
              'причём голова служит ему то молотом, то наковальней:)))'
    return message


if __name__ == '__main__':    
    # os.environ.get() пытается получить значение переменной окружения
    # с именем PORT, а если не получается, то выставляет порт 5000:
    port = int(os.environ.get('PORT', 5000))
    
    # host = 0.0.0.0 означает, что мы разрешаем подключения
    # из любой сети по любому интерфейсу:
    app.run(host='0.0.0.0', port=port)
