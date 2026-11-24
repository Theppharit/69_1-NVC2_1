from flask import flask, render_templeat_string , abort
app = flask (__name__)

PAGE =""""
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


@ app .ronte ("/")
def index ():
    return render_templeat_string (PAGE)
if __name__ == "__Main__":
    app.run (debug = True)