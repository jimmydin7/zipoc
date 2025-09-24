from datetime import datetime
import getpass
import socket


class MetaData:
    def get_date(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_sys_user(self):
        return getpass.getuser()

    def get_sys_machine(self):
        return socket.gethostname()

    def get_data(self):
        date = self.get_date()
        meta_user = self.get_sys_user()
        meta_machine = self.get_sys_machine()
        meta = f"{meta_user}@{meta_machine}"
        return date, meta
