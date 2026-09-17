import os
from typing import List, Set, Dict

from loguru import logger

from app.base import APPBase


class AdGuardHomeWhitelist(APPBase):
    """
    独立白名单生成器：仅输出 unblockList（上游/本地白名单解析出的放行域名），
    不写入任何拦截规则，产物可作为 AdGuardHome 的一条独立自定义过滤列表订阅。
    """

    def __init__(self, blockList: List[str], unblockList: List[str], filterDict: Dict[str, str], filterList: List[str], filterList_var: List[str], ChinaSet: Set[str], fileName: str, sourceRule: str):
        super(AdGuardHomeWhitelist, self).__init__(blockList, unblockList, filterDict, filterList, filterList_var, ChinaSet, fileName, sourceRule)

    def generate(self, isLite=False):
        try:
            if isLite:
                logger.info("generate AdGuardHome Whitelist Lite...")
                fileName = self.fileNameLite
                unblockList = self.unblockListLite
            else:
                logger.info("generate AdGuardHome Whitelist...")
                fileName = self.fileName
                unblockList = self.unblockList

            if os.path.exists(fileName):
                os.remove(fileName)

            with open(fileName, 'a') as f:
                f.write("!\n")
                if isLite:
                    f.write("! Title: AdBlock DNS Whitelist Lite\n")
                    f.write("! Description: 适用于 AdGuardHome 的独立放行规则（白名单），每 12 小时更新一次。规则源：%s。Lite 版仅针对国内域名。\n" % (self.sourceRule))
                else:
                    f.write("! Title: AdBlock DNS Whitelist\n")
                    f.write("! Description: 适用于 AdGuardHome 的独立放行规则（白名单），每 12 小时更新一次。规则源：%s。\n" % (self.sourceRule))
                f.write("! Homepage: %s\n" % (self.homepage))
                f.write("! Source: %s/%s\n" % (self.source, os.path.basename(fileName)))
                f.write("! Version: %s\n" % (self.version))
                f.write("! Last modified: %s\n" % (self.time))
                f.write("! Whitelisted domains: %s\n" % (len(unblockList)))
                f.write("!\n")
                for domain in unblockList:
                    f.write("@@||%s^\n" % (domain))

            if isLite:
                logger.info("AdGuardHome Whitelist Lite: unblock=%d" % (len(unblockList)))
            else:
                logger.info("AdGuardHome Whitelist: unblock=%d" % (len(unblockList)))
        except Exception as e:
            logger.error("%s" % (e))

    # 覆盖基类：基类以 blockList 是否非空决定是否生成，这里改成看 unblockList
    def generateAll(self):
        try:
            if len(self.unblockList):
                self.generate()
            if len(self.unblockListLite):
                self.generate(isLite=True)
        except Exception as e:
            logger.error("%s" % (e))
