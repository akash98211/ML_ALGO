from flask import Flask, config,jsonify,request
import project_db
import math_calculation
import utils
import config
app = Flask(__name__)

#########################################################################
################### Addition API ########################################
#########################################################################

@app.route('/credit/addition/add_two_numbers') 
def addition():
    data = request.form
    print(" data >>>>>>> ",data)
    a = int(data['a'])
    b = int(data['b'])
    result = math_calculation.get_addition(a,b)

    print(f'Addition of {a} and {b} is', result)
    return jsonify({'Message': f"Addition is {result}"})

@app.route('/credit/addition/add_three_numbers') 
def addition_three_numbers():
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

@app.route('/credit/multiplication') 
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

@app.route('/credit/register',methods = ['GET','POST']) 
def register():
    if request.method == 'POST':
        print('Testing Registration API')
        data = request.form

        response = project_db.register_user(data)
        print("Hello")
        return jsonify({'Message': response})

    print("*************************************")
    return jsonify({'Message': "Unsuccessful"})

########################################################################
####################### Register API ###################################
########################################################################

@app.route('/credit/login') 
def login():
    print('Testing Login API')
    data = request.form

    response = project_db.login_user(data)
    
    return jsonify({'Message': response})


########################################################################
####################### Predict Price API ###################################
########################################################################

@app.route('/credit/predict_class') 
def predict_class():
    print('predict_class API')

    data = request.form

    response = utils.get_predicted_class(data)
    
    return jsonify({'Message': f"Predicted Class is:{response} "})


if __name__ == "__main__":
    app.run(host = '0.0.0.0' , port = config.PORT_NUMBER, debug = True)