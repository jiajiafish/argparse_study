import argparse
parser = argparse.ArgumentParser(description="计算x和Y的平均值")
group =parser.add_mutually_exclusive_group()
parser.add_argument("x",type = int,help ="基数")
parser.add_argument("y",type = int,help ="乘数")
# parser.add_argument("square",type = int,help ="显示一个数字的平方")
group.add_argument("-v","--verbosity",action = "store_true")
group.add_argument("-q","--quiet",action = "store_true")


# parser.add_argument("-v","--verbosity",help ="increase output verbosity",action ="store_true")
# parser.add_argument("-v","--verbosity",action = "count",help="dddddddd",default = 0)
args = parser.parse_args()
answer = args.x*args.y
if args.quiet:
    print(answer)
elif args.verbosity:
    print("{}乘以{} 等于{}".format(args.x,args.y,answer))
else:
    print("{}*{}={}".format(args.x,args.y,answer))
    
# if args.verbosity:
#     print("the square of {} equals {}".format(args.square,answer))
# else:
#     print(answer))