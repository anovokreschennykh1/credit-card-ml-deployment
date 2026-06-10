# ML Implementation - AB in "Credit Card Default Prediction Service"
Разработка и внедрение сервиса прогнозирования дефолта по кредитным картам с контейнеризацией и A/B-тестированием
## Контекст

## Цель
Разработать и внедрить в production-like-среду сервис машинного обучения для прогнозирования дефолта по кредитным картам, который охватывает полный цикл от сохранения модели до организации A/B-тестирования.

## Структура проекта
|app\
|--__init__.py
|--api.py
|models\
|--_model_v1.pkl # модель в группе A
|--_model_v2.pkl # модель в группе B
|notebooks\
|--Model_selection.ipynb # обучение и запись моделей в pickle
|screenshots\ # папка с тестами: скринами примера запросов и ответов
|Dockerfile # сборка докер образа
|requirements.txt # файл с зависимостями
|README.md

## Описание данных
Датасет [](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)
