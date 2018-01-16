from FabricService.FabricCommandClass import FabricCommandClass
from FabricService import host,  password, user,DnsCryptDownloadLink,\
    DnsCryptExractDir,DnsCryptResolverCsvLink, DnsCryptResolverDir,\
    DnsCryptResolverNames, LoopBackStartAddress
from fabric.context_managers import env
from fabric.tasks import execute


class FabricExecuteClass(FabricCommandClass):


    def __init__(self,user: str = user, password: str = password,
                 host: str = host,DnsCryptDownloadLink: str = DnsCryptDownloadLink,
                 DnsCryptExractDir: str = DnsCryptExractDir,
                 DnsCryptResolverNames: list = DnsCryptResolverNames,
                 LoopBackStartAddress: str = LoopBackStartAddress):
        env.user = user
        env.password = password
        self.host = host
        super().__init__(DnsCryptDownloadLink=DnsCryptDownloadLink,
                         DnsCryptExractDir=DnsCryptExractDir,
                         DnsCryptResolverCsvLink=DnsCryptResolverCsvLink,
                         DnsCryptResolverDir=DnsCryptResolverDir,
                         DnsCryptResolverNames=DnsCryptResolverNames,
                         LoopBackStartAddress=LoopBackStartAddress)




    def ExecuteSystemPackages(self):
        execute(self.CommandSystemPackages, host=self.host)

    def ExecuteBuildDNSCrypt(self):
        execute(self.CommandBuildDNSCrypt, host=self.host)

    def ExecuteAddDnsCryptUser(self):
        execute(self.CommandAddDnsCryptUser, host=self.host)

    def ExecuteUpdateDnsCryptResolvers(self):
        execute(self.CommandUpdateDnsCryptResolvers, host=self.host)

    def ExecuteCreateDNSCryptProxies(self):
        execute(self.CommandCreateDNSCryptProxies, host=self.host)