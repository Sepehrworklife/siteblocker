import os


class BlockSite:

    def __init__(self):
        self.addSiteBlockerComment()

    def getListOfBlockedSite(self):
       startComment = self.indexOfSiteBlockerComment("#SiteBlockerSection")
       endComment = self.indexOfSiteBlockerComment("#EndSiteBlockerSection") 
       listOfBlockedSite = []
       with open(self.getOSHostsFilePath(), 'r') as file:
           allLines = file.readlines()
           for i in range(startComment, endComment-1):
               line = allLines[i].replace("\n", "").replace(" ", "").replace("127.0.0.1\t", "")
               listOfBlockedSite.append(line)
           return listOfBlockedSite



    def addSiteBlock(self, url):
        with open(self.getOSHostsFilePath(), 'r+') as file:
            contents = file.read().replace('#SiteBlockerSection', '#SiteBlockerSection\n127.0.0.1\t' + url)
            file.seek(0)
            file.truncate()
            file.write(contents)


    def addSiteBlockerComment(self):
        if self.isSiteBlockerCommentAdded() == False:
            with open(self.getOSHostsFilePath(),'a') as file:
                file.write('\n#SiteBlockerSection\n#EndSiteBlockerSection')


    def isSiteBlockerCommentAdded(self):
        with open(self.getOSHostsFilePath()) as file:
                  if '#SiteBlockerSection' in file.read():
                        return True
                  else :
                        return False



    def getOSHostsFilePath(self):
        osName = os.uname().sysname
        if osName == 'Linux':
           return '/etc/hosts'
        elif osName == 'Windows':
            return 'C:\Windows\System32\drivers\etc\hosts'
        else :
            exit()


    def indexOfSiteBlockerComment(self, endOrStart):
            with open(self.getOSHostsFilePath(), 'r') as file:
                index = 0
                for line in file:
                    index += 1
                    if endOrStart in line:
                        return index 
