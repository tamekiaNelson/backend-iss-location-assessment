#!/usr/bin/env python
import requests
import time
import turtle

__author__ = 'tamekiaNelson'


def get_astronaunts():
    """gets list of astronauts who are currently in space"""
    url = "http://api.open-notify.org/astros.json"
    r = requests.get(url)
    d = r.json()
    return d["people"]


def get_location():
    """ gets current geographic coordinates (lat/lon)
    of the space station, along with a timestamp """
    url_location = "http://api.open-notify.org/iss-now.json"
    r = requests.get(url_location)
    result = r.json()
    d = result['iss_position']
    lat = float(d['latitude'])
    lon = float(d['longitude'])
    t = time.ctime(result['timestamp'])
    return lat, lon, t


def get_world_map(lon, lat, pass_time):
    """creates a graphics screen with the world map background image"""
    screen = turtle.Screen()
    screen.bgpic('map.gif')
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.penup()
    iss.goto(lon, lat)
    Indy_pos = turtle.Turtle()
    Indy_pos.shape('circle')
    Indy_pos.color('yellow')
    Indy_pos.penup()
    Indy_pos.goto(-86.1349, 40.273502)
    message = turtle.Turtle()
    message.color('yellow')
    message.write(pass_time, True, align='center', font=('Arial', 20, 'normal'))
    screen.exitonclick()


def passing_over_Indy():
    """Find out the next time that the ISS
    will be overhead of Indianapolis IN."""
    url_indy_passover = "http://api.open-notify.org/iss-pass.json?lat=40&lon=-86.1349"
    r = requests.get(url_indy_passover)
    results = r.json()
    d = results['response'][1]
    time_over = time.ctime(d['risetime'])
    return time_over


def main():
    people_li = get_astronaunts()
    for astro in people_li:
        print("{} is aboard {}".format(astro["name"], astro["craft"]))
    lat, lon, t = get_location()
    print("Current ISS location lat = {}, lon = {}, time = {}".format(lat, lon, t))
    time_over = passing_over_Indy()
    print("Next pass over Indy is {}".format(time_over))
    get_world_map(lon, lat, time_over)


if __name__ == '__main__':
    main()
