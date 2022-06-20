from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/') 
def hello_flask():
    print('Testing Flask')

    return 'Hello Python'

@app.route('/test') 
def test():
    print('Testing API')
    # return jsonify({'Message':'API Tested Successfully'})
    return jsonify({'Message':'Successful'})

@app.route('/name/<name>')  # Default datatype of name variable is string
def Name(name):
    print('Name is ',name)
    return jsonify({'Message':'Successful'})

@app.route('/marks/<int:mark>')  
def student_marks(mark):
    print('Student Marks : ',mark,type(mark))
    return jsonify({'Message': f'Student Marks : {mark}'})

if __name__ == "__main__":
    app.run()