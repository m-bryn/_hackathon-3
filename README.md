# _hackathon-3

<p align="center">

<img src="https://img.shields.io/badge/-Python-488BBE.svg?logo=python&logoColor=FFE873&logoWidth=20&style=flat&textColor=white">

<img src="https://img.shields.io/github/languages/top/m-bryn/_hackathon-3.svg?color=488BBE&style=flat">

<img src="https://img.shields.io/github/issues/m-bryn/_hackathon-3.svg?color=488BBE&style=flat">

<img src="https://img.shields.io/github/stars/m-bryn/_hackathon-3.svg?color=488BBE&style=flat">

</p>

## Demand Forecasting and Shift Scheduling


__Forecasting__

We work with the 'date' column and extract the 'hour' and 'weekday' columns from the table. Predictions are made for each specific day of the week, broken down by zone. The best forecast is achieved by training the model using the 'hour' column. We use *LGBMRegressor* to generate forecasts and find the optimal solution (using the ratio of partners to orders as the target variable).

Result: pickle files containing predictions.
>Code file: [prediction.ipynb](https://github.com/m-bryn/_hackathon-3/blob/main/simplex_method.ipynb)

<br>

__Shift Tiling__

Here, we solve an optimization problem using the simplex method.

![Shift tiling for region 0 (Monday)](https://github.com/m-bryn/_hackathon-3/blob/main/imagine.png)
<br>
Result: pickle files containing the tiling configurations for all days of the week and all regions.
>Code file: [simplex_method.ipynb](https://github.com/m-bryn/_hackathon-3/blob/main/simplex_method.ipynb)
