from argparse import ArgumentParser
from trainer import Predictor

parser = ArgumentParser()
parser.add_argument("--userid", type=str)
parser.add_argument("--imgurl", type=str)
parser.add_argument("--train", action='store_true')
parser.add_argument("--add", action='store_true')
parser.add_argument("--is_pos", action='store_true')
(options, args) = parser.parse_args()
userid = options.userid
imgurl = options.imgurl
predictor = Predictor(userid)

pos_file = "../data/" + userid + ".pos"
neg_file = "../data/all_data"
# Assuming the pos file has been created by Javascript 
if options.add:
	predictor.add_to_training_set(imgurl, options.is_pos)
if options.train:
	with open(pos_file, "r") as pos, open(neg_file, "r") as neg:
		pos_data = pos.readlines()
		neg_data = neg.readlines()
	predictor.train(pos_data, neg_data)
else:
	print(predictor.predict(imgurl))
	with open(pos_file, "a") as pos:
		pos.write(imgurl + "\n")
	with open(neg_file, "a") as neg:
		neg.write(imgurl + "\n")