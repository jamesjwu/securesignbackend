"""
Trainer.py - using clarifai API a bunch of signatures from the file

Command line: takes in a list of files
"""
import threading

import os
from clarifai_basic import ClarifaiCustomModel
os.environ["CLARIFAI_APP_SECRET"] = "Jf6Sm2o8bY-MopRVJUjPeTzfJvTPtNC9nW20rVoL"
os.environ["CLARIFAI_APP_ID"] = "BQv24SbZOmKS-LE1I7z_xXc01AX32luGBy84OKDI"
# instantiate clarifai client
threshold = 0.5
concept = ClarifaiCustomModel()

filename = "test.txt"
class Predictor(object):    
    def __init__(self, userid):
        self.userid = userid

    def train(self, positives, negatives):
        map(lambda x: concept.positive(x, self.userid), positives)
        map(lambda x: concept.negative(x, self.userid), negatives)
        concept.train(self.userid)
        print "Trained!"

    def add_to_training_set(self, img, positive):
        if positive:
            concept.positive(img, self.userid)
        else:
            concept.negative(img, self.userid)
        # retrain the data
        concept.train()

    def predict(self, image):
        result = concept.predict(image, self.userid)
        if result['status']['status'] == 'OK':
            print result['urls'][0]['score']

            return result['urls'][0]['score'] > threshold





def test():
    p = Predictor("sonya")
    print p.predict("http://i.imgur.com/rf4CxZG.jpg")

test()
print "Done"


