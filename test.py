from flask import *

app = Flask(
    __name__
)

@app.route('/')
def index():
    return 'By Aren Elchinyan, vk.com/0Nera'

if __name__ == "__main__":
    app.run(
        host='localhost',
        debug = True
    )
else:
    print(__name__)
    print("Run as file, not module!!!")