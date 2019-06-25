# # encoding=utf-8
# import ConfigParser
# from dointerface.conf.VarConfig import pageElementLocatorPath
# class ParseCofigFile(object):
#     def __init__(self):
#         self.cf=ConfigParser.ConfigParser()
#         self.cf.read(pageElementLocatorPath)
#
#     def getItemsSection(self,sectionName):
#         optionsDict=dict(self.cf.items(sectionName))
#         return optionsDict
#     def getOptionValue(self,sectionName,optionName):
#         value=self.cf.get(sectionName,optionName)
#         return value
#
# if __name__=='__main__':
#     pc=ParseCofigFile()
#     print pc.getItemsSection("126mail_login")
#     print pc.getOptionValue("126mail_login","loginPage.frame")
#
#
#
