import pickle
import config

def get_predicted_class(data):

    with open(config.MODEL_PATH,'rb') as f:
        model = pickle.load(f)

    x1 = float(data['x1'])
    x2 = float(data['x2'])
    x3 = float(data['x3'])
    x4 = float(data['x4'])

    result = model.predict([[x1,x2,x3,x4]])

    return result[0]


