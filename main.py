import sys
import plan
import apply

action = sys.argv[1]

if action == "plan":
    plan.plan()

if action == "apply":
    apply.apply()