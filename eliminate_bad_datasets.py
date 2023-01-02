# Linaqruf

import argparse
import json
import os

# Define the argument parser
parser = argparse.ArgumentParser()

# Add arguments for the input directory, input JSON file, and output directory
parser.add_argument("--input_dir", required=True, help="Path to the directory containing the images")
parser.add_argument("--input_json", required=True, help="Path to the JSON file")
parser.add_argument("--bad_images_dir", required=True, help="Path to the bad images directory")
parser.add_argument("--threshold", required=False, help="Filtering threshold (move any image that <= this value away from the training dataset)", default=0.75)

# Parse the arguments
args = parser.parse_args()

# Load the JSON file
with open(args.input_json, "r") as f:
  results = json.load(f)

# Check if the output folder exists, if not create it
if not os.path.exists(args.bad_images_dir):
  os.makedirs(args.bad_images_dir)

# Iterate over the results
for result in results:
  # Get the filename and aesthetic score
  filename = result["filename"]
  aesthetic_score = result["aesthetic"]["aesthetic"]

  # Check if the aesthetic score is less than or equal to threshold
  if aesthetic_score <= args.threshold:
    # Move the file to the output folder
    os.rename(os.path.join(args.input_dir, filename), os.path.join(args.bad_images_dir, filename))
