import numpy as np
import random
import time
import argparse

def arg_parse():
	desc = 'Lottery parser'
	parser = argparse.ArgumentParser(description = desc)
	parser.add_argument('--seed', type=int, required=True)

	return parser.parse_args()

def convert_seed(seed):
	return int(time.time() * seed)

if __name__=="__main__":
	arg = arg_parse()

	n_students = 150

	converted_seed = convert_seed(arg.seed)
	random.seed(converted_seed)

	result = np.arange(n_students) + 1
	random.shuffle(result)

	print("Seed was: {}".format(converted_seed))
	print("Result is: {}".format(result))