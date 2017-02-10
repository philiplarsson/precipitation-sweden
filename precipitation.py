#!/usr/bin/env python3

## Author: Philip Larsson
#
# Check if there is any precipitation for specified hours forward (8 is default).
# Use this link to get correct latitude and longitude: http://opendata.smhi.se/apidocs/metfcst/demo_point.html
# Change using --latitude and --longitude to get correct geographic area. Default is Lund Sweden.
# See more using -h or --help.
#
# Using API from SMHI Open Data.
# Read more here: http://opendata.smhi.se/apidocs/
#
##

import requests, json, time, sys
from pprint import pprint
from datetime import datetime
import argparse

# Global variables (default values)
hours_forward = 8
latitude = 55.71
longitude = 13.19
print_category = True

time_now_as_string = "%d-%d-%dT%d:00:00Z" % (datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour)

categorys = {
        0: "no precipitation",
        1: "snow",
        2: "snow and rain",
        3: "rain",
        4: "drizzle",
        5: "freezing rain",
        6: "freezing drizzle"
}


def parse_command_line_options():
    global hours_forward, latitude, longitude, print_category

    parser = argparse.ArgumentParser(description='Check if there is any precipitation in specified latitude longitude.')
    parser.add_argument("--hours", help="specify upper limit on hours to check for precipitation", required=False)
    parser.add_argument("--latitude", help="latitude for where to get precipitation data")
    parser.add_argument("--longitude", help="longitude for where to get precipitation data")
    parser.add_argument("--list_categorys", help="list all categorys that are returned when using the --only_value flag.", action="store_true")
    parser.add_argument("--only_value", help="only prints the precipitation category and not it's meaning.", action="store_true")
    args = parser.parse_args()

    if args.hours:
        hours_forward = int(args.hours)

    if args.latitude:
        latitude = args.latitude

    if args.longitude:
        longitude = args.longitude

    if args.list_categorys:
        print("Printing categorys.\n value: meaning")
        pprint(categorys)
        sys.exit()

    if args.only_value:
        print_category = False

def get_data():
    base_api_link = "http://opendata-download-metfcst.smhi.se/api/category/pmp2g/version/2/"
    r = base_api_link + "geotype/point/lon/" + str(longitude) + "/lat/" + str(latitude) + "/"
    r += "data.json"

    req = requests.get(r)
    data = json.loads(req.text)
    return data

def get_type_of_downfall(data):
    start_index = 0
    # Find current time 'index'
    for x in range(0, len(data["timeSeries"])) :
        if (data["timeSeries"][x]["validTime"] == time_now_as_string):
            start_index = x
            break

    # Check if any downfall in the next 'hours_forward'.
    for x in range(start_index, start_index + hours_forward):
        for i in range(0, 19):
            if (data["timeSeries"][x]["parameters"][i]["name"] == "pcat"):
                # We have pacs data.
                pacs_data = data["timeSeries"][x]["parameters"][i]["values"][0]

                # Rain- or snow-fall
                if (pacs_data > 0):
                    # print(data["timeSeries"][x]["validTime"])
                    return pacs_data

    return 0;

# ====================== End of Functions =====================

parse_command_line_options()
data = get_data()
pcat = get_type_of_downfall(data)

if print_category:
    print(categorys[pcat])
else:
    print(pcat)


