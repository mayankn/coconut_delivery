#!/usr/bin/python

__author__ = 'mayanknarasimhan'

'''
Description:
A swallow has an assignment to deliver a coconut to a possibly-insane king.
To save energy for the flight, the swallow will take advantage of jet streams that will lower his flying energy
consumption.
Before the flight, the delivery service gave the swallow an input file in the following format:
First line contains only 1 integer, which is the constant energy it takes to fly 1 mile WITHOUT jet streams.
Every subsequent line contains 3 space-separated integers: the start mile marker of the jet stream,
the end mile marker of the jet stream, and lastly an integer denoting the overall energy needed to fly that jet stream's
distance.
For instance, the line "3 7 12" means it takes 12 energy units to fly the 4 miles between mile-markers 3 and 7.
Jet streams can overlap, but the swallow cannot be on more than one jet stream at a time, and it cannot fly partial jet
streams.
For simplicity, consider the end mile marker of the farthest jet stream as the end of the flight.
Write a python program that takes in an input file flight_paths to plan out the optimal sequence of jet streams,
the swallow should fly on to minimize his energy consumption throughout the entire flight.
All integers in the input file are non-negative.
As output, print out the minimum total energy and a list of tuples denoting the jet streams' endpoints.

Solution:
The following program solves the coconut delivery problem and finds the optimal sequence of paths to travel on in order
to minimize the total energy consumed in the flight to the destination.
It follows the approach of dynamic programming and builds the optimal path sequence iteratively in a bottom-up manner.
The sub-problem is as follows:
optimal_path[i] = min(optimal_path[i - 1] + ENERGY_WITHOUT_JET_STREAM,
                      optimal_path[start_marker[i]] + ENERGY_REQUIRED[start_marker[i]])
'''

from sys import argv
from sys import maxint


def find_optimal_sequence(flight_paths):
    end_markers = {}
    origin = 0
    begin_value = maxint
    destination = 0
    lines = open(flight_paths, 'r').read().splitlines()
    ENERGY_WITHOUT_JET_STREAM = int(lines[0])
    for i in range(1, len(lines)):
        line = [int(x) for x in lines[i].split()]
        start = line[0]
        end = line[1]
        energy = line[2]

        # store the end mile marker along with the from mile marker to start from and the energy for this journey
        end_markers[end] = (start, energy)

        # find out the beginning of the jet stream and the destination of the flight
        if start < begin_value:
            begin_value = start
        if end > destination:
            destination = end

    # holds the optimal energy required to reach each and every mile marker
    # and also the parent mile marker to get to each mile marker
    optimal_path = {}
    no_parent = -1

    # calculate energy required to the first jet stream and its parent
    if begin_value == origin:
        optimal_path[begin_value] = (0, no_parent)
    else:
        optimal_path[begin_value] = ((begin_value) * ENERGY_WITHOUT_JET_STREAM, no_parent)

    # for every single mile marker from the beginning of the jet stream
    for idx in range(begin_value + 1, destination + 1):
        # there exists a jet stream to get to this mile marker
        if idx in end_markers:
            path_without_jet_stream = optimal_path[idx - 1][0] + ENERGY_WITHOUT_JET_STREAM
            path_with_jet_stream = optimal_path[end_markers[idx][0]][0] + end_markers[idx][1]
            parent = idx - 1
            if path_with_jet_stream < path_without_jet_stream:
                parent = end_markers[idx][0]
            optimal_path[idx] = (min(path_without_jet_stream, path_with_jet_stream), parent)
        else:
            optimal_path[idx] = (optimal_path[idx - 1][0] + ENERGY_WITHOUT_JET_STREAM, idx - 1)

    print 'Minimum total energy needed:', optimal_path[destination][0], 'energy units'
    print_optimal_sequence_path(destination, optimal_path, end_markers)


def print_optimal_sequence_path(destination, optimal_path, end_markers):
    path = []
    parent = destination
    no_parent = -1

    # Back-track through the parent mile markers and add the jet stream tuples to a list
    while parent is not no_parent:
        if parent in end_markers:
            path.append((end_markers[parent][0], parent))
        parent = optimal_path[parent][1]

    print 'Optimal sequence of jet streams:', sorted(path)


if __name__ == '__main__':
    # find_optimal_sequence('sample_paths.txt')
    find_optimal_sequence(argv[1])
