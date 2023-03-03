# test_API
Тестовое задание:

Необходимо создать REST API на Python Django. Настроить JWT и пользователя для доступа к рест и админке. БД SQLite.

Модели: 
1. группы;
2. студенты; 
3. предметы; 
4. оценки.

Необходимо провести связку между моделями foreign key.

На странице входа нужно вести логин и пароль

login: Albert

password: admin

после этого вас редиректит на лендинг где предоставлены отчеты и свагер со всеми данными

users/ - какие user есть в базе

subjects/ - какие предметы есть в базе

groups/ -  какие группы есть в базе

students/ -  какие студенты есть в базе

students_sort/ - запрос средних оценок по предметам по конкретному студенту 

group_sort/ - запрос средних оценок по предметам по конкретной группе 

score/ - какие оценоки есть в базе (внешние ключи к студентам группе предметы)

score/1 - редактирование оценок (внешние ключи к студентам группе предметы)