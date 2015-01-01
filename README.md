# Coconut Delivery Problem

A swallow has an assignment to deliver a coconut to a possibly-insane king.

To save energy for the flight, the swallow will take advantage of jet streams that will lower his flying energy consumption.

Before the flight, the delivery service gave the swallow an input file in the following format:

First line contains only 1 integer, which is the constant energy it takes to fly 1 mile WITHOUT jet streams.

Every subsequent line contains 3 space-separated integers: the start mile marker of the jet stream,
the end mile marker of the jet stream, and lastly an integer denoting the overall energy needed to fly that jet stream’s distance.

For instance, the line “3 7 12″ means it takes 12 energy units to fly the 4 miles between mile-markers 3 and 7.

Jet streams can overlap, but the swallow cannot be on more than one jet stream at a time, and it cannot fly partial jet streams.

For simplicity, consider the end mile marker of the farthest jet stream as the end of the flight.

Write a python program that takes in an input file flight_paths to plan out the optimal sequence of jet streams,
the swallow should fly on to minimize his energy consumption throughout the entire flight.

All integers in the input file are non-negative.
As output, print out the minimum total energy and a list of tuples denoting the jet streams’ endpoints.

### Approach

The following program solves the coconut delivery problem and finds the optimal sequence of paths to travel on in order
to minimize the total energy consumed in the flight to the destination.

It follows the approach of dynamic programming and builds the optimal path sequence iteratively in a bottom-up manner.

The sub-problem is as follows:

```
optimal_path[i] = min(optimal_path[i - 1] + ENERGY_WITHOUT_JET_STREAM,
                      optimal_path[start_marker[i]] + ENERGY_REQUIRED[start_marker[i]])
```
This is computed for every single mile marker from the beginning of the jet streams

### Usage

```
> python optimal_sequence.py <path_to_file_containing_flight_paths>
```