# course_work_4

## Задание

Напишите программу, которая будет получать информацию о вакансиях с разных платформ в России, сохранять ее в файл и
позволять удобно работать с ней (добавлять, фильтровать, удалять).

## Требования к реализации

1. Создать абстрактный класс для работы с API сайтов с вакансиями. Реализовать классы, наследующиеся от абстрактного 
2. класса, для работы с конкретными платформами. Классы должны уметь подключаться к API и получать вакансии.
3. Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты, такие как название вакансии,
4. ссылка на вакансию, зарплата, краткое описание или требования и т.п. (не менее четырех) Класс должен поддерживать
5. методы сравнения вакансий между собой по зарплате и валидировать данные, которыми инициализируются его атрибуты.
6. Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл, получения данных
7. из файла по указанным критериям и удаления информации о вакансиях. Создать класс для сохранения информации
8. о вакансиях в JSON-файл. Дополнительно, по желанию, можно реализовать классы для работы с другими форматами, например
9. с CSV- или Excel-файлом, с TXT-файлом.
10. Создать функцию для взаимодействия с пользователем. Функция должна взаимодействовать с пользователем через консоль. 
11. Самостоятельно придумать сценарии и возможности взаимодействия с пользователем. Например, позволять пользователю 
12. указать, с каких платформ он хочет получить вакансии, ввести поисковый запрос, получить топ N вакансий по зарплате, 
13. получить вакансии в отсортированном виде, получить вакансии, в описании которых есть определенные ключевые слова, 
14. например "postgres" и т.п.
15. Объединить все классы и функции в единую программу.

## Требования к реализации в парадигме ООП

1. Абстрактный класс и классы для работы с API сайтов с вакансиями должны быть реализованы в соответствии с принципом 
2. наследования.
3. Класс для работы с вакансиями должен быть реализован в соответствии с принципом инкапсуляции и поддерживать методы 
4. сравнения вакансий между собой по зарплате.
5. Классы и другие сущности в проекте должны удовлетворять минимум первым двум требованиям принципов SOLID.

## Платформы для сбора вакансий

1. **hh.ru** ([ссылка на API](https://github.com/hhru/api/blob/master/docs/general.md))
2. **superjob.ru** ([ссылка на API](https://api.superjob.ru/))
    - Прежде чем начать использовать API от SuperJob, 
    - необходимо [зарегистрироваться](https://www.superjob.ru/auth/login/?returnUrl=https://api.superjob.ru/register/) 
    - и получить токен для работы. Подробная инструкция дается по ссылке описания документации 
    - в разделе [Getting started](https://api.superjob.ru/#gettin). При регистрации приложения можно указать 
    - произвольные данные.

## Выходные данные

- Информация о вакансиях, полученная с разных платформ, сохраненная в JSON-файл.
- Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.
