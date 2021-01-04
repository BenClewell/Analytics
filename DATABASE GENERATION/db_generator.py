import sqlite3
import random
from datetime import datetime

# Create a blueprint on how each inventory category will populate the mock database

conn = sqlite3.connect("bin_database.db")
c = conn.cursor()
# information for database connection


def print_boxes(
    iteration_max,
    box_suffix_start,
    inv_prefix,
    upper_thres_low,
    upper_thres_high,
):
    """
    iteration_max: how far from the starting bin to iterate on the loop
    box_suffix_start: the bin number to begin iterating at
    inv_prefix: str: the string to put in front of the box suffix (int)
    upper_thres_low, upper_thres_high: the lower and upper bounds for how many samples will be in a bin.
    """

    # GENERATE A BRAND NEW DATABASE IN PLACE OF THE OLD ONE
    d = datetime.now()
    only_date = d.date()
    # insert date-time for disposal instances

    counter = 0
    # how many times looped
    boxnum = box_suffix_start
    # suffix of the box
    while counter <= iteration_max:
        # while loop times are less than the maximum boxes
        propagate_info = str(inv_prefix + str(boxnum))
        # string for what to put into the SQL base
        # the first part of the string is the str prefix

        list_upper_thres = random.randint(upper_thres_low, upper_thres_high)
        list_lower_thres = 1

        random_list = []
        for i in range(list_lower_thres, list_upper_thres):
            n = random.randint(1000000000, 9999999999)
            random_list.append(n)
        print(random_list)
        # the above block generates a list of entries

        for i in random_list:
            boxlist = [
                propagate_info,
                i,
                "DEMO_USER_1",
                propagate_info,
                "DEMO_USER_1",
            ]

            dispose_chance = random.randint(1, 25)

            boxlist_dispose = [
                propagate_info,
                i,
                "DEMO_USER_1",
                propagate_info,
                "DEMO_USER_1",
                only_date,
            ]
            # these are the values to insert into the database.

            # for each sample, give it a small chance to receive disposal status
            # this gives a stochastic variety for if sample disposed or not
            if dispose_chance != 1:
                c.executemany(
                    "INSERT INTO inventory (box, samplenum, usercheckin) VALUES (?,?,?) ON CONFLICT (samplenum) DO UPDATE SET box=(?), usercheckin= (?)",
                    (boxlist,),
                )
            else:
                c.executemany(
                    "INSERT INTO inventory (box, samplenum, usercheckin, disposaldate) VALUES (?,?,?,?) ON CONFLICT (samplenum) DO UPDATE SET box=(?), usercheckin= (?)",
                    (boxlist_dispose,),
                )
            print(boxlist)
            conn.commit()

        boxnum += 1
        # bump suffix of box up when finished propagating samples
        counter += 1
        # increase the counter
