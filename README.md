# _hackathon-3
## Прогноз спроса и планирование рабочих смен
---
__Задача два__ 

Работаем со столбцами 'date', достанем столбец 'hour', 'weekday' в таблице. Наилучший прогноз получается, если тренировать модель на столбце 'hour'. Для прогнозирования и поиска оптимального решения (по соотношению кол-ва партнеров к кол-ву заказов как целевой переменной) используем     
    LGBMRegressor 
    
Итог: [prediction.ipynb](https://github.com/m-bryn/_hackathon-3/blob/main/prediction.ipynb)
>Файл с кодом: prediction.ipynb



__Задача три__

Оптимизационная задача, использование симплекс-метода

Итог: ![Замощение сменами для региона 0 (Понедельник)](https://github.com/m-bryn/_hackathon-3/raw/main/imagine.png)

[simplex_method.ipynb]
(https://github.com/m-bryn/_hackathon-3/blob/main/simplex_method.ipynb)
>Файл с кодом:simplex_method.ipynb
