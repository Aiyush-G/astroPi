# -*- coding: utf-8 -*-
#      Life On Earth     #
#        PiHeads         #
#  Aiyush, Ibrahim, Alex #

from pathlib import Path
from logzero import logger, logfile
from sense_hat import SenseHat
from picamera import PiCamera
from orbit import ISS
from time import sleep
from datetime import datetime, timedelta
import csv
import os
from time import sleep
from skyfield.api import load
import sys

# Set the base folder
baseFolder = Path(__file__).parent.resolve()
# Set a logfile name
logfile(baseFolder/"events.log")

ephemeris = load("de421.bsp")
timescale = load.timescale()

while True:
    t = timescale.now()
    if ISS.at(t).is_sunlit(ephemeris):
        # ISS is in sunlight, suitable for taking pictures
        logger.info("in sunlight")

        # Record the start time
        startTime = datetime.now()

        def create_csv_file(data_file):
            # Create a new CSV and add a header row
            with open(data_file, 'w') as f:
                writer = csv.writer(f)
                header = ("Counter", "Date/time", "Latitude", "Longitude")
                writer.writerow(header)

        def add_csv_data(data_file, data):
            # Add a row of data to the CSV
            with open(data_file, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(data)

        def convert(angle):
            # Convert a 'skyfield' angle to an EXIF-appropriate represention (rationals)
            sign, degrees, minutes, seconds = angle.signed_dms()
            exif_angle = f'{degrees:.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'

            # Return a tuple containing a boolean and the converted angle,
            # Boolean indicates whether angle is negative
            return sign < 0, exif_angle

        def capture(camera, image):
            # Use the camera to capture an image wih location data
            location = ISS.coordinates()

            # Convert the latitude and longitude to EXIF-appropriate representations
            south, exif_latitude = convert(location.latitude)
            west, exif_longitude = convert(location.longitude)

            # Set the EXIF tags specifying the current location
            camera.exif_tags['GPS.GPSLatitude'] = exif_latitude
            camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
            camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
            camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"

            # Capture the image
            camera.capture(image)

        # Set up Sense Hat
        sense = SenseHat()

        # Set up camera
        cam = PiCamera()
        cam.resolution = (2592,1944)

        folder = "data"
        isFile = os.path.isdir(folder)
        subPath = f"{baseFolder}/{folder}"

        # Initialise the CSV file
        data_file = baseFolder/"data.csv"
        create_csv_file(data_file)

        if not isFile:
            # Folder Doesn't exist - create folder
            try:
                os.mkdir(subPath)
            except OSError as e:
                logger.error(f'{e.__class__.__name__}: {e}')

        # Initialise the photo counter
        counter = 1
        # Record the current time
        currentTime = datetime.now()

        # Run a loop for (almost) three hours
        while (currentTime < startTime + timedelta(minutes=178)):
            try:
                # Get coordinates of location on Earth below the ISS
                location = ISS.coordinates()
                # Save the data to the file
                data = (
                    counter,
                    datetime.now(),
                    location.latitude.degrees,
                    location.longitude.degrees
                )
                add_csv_data(data_file, data)
                # Capture image
                image_file = f"{subPath}/photo_{counter:03d}.jpg"
                capture(cam, image_file)
                # Log event
                logger.info(f"iteration {counter}")
                counter += 1
                sleep(30)
                # Update the current time
                currentTime = datetime.now()
            except Exception as e:
                logger.error(f'{e.__class__.__name__}: {e}')
        # Exits as otherwise it will run the whole "while True" loop again
        sys.exit()
    else:
        # ISS in darkness, photos are not useful until in sunlight
        logger.info("in darkness")      
    sleep(30)
