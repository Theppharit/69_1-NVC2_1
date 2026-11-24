from flask import Flask, render_template_string, abort
app = flask(__name__)
            
PAGE = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>อรณิชชา บุญยอม 06819100025</h1>
</body>
</html>

"""

@app.route("/")
def index():
    render_template_string(PAGE)
                           
if __name__=="__main__"  :
    app.run(debug=True)                         