import json, requests, yaml
# import logging
from datetime import datetime
from dateutil import tz

# logging.basicConfig(level=logging.INFO)
# logging.info('Start to work!')

CONFIG_PATH = "./config/config.yaml"

# Template of the api call
TEMPLATE = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units={units}&exclude={exclude}&appid={api_key}"

# Load the configurations
with open(CONFIG_PATH, "r") as stream:
    config = yaml.safe_load(stream)

# Make the api call url according to configurations
api_call = TEMPLATE.format(
    lat=config["coordinates"]["latitude"],
    lon=config["coordinates"]["longitude"],
    units=config['weather']['units'],
    exclude=",".join(config["weather"]["exclude"]),
    api_key=config["weather"]["api_key"],
)

# Call the api
r = requests.get(api_call)
# logging.info('I have successfully made the API call.')

# Save the response and the timestamp of it
if r.status_code == 200:
    ts = r.json().get('current').get('dt')  # time stamp
    dt = (datetime.utcfromtimestamp(ts)  # local datetime
                  .replace(tzinfo=tz.tzutc())
                  .astimezone(tz.tzlocal())
                  .strftime('%Y-%m-%d %H:%M:%S'))
    with open('newest_ts', 'w') as f:
        f.write(str(ts))
    with open(f'data/data_{ts}.json', 'w') as f:
        json.dump(r.json(), f)
    # logging.info(f"I have saved the API response at {dt}.")
else:
    pass
    # logging.error(f'The status code is {r.status_code}.')
