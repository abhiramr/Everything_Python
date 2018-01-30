# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy.stats import mode

def cleandf(df):

    #cleaning fare column
    df.Fare = df.Fare.map(lambda x: np.nan if x==0 else x)
    classmeans = df.pivot_table('Fare', rows='Pclass', aggfunc='mean')
    df.Fare = df[['Fare', 'Pclass']].apply(lambda x: classmeans[x['Pclass']] if pd.isnull(x['Fare']) else x['Fare'], axis=1 )
    
    #cleaning the age column
    meanAge=np.mean(df.Age)
    df.Age=df.Age.fillna(meanAge)
    
    #cleaning the embarked column
    df.Cabin = df.Cabin.fillna('Unknown')
    modeEmbarked = mode(df.Embarked)[0][0]
    df.embarked = df.Embarked.fillna(modeEmbarked)

    return df

def cleaneddf(no_bins=0):
    #you'll want to tweak this to conform with your computer's file system
    trainpath = 'C:/Documents and Settings/DIGIT/My Documents/Google Drive/Blogs/triangleinequality/Titanic/rawtrain.csv'
    testpath = 'C:/Documents and Settings/DIGIT/My Documents/Google Drive/Blogs/triangleinequality/Titanic/rawtest.csv'
    traindf = pd.read_csv(trainpath)
    testdf = pd.read_csv(testpath)
    
    #discretise fare
    if no_bins==0:
        return [cleandf(traindf), cleandf(testdf)]
    traindf=cleandf(traindf)
    testdf=cleandf(testdf)
    bins_and_binned_fare = pd.qcut(traindf.Fare, no_bins, retbins=True)
    bins=bins_and_binned_fare[1]
    traindf.Fare = bins_and_binned_fare[0]
    testdf.Fare = pd.cut(testdf.Fare, bins)
    
    #discretise age
    bins_and_binned_age = pd.qcut(traindf.Age, no_bins, retbins=True)
    bins=bins_and_binned_age[1]
    
    traindf.Age = bins_and_binned_age[0]
    testdf.Age = pd.cut(testdf.Age, bins)
    
    #create a submission file for kaggle
    predictiondf = pd.DataFrame(testdf['PassengerId'])
    predictiondf['Survived']=[0 for x in range(len(testdf))]
    predictiondf.to_csv('C:/Documents and Settings/DIGIT/My Documents/Google Drive/Blogs/triangleinequality/Titanic/prediction.csv',
                  index=False)
    return [traindf, testdf]
