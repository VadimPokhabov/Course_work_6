# Проект Онлайн рассылок 
В данном проекте реализована рассылка электронных писем для клиентов. Пользователь на сайте может заполнить форму с обратной связью. Эти данные попадают в БД, затем клиент, может создать сообщение для рассылки, с акциями например или новым поступлением. Затем он (пользователь) может создать рассылку, выбрать киента из списка, кому бы он хотел отправить электронные письма, и создать рассылку.
Так же клиент может выбирать периодичность отправки рассылок: раз в день, раз в неделю, раз в месяц, и когда заканчивать рассылку: число, месяц, год, время.
В проекте реализована регистрация, авторизация пользователя с проверкой, которая отправляет на email ссылку от нашего приложения.

В проекте подключены:

1. Регистрация и авторизация пользователя;
2. Админ-панель для суперпользователя;
3. Профиль пользователя с возможностью менять данные, добавления аватарки;
4. Возможность создавать, редактировать, удалять отдельные рассылки.

В данном проекте использован фреймворк Django, с подключением реляционной базы данных "PostgreSQL"
Использовалось виртуальное окружение venv В проекте построено 6 модель БД:

1. Таблица "Blog" прямая связь с таблицей "User";
2. Таблица "Recipients";
3. Таблица "User";
4. Таблица "MailingMessage" связи нет;
5. Таблица "MailingSettings" прямая связь с "MailingMessage", и связь через ManyToMany с "Recipients";
6. Таблица "MailingStatus" прямая связь c "MailingSettings", "Recipients";

Для запуска проекта необходимо сделать

1. git clone репозитория

```
git@github.com:VadimPokhabov/Mailing_List_management_Service.git
```
2. Установить виртуальное окружение venv
```
python3 -m venv venv
```
3. Подключить виртуальное окружение
```
source venv/bin/activate
```
4. Создать базу данных в PgAdmin, либо через терминал. Необходимо дать название в файле settings.py в каталоге 'config' в константе (словаре) 'DATABASES'
5. Обязательно установить пакет со всеми зависимостями
```
pip install -r requirements.txt
```
6. Создать файл .env в корне проекта и заполнить следующие данные:
```
SECRET_KEY=

DEBUG=

POSTGRES_DB=
POSTGRES_PASSWORD=
POSTGRES_USER=

EMAIL_HOST_USER_MAIL=
EMAIL_HOST_PASSWORD_MAIL=

ADMIN_EMAIL=

CACHE_ENABLED=
CACHES_BACKEND=
CACHES_LOCATION=
```
7. Для запуска рассылок сообщений клиентам необходимо использовать команду в терминале
```
python manage.py start_message
```
ВАЖНО чтобы рассылка заработала необходимо прежде активировать виртуальное окружение ШАГ 3

Чтобы установить группы доступа для пользователей в админ панели необходимо выполнить следующую команду
```
python manage.py loaddata fixtures/groups.json
```