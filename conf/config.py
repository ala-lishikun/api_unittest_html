# -*- coding: utf-8 -*-
import os
import ConfigParser
class Config():
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.conf_path = os.path.join(os.getcwd(), 'config.ini')
        self.config.read(self.conf_path)
        self.conf = {
            'sender': '', 'receiver': '', 'smtpserver': '', 'username': '', 'password': '',
            'login_url': '', 'search_url': '', 'upload_url': '', 'common_url': '',
            'uusername': '', 'upassword': '', 'search_query':'', 'search_rowkey':'', 'search_file': '',
            'txt': '', 'word': '', 'excel': '', 'csv': '', 'pdf': '', 'zip': ''
        }

    def get_conf(self):
        self.conf['sender'] = self.config.get("email", "sender")
        self.conf['receiver'] = self.config.get("email", "receiver")
        self.conf['smtpserver'] = self.config.get("email", "smtpserver")
        self.conf['eusername'] = self.config.get("email", "eusername")
        self.conf['epassword'] = self.config.get("email", "epassword")
        self.conf['login_url'] = self.config.get("url", "login_url")
        self.conf['search_url'] = self.config.get("url", "search_url")
        self.conf['uusername'] = self.config.get("user", "uusername")
        self.conf['upassword'] = self.config.get("user", "upassword")
        self.conf['upload_url'] = self.config.get("url", "upload_url")
        self.conf['common_url'] = self.config.get("url", "common_url")
        self.conf['txt'] = self.config.get("file", "txt")
        self.conf['word'] = self.config.get("file", "word")
        self.conf['excel'] = self.config.get("file", "excel")
        self.conf['csv'] = self.config.get("file", "csv")
        self.conf['pdf'] = self.config.get("file", "pdf")
        self.conf['zip'] = self.config.get("file", "zip")
        self.conf['search_query'] = self.config.get("query", "search_query")
        self.conf['search_rowkey'] = self.config.get("query", "search_rowkey")
        self.conf['search_file'] = self.config.get("query", "search_file")

        return self.conf

if __name__ == '__main__':
    Config()
