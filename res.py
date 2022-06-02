import json
import glob
import os

env_file = os.getenv('GITHUB_ENV')
results_name = glob.glob('/tmp/workspace/logs/*.json')
results = open(results_name[0], "rt")
res_obj = json.loads(results.read())
passed = []
failed = []

for test in res_obj["testCases"].keys():
    if res_obj["testCases"][test]["summaryResult"]["pass"]:
        passed.append(test)
    else:
        failed.append(res_obj["testCases"][test]["name"])

failed_tests = ", ".join(failed)

with open(env_file, "a") as myfile:
    myfile.write("NUM_PASSED="+ str(len(passed)))
    myfile.write("NUM_FAILED="+ str(len(failed)))
    myfile.write("TESTS_FAILED=" + failed_tests)
