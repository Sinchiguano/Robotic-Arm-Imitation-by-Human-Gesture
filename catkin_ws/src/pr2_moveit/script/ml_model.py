#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
import csv
import pandas as pd
from sklearn import linear_model, metrics, svm, preprocessing
import numpy as np
import sys
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD


from sklearn.datasets.samples_generator import make_regression
from sklearn import datasets
file_name='joint_data.csv'
joints=['r_shoulder_pan_joint','r_shoulder_lift_joint','r_upper_arm_roll_joint',
        'r_elbow_flex_joint','r_forearm_roll_joint','r_wrist_flex_joint',
        'r_wrist_roll_joint']

def csv_as_dataframe():
    """Load 'csv file and return dataframe"""
    tmp_data= pd.read_csv(file_name)
    X_=tmp_data[['RWrist = 6x','RWrist = 6y','RElbow = 7x','RElbow = 7y','RShoulder = 8x','RShoulder = 8y']]
    y_=tmp_data[joints]

    tmp_out=tmp_data[joints]
    print('joints')
    #print(tmp_data.head(3))
    #return X_,y_
    return X_,y_
def compute_err_MSE(y, yhat):
    """Return the mean squared error given the true values of y and predictions yhat."""
    # MODIFY THE FOLLOWING WITH YOUR CODE
    err=(yhat-y)**2
    err=np.sum(err)/len(y)
    return err

def main():
    print('=================')
    X_data,y_data=csv_as_dataframe()
    print('data for training')
    #print(X_data.head(5))
    #print(y_data.head(5 ))
    #sys.exit(0)

    # Scale the data
    sc = preprocessing.StandardScaler()
    #X_data= sc.fit_transform(X_data)
    print('=================')
    print(type(X_data))
    #print(X_data[:5])
    #print(y_data[:5])

    ####################################################
    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data,test_size=0.25)
    #print(y_train[:5])
    #print(y_test[:5])
    print('\nShapes of training and testing X:')
    print('X_train.shape',X_train.shape)
    print('X_test.shape',X_test.shape)
    print('Shapes of training and testing y:')
    print('y_train.shape',y_train.shape)
    print('y_test.shape',y_test.shape)
    #exit(0)
    #===================================================
    # MODELS
    #====================================================

    #Create a model!!!
    clf1 =  RandomForestRegressor(max_depth=30, random_state=2)
    #clf2=MultiOutputRegressor(RandomForestRegressor(max_depth=30,random_state=0))
    clf2 = MultiOutputRegressor(GradientBoostingRegressor(random_state=0))
    clf3 = MLPRegressor(solver='lbfgs',hidden_layer_sizes=(2,3))

     #Training step
    clf1.fit(X_train,y_train)
    clf2.fit(X_train,y_train)
    clf3.fit(X_train,y_train)

    model = Sequential()
    model.add(Dense(20, activation='relu', input_dim=6))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(7, activation='softmax'))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
                  optimizer=sgd,
                  metrics=['accuracy'])
    model.fit(X_train, y_train)

    #Make predictions!!!

    y_hat1=clf1.predict(X_test)
    y_hat2=clf2.predict(X_test)
    y_hat3=clf3.predict(X_test)
    y_hat4=model.predict(X_test)

    print('=========================')
    #Accuracy!!!
    # print('\nThe training and testing accuracies when simple split is used:')
    # mse1 = compute_err_MSE(y_test, y_hat1)#mean_squared_error(y_test, y_hat1)
    # mse2 = compute_err_MSE(y_test, y_hat2)#mean_squared_error(y_test, y_hat2)



    print('=====RandomForestRegressor=====')
    print('Training:',mean_squared_error(y_train, clf1.predict(X_train)))
    print('Testing:',mean_squared_error(y_test, y_hat1))
    print()
    print('====MultiOutputRegressor======')
    print('Training:',mean_squared_error(y_train, clf2.predict(X_train)))
    print('Testing:',mean_squared_error(y_test, y_hat2))
    print()
    print('========MLPRegressor=========')
    print('Training:',mean_squared_error(y_train, clf3.predict(X_train)))
    print('Testing:',mean_squared_error(y_test, y_hat3))
    print()
    print('=====keras.models=========')
    print('Training:',mean_squared_error(y_train, model.predict(X_train)))
    print('Testing:',mean_squared_error(y_test, y_hat4))
    #print(model.evaluate(X_test, y_test))
    print('==============')
    scores = model.evaluate(X_test, y_test, verbose=0)
    print("Test: %s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    scores = model.evaluate(X_train, y_train, verbose=0)
    print("Training:%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))



    #======================================
    # #Save my training model for machine learning algorithm done in python
    # from sklearn.externals import joblib
    #
    # filename = 'pre-trained_model.sav'
    # joblib.dump(model, filename)
    # #loaded_model = joblib.load(filename)


    from keras.models import model_from_json
    import numpy,h5py
    import os

    # # serialize model to JSON
    # model_json = model.to_json()
    # with open("model.json", "w") as json_file:
    #     json_file.write(model_json)
    # # serialize weights to HDF5
    # model.save_weights("model.h5")
    # print("Saved model to disk")
    # print('======================================')
    #
    # # later...
    # # load json and create model
    # json_file = open('model.json', 'r')
    # loaded_model_json = json_file.read()
    # json_file.close()
    # loaded_model = model_from_json(loaded_model_json)
    # # load weights into new model
    # loaded_model.load_weights("model.h5")
    # print("Loaded model from disk")
    # print('======================================')
    #
    # # evaluate loaded model on test data
    # loaded_model.compile(loss='categorical_crossentropy',
    #               optimizer=sgd,
    #               metrics=['accuracy'])
    # score = loaded_model.evaluate(X_test, y_test, verbose=0)
    # print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
    # scores = loaded_model.evaluate(X_train, y_train, verbose=0)
    # print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))



if __name__=='__main__':
    main()
