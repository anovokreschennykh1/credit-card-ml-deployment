# ML Implementation - AB in "Credit Card Default Prediction Service"
Разработка и внедрение сервиса прогнозирования дефолта по кредитным картам с контейнеризацией и A/B-тестированием

## Цель проекта
Разработать и внедрить в production-like-среду сервис машинного обучения для прогнозирования дефолта по кредитным картам, который охватывает полный цикл от сохранения модели до организации A/B-тестирования.

## Структура проекта
```text
.
├── app/
│   ├── __init__.py
│   └── api.py                  # Flask API: эндпоинты /predict и /health
├── models/
│   ├── _model_v1.pkl            # модель для контрольной группы A: GradientBoostingClassifier
│   └── _model_v2.pkl            # модель для тестовой группы B: LogisticRegression
├── notebooks/
│   └── Model_selection.ipynb    # обучение, сравнение моделей и сохранение в pickle
├── screenshots/                # скриншоты тестовых запросов и ответов API
├── Dockerfile                  # сборка Docker-образа
├── requirements.txt            # зависимости проекта
└── README.md                   # описание проекта и инструкция по запуску
```

## Описание данных
Датасет [Default of Credit Card Clients Dataset](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset) содержит информацию о клиентах кредитной карты на Тайване с таргетом default.payment.next.month (дефолт в следующем месяце). Включает демографические данные, историю платежей, суммы счетов.

## Инструкция по запуску
### Локально
1. Создать виртуальное окружение
python -m venv venv
2. Активировать окружение
source venv/bin/activate (Mac OS)
venv\Scripts\activate (Windows)
3. Установить зависимости
pip install -r requirements.txt
4. Запустить скрипт с Flask сервисом
python app/api.py
5. В отдельном окне терминала для запущенного сервиса на хосте 5000 можно дать команды

5.1) Проверить состояние сервиса
```text
curl -X GET http://localhost:5000/health
```
5.2) Дать предсказание дефолта по входным характеристикам
```text
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{
  "features": [
    {
      "LIMIT_BAL": 50000,
      "SEX": 2,
      "EDUCATION": 2,
      "MARRIAGE": 1,
      "AGE": 37,
      "PAY_0": 0,
      "PAY_2": 0,
      "PAY_3": 0,
      "PAY_4": 0,
      "PAY_5": 0,
      "PAY_6": 0,
      "BILL_AMT1": 46990,
      "BILL_AMT2": 48233,
      "BILL_AMT3": 49291,
      "BILL_AMT4": 28314,
      "BILL_AMT5": 28959,
      "BILL_AMT6": 29547,
      "PAY_AMT1": 2000,
      "PAY_AMT2": 2019,
      "PAY_AMT3": 1200,
      "PAY_AMT4": 1100,
      "PAY_AMT5": 1069,
      "PAY_AMT6": 1000
    }
  ]
}'
```
