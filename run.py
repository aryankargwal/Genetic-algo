# imports
import sys
import argparse
from gaevol import gaevol

parser = argparse.ArgumentParser(description="Enter string you want to see evolve:")
parser.add_argument("string", help="Add string without number and special characters")
parser.add_argument("populate", help="Enter poplation of each Generation")
parser.add_argument("mutrate", help="Probability of Mutation")
args = parser.parse_args()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        #        parser.print_help()
        print("Incorrect number of params")
        exit()
    else:
        gaevol(sys.argv[1], sys.argv[2], sys.argv[3])
