from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Viewport Width</title>
        <link rel="icon" type="image/x-icon" href="Pictures/favicon.ico">
        <link rel="stylesheet" href="practice.css">
    </head>
    <body>
        <div id="Section1"></div>
        <div id="Section2"></div>
        <div id="Section3"></div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)