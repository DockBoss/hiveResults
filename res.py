import json

results = open("result.json", "rt")
res_obj = json.loads(results.read())
passed = []
failed = []

for test in res_obj["testCases"].keys():
    if res_obj["testCases"][test]["summaryResult"]["pass"]:
        passed.append(test)
    else:
        failed.append(test)

print('Passed: ', len(passed), 'Failed: ', len(failed))
print(failed)
