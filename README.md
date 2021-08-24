# GitHubActionsTest

https://claude9493.com/GitHubActionsTest/

With GitHub Actions, this repository could regularly request weather information from [OpenWeather](https://openweathermap.org/) API, and do some simple analyze. The focus point is the usage of GitHub Actions.

## GitHub Actions

The workflow `CI` has following steps:
- Open a Ubuntu environment.
- Pull the repository into the environment.
- Install dependencies.
- Run the `get_weather.py` script to get weather information.
  - The obtained response is stored in a json file named by the current time stamp.
- Run the `vis_weather.ipynb` notebook and generate `index.html`.
  - Actually, the notebook is executed first, then a new notebook is generated and replaces the old one. After that, the html output is exported.
- Move previous weather information json file into the `historical` folder.
- Commit and push all above changes to repository.

The workflow is called every 30 minutes. See [this link](https://crontab.guru/every-1-hour) to learn more about the [cron job](https://en.wikipedia.org/wiki/Cron).

## Anywhere else we can use GitHub Actions

- Regularly data scraping
- Static page auto-generate and depoly (hugo), see [claude9493/homepage](https://github.com/claude9493/homepage)
- Freely use the GitHub server?
- Keep commit record everyday...
- ......
