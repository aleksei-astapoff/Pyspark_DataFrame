from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# Создание SparkSession
spark = SparkSession.builder.appName("ProductCategory").getOrCreate()


# Пример данных
products_data = [("p1", "Product1"), ("p2", "Product2"), ("p3", "Product3")]
categories_data = [("c1", "Category1"), ("c2", "Category2")]
product_category_data = [("p1", "c1"), ("p1", "c2"), ("p2", "c1")]

# Создание DataFrame
products_df = spark.createDataFrame(
    products_data, ["product_id", "product_name"]
    )
categories_df = spark.createDataFrame(
    categories_data, ["category_id", "category_name"]
    )
product_category_df = spark.createDataFrame(
    product_category_data, ["product_id", "category_id"]
    )

# Объединение для получения пар "Имя продукта – Имя категории"
product_category_pairs = product_category_df.join(
    products_df, "product_id"
    ).join(categories_df, "category_id").select(
        "product_name", "category_name"
        )

# Выводим результат
print("Имя продукта – Имя категории:")
product_category_pairs.show()

# Объединение для нахождения продуктов без категорий
products_without_categories = products_df.join(
    product_category_df, "product_id", "left"
    ).filter(col("category_id").isNull()).select("product_name")

# Добавляем фиктивное значение для категории (например, None)
products_without_categories = products_without_categories.withColumn(
    "category_name", lit(None)
    )

# Выводим результат
print("Имя продукта – Нет категории:")
products_without_categories.show()

# Объединяем результаты в один датафрейм
result_df = product_category_pairs.union(products_without_categories)

# Выводим итоговый результат
print("Объединение для получения пар:")
result_df.show()

# Закрываем SparkSession
spark.stop()
