# _hackathon-3

<p align="center">



<img src="https://img.shields.io/badge/-Python-488BBE.svg?logo=python&logoColor=FFE873&logoWidth=20&style=flat&textColor=white">

<img src="https://img.shields.io/github/languages/top/m-bryn/_hackathon-3.svg?&style=flat">

<img src="https://img.shields.io/github/issues/m-bryn/_hackathon-3.svg?&style=flat">

<img src="https://img.shields.io/github/stars/m-bryn/_hackathon-3.svg?style=flat">

</p>

## Прогноз спроса и планирование рабочих смен


__Задача два__ 

Работаем со столбцами 'date', достанем столбец 'hour', 'weekday' в таблице. Наилучший прогноз получается, если тренировать модель на столбце 'hour'. Для прогнозирования и поиска оптимального решения (по соотношению кол-ва партнеров к кол-ву заказов как целевой переменной) используем     
    LGBMRegressor 
    
Итог: [prediction.ipynb](https://github.com/m-bryn/_hackathon-3/blob/main/prediction.ipynb)
>Файл с кодом: prediction.ipynb



__Задача три__

Оптимизационная задача, использование симплекс-метода

![Замощение сменами для региона 0 (Понедельник)](https://github.com/m-bryn/_hackathon-3/raw/main/imagine.png)
Итог: [simplex_method.ipynb](https://github.com/m-bryn/_hackathon-3/blob/main/simplex_method.ipynb)
>Файл с кодом: simplex_method.ipynb
