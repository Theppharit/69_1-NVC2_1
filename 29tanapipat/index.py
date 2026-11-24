from flask import Flask, render_template_string, abort
app = Flask(__name__)

PAGE ="""
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<h1>ธนาพิพัฒน์ วังกชา เลขที่33</h1> 
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(PAGE)
if __name__ == "__main__":
    app.run(debug = True)