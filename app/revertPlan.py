from elasticsearch import Elasticsearch
import logging
import json
import os

logging.basicConfig(filename='/logs/app.log', level=logging.INFO)

def revertPlan():

    plan = json.load(open("/out/plan.json", "r"))

    for updated_course in plan:
        logging.info("Removing types from course with ID " + updated_course["course"]["id"])
        modules = updated_course["course"]["modules"]

        for module in modules:
            logging.info("    Removing type from module with ID " + module["id"])
            module.pop("type")

    with open("/out/revert-plan.json", "w") as revert_plan_file:
        revert_plan_file.write(json.dumps(plan))