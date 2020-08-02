import sqlite3

class SQLite:

    def __init__(self, db_file):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status = True):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `customers` WHERE `sign_up_status` = ?", (status,)).fetchall()

    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `customers` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def check_sign_up_status(self, user_id):
        '''Проверяем статус пользователя'''
        with self.connection:
            result = self.cursor.execute("SELECT 'sign_up_status' FROM `customers` WHERE `user_id` = ?", (user_id,)).fetchone()
            return bool(result)

    def add_subscriber(self, user_id, status = False):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `customers` (`user_id`, `sign_up_status`) VALUES(?,?)", (user_id,status))

    def add_telephone_number(self, user_id, telephone_number):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("UPDATE `customers` SET 'telephone_number' = ? WHERE `user_id` = ?", (telephone_number,user_id))

    def update_subscription(self, user_id, status):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `customers` SET `sign_up_status` = ? WHERE `user_id` = ?", (status, user_id))

    def save(self):
        """сохранение данных"""
        self.connection.commit()

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()