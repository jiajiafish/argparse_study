import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square",type = int,help ="显示一个数字的平方")
# parser.add_argument("-v","--verbosity",help ="increase output verbosity",action ="store_true")
parser.add_argument("-v","--verbosity",action = "count",help="dddddddd",default = 0)
args = parser.parse_args()
answer = args.square**2
if args.verbosity >=2:
    print("square of {} equals {}".format(args.square,answer))
elif args.verbosity >=1:
    print("{}^2 == {}".format(args.square,answer))
else:
    print(answer)
    
# if args.verbosity:
#     print("the square of {} equals {}".format(args.square,answer))
# else:
#     print(answer))