# conda create -n hydrate python=3.6.4 anaconda

import requests


def main():
	r=requests.get('http://api.wunderground.com/api/6d94041a38d2a909/conditions/q/us/02472.json')
	if r.status_code==200:
		w = r.json()
		temp = w["current_observation"]["temp_f"]
		hum = w["current_observation"]["relative_humidity"]
		print("wu says: temperature:{0}  humidity:{1}".format(temp,hum))
	else:
		print("error! code={0}".format(r.status_code))


if __name__ == "__main__":
    # execute only if run as a script
    main()