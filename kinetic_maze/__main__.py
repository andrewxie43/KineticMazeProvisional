import os
import logging
import argparse
from . import KineticMaze, logger

if __name__ == "__main__":
    logging.basicConfig(filename='../runlog.log', filemode='w', format="%(levelname)-7s | %(asctime)-23s | %(name)-8s | %(message)s") #not writing to log?
    parser = argparse.ArgumentParser(description="Run the kinetic maze.")

    #parser.add_argument("tracker_path",
                        #help="path to the `trackhands` executable")
    #parser.add_argument("tracker_working_directory",
                        #help="path to the working directory containing the data for trackhands")

    parser.add_argument("-v", "--verbose", action="store_true",
                        help="set logging to DEBUG")

    args = parser.parse_args()
    if args.verbose:
        logger.setLevel("INFO")

    km = KineticMaze()
    km.hardware_setup()
    km.run()
