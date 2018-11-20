#!/usr/bin/env python

# run with python --n <n>

import sys


def print_spaces(n):
    for i in range(n):
        sys.stdout.write(' ');

class Pyramid(list):
    def __init__(self):
        self.max = 2

    def append(self, entry):
        list.append(self, entry)
        for e in entry:
            if len(str(e)) > self.max:
                self.max = len(str(e))


    def print_pyr(self):
        #Get length of last line
        #max_int = self[-1][len(self[-1]) / 2]
        max_length = self.max + 2
        total_length = len(self[-1]) * max_length


        for row in self:
            row_length = len(row) * max_length
            diff_length = total_length - row_length
            print_spaces(diff_length / 2)

            for i in range(0, len(row)):

                entry = row[i]
                entry_length = len(str(entry))
                diff_indiv_len = max_length - entry_length

                print_spaces(diff_indiv_len / 2)
                if (diff_indiv_len % 2) != 0:
                    if (i + 1 > len(row) / 2):
                        print_spaces(1)

                sys.stdout.write(str(entry))

                if (diff_indiv_len % 2) != 0:
                    if (i + 1 <= len(row) / 2):
                        print_spaces(1)

                print_spaces(diff_indiv_len / 2)

            sys.stdout.write('\n')


def multiply_rows(row):
    new_rows = list()

    for i in range(0, len(row) - 1):
        j = i + 1;
        new_rows.append(row[i] * row[j])

    return new_rows


def add_rows(row):
    new_rows = list()

    for i in range(0, len(row) - 1):
        j = i + 1;
        new_rows.append(row[i] + row[j])

    return new_rows

def add_op(row, op):

    new_rows = list()

    for i in range(0, len(row) - 1):
        j = i + 1;

        new_entry = 0
        if op == '+':
            new_entry = row[i] + row[j]
        if op == '-':
            if i < (len(row) - 1) / 2:
                new_entry = row[j] - row[i]
            else:
                new_entry = row[i] - row[j]

        if op == '*':
            new_entry = row[i] * row[j]

        if op == 'div':
            if i < (len(row) - 1) / 2:
                new_entry = row[j] / row[i]
            else:
                new_entry = row[i] / row[j]

        if op == '%':
            if i < (len(row) - 1) / 2:
                new_entry = row[i] % row[j]
            else:
                new_entry = row[j] % row[i]

        new_rows.append(new_entry)

    return new_rows


def create_pyr_ops(n_rows, oplist):
    p = Pyramid()
    p.append([1])

    op = 0

    for i in range(1, n_rows):
        new_row = list()

        new_row = add_op(p[i - 1], oplist[op]);
        op = (op + 1) % len(oplist)

        new_row = [1] + new_row + [1]
        p.append(new_row)

    return p

def create_pyr(n_rows):
    return create_pyr_ops(n_rows, ['+', '*'])

#import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--n',type=int)
parser.add_argument('--ops',type=str)
args = parser.parse_args()

n = args.n
ops_list = args.ops.split(',')

if (len(ops_list) < 0):
    p = create_pyr(n)
else:
    p = create_pyr_ops(n, ops_list)

p.print_pyr()
#multiply_rows(p[0])
