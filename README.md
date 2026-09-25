# AdBlock DNS Filters Modified
[217heidai/adblockfilters](https://github.com/217heidai/adblockfilters) 去广告合并规则增强版，每天更新一次。  

| 指标 | 数值 |
| :- | :- |
| 上次更新（北京时间） | 2026/09/25 09:54:52 (UTC+08:00) |
| 上游规则总数（去重前） | 527199 |
| 上游规则总数（去重后） | 375766 |
| 上游规则去重率 | 28.72% |
| 有效规则数量（可解析） | 237575 |
| 有效规则占比（检测域名） | 71.15% |
| 中国规则数（Lite） | 6762 |
| 中国规则占比（Lite/成品） | 15.57% |

## 说明
1. 定时从上游各规则源获取更新，合并去重。
2. 工作流程：拉取上游规则 → 解析提取域名/规则 → 使用本地 SmartDNS 验证连通性并剔除失效域名（上游规则中存在大量无法解析的域名）→ 生成各类成品规则与统计。
3. 上游规则源增删方法：维护 README 中“上游规则源”表格的规则名/类型/链接，工作流会按表格自动拉取并参与生成。
4. 本地新增拦截/白名单：在 `sources/local/myblock.txt` 添加自定义拦截域名/规则；在 `sources/local/white2.txt` 添加放行域名或 `@@||domain^` 形式白名单规则，支持 `+.example.com`（主域+子域）/`*.example.com`（仅子域）语法，工作流会自动合并生效。
5. 本项目仅对上游规则进行合并、去重、去除无效域名，不做任何修改。如发现误拦截情况，可在 `sources/local/white2.txt` 中自行添加白名单（支持 `+.example.com`/`*.example.com` 语法），或临时添加放行规则（如 `@@||www.example.com^$important`），并向上游规则反馈。

性能说明：实测在 J4125 或同级别性能的 x86 主机上，百万级规则规模对 dnsmasq/AdGuard Home 的解析耗时影响不超过 1ms，可放心使用。

## 相比原版 adblockfilters 的改进与新增
1. 改进了处理逻辑，缩短工作流运行时间。
2. 改进了中国规则和无效规则的处理流程，现在每次生成规则前均会对这两类规则进行验证，不再使用历史数据。
3. 白名单自动同步上游仓库，并支持 `sources/local/white2.txt` 本地补充合并。
4. 域名提取与规则解析更完善，覆盖更多 filter/dns/host 规则格式，减少漏提取。
5. 新增/独有规则源（相对上游仓库，详见下表）：
<details>
<summary>点击展开/收起新增与独有规则源列表</summary>

- 217heidai-adblockfilters
- DD-AD
- DNS-Kuner_allowlist
- DNS-Kuner_blacklist.txt
- HG
- Halflife
- SMAdHosts
- TTDNS
- hyper_adrules_ads_adguard
- hyper_adrules_allow_adguard
- hyper_adrules_malware_adguard
- qy-Ads-Rule
- 喵二白名单
- 喵二黑名单
- 茯苓允许列表
- 茯苓广告规则
- 那个谁520广告白名单
- 那个谁520规则

</details>

## 订阅链接
1. 规则x’为规则x的 Lite 版，仅针对国内域名拦截，体积较小（如添加完整规则报错数量限制，请尝试 Lite 规则）
2. 默认使用 testingcf.jsdelivr.net CDN，加速大文件会自动切换至 github.boki.moe
3. AdGuard 等浏览器插件使用规则1 + 规则2（规则2为规则1的补充，仅适用浏览器插件）

| 规则 | 原始链接 | 加速链接 | 文件体积(MB) | 规则数量 | 适配说明 |
| :- | :- | :- | :- | :- | :- | 
| 规则1 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockdns.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockdns.txt) | 4.42 | 197504 | AdGuard、AdGuard Home 等 |
| 规则1' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockdnslite.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockdnslite.txt) | 0.22 | 10652 | AdGuard、AdGuard Home 等 |
| 规则2 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockfilters.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockfilters.txt) | 2.89 | 43420 | AdGuard 等 |
| 规则2' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockfilterslite.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockfilterslite.txt) | 0.23 | 6762 | AdGuard 等 |
| 规则3 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockdomain.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockdomain.txt) | 3.85 | 197504 | InviZible Pro、personalDNSfilter |
| 规则3' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockdomainlite.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockdomainlite.txt) | 0.19 | 10652 | InviZible Pro、personalDNSfilter |
| 规则4 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockdnsmasq.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockdnsmasq.txt) | 5.36 | 197504 | DNSMasq conf |
| 规则4' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockdnsmasqlite.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockdnsmasqlite.txt) | 0.27 | 10652 | DNSMasq conf |
| 规则5 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblocksmartdns.conf) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblocksmartdns.conf) | 6.00 | 200101 | SmartDNS |
| 规则5' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblocksmartdnslite.conf) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblocksmartdnslite.conf) | 0.36 | 12434 | SmartDNS |
| 规则6 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockclash.list) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockclash.list) | 8.75 | 197505 | Shadowrocket |
| 规则6' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockclashlite.list) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockclashlite.list) | 0.46 | 10653 | Shadowrocket |
| 规则7 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockqx.conf) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockqx.conf) | 7.43 | 197504 | QuantumultX |
| 规则7' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockqxlite.conf) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockqxlite.conf) | 0.39 | 10652 | QuantumultX |
| 规则8 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockmihomo.yaml) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockmihomo.yaml) | 5.36 | 197504 | Clash Meta(Mihomo) yaml |
| 规则8' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockmihomolite.yaml) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockmihomolite.yaml) | 0.27 | 10652 | Clash Meta(Mihomo) yaml |
| 规则9 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockmihomo.mrs) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockmihomo.mrs) | 1.50 | 197504 | Clash Meta(Mihomo) mrs |
| 规则9' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockmihomolite.mrs) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockmihomolite.mrs) | 0.08 | 10652 | Clash Meta(Mihomo) mrs |
| 规则10 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockhosts.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockhosts.txt) | 5.36 | 197518 | Hosts |
| 规则10' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockhostslite.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockhostslite.txt) | 0.27 | 10666 | Hosts |
| 规则11 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblocksingbox.json) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblocksingbox.json) | 5.92 | 197504 | sing-box 1.12.x json |
| 规则11' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblocksingboxlite.json) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblocksingboxlite.json) | 0.30 | 10652 | sing-box 1.12.x json |
| 规则12 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblocksingbox.srs) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblocksingbox.srs) | 1.37 | 197504 | sing-box 1.12.x srs |
| 规则12' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblocksingboxlite.srs) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblocksingboxlite.srs) | 0.06 | 10652 | sing-box 1.12.x srs |
| 规则13 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockloon.list) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockloon.list) | 6.49 | 197504 | Loon |
| 规则13' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockloonlite.list) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockloonlite.list) | 0.34 | 10652 | Loon |
| 规则14 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblocksurge.list) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblocksurge.list) | 4.04 | 197504 | Surge |
| 规则14' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblocksurgelite.list) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblocksurgelite.list) | 0.20 | 10652 | Surge |
| 规则15 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockmosdns.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockmosdns.txt) | 4.79 | 197504 | MosDNS v5 |
| 规则15' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockmosdnslite.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockmosdnslite.txt) | 0.24 | 10652 | MosDNS v5 |
| 规则16 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblocksurgeruleset.list) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblocksurgeruleset.list) | 5.17 | 197504 | Surge RULE-SET |
| 规则16' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblocksurgerulesetlite.list) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblocksurgerulesetlite.list) | 0.26 | 10652 | Surge RULE-SET |
| 规则17 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockclashclassical.yaml) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockclashclassical.yaml) | 5.92 | 197504 | Clash Classical yaml |
| 规则17' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockclashclassicallite.yaml) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockclashclassicallite.yaml) | 0.30 | 10652 | Clash Classical yaml |
| 规则18 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockrouteros.txt) | [加速链接](https://github.boki.moe/https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockrouteros.txt) | 21.83 | 395008 | RouterOS |
| 规则18' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockrouteroslite.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockrouteroslite.txt) | 1.15 | 21304 | RouterOS |
| 规则19 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockrouterosadlist.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockrouterosadlist.txt) | 9.77 | 395010 | RouterOS AdList |
| 规则19' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockrouterosadlistlite.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockrouterosadlistlite.txt) | 0.50 | 21306 | RouterOS AdList |
| 规则20 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockdnsmasqaddnhosts.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockdnsmasqaddnhosts.txt) | 5.36 | 197504 | DNSMasq addn-hosts |
| 规则20' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockdnsmasqaddnhostslite.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockdnsmasqaddnhostslite.txt) | 0.27 | 10652 | DNSMasq addn-hosts |
| 规则21 | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockdnsmasqservers.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockdnsmasqservers.txt) | 5.55 | 197504 | DNSMasq servers |
| 规则21' | [原始链接](https://raw.githubusercontent.com/dongone105/adblockfilters-modified/main/rules/adblockdnsmasqserverslite.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/rules/adblockdnsmasqserverslite.txt) | 0.28 | 10652 | DNSMasq servers |

## 上游规则源
1. 感谢各位广告过滤规则维护大佬们的辛苦付出。

| 规则 | 类型 | 原始链接 | 加速链接 | 规则数量 | 更新日期 |
| :- | :- | :- | :- | :- | :- | 
| 217heidai-adblockfilters | dns | [原始链接](https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockdns.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/217heidai-adblockfilters.txt) | 213882 | 2026/09/25 |
| Halflife | filter | [原始链接](https://cdn.jsdelivr.net/gh/sbwml/halflife-list@master/ad.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/Halflife.txt) | 22052 | 2026/09/22 |
| DD-AD | filter | [原始链接](https://raw.githubusercontent.com/afwfv/DD-AD/refs/heads/release/easylist.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/DD-AD.txt) | 70022 | 2026/09/25 |
| qy-Ads-Rule | filter | [原始链接](https://raw.githubusercontent.com/rssvcn/qy-Ads-Rule/main/black.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/qy-Ads-Rule.txt) | 574 | 2026/09/17 |
| SMAdHosts | host | [原始链接](https://raw.githubusercontent.com/2Gardon/SM-Ad-FuckU-hosts/master/SMAdHosts) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/SMAdHosts.txt) | 5358 | 2026/09/17 |
| 那个谁520规则 | filter | [原始链接](https://raw.githubusercontent.com/qq5460168/666/refs/heads/master/rules.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/那个谁520规则.txt) | 33524 | 2026/09/25 |
| TTDNS | dns | [原始链接](https://raw.githubusercontent.com/TTDNS/Cat/refs/heads/main/DNS.TXT) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/TTDNS.txt) | 257 | 2026/09/17 |
| 茯苓广告规则 | filter | [原始链接](https://raw.githubusercontent.com/Kuroba-Sayuki/FuLing-AdRules/Master/FuLingRules/FuLingBlockList.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/茯苓广告规则.txt) | 653 | 2026/09/17 |
| HG | filter | [原始链接](https://raw.githubusercontent.com/2771936993/HG/main/hg1.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/HG.txt) | 13030 | 2026/09/25 |
| hyper_adrules_ads_adguard | filter | [原始链接](https://github.com/Lynricsy/HyperADRules/releases/latest/download/hyper_adrules_ads_adguard.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/hyper_adrules_ads_adguard.txt) | 156751 | 2026/09/23 |
| hyper_adrules_malware_adguard | filter | [原始链接](https://github.com/Lynricsy/HyperADRules/releases/latest/download/hyper_adrules_malware_adguard.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/hyper_adrules_malware_adguard.txt) | 6294 | 2026/09/17 |
| 喵二黑名单 | filter | [原始链接](https://raw.githubusercontent.com/miaoermua/AdguardFilter/main/rule.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/喵二黑名单.txt) | 332 | 2026/09/17 |
| DNS-Kuner_blacklist.txt | dns | [原始链接](https://raw.githubusercontent.com/Kuner-mw/DNS-Kuner/main/FilterRules/blacklist.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/DNS-Kuner_blacklist.txt.txt) | 151 | 2026/09/17 |
| 茯苓允许列表 | filter | [原始链接](https://raw.githubusercontent.com/Kuroba-Sayuki/FuLing-AdRules/Master/FuLingRules/FuLingAllowList.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/茯苓允许列表.txt) | 1313 | 2026/09/17 |
| 那个谁520广告白名单 | filter | [原始链接](https://raw.githubusercontent.com/qq5460168/666/master/allow.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/那个谁520广告白名单.txt) | 3704 | 2026/09/25 |
| DNS-Kuner_allowlist | dns | [原始链接](https://raw.githubusercontent.com/Kuner-mw/DNS-Kuner/main/FilterRules/allowlist.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/DNS-Kuner_allowlist.txt) | 65 | 2026/09/17 |
| 喵二白名单 | filter | [原始链接](https://raw.githubusercontent.com/miaoermua/AdguardFilter/main/whitelist.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/喵二白名单.txt) | 514 | 2026/09/17 |
| hyper_adrules_allow_adguard | filter | [原始链接](https://github.com/Lynricsy/HyperADRules/releases/latest/download/hyper_adrules_allow_adguard.txt) | [加速链接](https://testingcf.jsdelivr.net/gh/dongone105/adblockfilters-modified@main/sources/upstream/hyper_adrules_allow_adguard.txt) | 686 | 2026/09/17 |

## Star History
<a href="https://www.star-history.com/#dongone105/adblockfilters-modified&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=dongone105/adblockfilters-modified&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=dongone105/adblockfilters-modified&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=dongone105/adblockfilters-modified&type=Date" />
 </picture>
</a>
