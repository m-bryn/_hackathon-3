# _hackathon-3

<p align="center">



<img src="https://img.shields.io/badge/-Python-488BBE.svg?logo=python&logoColor=FFE873&logoWidth=20&style=flat&textColor=white">

<img src="https://img.shields.io/github/languages/top/m-bryn/_hackathon-3.svg?color=488BBE&style=flat">

<img src="https://img.shields.io/github/issues/m-bryn/_hackathon-3.svg?color=488BBE&style=flat">

<img src="https://img.shields.io/github/stars/m-bryn/_hackathon-3.svg?color=488BBE&style=flat">

</p>

## Прогноз спроса и планирование рабочих смен


__Прогноз__ 

Работаем со столбцами 'date', достанем столбец 'hour', 'weekday' в таблице. Делаем предсказания для каждого отдельного дня недели с разбивкой на зоны. Наилучший прогноз получается, если тренировать модель на столбце 'hour'. Для прогнозирования и поиска оптимального решения (по соотношению кол-ва партнеров к кол-ву заказов как целевой переменной) используем *LGBMRegressor* 
    
Итог: получаем файлы pickles с предиктами
>Файл с кодом: [prediction.ipynb](https://github.com/m-bryn/_hackathon-3/blob/main/simplex_method.ipynb)

<br>

__Замощение сменами__

Здесь мы решаем оптимизационную задачу, используя симплекс-метод

![Замощение сменами для региона 0 (Понедельник)](https://github.com/m-bryn/_hackathon-3/blob/main/imagine.png)
Итог: получаем файлы pickles с замощением для всех дней недели - всех регионов
>Файл с кодом: [simplex_method.ipynb](https://github.com/m-bryn/_hackathon-3/blob/main/simplex_method.ipynb)
