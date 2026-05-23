from app.database import SessionLocal, engine, Base
from app import models

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Категории
cat1 = models.Category(name="Краны-манипуляторы")
cat2 = models.Category(name="Разгрузочные ленты")
cat3 = models.Category(name="Электрические тележки")
db.add_all([cat1, cat2, cat3])
db.commit()

# Товары
products = [
    models.Product(name="Кран ZOOMLION ZTC250", description="Грузоподъёмность 25 т, длина стрелы 28 м", price=12_500_000, image_url="https://via.placeholder.com/300?text=ZOOMLION+ZTC250", category_id=cat1.id),
    models.Product(name="Кран XCMG XCT25L5", description="25 т, 5-секционная стрела 42 м", price=13_200_000, image_url="https://via.placeholder.com/300?text=XCMG+XCT25L5", category_id=cat1.id),
    models.Product(name="Кран SANY STC250E", description="25 т, 4-секционная стрела 33 м", price=11_800_000, image_url="https://via.placeholder.com/300?text=SANY+STC250E", category_id=cat1.id),
    models.Product(name="Лента разгрузочная L=6 м", description="Ширина 600 мм, привод 3 кВт", price=450_000, image_url="https://via.placeholder.com/300?text=Lenta+6m", category_id=cat2.id),
    models.Product(name="Лента разгрузочная L=10 м", description="Ширина 800 мм, привод 5.5 кВт", price=780_000, image_url="https://via.placeholder.com/300?text=Lenta+10m", category_id=cat2.id),
    models.Product(name="Электрическая тележка EP ESL 202", description="2 т, вилы 1150 мм", price=320_000, image_url="https://via.placeholder.com/300?text=EP+ESL+202", category_id=cat3.id),
    models.Product(name="Штабелёр EP ES14", description="1400 кг, подъём 3 м", price=550_000, image_url="https://via.placeholder.com/300?text=EP+ES14", category_id=cat3.id),
    models.Product(name="Ричтрак EP RE 16", description="1.6 т, подъём 5.5 м", price=1_100_000, image_url="https://via.placeholder.com/300?text=EP+RE+16", category_id=cat3.id),
]
db.add_all(products)
db.commit()
db.close()
print("Добавлено 8 товаров в 3 категории")