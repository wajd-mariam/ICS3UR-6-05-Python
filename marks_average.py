#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: December 2019
# This program calculates average of all the marks enterd.


def average(marks):
    # this function calculates average and returns it.

    # variables
    total = 0
    number_of_marks = 0

    # process
    for item in marks:
        total = total + item
        number_of_marks = number_of_marks + 1

    # avg calculating
    avg = total / number_of_marks

    # returning average
    return round(avg)


def main():
    # this function takes all the input marks from user.

    # variables
    marks = []
    a_single_mark = 0
    final_avg = 0

    # input & process
    while a_single_mark != -1:
        a_single_mark = int(input("Enter a mark: "))
        marks.append(a_single_mark)

    marks.pop()

    final_avg = average(marks)

    # output
    print("The average of all of your marks is {}%".format(final_avg))


if __name__ == "__main__":
    main()
