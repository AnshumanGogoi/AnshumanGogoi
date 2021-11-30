import configparser
import os

file = '/Users/anshumangogoi/PycharmProjects/TestingFrameWork/Configurations/properties.ini'
config = configparser.RawConfigParser()
config.read(file)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url
        #print(config.sections())

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
