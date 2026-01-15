#!/usr/bin/env python3

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename', nargs='?', default='locations.csv')


if __name__ == "__main__":
    args = parser.parse_args()
    print(args.filename)
