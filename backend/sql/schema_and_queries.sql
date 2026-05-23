-- Создание таблиц PostgreSQL
CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR(120) NOT NULL UNIQUE
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  description TEXT NOT NULL,
  price NUMERIC(12,2) NOT NULL,
  stock INT NOT NULL DEFAULT 0,
  category_id INT NOT NULL REFERENCES categories(id)
);

CREATE TABLE inquiries (
  id SERIAL PRIMARY KEY,
  customer_name VARCHAR(120) NOT NULL,
  phone VARCHAR(32) NOT NULL,
  message TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Наполнение тестовыми данными
INSERT INTO categories (name) VALUES
('Краны-манипуляторы'),
('Ленты для разгрузки'),
('Подъем и перевозка поддонов');

INSERT INTO products (name, description, price, stock, category_id) VALUES
('XCMG 6T', 'Кран манипулятор 6 тонн', 2200000.00, 3, 1),
('AS Belt 1200', 'Лента для разгрузки грузовиков', 320000.00, 12, 2),
('LiftPro 2.5T', 'Машинка для подъема и перевозки поддонов', 180000.00, 8, 3);

INSERT INTO inquiries (customer_name, phone, message)
VALUES ('Иван Петров', '+7 900 123-45-67', 'Нужна консультация по крану XCMG 6T');

-- 5+ проверочных запросов
-- 1) SELECT с условием
SELECT * FROM products WHERE price > 300000;

-- 2) INSERT
INSERT INTO inquiries (customer_name, phone, message)
VALUES ('ООО Логистик', '+7 901 000-00-00', 'Запрос КП на 2 единицы LiftPro');

-- 3) UPDATE
UPDATE products SET stock = stock - 1 WHERE id = 1;

-- 4) DELETE
DELETE FROM inquiries WHERE customer_name = 'ООО Логистик';

-- 5) SELECT с JOIN
SELECT p.id, p.name, p.price, c.name AS category
FROM products p
JOIN categories c ON c.id = p.category_id
ORDER BY p.price DESC;

-- 6) Дополнительно: агрегат
SELECT c.name, COUNT(p.id) AS products_count
FROM categories c
LEFT JOIN products p ON p.category_id = c.id
GROUP BY c.name;
