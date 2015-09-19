"""
Simple example showing Clarifai Custom Model training and prediction

This example trains a concept classifier that recognizes photos of the band Phish.
"""

from clarifai_basic import ClarifaiCustomModel

import os

os.environ["CLARIFAI_APP_SECRET"] = "Jf6Sm2o8bY-MopRVJUjPeTzfJvTPtNC9nW20rVoL"
os.environ["CLARIFAI_APP_ID"] = "BQv24SbZOmKS-LE1I7z_xXc01AX32luGBy84OKDI"
# instantiate clarifai client
concept = ClarifaiCustomModel()

print "Training positives"
concept.positive('http://i.imgur.com/rf4CxZG.jpg', 'sonya')
concept.positive('http://i.imgur.com/EnpQf7j.jpg', 'sonya')
concept.positive('http://i.imgur.com/epDGjYJ.jpg', 'sonya')
concept.positive('http://i.imgur.com/vrAKrHZ.jpg', 'sonya')
concept.positive('http://i.imgur.com/J35qiyl.jpg', 'sonya')

print "Training negatives"
concept.negative('http://i.imgur.com/uoLlVin.jpg', 'sonya')
concept.negative('http://i.imgur.com/1SLeV0t.jpg', 'sonya')
concept.negative('http://i.imgur.com/WvNMnEh.jpg', 'sonya')
concept.negative('http://i.imgur.com/0OkfP6n.jpg', 'sonya')
concept.negative('http://i.imgur.com/3IZeBl1.jpg', 'sonya')

TESTS = ['http://i.imgur.com/Srg5yNf.jpg', 'http://i.imgur.com/8vH4H5X.jpg']


for test in TESTS:
  result = concept.predict(test, 'sonya')
  print result['status']['message'], "%0.3f" % result['urls'][0]['score'], result['urls'][0]['url']

# Our output is the following. Your results will vary as there are some non-deterministic elements
# of the algorithms used.

# Success 0.797 http://phishthoughts.com/wp-content/uploads/2012/07/photo-1-11-e1342391144673.jpg
# Success 0.706 http://bobmarley.cdn.junip.com/wp-content/uploads/2014/10/DSC01226-e1311293061704.jpg
# Success 0.356 http://farm3.static.flickr.com/2161/2141620332_2b741028b3.jpg
# Success 0.273 http://www.mediaspin.com/joel/grateful_dead230582_15-52.jpg
