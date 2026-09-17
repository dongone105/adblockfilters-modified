import os
import time
import hashlib
import asyncio
import json
from typing import List,Tuple

import httpx
from loguru import logger

from readme import Rule

# 上游规则更新
class Updater(object):
    def __init__(self, ruleList:List[Rule]):
        self.ruleList = ruleList
        self.isNeedUpdate = False
        self.__min_change_ratio = 0.7
        self.__max_change_ratio = 1.5
        self.__min_change_abs = 1000
        self.__meta = {}
        self.__meta_path = ""

    def update(self, path:str) -> Tuple[bool,List[Rule]]:
        self.__meta_path = os.path.join(path, ".source_meta.json")
        self.__meta = self.__load_meta()
        # 启动异步循环
        loop = asyncio.get_event_loop()
        # 添加异步任务
        taskList = []
        for rule in self.ruleList:
            logger.info("updating %s..."%(rule.name))
            task = asyncio.ensure_future(self.__Download(rule, path))
            taskList.append(task)
        # 等待异步任务结束
        loop.run_until_complete(asyncio.wait(taskList))
        # 获取异步任务结果
        for task in taskList:
            new, meta_update = task.result()
            for rule in self.ruleList:
                if new.name == rule.name:
                    rule.latest = new.latest
                    rule.update = new.update
                    if rule.update:
                        self.isNeedUpdate = rule.update
                    break
            if meta_update:
                self.__meta[meta_update.get("filename")] = meta_update
        self.__save_meta()
        return self.isNeedUpdate, self.ruleList

    def __load_meta(self) -> dict:
        if not self.__meta_path or not os.path.exists(self.__meta_path):
            return {}
        try:
            with open(self.__meta_path, "r") as f:
                return json.load(f)
        except Exception:
            return {}

    def __save_meta(self):
        if not self.__meta_path:
            return
        try:
            with open(self.__meta_path, "w") as f:
                json.dump(self.__meta, f, indent=2, sort_keys=True)
        except Exception as e:
            logger.error("save meta failed: %s" % e)

    def __count_file_lines(self, filename: str) -> int:
        try:
            with open(filename, "r") as f:
                return sum(1 for line in f if line.strip())
        except Exception:
            return 0

    def __is_probably_text(self, content: bytes) -> bool:
        sample = content[:2048]
        if b"\x00" in sample:
            return False
        lowered = sample.lstrip().lower()
        if lowered.startswith(b"<!doctype html") or b"<html" in lowered:
            return False
        return True

    def __is_anomalous_lines(self, new_lines: int, old_lines: int) -> bool:
        if old_lines < 1000:
            return False
        diff = abs(new_lines - old_lines)
        if diff < self.__min_change_abs:
            return False
        ratio = new_lines / old_lines if old_lines else 1
        return ratio < self.__min_change_ratio or ratio > self.__max_change_ratio

    def __CalcFileSha256(self, filename):
        with open(filename, "rb") as f:
            sha256obj = hashlib.sha256()
            sha256obj.update(f.read())
            hash_value = sha256obj.hexdigest()
            return hash_value

import os
from typing import List, Set, Dict

from loguru import logger

from app.base import APPBase

class AdGuard(APPBase):
    def __init__(self, blockList:List[str], unblockList:List[str], filterDict:Dict[str,str], filterList:List[str], filterList_var:List[str], ChinaSet:Set[str], fileName:str, sourceRule:str):
        super(AdGuard, self).__init__(blockList, unblockList, filterDict, filterList, filterList_var, ChinaSet, fileName, sourceRule)

    def generate(self, isLite=False):
        try:
            if isLite:
                logger.info("generate adblock AdGuard Lite...")
                fileName = self.fileNameLite
                filterList = self.filterListLite
            else:
                logger.info("generate adblock AdGuard...")
                fileName = self.fileName
                filterList = self.filterList
            
            if os.path.exists(fileName):
                os.remove(fileName)

            # 去除放行规则（@@ 开头），放行规则已单独输出到白名单文件
            filterList = [fiter for fiter in filterList if not fiter.startswith('@@')]

            # 生成规则文件
            with open(fileName, 'a') as f:
                f.write("!\n")
                if isLite:
                    f.write("! Title: AdBlock Filter Lite\n")
                    f.write("! Description: 适用于 AdGuard 的去广告合并规则，每 12 小时更新一次。规则源：%s。Lite 版仅针对国内域名拦截。\n"%(self.sourceRule))
                else:
                    f.write("! Title: AdBlock Filter\n")
                    f.write("! Description: 适用于 AdGuard 的去广告合并规则，每 12 小时更新一次。规则源：%s。\n"%(self.sourceRule))
                f.write("! Homepage: %s\n"%(self.homepage))
                f.write("! Source: %s/%s\n"%(self.source, os.path.basename(fileName)))
                f.write("! Version: %s\n"%(self.version))
                f.write("! Last modified: %s\n"%(self.time))
                f.write("! Blocked Filters: %s\n"%(len(filterList)))
                f.write("!\n")
                for fiter in self.filterList_var:
                    f.write("%s\n"%(fiter))
                for fiter in filterList:
                    f.write("%s\n"%(fiter))
            
            if isLite:
                logger.info("adblock AdGuard Lite: block=%d"%(len(filterList)))
            else:
                logger.info("adblock AdGuard: block=%d"%(len(filterList)))
        except Exception as e:
            logger.error("%s"%(e))
