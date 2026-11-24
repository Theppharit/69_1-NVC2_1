from flask import Flask, render_template_straing, abourt
app = Flask(__name__)

PAGE = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>


</head>
<body>
    <H1> นาย ศุภสิน รื่นนุสาร 68219100037 </H1>
</body>


</html>

"""
@app.route("/")
def index():
 return render_template_straing(PAGE)

if __name__ == "__main__":
     app.run(debug=True)

