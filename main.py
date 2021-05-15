import argparse
from api_handler import make_api_call

parser = argparse.ArgumentParser()
parser.add_argument('-p', help='Enter pincode', required=True)
parser.add_argument('-d', help='Enter date', required=True)
args = vars(parser.parse_args())

date = str(args['d'])
pincode = str(args['p']).strip()


make_api_call(pincode, date)
