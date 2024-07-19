## Описание
# Pyspark_DataFrame

"Тестовое задание: В PySpark приложении датафреймами(pyspark.sql.DataFrame) заданы продукты, категории и их связи. Каждому продукту может соответствовать несколько категорий или ни одной. А каждой категории может соответствовать несколько продуктов или ни одного. Напишите метод на PySpark, который в одном датафрейме вернет все пары «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий."

## Стек технологий

- Python
- Pyspark

## Локальный запуск кода

0. #### подготовка к работе.
"Обратите внимание для запуска у вас должен быть установлены следующие пакеты на примере менеджера brew. Введите следующие команды в терминале: 
```
brew install openjdk
brew install apache-spark

```
Далее в терминале введите команду:
```
nano ~/.zshrc
```
В открывшемся файле вставьте следующие строки кода:
```
export JAVA_HOME=$(brew --prefix openjdk)
export SPARK_HOME=$(brew --prefix apache-spark)/libexec
export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$PATH
```
Сохраните изменения и закройте редактор (Ctrl+X, затем Y и Enter)
"

1. #### Склонируйте репозиторий:
```
git clone git@github.com:aleksei-astapoff/pyspark_data_frame.git
```

2. #### Создайте и активируйте виртуальное окружение если его нет:
Команда для установки виртуального окружения на Mac или Linux:
```
python3 -m venv env

source venv/bin/activate
```

Команда для установки виртуального окружения на Windows:
```
python -m venv venv

source venv/Scripts/activate
```

3. #### Установите зависимости:
В папке где находится файл requirements.txt выполните команду:
```
pip install -r requirements.txt
```

4. #### Запустите исполняемый файл pyspark_data_frame.py
Запуск  через IDE или в терминале:
```
python3 pyspark_data_frame.py
```