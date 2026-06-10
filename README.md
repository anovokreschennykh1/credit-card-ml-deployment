# ML Implementation - AB in "Credit Card Default Prediction Service"
Разработка и внедрение сервиса прогнозирования дефолта по кредитным картам с контейнеризацией и A/B-тестированием
## Контекст

## Цель
Разработать и внедрить в production-like-среду сервис машинного обучения для прогнозирования дефолта по кредитным картам, который охватывает полный цикл от сохранения модели до организации A/B-тестирования.

## Структура проекта
├── app/
│   ├── __init__.py
│   └── api.py                  # Flask API: эндпоинты /predict и /health
├── models/
│   ├── _model_v1.pkl            # модель для контрольной группы A
│   └── _model_v2.pkl            # модель для тестовой группы B
├── notebooks/
│   └── Model_selection.ipynb    # обучение, сравнение моделей и сохранение в pickle
├── screenshots/                # скриншоты тестовых запросов и ответов API
├── Dockerfile                  # сборка Docker-образа
├── requirements.txt            # зависимости проекта
└── README.md                   # описание проекта и инструкция по запуску

## Описание данных
Датасет [Default of Credit Card Clients Dataset](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)
