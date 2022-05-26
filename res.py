import json
import glob

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

print('Passed: ', len(passed), 'Failed: ', len(failed))
print(failed)
