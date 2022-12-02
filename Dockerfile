# Установка базового образа
FROM python:3.8


USER root

# Установка рабочей дериктории
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

# Копирование проекта
COPY . .

# Предустанавливаем команду pytest и отчёт
ENTRYPOINT ["pytest", "--alluredir", "allure-report"]
