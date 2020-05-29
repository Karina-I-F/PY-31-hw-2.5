from datetime import datetime


class OpenTimeLog:
    def __init__(self, log_path):
        self.log_path = log_path

    def __enter__(self):
        self.start_time = datetime.now()
        self.log = open(self.log_path, 'a', encoding='utf8')
        self.log.write(f'Время начала работы программы: {datetime.utcnow()}\n')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.log.write(f'Время завершения работы программы: {datetime.utcnow()}\n')
        self.log.write(f'Время, затраченное на выполнение программы: {datetime.now() - self.start_time}\n')
        self.log.close()
