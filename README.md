# 2023-product-matching-project
Проект 2023-product-matching-project состоит из 5 частей:
- data_collection - директория содержащая все скрипты для сбора данных с российских онлайн магазинов
- generating_pairs - директория содержащая скрипты для построения пар товаров для последующей разметки
- base_classification - директория содержащая скрипты для построения и нахождения лучшей модели классификации сопоставлений, основанной на базовых моделях
- bert_classification - директория содержащая скрипты для построения модели BERT для классификации сопоставлений
- web-app - директория содержащая скрипты для создания веб приложения на базе Flask

**data_collection**
- selenium_parsers - папка со скриптами для парсинга товаров с помощью инструмента selenium
  - dns - папка со скриптами для парсинга смартфонов с онлайн магазина dns
    - parse_dns_pages.py - скрипт для прохождения по всем страницам категории для получения ссылок на все товары категории
    - dns_get_cards.py - скрипт для получения всей информации о товарах по их url
  - wb - папка со скриптами для парсинга смартфонов с маркетплейса wildberries
    - parse_wb_pages.py - скрипт для прохождения по всем страницам категории для получения ссылок на все товары категории
    - wb_get_cards.py - скрипт для получения всей информации о товарах по их id
  - get_specs_cg.py - скрипт для получения всех характеритик товаров по их url из онлайн магазина Читай-город
- api_parsers - папка со скриптами для парсинга информации о товарах с помощью api онлайн магазинов
  - cg_data_collection - скрипт для парсинга товаров категории "книги" с онлайн магазина Читай-город
  - mvideo_data_collection - скрипт для парсинга товаров категории "телевизоры" с онлайн магазина Мвидео
  - wb_data_collection - скрипт для парсинга товаров категорий: книги, телевизоры, игрушки LEGO с онлайн магазина wildberries

**generating_pairs**
- build_pairs.py - скрипт для генерации пар способом описанным в отчете "Описание метода построения пар"
- build_pairs_by_identifier.py - скрипт для генерации пар способом объединения товаров по идентификатору, описанным в отчете "Описание метода построения пар"
- build_pairs_by_model.py - скрипт для генерации пар способом объединения товаров по модели и дополнительным признакам, описанным в отчете "Описание метода построения пар"
- preprocess_utils - набор функций для предобработки данных

**base_classification**
- models - папка, содержащая всю информацию о построении моделей, а также сами модели
  - interm_data - папка с полученными моделями и векторизаторами после обучения и тестирования моделей
    - best_model.pickle - модель, показывающая лучшие показатели на тестовых данных
    - best_params.pickle - параметры моделей, при которых тестируемые модели из classifier_models.py показывают лучшее качество
    - count_vectorizers.pickle - модели для построения векторного представления для каждого признака
  - baseline.py - скрипт содержащий полный цикл построения модели классификации: от загрузки и векторизации данных до нахождения лучших парамтеров и модели
  - classifier_models.py - файл, содержащий используемые для тестирования модели классификации, а также возможные параметры для настройки моделей
  - predict_match.py - скрипт для тестирования полученной модели
  - similarities.py - файл, содержащий функции для нахождения близости между значениями

- pairs
  - pairs_info.py - скрипт для получения данных о товарах и данных о парах из базы данных и объединения этих таблиц
  - preprocess.py - предобработка полученного датасета из скарипта pairs_info.py
- utils.py - файл, содержащий функции для предобработки текстовых данных

**bert_classification**
- bert_classifier - папка, содержащая все необходимые файлы для построение модели классификации на основе предобученной модели BERT
  - train.py - скрипт для построения и тестирования модели
  - test.py - скрипт для тестирования модели на валидационных данных
 
 **web-app**
 - data - папка, содержащая все файлы с данными для работы приложения
 - models - папка, содержащая все файлы с моделями классификации и моделями для построения векторного простарнства, необходимыми для работы приложения
 - static/css - папка, содержащая все файлы со стилями для шаблонов
 - templates - папка, содержащая все шаблоны для приложения
 - utils.py - файл с дополнительными функциями по работе с данными
 - main.py - главный файл для запуска веб-приложения со всеми обработчиками маршрутов приложения
 