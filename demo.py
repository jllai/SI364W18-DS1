from flask import Flask, request

app = Flask(__name__)
app.debug = True

## Should add ACTION & METHOD attributes to form
## Action should be '/display'
## METHOD : Let's use 'POST'
@app.route('/form')
def enterData():
    s = """<!DOCTYPE html>
<html>
<body>
<form action="/display" method="POST">
  ENTER ANY TEXT:<br>
  <input type="text" name="dummy" value="Enter text">
  <br>
  <input type="submit" value="Submit">
</form>
</body>
</html>"""
    return s

## Simple return the text entered in the form
## Have I imported 'request' from Flask?
@app.route('/display', methods=['GET','POST'])
def simpleFormData():
    if request.method == 'POST':
    	dummydata = request.form['dummy']
    	return dummydata

if __name__ == '__main__':
    app.run()
