import json
import pingparsing
import csv
import datetime
import os.path

date_obj = datetime.datetime.now()
date_day = date_obj.date().strftime("%m/%d/%y")
date_hour = date_obj.time().strftime("%H:%M")

ping_parser = pingparsing.PingParsing()
transmitter = pingparsing.PingTransmitter()
transmitter.destination = "google.com"
transmitter.count = 100
result = transmitter.ping()
ping_stats = json.dumps(ping_parser.parse(result).as_dict())
ping_stats_formatted = json.loads(ping_stats)

ping_stats_formatted['date'] = date_day
ping_stats_formatted['time'] = date_hour

file_exists = os.path.isfile('starlink_stats.csv')

with open('starlink_stats.csv', mode='a') as csv_file:
    fieldnames = [
        "date",
        "time",
        "destination",
        "packet_transmit",
        "packet_receive",
        "packet_loss_count",
        "packet_loss_rate",
        "rtt_min",
        "rtt_avg",
        "rtt_max",
        "rtt_mdev",
        "packet_duplicate_count",
        "packet_duplicate_rate",
                  ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    if not file_exists:
        writer.writeheader()
    writer.writerow(ping_stats_formatted)
