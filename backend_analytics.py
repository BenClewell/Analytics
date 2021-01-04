import numpy as np
import pandas as pd
import sqlite3

import plotly
import plotly.graph_objs as go

import main


con = sqlite3.connect("DATABASE GENERATION/bin_database.db")
# connect to the demo database
inv = pd.read_sql_query("SELECT * FROM inventory", con)
# turn the inventory into a pandas dataframe
inv_active = inv[inv["disposaldate"].isnull()]
# filter out all samples that have a disposal date
lcd_total_read = len(inv_active)
lcd_inv_disposed = len(inv) - len(inv_active)
# for the main program, assign values for active and disposed samples in the inventory


class Operations:
    """create a class for each inventory category to instance from"""

    def __init__(self, keyword):
        self.keyword = keyword
        # specify the category of inventory you're working with.
        self.filter_TYPE = inv_active[
            inv_active["box"].str.lower().str.contains(self.keyword)
        ]
        self.filter_len = len(
            inv_active[
                inv_active["box"].str.lower().str.contains(self.keyword)
            ]
        )
        self.filter_boxfill = self.filter_TYPE["box"].value_counts()
        self.boxfill_mean = int(np.mean(self.filter_boxfill))
        self.filter_in_use = self.filter_TYPE["box"].nunique()

    def create_graph(self, barcolor, linecolor):
        #play a randomized sound when generating
        if self.keyword != "":
            # new function, perform value counts on filter_TYPE
            # establishes the value counts
            inv_vcounts = pd.DataFrame(
                data=[self.filter_TYPE["box"].value_counts()], index=None
            )
            inv_vcounts_swap = inv_vcounts.transpose().reset_index()
            # transpose and reset the index
            inv_vcounts_swap.rename(
                columns={"index": "box number", "box": "fill amount"},
                inplace=True,
            )
            # renaming parameters
            nums_only = pd.DataFrame(
                data=(
                    inv_vcounts_swap["box number"].str.extract(
                        "(\d+)", expand=False
                    )
                )
            )
            # stripping the text away from the associated integers

            nums_only.rename(
                columns={"box number": "boxnum_only"}, inplace=True
            )

            comparison = pd.concat([inv_vcounts_swap, nums_only], axis=1)

            ready_to_plot = comparison.sort_values("boxnum_only")

            trace1 = {
                "x": ready_to_plot["boxnum_only"],
                "y": ready_to_plot["fill amount"],
                "type": "bar",
                "marker_color": barcolor,
                "marker_line_color": linecolor,
                "marker_line_width": 1.5,
                "opacity": 0.6,
            }

            data = [trace1]
            plotly.offline.plot(
                {
                    "data": data,
                    "layout": go.Layout(
                        hovermode="x",
                        template="plotly_dark",
                        title_text=(
                            self.keyword.title() + ": Samples per Box"
                        ),
                        title_x=0.1,
                        xaxis_title=(self.keyword.title() + " Boxes"),
                        yaxis_title="Number of Samples",
                        font=dict(family="Android 101", size=12),
                    ),
                }
            )
        else:
            main.HomeScreen.show_message(
                "",
                "Cannot Provide Visualization",
                """You have visualization mode enabled,
                but combined inventory categories cannot generate a visualization.""",
            )


# Assign an instance for each category in the demo inventory

AlphaCalc = Operations("alpha")
AlphaTransCalc = Operations("a_trans")
BetaCalc = Operations("beta")
BetaTransCalc = Operations("b_trans")
GammaCalc = Operations("gamma")
EpsilonCalc = Operations("epsilon")
ZetaCalc = Operations("zeta")
TotalCalc = Operations("")