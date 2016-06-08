"""
Create directories if not already present
"""
import os
from utils.logger import logger


# Create output directory in directory of input file
def create_dir(dir_name):
    current_dir = os.getcwd()
    output_dir_path = os.path.join(current_dir, dir_name)
    logger.info('Creating new directory here: {}'.format(output_dir_path))
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)


def create_output_dir(csv_file_dir, output_dir='output'):
    output_dir_path = os.path.join(csv_file_dir, output_dir)
    logger.info('Creating new directory here: {}'.format(output_dir_path))
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
