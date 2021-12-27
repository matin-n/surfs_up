# Surfs Up

## Project Overview
### Purpose
The purpose of this project is to analyze Oahu's temperature data for June and December to determine if a surf and ice cream shop is sustainable year-round. W. Avy and the investors want to open a surf shop and have requested information about temperature trends. Additionally, I have created an API to allow W. Avy and the board of directors to access the analysis easily. The endpoints show the Precipitation, Stations, Monthly Temperature, and Statistics.


## Results
### Summary Statistics
As expected, the December temperatures is lower when compared to June as the Winter season has colder climate conditions and the Summer season has warmer climate conditions.

#### Summary Statistics for June

|       |       tobs |
|:------|-----------:|
| count | 1700       |
| mean  |   74.9441  |
| std   |    3.25742 |
| min   |   64       |
| 25%   |   73       |
| 50%   |   75       |
| 75%   |   77       |
| max   |   85       |

- Standard deviation: 3.26
- Minimum temperature: 64 °F
- Average temperature: 75 °F
- Maximum temperature: 85 °F

#### Summary Statistics for December

|       |       tobs |
|:------|-----------:|
| count | 1517       |
| mean  |   71.0415  |
| std   |    3.74592 |
| min   |   56       |
| 25%   |   69       |
| 50%   |   71       |
| 75%   |   74       |
| max   |   83       |

- Standard deviation: 3.75
- Minimum temperature: 56 °F
- Average temperature: 71 °F
- Maximum temperature: 83 °F

### Climate Analysis API
#### Available Routes
```
/api/v1.0/precipitation
/api/v1.0/stations
/api/v1.0/tobs
/api/v1.0/temp/{start}/{end}
```

## Summary
- Temperature
  - The minimum temperature in December is lower when compared to June
  - The average temperature in June is higher when compared to December
  - The maximum temperature in June is slightly high when compared to December

Additionally, a query to determine the temperature between a range of dates could provide additional insight. For example, a function like this would output the results between two specified dates:

```python
def calc_temps(start_date, end_date):

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    temperature_results = (
        session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs),
        )
            .filter(Measurement.date >= start_date)
            .filter(Measurement.date <= end_date)
            .all()
    )

    # return minimum, average, and max temperature
    return temperature_results[0]
```

It would be interesting to analyze various dates daily, monthly, yearly, or by seasons and conduct further analysis. Then, a plot could be created to visualize, illustrate and determine any relationships within the data.

  ## Resources
  - Data Source: [`hawaii.sqlite`](https://github.com/matin-n/surfs_up/blob/main/hawaii.sqlite)
  - Source Code: [`climate_analysis.ipynb`](https://github.com/matin-n/surfs_up/blob/main/climate_analysis.ipynb), [`SurfsUp_Challenge.ipynb`](https://github.com/matin-n/surfs_up/blob/main/SurfsUp_Challenge.ipynb)
  - Software: [`Python 3.6.10`](https://www.python.org/downloads/release/python-3610/), [`Jupyter Notebook`](https://jupyter.org/), [`JetBrains DataSpell`](https://www.jetbrains.com/dataspell/)
  - Libraries: [`Pandas`](https://pandas.pydata.org/), [`Matplotlib`](https://matplotlib.org/), [`SQLAlchemy`](https://www.sqlalchemy.org/), [`Flask`](https://github.com/pallets/flask), [`SQLite`](https://sqlite.org/index.html)
