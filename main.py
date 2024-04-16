import sys
import plan
import apply
import revertPlan

action = sys.argv[1]

if action == "plan":
    plan.plan()

if action == "apply":
    apply.apply("plan.json")

if action == "revert-plan":
    revertPlan.revertPlan()

if action == "revert-apply":
    apply.apply("revert-plan.json")