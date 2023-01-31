import os
import requests


header_api_token = "bearer" + os.environ["LogScaleIngestToken"]
logscale_header = {'content-type': 'application/json', 'Authorization': header_api_token}


async def send_log(log_body):
    """This funciton sends the logs via HEC to LogScale."""
    return requests.post(os.environ["LogScaleURL"], headers = logscale_header, data = log_body)
