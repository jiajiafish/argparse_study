import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
# parser.add_argument("echo",help="show the string you use here")
# args = parser.parse_args()
# print(args.echo)

parser.add_argument("square",help="display a square",type=int)
args = parser.parse_args()
print(args.square**2)