from flask import Flask

app = Flask(__name__)


@app.get("/welcome")
def greet_user():
    """ Display HTML to greet user """

    return """
        <html>
            <body>
                <h1>welcome</h1>
            </body>
        </html>
    """

@app.get("/welcome/home")
def greet_user_at_home():
    """ Display HTML to greet user to home"""

    return """
        <html>
            <body>
                <h1>welcome home</h1>
            </body>
        </html>
    """

@app.get("/welcome/back")
def greet_user_back():
    """ Display HTML to greet user back"""

    return """
        <html>
            <body>
                <h1>welcome back</h1>
            </body>
        </html>
    """
