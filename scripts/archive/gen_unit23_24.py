# -*- coding: utf-8 -*-
import json
import os

story_dir = r"单词故事本"

# Unit 23 Data (57 words)
unit23_data = {
    "unit": 23,
    "stories": [
        {
            "id": "s1",
            "en": "Scientific Inquiry and Governance",
            "zh": "科学探究与治理",
            "theme": "科学 / 治理",
            "ps": [
                {
                    "en": "To present a [[logical]] argument during the emergency meeting, researchers had to [[rescue]] critical field data before their server crashed. They launched comprehensive [[research]] to examine why citizens [[resentment|resent]] bureaucratic delays, offering cold drinks to [[refresh]] weary team members.",
                    "zh": "为了在紧急会议上提出逻辑严密的论据，研究人员必须在服务器崩溃前救援关键的野外数据。他们开展了全面的研究，探讨市民为何对官僚延误感到愤恨，并向疲惫的团队成员提供冷饮以使其恢复精力。"
                },
                {
                    "en": "The lead scholar managed to [[refute]] groundless accusations in the regional [[region]]. The committee established a [[regular]] schedule to [[regulate]] industrial emissions, enforcing a strict [[regulation]] to [[replace]] outdated safety rules.",
                    "zh": "首席学者成功驳斥了该区域内无端的指责。委员会确立了例行日程来监管工业排放，执行严格的规则以替换过时的安全规定。"
                },
                {
                    "en": "In a prompt [[reply]], a senior official published an audit [[report]], while an investigative [[reporter]] praised the council's glowing [[reputation]]. They approved a formal [[request]] to [[require]] every department to fulfill each environmental [[requirement]] and accurately [[assess]] potential risks.",
                    "zh": "在迅速的回复中，一位高级官员公布了一份审计报告，而一名调查记者赞扬了委员会良好的声誉。他们批准了一项正式请求，要求每个部门履行各项环境要求并准确评估潜在风险。"
                }
            ]
        },
        {
            "id": "s2",
            "en": "Social Assimilation and Governance",
            "zh": "社会同化与同化治理",
            "theme": "社会 / 融合",
            "ps": [
                {
                    "en": "Immigrants worked hard to [[assimilate]] into local culture, relying on community centers to [[assist]] their transition. Timely financial [[assistance]] enabled a skilled administrative [[assistant]] to pursue higher education. Leaders [[assumed|assume]] that this reasonable [[assumption]] would hold true across all sectors.",
                    "zh": "移民努力融入当地文化，依靠社区中心协助其转型。及时的经济援助使一位有技能的行政助理能够接受高等教育。领导层假设这一合理的假定将在所有部门都适用。"
                },
                {
                    "en": "Civic groups strove to [[contribute]] to urban renewal, making a lasting [[contribution]] to public health despite a [[controversial]] debate. Surrounding the policy [[controversy]], officials maintained firm [[control]] over project timelines.",
                    "zh": "公民团体努力为城市更新做出贡献，尽管存在有争议的辩论，但仍对公共卫生作出了持久的贡献。围绕该政策争议，官员们保持着对项目时间表的确切控制。"
                },
                {
                    "en": "Organizers decided to [[convene]] an international summit according to diplomatic [[convention]]. As diverse opinions began to [[converge]], delegates succeeded to [[convey]] their shared vision. In the economic [[domain]], [[domestic]] industries sought to become [[dominant]] and [[dominate]] global markets.",
                    "zh": "组织者决定按照外交惯例召开一次国际峰会。随着多元观点开始趋同，代表们成功地传达了他们共同的愿景。在经济领域，国内产业试图变得占主导地位并主导全球市场。"
                }
            ]
        },
        {
            "id": "s3",
            "en": "Productivity and Career Growth",
            "zh": "生产力与职业成长",
            "theme": "经济 / 职业",
            "ps": [
                {
                    "en": "Ignoring economic warnings could [[doom]] ambitious startups to sudden failure. High inflation led to a [[double]] increase in operational costs, leaving no [[doubt]] that a deep [[probe]] was needed. Engineers revised every legal [[procedure]] before they could [[proceed]] with judicial [[proceedings|proceeding]].",
                    "zh": "忽视经济警告可能会使雄心勃勃的初创公司注定突然失败。高通胀导致运营成本翻倍增加，毫无疑问需要进行深入调查。工程师们在继续司法程序之前修改了每一项法定程序。"
                },
                {
                    "en": "They optimized the manufacturing [[process]] to ensure an orderly [[procession]] of goods. Leaders chose to [[proclaim]] new standards to [[produce]] a high-quality [[product]].",
                    "zh": "他们优化了制造过程，以确保货物的有序行列。领导人选择宣告新标准，以生产高质量的产品。"
                },
                {
                    "en": "Mass [[production]] boosted [[productive]] efficiency, elevating overall [[productivity]] across the manufacturing sector. Entering a prestigious [[profession]], every [[professional]] sought to [[expand]] market reach, paving the way for rapid corporate [[expansion]].",
                    "zh": "大批量生产提高了生产效率，提升了整个制造业的整体生产力。进入一个受人尊敬的职业，每一位专业人士都试图扩大市场覆盖，为企业的快速扩张铺平道路。"
                }
            ]
        }
    ],
    "words": [
        {"w": "logical", "ipa": "ˈlɒdʒɪkl", "pos": "adj.", "s": "s1", "zh": "合逻辑的", "exam": "逻辑（上）的；符合逻辑的", "c": ["logical conclusion 逻辑结论", "logical thinking 逻辑思维"], "syn": ["rational", "reasonable", "coherent"], "fam":["logically adv. 逻辑上"], "dif": "logical 指符合逻辑推导规则或理性的；rational 指有理智的。", "pat": "The report reached a logical conclusion based on solid empirical evidence.", "patZh": "该报告根据坚实的经验证据得出了一个符合逻辑的结论。"},
        {"w": "rescue", "ipa": "ˈreskjuː", "pos": "vt. / n.", "s": "s1", "zh": "救援", "exam": "营救；救援", "c": ["rescue mission 救援任务", "come to the rescue 赶来救援"], "syn": ["save", "deliver", "salvage"], "fam":["rescuer n. 救援者"], "dif": "rescue 指从危险、困境中营救或救出。", "pat": "Firefighters worked through the night to rescue trapped victims.", "patZh": "消防员整夜工作以营救被困受害者。"},
        {"w": "research", "ipa": "rɪˈsɜːtʃ", "pos": "n. / v.", "s": "s1", "zh": "研究", "exam": "研究；调查", "c": ["conduct research 进行研究", "research findings 研究结果"], "syn": ["investigation", "inquiry", "study"], "fam":["researcher n. 研究员"], "dif": "research 侧重系统严谨的学术科学探索与调查。", "pat": "Scientists continue to conduct research into renewable energy solutions.", "patZh": "科学家们继续就可再生能源解决方案开展研究。"},
        {"w": "resent", "ipa": "rɪˈzent", "pos": "vt.", "s": "s1", "zh": "愤恨", "exam": "对…感到愤恨；怨恨", "c": ["resent the decision 对决定感到怨恨", "deeply resent 深感愤恨"], "syn": ["begrudge", "dislike", "grudge"], "fam":["resentment n. 愤恨"], "dif": "resent 指对不公正对待或冒犯心怀怨恨不满。", "pat": "Employees began to resent the management's unfair policy changes.", "patZh": "员工们开始对管理层不公平的政策变更感到愤恨。"},
        {"w": "refresh", "ipa": "rɪˈfreʃ", "pos": "v.", "s": "s1", "zh": "使精力恢复", "exam": "使恢复精力；提神；刷新", "c": ["refresh one's memory 唤起记忆", "refresh the page 刷新页面"], "syn": ["revitalize", "renew", "restore"], "fam":["refreshment n. 提神物品；茶点"], "dif": "refresh 指使身心恢复疲劳，或刷新网页数据。", "pat": "A short walk in the park helped refresh her tired mind.", "patZh": "在公园散步片刻有助于恢复她疲惫的心智。"},
        {"w": "refute", "ipa": "rɪˈfjuːt", "pos": "vt.", "s": "s1", "zh": "驳斥", "exam": "驳斥；反驳", "c": ["refute an argument 驳斥某种观点", "refute allegations 驳斥指控"], "syn": ["disprove", "rebut", "confute"], "fam":["refutation n. 反驳"], "dif": "refute 指用事实证据有力地证明某种言论推论错误。", "pat": "The attorney presented evidence to refute the prosecution's claims.", "patZh": "律师出示证据驳斥了控方的指控。"},
        {"w": "region", "ipa": "ˈriːdʒən", "pos": "n.", "s": "s1", "zh": "区域", "exam": "地区；区域；范围", "c": ["coastal region 沿海地区", "autonomous region 自治区"], "syn": ["area", "district", "zone"], "fam":["regional adj. 区域的"], "dif": "region 指地理、自然或行政划分的大片区域。", "pat": "Economic growth varied significantly across different regions of the country.", "patZh": "国家不同区域之间的经济增长存在显著差异。"},
        {"w": "regular", "ipa": "ˈreɡjələ", "pos": "adj.", "s": "s1", "zh": "例行的", "exam": "规则的；定期的；常规的；例行的", "c": ["regular exercise 定期运动", "regular meeting 例会"], "syn": ["routine", "systematic", "standard"], "fam":["regularly adv. 定期地"], "dif": "regular 指按既定时间间隔或标准规则进行的。", "pat": "Maintaining regular sleep patterns promotes better overall physical health.", "patZh": "保持规律的睡眠模式有助于促进更好的整体身体健康。"},
        {"w": "regulate", "ipa": "ˈreɡjuleɪt", "pos": "vt.", "s": "s1", "zh": "监管", "exam": "管理；调节；监管", "c": ["regulate temperature 调节温度", "regulate the market 监管市场"], "syn": ["control", "adjust", "govern"], "fam":["regulation n. 规则；监管"], "dif": "regulate 侧重依法规、标准对市场、温度或行为进行管制调节。", "pat": "Governments enact strict laws to regulate chemical waste disposal.", "patZh": "政府制定严格的法律来监管化学废物的处置。"},
        {"w": "regulation", "ipa": "ˌreɡjuˈleɪʃn", "pos": "n.", "s": "s1", "zh": "规则", "exam": "规章；规则；管理；调节", "c": ["safety regulation 安全规章", "strict regulation 严格的规章"], "syn": ["rule", "statute", "ordinance"], "fam":["regulate v. 监管"], "dif": "regulation 指官方颁布实施的具体规章制度法规。", "pat": "Compliance with environmental regulation is mandatory for all factories.", "patZh": "遵守环境规章对所有工厂来说都是强制性的。"},
        {"w": "replace", "ipa": "rɪˈpleɪs", "pos": "vt.", "s": "s1", "zh": "替换", "exam": "替换；取代；把…放回原处", "c": ["replace old equipment 替换旧设备", "replace A with B 用B替换A"], "syn": ["substitute", "supplant", "exchange"], "fam":["replacement n. 替换"], "dif": "replace 强调拿新的或别的东西取代原有的物品职位。", "pat": "Renewable energy sources will gradually replace fossil fuels in the future.", "patZh": "在未来，可再生能源将逐步取代化石燃料。"},
        {"w": "reply", "ipa": "rɪˈplaɪ", "pos": "v. / n.", "s": "s1", "zh": "回复", "exam": "回答；答复；回复", "c": ["reply to an email 回复邮件", "in reply to 作为对…的答复"], "syn": ["respond", "answer", "retort"], "fam":["reply n. 回复"], "dif": "reply 侧重对问题、信件或请求做出针对性的具体答复。", "pat": "The company promised to reply to customer inquiries within 24 hours.", "patZh": "公司承诺在24小时内回复客户的询价。"},
        {"w": "report", "ipa": "rɪˈpɔːt", "pos": "n. / v.", "s": "s1", "zh": "报告", "exam": "报告；汇报；报道；新闻报道", "c": ["annual report 年度报告", "report news 报道新闻"], "syn": ["account", "statement", "broadcast"], "fam":["reporter n. 记者"], "dif": "report 指书面或口头的系统汇报，或媒体新闻报道。", "pat": "The task force published a detailed report on healthcare reform.", "patZh": "专责小组发表了一份关于医疗改革的详细报告。"},
        {"w": "reporter", "ipa": "rɪˈpɔːtə", "pos": "n.", "s": "s1", "zh": "记者", "exam": "记者；通讯员", "c": ["investigative reporter 调查记者", "newspaper reporter 报社记者"], "syn": ["journalist", "correspondent", "pressman"], "fam":["report n. 报告"], "dif": "reporter 专指采集采写并报道新闻资讯的从业人员。", "pat": "The investigative reporter uncovered critical evidence of corruption.", "patZh": "这名调查记者揭露了腐腐败的关键证据。"},
        {"w": "reputation", "ipa": "ˌrepjuˈteɪʃn", "pos": "n.", "s": "s1", "zh": "声誉", "exam": "名声；声誉", "c": ["build a reputation 建立声誉", "good reputation 良好的名声"], "syn": ["fame", "prestige", "stature"], "fam":["reputable adj. 声誉良好的"], "dif": "reputation 指公众对某人、某机构品质成就的普遍评价。", "pat": "The university enjoys an international reputation for scientific excellence.", "patZh": "该大学在科学卓越方面享有国际声誉。"},
        {"w": "request", "ipa": "rɪˈkwest", "pos": "n. / vt.", "s": "s1", "zh": "请求", "exam": "请求；要求", "c": ["at the request of 应…的请求", "formal request 正式请求"], "syn": ["appeal", "solicitation", "demand"], "fam":["request v. 请求"], "dif": "request 侧重有礼貌或正式地提出希望得到帮助的表达。", "pat": "The manager submitted a formal request for additional office space.", "patZh": "经理提交了一份要增加办公空间的正式请求。"},
        {"w": "require", "ipa": "rɪˈkwaɪə", "pos": "vt.", "s": "s1", "zh": "要求", "exam": "需要；要求；命令", "c": ["require attention 需要注意", "require that 要求…"], "syn": ["need", "demand", "mandate"], "fam":["requirement n. 要求"], "dif": "require 指基于法律、标准或客观条件而提出的强制性需要。", "pat": "Modern job markets require professionals to continuously update their skills.", "patZh": "现代就业市场要求专业人士不断更新技能。"},
        {"w": "requirement", "ipa": "rɪˈkwaɪəmənt", "pos": "n.", "s": "s1", "zh": "要求", "exam": "要求；必要条件", "c": ["meet requirements 满足要求", "basic requirement 基本条件"], "syn": ["condition", "prerequisite", "specification"], "fam":["require v. 要求"], "dif": "requirement 指达到某种目的所必须满足的条件或标准。", "pat": "Fulfilling safety requirements is essential before releasing the software.", "patZh": "在发布软件前满足安全要求是至关重要的。"},
        {"w": "assess", "ipa": "əˈses", "pos": "vt.", "s": "s1", "zh": "评估", "exam": "评估；估价；评定", "c": ["assess risk 评估风险", "assess performance 评定绩效"], "syn": ["evaluate", "appraise", "estimate"], "fam":["assessment n. 评估"], "dif": "assess 侧重对性质、价值、数量或风险进行全面系统评价。", "pat": "Experts gather to assess the environmental impact of the new highway.", "patZh": "专家们聚集在一起评估新公路的环境影响。"},

        {"w": "assimilate", "ipa": "əˈsɪməleɪt", "pos": "v.", "s": "s2", "zh": "同化", "exam": "吸收；同化；融入", "c": ["assimilate into society 融入社会", "assimilate knowledge 吸收知识"], "syn": ["absorb", "integrate", "incorporate"], "fam":["assimilation n. 同化"], "dif": "assimilate 指将思想知识吸收融会贯通，或使人群融入主导文化。", "pat": "Immigrants often strive to assimilate into the cultural mainstream.", "patZh": "移民往往努力融入文化主流。"},
        {"w": "assist", "ipa": "əˈsɪst", "pos": "v. / n.", "s": "s2", "zh": "协助", "exam": "帮助；协助", "c": ["assist in doing 协助做…", "assist with 帮助处理…"], "syn": ["help", "aid", "support"], "fam":["assistance n. 援助", "assistant n. 助理"], "dif": "assist 比 help 正式，侧重在旁提供次要辅助配合。", "pat": "Volunteers stepped forward to assist emergency teams during the flood.", "patZh": "在洪水期间志愿者们走上前去协助紧急救援队。"},
        {"w": "assistance", "ipa": "əˈsɪstəns", "pos": "n.", "s": "s2", "zh": "援助", "exam": "帮助；援助", "c": ["financial assistance 经济援助", "provide assistance 提供帮助"], "syn": ["aid", "help", "support"], "fam":["assist v. 协助"], "dif": "assistance 指正式提供的支持、救助或经济援助。", "pat": "The government pledged financial assistance to small businesses in crisis.", "patZh": "政府承诺向处于危机中的小企业提供经济援助。"},
        {"w": "assistant", "ipa": "əˈsɪstənt", "pos": "n. / adj.", "s": "s2", "zh": "助理", "exam": "助手；助理；辅助的", "c": ["research assistant 研究助理", "executive assistant 行政助理"], "syn": ["aide", "helper", "deputy"], "fam":["assist v. 协助"], "dif": "assistant 特指协助上级或专业人员处理日常事务的职位人员。", "pat": "The executive assistant organized the schedule for the international conference.", "patZh": "行政助理为国际会议安排了日程。"},
        {"w": "assume", "ipa": "əˈsjuːm", "pos": "vt.", "s": "s2", "zh": "假设", "exam": "假定；假设；承担；呈现", "c": ["assume responsibility 承担责任", "assume that 假设…"], "syn": ["presume", "suppose", "undertake"], "fam":["assumption n. 假设"], "dif": "assume 指在无确凿证据前假设某事为真，或开始承担责任。", "pat": "We cannot simply assume that the economic recovery will continue indefinitely.", "patZh": "我们不能简单地假设经济复苏会无限期持续下去。"},
        {"w": "assumption", "ipa": "əˈsʌmpʃn", "pos": "n.", "s": "s2", "zh": "假设", "exam": "假定；假设；承担", "c": ["make an assumption 作出假设", "under the assumption 在…假设下"], "syn": ["presumption", "hypothesis", "premise"], "fam":["assume v. 假设"], "dif": "assumption 指基于缺乏证据推断出的前提设想。", "pat": "The decision was based on the false assumption that market demand would stay high.", "patZh": "该决定是建立在市场需求将保持高位这一错误假设之上的。"},
        {"w": "contribute", "ipa": "kənˈtrɪbjuːt", "pos": "v.", "s": "s2", "zh": "贡献", "exam": "捐献；贡献；促成；投稿", "c": ["contribute to 促成/贡献", "contribute money 捐款"], "syn": ["donate", "add", "conduce"], "fam":["contribution n. 贡献"], "dif": "contribute 搭配 to 表示促成某结果，或捐赠资金力量。", "pat": "Regular physical activity can contribute significantly to overall longevity.", "patZh": "规律的体育活动有助于显著促进整体长寿。"},
        {"w": "contribution", "ipa": "ˌkɒntrɪˈbjuːʃn", "pos": "n.", "s": "s2", "zh": "贡献", "exam": "贡献；捐款；稿件", "c": ["make a contribution 作出贡献", "significant contribution 显赫贡献"], "syn": ["donation", "input", "offering"], "fam":["contribute v. 贡献"], "dif": "contribution 指个人或团队做出的实质性有益成果或捐助。", "pat": "Her groundbreaking research made a major contribution to medical science.", "patZh": "她突破性的研究为医学科学作出了重大贡献。"},
        {"w": "controversial", "ipa": "ˌkɒntrəˈvɜːʃl", "pos": "adj.", "s": "s2", "zh": "有争议的", "exam": "引起争论的；有争议的", "c": ["controversial topic 有争议的话题", "controversial policy 有争议的政策"], "syn": ["disputed", "contentious", "debatable"], "fam":["controversy n. 争论"], "dif": "controversial 指引发不同阵营剧烈公开辩论争议的。", "pat": "The parliament passed a controversial law regarding digital copyright protection.", "patZh": "议会通过了一项关于数字版权保护的争议性法律。"},
        {"w": "controversy", "ipa": "ˈkɒntrəvɜːsi", "pos": "n.", "s": "s2", "zh": "争论", "exam": "争论；辩论", "c": ["arouse controversy 引起争论", "fuel controversy 助长争论"], "syn": ["dispute", "debate", "argument"], "fam":["controversial adj. 有争议的"], "dif": "controversy 指公众或学术界持续长期的公开争论。", "pat": "The sudden policy shift caused intense controversy among financial analysts.", "patZh": "突然的政策转向在金融分析师中引发了强烈的争论。"},
        {"w": "control", "ipa": "kənˈtrəʊl", "pos": "n. / vt.", "s": "s2", "zh": "控制", "exam": "控制；支配；克制；控制装置", "c": ["under control 在控制之下", "take control of 控制…"], "syn": ["command", "dominate", "regulate"], "fam":["controller n. 控制者"], "dif": "control 侧重掌握局势支配权或对系统加以约束管辖。", "pat": "Central banks strive to keep inflation under control during economic volatility.", "patZh": "中央银行在经济波动期间努力保持通胀处于控制之中。"},
        {"w": "convene", "ipa": "kənˈviːn", "pos": "v.", "s": "s2", "zh": "召开", "exam": "召开；召集；集合", "c": ["convene a meeting 召开会议", "convene a committee 召集委员会"], "syn": ["assemble", "summon", "gather"], "fam":["convention n. 大会；惯例"], "dif": "convene 侧重官方或正式召集许多人开会集合。", "pat": "The board decided to convene an extraordinary meeting to discuss the crisis.", "patZh": "董事会决定召开一次特别会议讨论危机。"},
        {"w": "convention", "ipa": "kənˈvenʃn", "pos": "n.", "s": "s2", "zh": "惯例", "exam": "大会；公约；惯例；传统", "c": ["social convention 社会惯例", "annual convention 年度大会"], "syn": ["custom", "protocol", "assembly"], "fam":["conventional adj. 传统的"], "dif": "convention 指社会长久形成的惯例俗成，或正式大型代表大会。", "pat": "Challenging traditional convention can lead to innovative artistic breakthroughs.", "patZh": "挑战传统惯例可以带来创新的艺术突破。"},
        {"w": "converge", "ipa": "kənˈvɜːdʒ", "pos": "vi.", "s": "s2", "zh": "趋同", "exam": "（在一点）会合；趋同；聚集", "c": ["converge on/towards 汇聚于…", "converge in opinion 意见趋同"], "syn": ["meet", "merge", "coincide"], "fam":["convergence n. 汇聚"], "dif": "converge 侧重多条道路、不同流派观点向同一焦点汇合趋同。", "pat": "Thousands of peaceful protesters began to converge on the central plaza.", "patZh": "数千名和平抗议者开始聚集在中央广场。"},
        {"w": "convey", "ipa": "kənˈveɪ", "pos": "vt.", "s": "s2", "zh": "传达", "exam": "传送；运送；表达；传达", "c": ["convey a message 传达信息", "convey emotions 表达情感"], "syn": ["communicate", "transmit", "express"], "fam":["conveyor n. 传送带"], "dif": "convey 侧重清楚地向他人传递信息、观点或情感。", "pat": "The art installation managed to convey complex feelings of nostalgia.", "patZh": "该艺术装置成功地传达了复杂的怀旧情感。"},
        {"w": "domain", "ipa": "dəˈmeɪn", "pos": "n.", "s": "s2", "zh": "领域", "exam": "领地；领域；域名", "c": ["public domain 公有领域", "economic domain 经济领域"], "syn": ["realm", "sphere", "territory"], "fam":["domain n. 领域"], "dif": "domain 指知识、活动或思想的专属范围领域。", "pat": "Cyber security has become a critical domain in modern national defense.", "patZh": "网络安全已成为现代国防中的一个关键领域。"},
        {"w": "domestic", "ipa": "dəˈmestɪk", "pos": "adj.", "s": "s2", "zh": "国内的", "exam": "本国的；国内的；家务的；驯养的", "c": ["domestic market 国内市场", "domestic violence 家庭暴力"], "syn": ["internal", "national", "household"], "fam":["domestically adv. 在国内"], "dif": "domestic 与 international（国际的）相对，指本国内部的。", "pat": "The government implemented new fiscal policies to stimulate domestic consumption.", "patZh": "政府实施了新的财政政策以刺激国内消费。"},
        {"w": "dominant", "ipa": "ˈdɒmɪnənt", "pos": "adj.", "s": "s2", "zh": "主导的", "exam": "占优势的；支配的；主导的", "c": ["dominant role 主导角色", "dominant position 优势地位"], "syn": ["prevailing", "chief", "superior"], "fam":["dominate v. 支配"], "dif": "dominant 指在力量、影响力或数量上占据支配主导地位的。", "pat": "English remains the dominant language in global business communications.", "patZh": "英语依然是全球商务沟通中的主导语言。"},
        {"w": "dominate", "ipa": "ˈdɒmɪneɪt", "pos": "v.", "s": "s2", "zh": "主导", "exam": "支配；统治；主导；耸立于", "c": ["dominate the market 主导市场", "dominate the discussion 支配讨论"], "syn": ["control", "rule", "govern"], "fam":["dominant adj. 占主导地位的"], "dif": "dominate 侧重全面控制、占据主要地位或统治支配。", "pat": "Tech giants continue to dominate the global cloud computing market.", "patZh": "科技巨头继续主导全球云计算市场。"},

        {"w": "doom", "ipa": "duːm", "pos": "n. / vt.", "s": "s3", "zh": "注定", "exam": "厄运；毁灭；注定（失败等）", "c": ["be doomed to 注定…", "doom and gloom 悲观绝望"], "syn": ["ruin", "destiny", "condemn"], "fam":["doomed adj. 注定失败的"], "dif": "doom 强调无法规避的悲惨命运、厄运或注定失败。", "pat": "Poor planning will inevitably doom any ambitious infrastructure project.", "patZh": "糟糕的规划将不可避免地使任何雄心勃勃的基础设施项目注定失败。"},
        {"w": "double", "ipa": "ˈdʌbl", "pos": "adj. / v. / n.", "s": "s3", "zh": "翻倍", "exam": "双重的；两倍的；加倍；翻倍", "c": ["double standard 双重标准", "double in size 规模翻倍"], "syn": ["dual", "twin", "duplicate"], "fam":["doubly adv. 双重地"], "dif": "double 侧重数量乘以二或兼具双重属性。", "pat": "The firm managed to double its net profits within three fiscal quarters.", "patZh": "该公司成功在三个财政季度内将其净利润翻倍。"},
        {"w": "doubt", "ipa": "daʊt", "pos": "n. / v.", "s": "s3", "zh": "怀疑", "exam": "怀疑；不信任；怀疑", "c": ["no doubt 毫无疑问", "cast doubt on 对…提出怀疑"], "syn": ["skepticism", "uncertainty", "distrust"], "fam":["doubtful adj. 怀疑的"], "dif": "doubt 指对某事的真实性、可行性持怀疑犹豫态度。", "pat": "There is little doubt that renewable energy is the future of power generation.", "patZh": "毫无疑问，可再生能源是发电的未来。"},
        {"w": "probe", "ipa": "prəʊb", "pos": "v. / n.", "s": "s3", "zh": "调查", "exam": "探查；查明；深入调查；探测器", "c": ["probe into 深入调查", "space probe 空间探测器"], "syn": ["investigate", "explore", "scrutinize"], "fam":["probe n. 探测"], "dif": "probe 侧重用工具或精细询问进行深入彻底的调查探究。", "pat": "Auditors were appointed to probe into suspicious accounting practices.", "patZh": "审计员被任命去深入调查可疑的会计行为。"},
        {"w": "procedure", "ipa": "prəˈsiːdʒə", "pos": "n.", "s": "s3", "zh": "程序", "exam": "程序；手续；步骤", "c": ["standard procedure 标准程序", "legal procedure 法定程序"], "syn": ["process", "routine", "protocol"], "fam":["procedural adj. 程序上的"], "dif": "procedure 指必须依次遵循的正式固定步骤手续。", "pat": "Surgeons must strictly adhere to sanitary procedures before operating.", "patZh": "外科医生在手术前必须严格遵守卫生程序。"},
        {"w": "proceed", "ipa": "prəˈsiːd", "pos": "vi.", "s": "s3", "zh": "继续进行", "exam": "进行；继续进行；发生", "c": ["proceed with 继续进行…", "proceed to 前往/进而做"], "syn": ["continue", "advance", "progress"], "fam":["proceeding n. 诉讼程序"], "dif": "proceed 侧重在停顿或筹备后继续向前推进。", "pat": "The court decided to proceed with the hearing despite the objection.", "patZh": "尽管有人反对，法院仍决定继续进行听证会。"},
        {"w": "proceeding", "ipa": "prəˈsiːdɪŋ", "pos": "n.", "s": "s3", "zh": "诉讼程序", "exam": "诉讼；议程；过程", "c": ["legal proceedings 法律诉讼", "conference proceedings 会议论文集"], "syn": ["litigation", "action", "records"], "fam":["proceed v. 继续进行"], "dif": "proceeding 复数特指法院的法律诉讼程序或会议记录。", "pat": "The company initiated legal proceedings against its former partner.", "patZh": "该公司发起了针对前合作伙伴的法律诉讼。"},
        {"w": "process", "ipa": "ˈprəʊses", "pos": "n. / vt.", "s": "s3", "zh": "过程", "exam": "过程；进程；加工；处理", "c": ["process data 处理数据", "in the process of 在…过程中"], "syn": ["procedure", "course", "handle"], "fam":["processing n. 加工处理"], "dif": "process 指随时间推移演进的自然或人为操作过程。", "pat": "Developing a robust medical vaccine is a lengthy and complex process.", "patZh": "研发一款强效的医疗疫苗是一个漫长而复杂的过程。"},
        {"w": "procession", "ipa": "prəˈseʃn", "pos": "n.", "s": "s3", "zh": "行列", "exam": "队伍；行列", "c": ["funeral procession 葬礼队伍", "procession of cars 车队"], "syn": ["parade", "cavalcade", "march"], "fam":["process v. 列队前进"], "dif": "procession 特指按特定仪式顺次前进的人群队伍或车队。", "pat": "A colorful carnival procession marched through the historical district.", "patZh": "一支色彩斑斓的狂欢节队伍游行穿过了历史街区。"},
        {"w": "proclaim", "ipa": "prəˈkleɪm", "pos": "vt.", "s": "s3", "zh": "宣告", "exam": "宣告；声明；表明", "c": ["proclaim independence 宣告独立", "proclaim victory 宣布胜利"], "syn": ["declare", "announce", "assert"], "fam":["proclamation n. 宣言"], "dif": "proclaim 侧重正式、庄严地向大众公开宣告某重大事实。", "pat": "The president decided to proclaim a national day of mourning.", "patZh": "总统决定宣告设立国家哀悼日。"},
        {"w": "produce", "ipa": "prəˈdjuːs", "pos": "vt. / n.", "s": "s3", "zh": "生产", "exam": "生产；产生；展现；农产品", "c": ["produce results 产生结果", "fresh produce 新鲜农产品"], "syn": ["manufacture", "generate", "yield"], "fam":["product n. 产品", "producer n. 生产者"], "dif": "produce 动词指制造生产，重音在前为农产品总称。", "pat": "Modern solar panels produce clean electricity even on cloudy days.", "patZh": "现代太阳能电池板即使在阴天也能生产清洁电力。"},
        {"w": "product", "ipa": "ˈprɒdʌkt", "pos": "n.", "s": "s3", "zh": "产品", "exam": "产品；产物；结果", "c": ["consumer product 消费品", "finished product 成品"], "syn": ["goods", "merchandise", "output"], "fam":["produce v. 生产"], "dif": "product 指工业制造或农业加工出的具体制成品。", "pat": "The new smartphone rapidly became the company's best-selling product.", "patZh": "这款新智能手机迅速成为了该公司最畅销的产品。"},
        {"w": "production", "ipa": "prəˈdʌkʃn", "pos": "n.", "s": "s3", "zh": "生产", "exam": "生产；产量；制作", "c": ["mass production 批量生产", "line of production 生产线"], "syn": ["manufacturing", "output", "creation"], "fam":["productive adj. 生产的"], "dif": "production 指制造生产的过程或总产量。", "pat": "Automated robotics helped streamline factory production significantly.", "patZh": "自动化机器人帮助大幅简化了工厂生产。"},
        {"w": "productive", "ipa": "prəˈdʌktɪv", "pos": "adj.", "s": "s3", "zh": "富有成效的", "exam": "多产的；富有成效的；生产的", "c": ["productive meeting 富有成效的会议", "productive worker 高产工人"], "syn": ["fruitful", "prolific", "constructive"], "fam":["productivity n. 生产力"], "dif": "productive 强调产出高、充满成效或多产。", "pat": "Both parties held a highly productive discussion on bilateral trade.", "patZh": "双方就双边贸易举行了一场高度富有成效的讨论。"},
        {"w": "productivity", "ipa": "ˌprɒdʌkˈtɪvəti", "pos": "n.", "s": "s3", "zh": "生产力", "exam": "生产率；生产力", "c": ["increase productivity 提高生产力", "labor productivity 劳动生产率"], "syn": ["efficiency", "yield", "output rate"], "fam":["productive adj. 富有成效的"], "dif": "productivity 指单位时间内投入与产出比率。", "pat": "Investing in modern equipment boosted worker productivity by twenty percent.", "patZh": "投资现代设备将工人生产力提升了百分之二十。"},
        {"w": "profession", "ipa": "prəˈfeʃn", "pos": "n.", "s": "s3", "zh": "职业", "exam": "职业；同行；表白", "c": ["medical profession 医疗行业", "by profession 按职业论"], "syn": ["occupation", "career", "vocation"], "fam":["professional adj. 专业的"], "dif": "profession 特指需要高等教育和专业训练的专门职业（如医生律师）。", "pat": "Entering the teaching profession requires dedication and continuous study.", "patZh": "进入教师这一职业需要奉献精神和持续学习。"},
        {"w": "professional", "ipa": "prəˈfeʃənl", "pos": "adj. / n.", "s": "s3", "zh": "专业的", "exam": "专业的；职业的；专业人员", "c": ["professional advice 专业建议", "young professional 年轻专业人士"], "syn": ["expert", "qualified", "specialist"], "fam":["profession n. 职业"], "dif": "professional 指符合行业高标准的专业化人员或水准。", "pat": "The firm employs highly qualified professionals to manage clients' assets.", "patZh": "该公司聘用高素质的专业人士来管理客户资产。"},
        {"w": "expand", "ipa": "ɪkˈspænd", "pos": "v.", "s": "s3", "zh": "扩张", "exam": "扩大；扩展；膨胀", "c": ["expand business 扩张业务", "expand horizons 开阔视野"], "syn": ["enlarge", "extend", "broaden"], "fam":["expansion n. 扩张"], "dif": "expand 侧重在规模、范围、体积或数量上的扩大展开。", "pat": "The retailer plans to expand its operational store network internationally.", "patZh": "该零售商计划在国际上扩张其运营门店网络。"},
        {"w": "expansion", "ipa": "ɪkˈspænʃn", "pos": "n.", "s": "s3", "zh": "扩张", "exam": "扩大；扩张；膨胀", "c": ["economic expansion 经济扩张", "rapid expansion 快速扩张"], "syn": ["growth", "extension", "enlargement"], "fam":["expand v. 扩张"], "dif": "expansion 指规模、业务或领土扩大的过程或状态。", "pat": "Rapid market expansion created thousands of new employment opportunities.", "patZh": "快速的市场扩张创造了数以千计的新就业机会。"}
    ]
}

# Unit 24 Data (53 words)
unit24_data = {
    "unit": 24,
    "stories": [
        {
            "id": "s1",
            "en": "Scientific Inquiry and Institutional Standards",
            "zh": "科学探究与机构标准",
            "theme": "科学 / 机构",
            "ps": [
                {
                    "en": "Exceeding initial [[expectations|expectation]], scholars with deep research [[experience]] conducted a groundbreaking [[experiment]]. They consulted a leading [[expert]] who shared her vast [[expertise]] before the patent was set to [[expire]].",
                    "zh": "超出最初的预期，拥有深厚研究经验的学者们进行了一项突破性的实验。他们咨询了一位顶尖专家，在专利即将到期前分享了她的广博专业知识。"
                },
                {
                    "en": "Relying on natural [[instinct]], directors established a research [[institute]] as a formal [[institution]]. To protecting asset value, they applied for financial [[insurance]] to [[insure]] against market risks.",
                    "zh": "依靠直觉，管理者们建立了一家研究机构作为正式制度。为了保护资产价值，他们申请了金融保险，以投保应对市场风险。"
                },
                {
                    "en": "Maintaining [[integral]] safety rules allowed engineers to [[integrate]] AI modules while upholding moral [[integrity]]. Driven by [[curious]] inquiries, student [[curiosity]] focused on how global [[currency]] reflects the [[current]] economic state.",
                    "zh": "维持完整的安全规则让工程师们在维护道德诚信的同时得以整合人工智能模块。在好奇探究的驱动下，学生的好奇心集中在全球货币如何反映当前经济状况上。"
                }
            ]
        },
        {
            "id": "s2",
            "en": "Evaluating Risks and Awkward Issues",
            "zh": "评估风险与尴尬议题",
            "theme": "社会 / 风险",
            "ps": [
                {
                    "en": "To [[cut]] operational expenses and manage [[cumulative]] debt, financial analysts computed the [[average]] profit. They advised executives to [[avoid]] hasty choices, stay [[awake]] during crisis, and [[award]] resilient teams, making every leader [[aware]] of potential challenges.",
                    "zh": "为了削减运营费用并管理累积债务，金融分析师计算了平均利润。他们建议高管避免草率决定，在危机期间保持清醒，并奖励有韧性的团队，使每位领导者都意识到潜在的挑战。"
                },
                {
                    "en": "Handling an [[awkward]] negotiation, diplomats avoided [[extravagant]] claims under [[extreme]] pressure. Although the underlying danger remained [[invisible]], they sought to [[invoke]] treaty terms that would [[involve]] all member states in resolving a contentious [[issue]] over a single budget [[item]].",
                    "zh": "在处理一场尴尬的谈判时，外交官们在极度压力下避免了奢华不实的主张。尽管潜在的危险依然隐形，他们试图援引条约条款，让所有成员国都参与解决围绕单一预算项目的有争议议题。"
                },
                {
                    "en": "Legal advisors warned that bad decisions could [[overturn]] court rulings and [[overwhelm]] local institutions.",
                    "zh": "法律顾问警告说，糟糕的决定可能会推翻法院裁决并压垮当地机构。"
                }
            ]
        },
        {
            "id": "s3",
            "en": "The Quest for Excellence",
            "zh": "追求卓越的旅程",
            "theme": "个人 / 追求",
            "ps": [
                {
                    "en": "Investors agreed to [[purchase]] new equipment to [[pursue]] sustainable growth. In their relentless [[pursuit]] of truth, researchers solved a complex [[puzzle]], opting to [[reverse]] outdated procedures and [[review]] recent test results.",
                    "zh": "投资者同意购买新设备以追求可持续增长。在对真理的不懈追求中，研究人员解开了一个复杂的谜团，选择颠倒过时的程序并审查最近的测试结果。"
                },
                {
                    "en": "Specialists met to [[revise]] regulatory guidelines and [[revive]] local commerce. Giving a substantial [[reward]] to innovative talent enriched [[rich]] communities, causing profit to [[rise]] without increasing systemic [[risk]].",
                    "zh": "专家们开会修改监管指南并复苏当地商业。给予创新人才实质性奖励丰富了富裕社区，在不增加系统性风险的情况下促进了利润增长。"
                },
                {
                    "en": "Facing a tough [[rival|riva]], each contestant embraced their unique [[role]]. They decided to [[roll]] out fresh strategies, trace the root cause to its [[root]], plan a clear [[route]], and establish a steady [[routine]].",
                    "zh": "面对强劲的对手，每位参赛者都拥抱了自己独特的角色。他们决定推出全新的策略，将根本原因追溯至根源，规划一条清晰的路线，并建立稳定的日常惯例。"
                }
            ]
        }
    ],
    "words": [
        {"w": "expectation", "ipa": "ˌekspekˈteɪʃn", "pos": "n.", "s": "s1", "zh": "期望", "exam": "期望；预期；前程", "c": ["live up to expectations 达到期望", "beyond expectation 超出预期"], "syn": ["anticipation", "prospect", "hope"], "fam":["expect v. 期望"], "dif": "expectation 指对未来事物发生的预料期待或期望。", "pat": "The new product line exceeded all financial expectations.", "patZh": "新产品线超出了所有财务预期。"},
        {"w": "experience", "ipa": "ɪkˈspɪəriəns", "pos": "n. / vt.", "s": "s1", "zh": "经验", "exam": "经验；经历；体验；感受", "c": ["gain experience 积累经验", "work experience 工作经验"], "syn": ["knowledge", "background", "undergo"], "fam":["experienced adj. 有经验的"], "dif": "experience 作不可数名词指经验，作可数名词指个人经历。", "pat": "Hands-on work experience is invaluable for career advancement.", "patZh": "亲身体验的工作经验对职业提升宝贵无比。"},
        {"w": "experiment", "ipa": "ɪkˈsperɪmənt", "pos": "n. / vi.", "s": "s1", "zh": "实验", "exam": "实验；试验；做实验", "c": ["conduct an experiment 做实验", "scientific experiment 科学实验"], "syn": ["test", "trial", "investigation"], "fam":["experimental adj. 实验性的"], "dif": "experiment 侧重为检验某种假设科学理论而进行的试验操作。", "pat": "Researchers performed a controlled experiment to test the hypothesis.", "patZh": "研究人员进行了一项对照实验来检验该假设。"},
        {"w": "expert", "ipa": "ˈekspɜːt", "pos": "n. / adj.", "s": "s1", "zh": "专家", "exam": "专家；能手；熟练的；专家的", "c": ["industry expert 行业专家", "expert advice 专家的建议"], "syn": ["specialist", "authority", "master"], "fam":["expertise n. 专门知识"], "dif": "expert 指在特定专业领域具有深厚知识和技能的人士。", "pat": "The court summoned an expert witness to evaluate the technical report.", "patZh": "法院传唤了一位专家证人来评估该技术报告。"},
        {"w": "expertise", "ipa": "ˌekspɜːˈtiːz", "pos": "n.", "s": "s1", "zh": "专门知识", "exam": "专门知识；专长", "c": ["technical expertise 技术专长", "professional expertise 专业知识"], "syn": ["know-how", "skill", "mastery"], "fam":["expert n. 专家"], "dif": "expertise 指在某领域长期积累的深厚专门技能与知识。", "pat": "Her technical expertise proved vital during the software overhaul.", "patZh": "在软件彻底改造期间，她的技术专长被证明至关重要。"},
        {"w": "expire", "ipa": "ɪkˈspaɪə", "pos": "vi.", "s": "s1", "zh": "到期", "exam": "期满；到期；终止", "c": ["passport expire 护照到期", "contract expire 合同到期"], "syn": ["terminate", "elapse", "run out"], "fam":["expiration n. 到期"], "dif": "expire 指协议、证件、期限届满失效。", "pat": "Check your passport validity before booking international flights as it may expire.", "patZh": "在预订国际航班前检查护照有效期，因为护照可能会到期。"},
        {"w": "instinct", "ipa": "ˈɪnstɪŋkt", "pos": "n.", "s": "s1", "zh": "直觉", "exam": "本能；直觉；天性", "c": ["basic instinct 基本本能", "by instinct 出于本能"], "syn": ["intuition", "impulse", "aptitude"], "fam":["instinctive adj. 本能的"], "dif": "instinct 指与生俱来的本能反应或无须理性推理的直觉。", "pat": "Animals rely on natural instinct to navigate long migrations.", "patZh": "动物依靠天然本能来进行长途迁徙。"},
        {"w": "institute", "ipa": "ˈɪnstɪtjuːt", "pos": "n. / vt.", "s": "s1", "zh": "机构", "exam": "研究所；学院；建立；制定", "c": ["research institute 研究所", "institute legal action 发起诉讼"], "syn": ["academy", "foundation", "establish"], "fam":["institution n. 机构；制度"], "dif": "institute 作名词指专门的科研教育机构，作动词指建立实施规章。", "pat": "The medical institute announced a breakthrough in cancer research.", "patZh": "该医疗研究所宣布了癌症研究方面的突破。"},
        {"w": "institution", "ipa": "ˌɪnstɪˈtjuːʃn", "pos": "n.", "s": "s1", "zh": "制度", "exam": "社会机构；制度；建立", "c": ["financial institution 金融机构", "social institution 社会制度"], "syn": ["organization", "system", "establishment"], "fam":["institutional adj. 机构的"], "dif": "institution 指社会公共机构、知名大学，或长久确立的社会制度。", "pat": "Trust in public institutions remains vital for democratic stability.", "patZh": "对公共机构的信任对于民主稳定依然至关重要。"},
        {"w": "insurance", "ipa": "ɪnˈʃʊərəns", "pos": "n.", "s": "s1", "zh": "保险", "exam": "保险；保险费；保障", "c": ["health insurance 健康保险", "insurance policy 保险单"], "syn": ["coverage", "protection", "assurance"], "fam":["insure v. 投保"], "dif": "insurance 特指支付保费以防范风险损失的商业保险体系。", "pat": "Comprehensive health insurance covers emergency hospital visits.", "patZh": "综合健康保险涵盖紧急住院费用。"},
        {"w": "insure", "ipa": "ɪnˈʃʊə", "pos": "vt.", "s": "s1", "zh": "投保", "exam": "给…保险；投保；保证", "c": ["insure against loss 为…投保防范损失", "insure property 给财产保险"], "syn": ["underwrite", "guarantee", "protect"], "fam":["insurance n. 保险"], "dif": "insure 特指向保险公司购买保费投保。", "pat": "Homeowners should insure their properties against flood and fire damage.", "patZh": "业主应当为其财产投保以防范洪水和火灾损失。"},
        {"w": "integral", "ipa": "ˈɪntɪɡrəl", "pos": "adj.", "s": "s1", "zh": "不可或缺的", "exam": "构成整体所必需的；不可或缺的；完整的", "c": ["integral part 不可或缺的部分", "integral component 核心组件"], "syn": ["essential", "fundamental", "vital"], "fam":["integrate v. 整合"], "dif": "integral 强调作为整体不可分割的有机组成部分。", "pat": "Teamwork is an integral element of our corporate culture.", "patZh": "团队合作是公司文化中不可或缺的要素。"},
        {"w": "integrate", "ipa": "ˈɪntɪɡreɪt", "pos": "v.", "s": "s1", "zh": "整合", "exam": "使合并；使成为一体；整合", "c": ["integrate into/with 整合入…", "integrate systems 整合系统"], "syn": ["incorporate", "merge", "combine"], "fam":["integration n. 整合"], "dif": "integrate 侧重将不同部分有机结合融为一体。", "pat": "The new software allows users to integrate cloud services seamlessly.", "patZh": "新软件允许用户无缝整合云服务。"},
        {"w": "integrity", "ipa": "ɪnˈteɡrəti", "pos": "n.", "s": "s1", "zh": "诚信", "exam": "正直；诚实；完整；完全", "c": ["personal integrity 个人诚信", "structural integrity 结构完整性"], "syn": ["honesty", "uprightness", "wholeness"], "fam":["integral adj. 完整的"], "dif": "integrity 侧重坚守道德操守的正直诚信，或结构的完整性。", "pat": "Leaders must act with high moral integrity to gain public trust.", "patZh": "领导者必须以高度的道德诚信行事以赢得公众信任。"},
        {"w": "curious", "ipa": "ˈkjʊəriəs", "pos": "adj.", "s": "s1", "zh": "好奇的", "exam": "好奇的；求知的；奇特的", "c": ["be curious about 对…感到好奇", "curious expression 奇特的表情"], "syn": ["inquisitive", "eager", "peculiar"], "fam":["curiosity n. 好奇心"], "dif": "curious 指对新事物充满强烈求知欲望或事物奇特。", "pat": "Children are naturally curious about the mysteries of the natural world.", "patZh": "孩子们对自然界的奥秘天然感到好奇。"},
        {"w": "curiosity", "ipa": "ˌkjʊəriˈɒsəti", "pos": "n.", "s": "s1", "zh": "好奇心", "exam": "好奇心；求知欲；奇珍异宝", "c": ["out of curiosity 出于好奇", "arouse curiosity 引起好奇心"], "syn": ["inquisitiveness", "interest", "rarity"], "fam":["curious adj. 好奇的"], "dif": "curiosity 指强烈的求知探究心理，或罕见奇特之物。", "pat": "Out of curiosity, she opened the old leather-bound journal.", "patZh": "出于好奇，她打开了那本精装旧皮质日记。"},
        {"w": "currency", "ipa": "ˈkʌrənsi", "pos": "n.", "s": "s1", "zh": "货币", "exam": "货币；通用；流行", "c": ["foreign currency 外币", "gain currency 流行开来"], "syn": ["money", "legal tender", "prevalence"], "fam":["current adj. 当前的"], "dif": "currency 指流通的国家法定货币，或概念的普遍流行。", "pat": "Fluctuations in foreign currency exchange rates affect international trade.", "patZh": "外币汇率的波动会影响国际贸易。"},
        {"w": "current", "ipa": "ˈkʌrənt", "pos": "adj. / n.", "s": "s1", "zh": "当前的", "exam": "当前的；通行的；水流；电流；趋势", "c": ["current situation 当前局势", "ocean current 洋流"], "syn": ["present", "prevailing", "flow"], "fam":["currently adv. 当前"], "dif": "current 作形容词指当前的，作名词指水流、电流或思潮。", "pat": "Under current regulations, all safety tests must be documented.", "patZh": "在当前规定下，所有安全测试都必须予以记录。"},

        {"w": "cut", "ipa": "kʌt", "pos": "v. / n.", "s": "s2", "zh": "削减", "exam": "切；割；削减；伤口；削减", "c": ["cut costs 削减成本", "cut down 砍倒/减少"], "syn": ["reduce", "slash", "incision"], "fam":["cutter n. 切割器"], "dif": "cut 可指物理上的切割切开，也可指大幅削减预算费用。", "pat": "The board decided to cut operational spending to preserve cash reserves.", "patZh": "董事会决定削减运营支出以保留现金储备。"},
        {"w": "cumulative", "ipa": "ˈkjuːmjələtɪv", "pos": "adj.", "s": "s2", "zh": "累积的", "exam": "累积的；渐增的", "c": ["cumulative effect 累积效应", "cumulative total 累计总额"], "syn": ["accumulated", "increasing", "aggregate"], "fam":["accumulate v. 积累"], "dif": "cumulative 强调随着时间连续不断叠加积累而成的。", "pat": "The cumulative impact of long-term stress can damage physical health.", "patZh": "长期压力的累积影响会损害身体健康。"},
        {"w": "average", "ipa": "ˈævərɪdʒ", "pos": "adj. / n. / v.", "s": "s2", "zh": "平均的", "exam": "平均的；普通的；平均数；平均为", "c": ["above average 高于平均水平", "on average 平均而言"], "syn": ["mean", "ordinary", "standard"], "fam":["average adj. 平均的"], "dif": "average 指数学上的算术平均数，或一般的、普通的。", "pat": "On average, employees work forty hours per week in this company.", "patZh": "平均而言，这家公司的员工每周工作四十个小时。"},
        {"w": "avoid", "ipa": "əˈvɔɪd", "pos": "vt.", "s": "s2", "zh": "避免", "exam": "避免；回避；避开", "c": ["avoid risk 避免风险", "avoid doing 避免做…"], "syn": ["evade", "shun", "prevent"], "fam":["avoidance n. 回避"], "dif": "avoid 侧重采取措施防止不愉快或危险的事情发生。", "pat": "Drivers should slow down in bad weather to avoid accidents.", "patZh": "驾驶员在恶劣天气下应当减速以避免事故。"},
        {"w": "awake", "ipa": "əˈweɪk", "pos": "adj. / v.", "s": "s2", "zh": "清醒的", "exam": "醒着的；警觉的；唤醒；意识到", "c": ["wide awake 完全清醒的", "awake to 意识到…"], "syn": ["conscious", "alert", "waken"], "fam":["awaken v. 唤醒"], "dif": "awake 侧重处于非睡眠的清醒状态或对风险警觉。", "pat": "She lay awake listening to the heavy rain falling on the roof.", "patZh": "她躺着清醒地听着倾盆大雨敲打屋顶。"},
        {"w": "award", "ipa": "əˈwɔːd", "pos": "vt. / n.", "s": "s2", "zh": "奖励", "exam": "授予；奖赏；奖品；裁决", "c": ["win an award 获奖", "award a contract 授予合同"], "syn": ["grant", "prize", "honesty"], "fam":["awardee n. 获奖者"], "dif": "award 侧重经正式评判授予奖项、荣誉或判定赔偿。", "pat": "The jury decided to award the young scientist a research grant.", "patZh": "评审团决定向这位年轻科学家授予一项研究资助。"},
        {"w": "aware", "ipa": "əˈweə", "pos": "adj.", "s": "s2", "zh": "意识到的", "exam": "意识到的；知道的", "c": ["be aware of 意识到…", "environmentally aware 具环保意识的"], "syn": ["conscious", "mindful", "informed"], "fam":["awareness n. 意识"], "dif": "aware 强调通过感知、察觉而对某情况有清楚了解。", "pat": "Consumers are increasingly aware of the health risks of sugar.", "patZh": "消费者越来越意识到糖的健康风险。"},
        {"w": "awkward", "ipa": "ˈɔːkwəd", "pos": "adj.", "s": "s2", "zh": "尴尬的", "exam": "笨拙的；尴尬的；难处理的", "c": ["awkward silence 尴尬的沉默", "awkward situation 难处理的局势"], "syn": ["clumsy", "embarrassing", "ungainly"], "fam":["awkwardly adv. 笨拙地"], "dif": "awkward 指动作笨拙、局面尴尬或问题棘手难办。", "pat": "There was an awkward silence when the embarrassing mistake was revealed.", "patZh": "当令人尴尬的错误被揭露时，现场出现了一片尴尬的沉默。"},
        {"w": "extravagant", "ipa": "ɪkˈstrævəɡənt", "pos": "adj.", "s": "s2", "zh": "奢侈的", "exam": "奢侈的；挥霍的；过度的", "c": ["extravagant lifestyle 奢侈的生活方式", "extravagant claim 过度的断言"], "syn": ["lavish", "wasteful", "excessive"], "fam":["extravagance n. 挥霍"], "dif": "extravagant 指超出合理限度的挥霍、奢华或过分评价。", "pat": "The CEO was criticized for his extravagant spending on private jets.", "patZh": "首席执行官因在私人飞机上的奢华花费而受到批评。"},
        {"w": "extreme", "ipa": "ɪkˈstriːm", "pos": "adj. / n.", "s": "s2", "zh": "极度的", "exam": "极度的；末端的；极端", "c": ["extreme weather 极端天气", "go to extremes 走极端"], "syn": ["intense", "severe", "utmost"], "fam":["extremely adv. 极度地"], "dif": "extreme 指程度达到最高极限或处在最边缘末端。", "pat": "Mountaineers face extreme cold and severe oxygen deprivation on high peaks.", "patZh": "登山者在高峰上面对极度严寒和严重缺氧。"},
        {"w": "invisible", "ipa": "ɪnˈvɪzəbl", "pos": "adj.", "s": "s2", "zh": "隐形的", "exam": "看不见的；无形的", "c": ["invisible barrier 无形的屏障", "invisible ink 隐形墨水"], "syn": ["unseen", "imperceptible", "hidden"], "fam":["invisibility n. 隐形"], "dif": "invisible 指肉眼无法看见或在经济社会中无形存在的。", "pat": "Microscopic bacteria are invisible to the naked eye.", "patZh": "微小的细菌用肉眼是看不见的。"},
        {"w": "invoke", "ipa": "ɪnˈvəʊk", "pos": "vt.", "s": "s2", "zh": "援引", "exam": "援引；祈求；唤起", "c": ["invoke a clause 援引条款", "invoke a law 引用法律"], "syn": ["cite", "summon", "appeal to"], "fam":["invocation n. 祈求；援引"], "dif": "invoke 侧重在辩论或法律诉讼中援引法规或祈求神灵。", "pat": "The defense attorney chose to invoke constitutional rights during trial.", "patZh": "辩护律师选择在审判期间援引宪法权利。"},
        {"w": "involve", "ipa": "ɪnˈvɒlv", "pos": "vt.", "s": "s2", "zh": "包含", "exam": "包含；牵涉；使参与", "c": ["involve doing 包含做…", "be involved in 参与…"], "syn": ["include", "entail", "engage"], "fam":["involvement n. 参与"], "dif": "involve 侧重作为必要部分包含其中，或使人卷入参与。", "pat": "Implementing the new policy will involve collaboration among multiple departments.", "patZh": "实施新政策将需要多个部门之间的协作。"},
        {"w": "issue", "ipa": "ˈɪʃuː", "pos": "n. / vt.", "s": "s2", "zh": "议题", "exam": "问题；议题；发行；颁布", "c": ["key issue 关键议题", "issue a statement 发表声明"], "syn": ["topic", "matter", "release"], "fam":["issuance n. 发行"], "dif": "issue 侧重引起讨论辩论的核心争议焦点，或官方发行证书。", "pat": "Climate change has become a crucial political issue worldwide.", "patZh": "气候变化已成为全球范围内一个关键的政治议题。"},
        {"w": "item", "ipa": "ˈaɪtəm", "pos": "n.", "s": "s2", "zh": "项目", "exam": "条；项目；商品", "c": ["budget item 预算项目", "item of news 一条新闻"], "syn": ["object", "article", "entry"], "fam":["itemize v. 逐项列出"], "dif": "item 指清单列表中的单一条目、具体单件物品。", "pat": "The committee reviewed each item on the meeting agenda carefully.", "patZh": "委员会仔细审查了会议议程上的每一项。"},
        {"w": "overturn", "ipa": "ˌəʊvəˈtɜːn", "pos": "v. / n.", "s": "s2", "zh": "推翻", "exam": "推翻；翻倒；颠覆", "c": ["overturn a decision 推翻决定", "overturn a boat 翻船"], "syn": ["reverse", "upend", "overthrow"], "fam":["overturn v. 推翻"], "dif": "overturn 指物理上的翻倒，或法律判决主张被正式撤销推翻。", "pat": "The supreme court voted to overturn the lower court's ruling.", "patZh": "最高法院投票决定推翻下级法院的裁决。"},
        {"w": "overwhelm", "ipa": "ˌəʊvəˈwelm", "pos": "vt.", "s": "s2", "zh": "压垮", "exam": "压倒；使受不了；征服", "c": ["be overwhelmed by 被…压垮", "overwhelm the defense 冲垮防御"], "syn": ["overpower", "swamp", "crush"], "fam":["overwhelming adj. 压倒性的"], "dif": "overwhelm 指在力量、数量或情绪上压倒压垮对方。", "pat": "The sudden surge of online orders threatened to overwhelm the warehouse.", "patZh": "线上订单的突然激增可能会压垮仓库。"},

        {"w": "purchase", "ipa": "ˈpɜːtʃəs", "pos": "vt. / n.", "s": "s3", "zh": "购买", "exam": "购买；采购；购买物", "c": ["purchase goods 购买商品", "make a purchase 开展采购"], "syn": ["buy", "acquire", "procure"], "fam":["purchaser n. 购买者"], "dif": "purchase 比 buy 更正式，常用于商业交易采购。", "pat": "The agency approved funds to purchase advanced medical equipment.", "patZh": "该机构批准资金采购先进的医疗设备。"},
        {"w": "pursue", "ipa": "pəˈsjuː", "pos": "vt.", "s": "s3", "zh": "追求", "exam": "追求；追赶；贯彻；从事", "c": ["pursue a goal 追求目标", "pursue a career 从事职业"], "syn": ["chase", "seek", "follow"], "fam":["pursuit n. 追求"], "dif": "pursue 侧重持续不懈地追赶目标、理想或事业。", "pat": "She decided to move abroad to pursue higher academic qualifications.", "patZh": "她决定出国以追求更高的学术学历。"},
        {"w": "pursuit", "ipa": "pəˈsjuːt", "pos": "n.", "s": "s3", "zh": "追求", "exam": "追求；追赶；嗜好", "c": ["in pursuit of 追求…", "academic pursuits 学术追求"], "syn": ["quest", "chase", "search"], "fam":["pursue v. 追求"], "dif": "pursuit 指追求目标的过程，或业余爱好的活动。", "pat": "The endless pursuit of knowledge drives scientific advancement.", "patZh": "对知识的无止境追求推动着科学进步。"},
        {"w": "puzzle", "ipa": "ˈpʌzl", "pos": "n. / v.", "s": "s3", "zh": "谜团", "exam": "谜；难题；使困惑", "c": ["solve a puzzle 解开谜团", "jigsaw puzzle 拼图"], "syn": ["riddle", "enigma", "perplex"], "fam":["puzzling adj. 令人困惑的"], "dif": "puzzle 指令人百思不得其解的谜团，或使人感到困惑。", "pat": "His mysterious disappearance remains an unsolved puzzle for detectives.", "patZh": "他的神秘失踪对于侦探来说依然是一个未解之谜。"},
        {"w": "reverse", "ipa": "rɪˈvɜːs", "pos": "v. / adj. / n.", "s": "s3", "zh": "颠倒", "exam": "颠倒；彻底改变；相反的；背面", "c": ["reverse the trend 扭转趋势", "in reverse 颠倒地"], "syn": ["invert", "undo", "opposite"], "fam":["reversal n. 颠倒"], "dif": "reverse 指方向、顺序或政策彻底向相反方向转变。", "pat": "The new manager hopes to reverse the company's declining sales.", "patZh": "新经理希望扭转公司销售额下滑的趋势。"},
        {"w": "review", "ipa": "rɪˈvjuː", "pos": "n. / vt.", "s": "s3", "zh": "审查", "exam": "审查；复习；评论；回顾", "c": ["peer review 同行评审", "under review 在审查中"], "syn": ["examine", "inspect", "appraisal"], "fam":["reviewer n. 评论员"], "dif": "review 侧重正式的复查、评估审查或书刊剧评。", "pat": "The committee will review all job applications by the end of the week.", "patZh": "委员会将在本周末前审查所有求职申请。"},
        {"w": "revise", "ipa": "rɪˈvaɪz", "pos": "vt.", "s": "s3", "zh": "修改", "exam": "修改；修订；复习", "c": ["revise a draft 修改草案", "revise a plan 修订计划"], "syn": ["amend", "modify", "alter"], "fam":["revision n. 修订"], "dif": "revise 指对书稿、法律条款或计划进行改动修订。", "pat": "The author had to revise the manuscript based on editors' feedback.", "patZh": "作者不得不根据编辑的反馈修改手稿。"},
        {"w": "revive", "ipa": "rɪˈvaɪv", "pos": "v.", "s": "s3", "zh": "复苏", "exam": "（使）复苏；恢复；重新上演", "c": ["revive the economy 复苏经济", "revive interest 重新激发兴趣"], "syn": ["resuscitate", "renew", "restore"], "fam":["revival n. 复苏"], "dif": "revive 指使处于衰落、濒死状态的事物重新恢复生机。", "pat": "Tax incentives helped revive local businesses after the recession.", "patZh": "税收优惠有助于在衰退后复苏当地商业。"},
        {"w": "reward", "ipa": "rɪˈwɔːd", "pos": "n. / vt.", "s": "s3", "zh": "奖励", "exam": "报答；奖赏；报酬；酬谢", "c": ["financial reward 经济奖励", "reward effort 奖赏努力"], "syn": ["recompense", "prize", "remuneration"], "fam":["rewarding adj. 值得的"], "dif": "reward 侧重对付出辛劳、善行给与的报答酬谢。", "pat": "Hard work and dedication will eventually bring a rich reward.", "patZh": "努力工作和奉献精神最终会带来丰厚的回报。"},
        {"w": "rich", "ipa": "rɪtʃ", "pos": "adj.", "s": "s3", "zh": "富裕的", "exam": "富裕的；丰富的；肥沃的", "c": ["rich in resources 资源丰富", "rich nation 富裕国家"], "syn": ["wealthy", "abundant", "affluent"], "fam":["richness n. 丰富"], "dif": "rich 指财产富裕、资源丰富或色彩风味浓郁。", "pat": "The region is rich in mineral deposits and natural resources.", "patZh": "该地区矿藏和自然资源丰富。"},
        {"w": "rise", "ipa": "raɪz", "pos": "vi. / n.", "s": "s3", "zh": "上升", "exam": "上升；升起；增加；提高", "c": ["rise in price 价格上涨", "rise to power 步入权力中心"], "syn": ["ascend", "increase", "climb"], "fam":["rising adj. 上升的"], "dif": "rise 为不及物动词，指自动上升、升起或提高。", "pat": "Temperatures are expected to rise rapidly during the weekend.", "patZh": "预计周末气温将迅速上升。"},
        {"w": "risk", "ipa": "rɪsk", "pos": "n. / vt.", "s": "s3", "zh": "风险", "exam": "风险；危险；冒…的风险", "c": ["at risk 处于风险中", "take a risk 冒风险"], "syn": ["hazard", "danger", "jeopardize"], "fam":["risky adj. 危险的"], "dif": "risk 指可能遭受损失伤害的不确定危险风险。", "pat": "Investing in early-stage startups involves a high level of risk.", "patZh": "投资早期初创公司涉及高水平的风险。"},
        {"w": "riva", "ipa": "ˈraɪvl", "pos": "n. / vt.", "s": "s3", "zh": "对手", "exam": "竞争者；对手；与…媲美；竞争的", "c": ["chief rival 主要对手", "rival firm 竞争对手公司"], "syn": ["competitor", "opponent", "adversary"], "fam":["rivalry n. 竞争"], "dif": "rival 指在同一领域相互竞争对抗的对手。", "pat": "The two tech companies have been fierce rivals for over a decade.", "patZh": "这两家科技公司十多年来一直是激烈的对手。"},
        {"w": "role", "ipa": "rəʊl", "pos": "n.", "s": "s3", "zh": "角色", "exam": "角色；作用；岗位", "c": ["play a key role 发挥关键作用", "lead role 主角"], "syn": ["part", "function", "position"], "fam":["role n. 角色"], "dif": "role 指戏剧中扮演的角色，或在活动中发挥的作用职责。", "pat": "Education plays a critical role in shaping a society's future.", "patZh": "教育在塑造社会未来方面发挥着关键作用。"},
        {"w": "roll", "ipa": "rəʊl", "pos": "v. / n.", "s": "s3", "zh": "滚动", "exam": "滚动；转动；卷；名单", "c": ["roll out 推出/展开", "roll call 点名"], "syn": ["revolve", "scroll", "roster"], "fam":["roller n. 滚筒"], "dif": "roll 指物体在平面上滚动转动，或卷状物、名册。", "pat": "The tech company plans to roll out new software updates next month.", "patZh": "该科技公司计划下个月推出新的软件更新。"},
        {"w": "root", "ipa": "ruːt", "pos": "n. / v.", "s": "s3", "zh": "根源", "exam": "根；根源；生根；固定", "c": ["root cause 根本原因", "take root 生根"], "syn": ["origin", "source", "stem"], "fam":["rooted adj. 根深蒂固的"], "dif": "root 指植物的根系，或事物发展的根本源头。", "pat": "Investigators sought to uncover the root cause of the system failure.", "patZh": "调查人员试图揭示系统故障的根本原因。"},
        {"w": "route", "ipa": "ruːt", "pos": "n. / vt.", "s": "s3", "zh": "路线", "exam": "路线；路程；途径", "c": ["trade route 贸易路线", "escape route 逃生路线"], "syn": ["path", "course", "way"], "fam":["routine n. 日常惯例"], "dif": "route 指从起点到终点的具体行驶或传输路线。", "pat": "The delivery truck followed a designated route through the city.", "patZh": "快递卡车沿着穿过城市的指定路线行驶。"},
        {"w": "routine", "ipa": "ruːˈtiːn", "pos": "n. / adj.", "s": "s3", "zh": "日常惯例", "exam": "例行公事；日常惯例；例行的；常规的", "c": ["daily routine 日常生活", "routine inspection 常规检查"], "syn": ["habit", "custom", "standard"], "fam":["routinely adv. 常规地"], "dif": "routine 指习惯性经常进行的例行工作事务。", "pat": "Following a healthy daily routine improves energy levels and focus.", "patZh": "遵循健康的日常惯例可以提高精力水平和专注力。"}
    ]
}

os.makedirs(story_dir, exist_ok=True)

with open(os.path.join(story_dir, "Unit23.json"), "w", encoding="utf-8") as f:
    json.dump(unit23_data, f, ensure_ascii=False, indent=2)

with open(os.path.join(story_dir, "Unit24.json"), "w", encoding="utf-8") as f:
    json.dump(unit24_data, f, ensure_ascii=False, indent=2)

print("Saved Unit23.json and Unit24.json successfully.")
