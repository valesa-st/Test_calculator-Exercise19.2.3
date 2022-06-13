# Тестовые данные для позитивных тестов
positive_data_division = [
    (6, 2, 3),
    (30, 15, 2),
    (90, -10, -9),
    (13.5, 4.5, 3)
]

positive_data_multiply = [
    (7, 2, 14),
    (21, 10, 210),
    (15, -4, -60),
    (2.25, 2.25, 5.0625)
]

positive_data_subtraction = [
    (13, 3, 10),
    (50, 40, 10),
    (15, -5, 20),
    (11, 3.3, 7.7)
]

positive_data_adding = [
    (14, 6, 20),
    (27, 13, 40),
    (-34, -6, -40),
    (8, 1.5, 9.5)
]

# Тестовые данные для негативных тестов
negative_data_division = [
    (ZeroDivisionError, 0, 10),
    (TypeError, '2', 20)
]

negative_data_multiply = [
    (1, 0, 2),
    (30, 20, 0),
    (50, -3, -3),
    (2, 2.5, 0)
]

negative_data_subtraction = [
    (15, 2, 0),
    (11, 10, 0),
    (16, -4, 0),
    (7.5, 2.5, 0)
]

negative_data_adding = [
    (8, 2, 0),
    (12, 12, 0),
    (23, -3, 0),
    (7, 2.5, 0)
]
