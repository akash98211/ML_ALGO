import pickle

def get_predicted_class(data):

    with open('model\iris_classification.pickle','rb') as f:
        model = pickle.load(f)

    print("MMMMMMMM",model)

    x1 = float(data['x1'])
    x2 = float(data['x2'])
    x3 = float(data['x3'])
    x4 = float(data['x4'])

    result = model.predict([[x1,x2,x3,x4]])

    return result[0]


