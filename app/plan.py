from elasticsearch import Elasticsearch
import logging
import json
import os

logging.basicConfig(filename='/logs/app.log', level=logging.INFO)

def plan():
    logging.info("Starting planning...")
    plan = []

    client = Elasticsearch(os.getenv("ES_HOST"), basic_auth=(os.getenv("ES_USERNAME"), os.getenv("ES_PASSWORD")))
    logging.info("Connected with ElasticSearch database.")

    types_from_classes = {
        "uk.gov.cslearning.catalogue.domain.module.LinkModule": "link",
        "uk.gov.cslearning.catalogue.domain.module.ELearningModule": "elearning",
        "uk.gov.cslearning.catalogue.domain.module.FaceToFaceModule": "face-to-face",
        "uk.gov.cslearning.catalogue.domain.module.FileModule": "file",
        "uk.gov.cslearning.catalogue.domain.module.VideoModule": "video"
    }

    logging.info("Retrieved all documents")
    documents = client.search(index="courses", size=10000)

    courses = documents["hits"]["hits"]
    logging.info(f"Retrieved {len(documents)} documents.")

    for course in courses:
        course_id = course["_id"]
        modules = course["_source"]["modules"]

        logging.info(f"Checking course with ID {course_id}...")
        
        modules_without_type = [module for module in modules if "type" not in module]

        logging.info(f"    Course has {len(modules_without_type)} modules without a type.")
        
        for module in modules_without_type:
            module["type"] = types_from_classes[module["_class"]]
            logging.info("    Added type to module with ID " + module["id"])

        if len(modules_without_type):
            plan.append({
                "courseId": course_id,
                "course": course["_source"]
            })
            logging.info("    Course with ID " + course_id + " added to plan")

    logging.info("Completed check for all courses. Creating plan file (plan.json)")
    with open("/out/plan.json", "w") as plan_file:
        plan_file.write(json.dumps(plan))

    logging.info(f"Planning completed. Plan contains updates for {len(plan)} courses.")
        
