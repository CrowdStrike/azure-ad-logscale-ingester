import azure.functions as func

from supplement import logscale


async def main(events: func.EventHubEvent):
    """Calling the send_log function for every new event"""
    for event in events:
        await logscale.send_log(event.get_body().decode('utf-8'))
