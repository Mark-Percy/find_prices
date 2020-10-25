import requests
import logging
import time

def main(id):
    print(f"Thread {id}: starting")
    logging.info(f"Thread {id}: starting")
    time.sleep(2)
    logging.info(f"Thread {id}: Finishing")
    print(f"Thread {id}: Finishing")
