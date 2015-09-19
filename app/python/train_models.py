from argparse import ArgumentParser
from trainer import Predictor

parser = ArgumentParser()
parser.add_argument("--userid", type=str)
parser.add_argument("--imgurl", type=str)
parser.add_argument("--train", action='store_true')
parser.add_argument("--add", action='store_true')
parser.add_argument("--is_pos", action='store_true')
args = parser.parse_args()
userid = args.userid
imgurl = args.imgurl
predictor = Predictor(userid)

pos_file = "../data/" + userid + ".pos"
neg_file = "../data/all_data"
# Assuming the pos file has byeen created by Javascript 
if args.add:
	predictor.add_to_training_set(imgurl, options.is_pos)
elif args.train:
	with open(pos_file, "r") as pos, open(neg_file, "r") as neg:
		pos_data = pos.readlines()
		neg_data = neg.readlines()
	predictor.train(pos_data, neg_data)
else:
	prediction = predictor.predict(imgurl)
	if prediction:
		with open(pos_file, "a") as pos:
			pos.write(imgurl + "\n")
	with open(neg_file, "a") as neg:
		neg.write(imgurl + "\n")