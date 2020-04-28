# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
import math
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import mean_squared_error
import os
from keras.utils import multi_gpu_model


# if train on GPU
os.environ["CUDA_VISIBLE_DEVICES"] = '0'

# set dataset and parameters
DATASET = 'data/crime_H.csv'
look_back = 72
look_forward = 24
epochs = 25
batch_size = 256


def create_dataset(dataset, look_back = 1, look_forward = 1):
    dataX, dataY = [], []
    feature_dim = dataset.shape[1]
    for i in range(len(dataset)-look_back-look_forward):
        X = dataset[i: (i+look_back), :]
        Y = dataset[i+look_back: i+look_back+look_forward, 0]
        dataX.append(X)
        dataY.append(Y)
    return numpy.array(dataX), numpy.array(dataY)
  

def create_resultset(dataset, look_back = 1):
    dataX = []    
    a = dataset[len(dataset)-look_back:len(dataset), :]
    dataX.append(a)
    return numpy.array(dataX)


def inverse_transform(dataY, feature_dim, look_forward = 1):
    dataset_like = numpy.zeros(shape=(len(dataY), feature_dim))
    for i in range(look_forward):
        dataset_like[:, 0:1] = dataY[:, i:i+1]
        dataY[:, i:i+1] = scaler.inverse_transform(dataset_like)[:, 0:1]
    return dataY
 

if __name__ == '__main__':
    
    # read dataset
    dataframe = read_csv(DATASET, usecols=['Type', 'Type_property', 'Type_violent', 'Loc_public', 'Loc_private',\
        'Arrest', 'Domestic'], engine='python')
    dataframe = dataframe[['Type', 'Type_property', 'Type_violent', 'Loc_public', 'Loc_private', 'Arrest', 'Domestic']]
    dataset = dataframe.values
    dataset = dataset.astype('float32')
    
    # normalization
    scaler = MinMaxScaler(feature_range = (0,1))
    dataset = scaler.fit_transform(dataset)
    
    # split trainset and testset
    train_size = int(len(dataset) * 3/4)
    test_size = len(dataset) - train_size
    train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

    # create trainset and testset
    print(train.shape)
    trainX, trainY = create_dataset(train, look_back, look_forward)
    testX, testY = create_dataset(test, look_back, look_forward)
    print(trainX.shape, trainY.shape)
    
    # reshape to LSTM input format (sample, step, feature_dim)
    trainX = numpy.reshape(trainX, (trainX.shape[0], look_back, train.shape[1]))
    testX = numpy.reshape(testX, (testX.shape[0], look_back, test.shape[1]))
    
    
    # LSTM (hidden units, step, feature_dim)
    model = Sequential()
    #model.add(LSTM(128, input_shape = (trainX.shape[1], trainX.shape[2])))
    model.add(LSTM(100, return_sequences=True, input_shape = (trainX.shape[1], trainX.shape[2])))
    model.add(LSTM(50))    
    model.add(Dense(trainY.shape[1]))
    model.compile(loss = 'mean_squared_error', optimizer = 'adam')
    model.fit(trainX, trainY, epochs = epochs, batch_size = batch_size, verbose = 2)

    #if trained parallelly
    #parallel_model = multi_gpu_model(model, gpus=2)
    #parallel_model.compile(loss='mean_squared_error', optimizer='adam')
    #parallel_model.fit(trainX, trainY, epochs = epochs, batch_size = batch_size, verbose = 2)    
    
    #model.save('model/model_%sb%sf.h5' % (look_back, look_forward))
    #del model
    #model = load_model('model/model_%sb%sf.h5' % (look_back, look_forward))
    
    # predict
    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)
    #print(trainPredict.shape, testPredict.shape)

    '''
    # if predict recursively
    trainPredict = numpy.concatenate((trainPredict, testPredict))
    trainPredict = numpy.append(trainPredict, testPredict)
    trainPredict = numpy.reshape(trainPredict, (trainPredict.shape[0], train.shape[1]))
    
    for i in range(12): 
        new_train =  create_trainset(trainPredict, look_back) 
        new_train = numpy.reshape(new_train, (new_train.shape[0], look_back, train.shape[1]))
        new_train = model.predict(new_train)
        trainPredict = numpy.concatenate((trainPredict, new_train))
    ''' 

    # inverse_transform
    print('Before transform:', trainPredict.shape, trainY.shape)
    trainPredict = inverse_transform(trainPredict, dataset.shape[1], look_forward)
    trainY = inverse_transform(trainY, dataset.shape[1], look_forward)
    testPredict = inverse_transform(testPredict, dataset.shape[1], look_forward)
    testY = inverse_transform(testY, dataset.shape[1], look_forward)
    print('After transform:', trainPredict.shape, trainY.shape)
    

    # calculate RMSE
    trainScore = math.sqrt(mean_squared_error(trainY, trainPredict))
    print('Train Score: %.2f RMSE' % (trainScore))
    testScore = math.sqrt(mean_squared_error(testY, testPredict))
    print('Test Score: %.2f RMSE' % (testScore))
    
    resultX = create_resultset(test, look_back)
    resultX = numpy.reshape(resultX, (resultX.shape[0], look_back, test.shape[1]))
    result = model.predict(resultX)
    result = inverse_transform(result, dataset.shape[1], look_forward)
    result = numpy.reshape(result, (look_forward, 1))
    #resultPredictPlot[len(dataset): len(dataset)+look_forward, 0] = result[:, 0]
    #print(result.shape, resultPredictPlot.shape)


    # save predicted value
    df = pd.DataFrame(result.astype(int))
    df.columns = ['Predict']
    df.to_csv('data/predict.csv', index = False)

    
    # plot for test
    '''
    trainPredictPlot = numpy.empty((len(trainPredict)+look_back, look_forward))
    trainPredictPlot[:, :] = numpy.nan
    trainPredictPlot[look_back:len(trainPredict)+look_back, 0] = trainPredict[:, 0]
    testPredictPlot = numpy.empty((len(dataset), look_forward))
    testPredictPlot[:, :] = numpy.nan
    testPredictPlot[len(dataset)-len(testPredict)-look_forward:len(dataset)-look_forward, 0] = testPredict[:, 0]

    resultPredictPlot = numpy.empty((len(dataset)+look_forward, 1))
    resultPredictPlot[:, :] = numpy.nan
    resultPredictPlot[len(dataset): len(dataset)+look_forward, 0] = result[:, 0]    
    
    datasetPlot = scaler.inverse_transform(dataset)
    plt.plot(datasetPlot[:, 0])
    plt.plot(trainPredictPlot)
    plt.plot(testPredictPlot)
    plt.plot(resultPredictPlot)
    #plt.savefig("test.png")
    plt.show()
    '''
    
