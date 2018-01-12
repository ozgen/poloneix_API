import json


def writeFile(filename, data):
    with open(
            filename,
            'w'  # set file write mode
    ) as f:
        f.write(json.dumps(data));