import db_generator as engine

# import instructions for managing each generation instance
import sqlite3
import random

"""Prepare the inventory for a fresh generation"""
conn = sqlite3.connect("bin_database.db")
c = conn.cursor()

c.execute("""DROP TABLE inventory""")
conn.commit()
# START FRESH
c.execute("""VACUUM""")
# VACUUM THE DATABASE

c.execute(
    """CREATE TABLE inventory(
        box TEXT,
        samplenum INTEGER PRIMARY KEY,
        disposaldate TEXT,
        usercheckin TEXT,
        userdisposal TEXT,
        comment TEXT
        )"""
)
conn.commit()


# BUILD THE DATABASE IN A WAY THAT GIVES UNIQUE TRAITS TO EACH OF THE SIX MAIN CATEGORIES

"""ALPHA BOXES:
 *** Tend to be more filled toward the lower numbers, decrease as you move toward 250
"""
engine.print_boxes(
    iteration_max=49,
    box_suffix_start=1,
    inv_prefix="ALPHA",
    upper_thres_low=20,
    upper_thres_high=55,
)
engine.print_boxes(
    iteration_max=49,
    box_suffix_start=51,
    inv_prefix="ALPHA",
    upper_thres_low=15,
    upper_thres_high=50,
)
engine.print_boxes(
    iteration_max=49,
    box_suffix_start=101,
    inv_prefix="ALPHA",
    upper_thres_low=10,
    upper_thres_high=40,
)
engine.print_boxes(
    iteration_max=49,
    box_suffix_start=151,
    inv_prefix="ALPHA",
    upper_thres_low=5,
    upper_thres_high=25,
)
engine.print_boxes(
    iteration_max=24,
    box_suffix_start=201,
    inv_prefix="ALPHA",
    upper_thres_low=2,
    upper_thres_high=10,
)
engine.print_boxes(
    iteration_max=24,
    box_suffix_start=226,
    inv_prefix="ALPHA",
    upper_thres_low=1,
    upper_thres_high=5,
)
#
#
#
engine.print_boxes(
    iteration_max=9,
    box_suffix_start=1,
    inv_prefix="A_TRANS",
    upper_thres_low=10,
    upper_thres_high=20,
)
engine.print_boxes(
    iteration_max=9,
    box_suffix_start=11,
    inv_prefix="A_TRANS",
    upper_thres_low=5,
    upper_thres_high=15,
)
#
#
#
"""BETA BOXES:
 *** Are evenly filled per box, but different subcategories of beta boxes tend to be grouped at the start and the end of the inventory, leaving a gap in the middle.
"""
engine.print_boxes(
    iteration_max=99,
    box_suffix_start=1,
    inv_prefix="BETA",
    upper_thres_low=30,
    upper_thres_high=50,
)
engine.print_boxes(
    iteration_max=49,
    box_suffix_start=200,
    inv_prefix="BETA",
    upper_thres_low=30,
    upper_thres_high=50,
)
#
#
#
engine.print_boxes(
    iteration_max=9,
    box_suffix_start=1,
    inv_prefix="B_TRANS",
    upper_thres_low=5,
    upper_thres_high=20,
)
engine.print_boxes(
    iteration_max=4,
    box_suffix_start=15,
    inv_prefix="B_TRANS",
    upper_thres_low=5,
    upper_thres_high=20,
)
#
#
#
"""GAMMA BOXES:
 *** Tend to be most filled toward the middle, with straggling samples being grouped to either side. (bell)
"""
engine.print_boxes(
    iteration_max=24,
    box_suffix_start=1,
    inv_prefix="GAMMA",
    upper_thres_low=1,
    upper_thres_high=5,
)
engine.print_boxes(
    iteration_max=24,
    box_suffix_start=25,
    inv_prefix="GAMMA",
    upper_thres_low=2,
    upper_thres_high=20,
)
engine.print_boxes(
    iteration_max=50,
    box_suffix_start=50,
    inv_prefix="GAMMA",
    upper_thres_low=10,
    upper_thres_high=30,
)
engine.print_boxes(
    iteration_max=50,
    box_suffix_start=101,
    inv_prefix="GAMMA",
    upper_thres_low=20,
    upper_thres_high=50,
)
engine.print_boxes(
    iteration_max=49,
    box_suffix_start=151,
    inv_prefix="GAMMA",
    upper_thres_low=10,
    upper_thres_high=30,
)
engine.print_boxes(
    iteration_max=24,
    box_suffix_start=201,
    inv_prefix="GAMMA",
    upper_thres_low=2,
    upper_thres_high=20,
)
engine.print_boxes(
    iteration_max=24,
    box_suffix_start=225,
    inv_prefix="GAMMA",
    upper_thres_low=1,
    upper_thres_high=5,
)
"""EPSILON BOXES:
 *** Tend to be most filled at the end since the inventory's end is physically closer, and less filled at the beginning.
"""
engine.print_boxes(
    iteration_max=24,
    box_suffix_start=101,
    inv_prefix="EPSILON",
    upper_thres_low=1,
    upper_thres_high=10,
)
engine.print_boxes(
    iteration_max=24,
    box_suffix_start=125,
    inv_prefix="EPSILON",
    upper_thres_low=1,
    upper_thres_high=50,
)
engine.print_boxes(
    iteration_max=49,
    box_suffix_start=151,
    inv_prefix="EPSILON",
    upper_thres_low=50,
    upper_thres_high=80,
)
engine.print_boxes(
    iteration_max=49,
    box_suffix_start=201,
    inv_prefix="EPSILON",
    upper_thres_low=75,
    upper_thres_high=100,
)
"""EPSILON BOXES:
 *** Are filled fully to capacity before moving on to the next box.
"""
engine.print_boxes(
    iteration_max=249,
    box_suffix_start=1,
    inv_prefix="ZETA",
    upper_thres_low=1,
    upper_thres_high=60,
)
