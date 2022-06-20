from flask import Flask,jsonify,request
import project_db
import math_calculation
import utils

app = Flask(__name__)

#########################################################################
################### Addition API ########################################
#########################################################################

@app.route('/addition') 
def addition():
    data = request.form
    print(" data >>>>>>> ",data)
    a = int(data['a'])
    b = int(data['b'])
    result = math_calculation.get_addition(a,b)

    print(f'Addition of {a} and {b} is', result)
    return jsonify({'Message': f"Addition is {result}"})


###########################################################################
########################### Multiplication API ############################
###########################################################################

@app.route('/multiplication') 
def multiplication():
    data = request.get_json()
    print(" data >>>>>>> ",data)
    a = int(data['a'])
    b = int(data['b'])

    add = a + b
    print(f'Addition of {a} and {b} is', add)
    return jsonify({'Message': f"Addition is {add}"})

########################################################################
####################### Register API ###################################
########################################################################

@app.route('/register') 
def register():
    print('Testing Registration API')
    data = request.form

    response = project_db.register_user(data)
    
    return jsonify({'Message': response})

########################################################################
####################### Register API ###################################
########################################################################

@app.route('/login') 
def login():
    print('Testing Login API')
    data = request.form

    response = project_db.login_user(data)
    
    return jsonify({'Message': response})


########################################################################
####################### Predict Price API ###################################
########################################################################

@app.route('/predict_class') 
def predict_class():
    print('predict_class API')

    data = request.form

    response = utils.get_predicted_class(data)
    
    return jsonify({'Message': f"Predicted Class is:{response} "})


if __name__ == "__main__":
    app.run()