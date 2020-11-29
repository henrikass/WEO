from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import pickle
import sklearn
from sklearn import preprocessing
import numpy as np

app = Flask(__name__)
api = Api(app)

filename = 'model_decision_tree.pck'
model = pickle.load(open(filename, 'rb'))


get_args = reqparse.RequestParser()
get_args.add_argument('Total investment', type=float,
                         help='Total investment must not be empty', required=True)
get_args.add_argument('General government revenue', type=float, 
                        help='General government revenue must not be empty', required=True)
get_args.add_argument('General government total expenditure', type=float, 
                        help='General government total expenditure must not be empty' , required=True)
get_args.add_argument('General government primary net lending/borrowing', type=float, 
                        help='General government primary net lending/borrowing must not be empty', required=True)
get_args.add_argument('General government gross debt', type=float, 
                        help='General government gross debt must not be empty', required=True)

class Weo(Resource):
    def get(self):
        args = get_args.parse_args()
        X = []
        X.append(args['Total investment'])
        X.append(args['General government revenue'])
        X.append(args['General government total expenditure'])
        X.append(args['General government primary net lending/borrowing'])
        X.append(args['General government gross debt'])
        X = preprocessing.scale(X)
        print('Incoming data is: ', X)
        print('-'*80)
        pred = model.predict([X])
        print('Prediction: ', pred)
        return {'Predicted GDP per capita': pred[0]}, 200

api.add_resource(Weo, '/weo')

if __name__ == "__main__":
    app.run(debug=True)


# http://127.0.0.1:5000/

# important_cols = ['Total investment',
#         'General government revenue',
#        'General government total expenditure',
#        'General government primary net lending/borrowing',
#        'General government gross debt',
#         'Gross domestic product, constant prices']