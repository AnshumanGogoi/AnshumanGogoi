import configparser

file = '/Users/anshumangogoi/PycharmProjects/TestingFrameWork/utilities/properties.ini'
config = configparser.ConfigParser()
config.read(file)
print(config.sections())
print((config['common info']['username']))




