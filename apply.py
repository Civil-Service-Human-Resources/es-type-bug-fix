from elasticsearch import Elasticsearch
import logging
import json
import os

client = Elasticsearch(os.getenv("ES_HOST"), basic_auth=(os.getenv("ES_USERNAME"), os.getenv("ES_PASSWORD")))
logging.basicConfig(filename='/logs/app.log', level=logging.INFO)

def apply():
    plan = json.load(open("/out/plan.json", "r"))

    for updated_course in plan:
        logging.info("Updating course with ID: " + updated_course["courseId"])
        client.update(index="courses", id=updated_course["courseId"], doc=updated_course["course"])
        logging.info("Update for course " + updated_course["courseId"] + " completed")

    logging.info("Apply completed")