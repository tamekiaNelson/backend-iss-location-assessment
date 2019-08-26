#!/usr/bin/env python

__author__ = '???'


#Part A
# Using this public API, write a python program to obtain a list of the
# astronauts who are currently in space.  Print their full names, the
# spacecraft they are currently on board, and the total number of astronauts
# in space.
# http://api.open-notify.org/astros.json
def get_astronauts(url):
    return url


#Part B
# Using another public API, obtain the current geographic coordinates (lat/lon)
# of the space station, along with a timestamp.
# http://api.open-notify.org/iss-now.json
def get_coordinates(url):
    return url


#Part C
# With the turtle graphics library (part of standard Python), create a
# graphics screen with the world map background image.  Use turtle methods
# such as Screen, setup, bgpic, setworldcoordinates.  Register an icon
# image for the ISS station within the turtle screen context, and create a
# turtle.Turtle() context to move the ISS station to its current lat/lon
# on the map.  Use methods such as shape, setheading, penup, and goto.
def create_graphics_screen(url):
    return url


#Part D
# Find out the next time that the ISS will be overhead of Indianapolis IN.
# Use our geographic lat/lon to plot a yellow dot on the map.  Use this
# public API to query the next pass:
# http://api.open-notify.org/iss-pass.json
# You will need to supply the lat/lon coordinates as query parameters to
# this url.  The passover times are returned as timestamps, so you will
# need to use the time.ctime() method to convert them to human-readable text.
# Render the next passover time next to the Indianapolis location dot that
# you plotted earlier.
def get_iss_pass(url, lat, lon):
    return url, lat, lon





def main():
    print(get_astronauts('http://api.open-notify.org/astros.json'))
    print(get_coordinates('http://api.open-notify.org/iss-now.json'))
    print(create_graphics_screen('http://api.open-notify.org/iss-now.json'))
    print(get_iss_pass('http://api.open-notify.org/iss-pass.json', 39.768403, -86.158068))



if __name__ == '__main__':
    main()
