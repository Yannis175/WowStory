# -*- coding: utf-8 -*-
import json
import os

story_dir = r"单词故事本"

# Unit 25 Data (84 words)
unit25_data = {
    "unit": 25,
    "stories": [
        {
            "id": "s1",
            "en": "Surveillance and Survival",
            "zh": "监控与生存",
            "theme": "管理 / 生存",
            "ps": [
                {
                    "en": "Under strict regulatory [[rules|rule]], the local [[ruler]] recorded each citizen's [[surname]] to ensure public order. Citizens sought to [[surpass]] expectations, producing a economic [[surplus]] that came as a pleasant [[surprise]]. To evaluate security, officials conducted a comprehensive [[survey]] and installed digital [[surveillance]] across the district.",
                    "zh": "在严格的监管规则下，当地统治者记录了每位公民的姓氏以确保公共秩序。公民试图超越期望，产生了令人惊喜的经济剩余。为了评估安全，官员们开展了一项全面的调查，并在全区安装了数字监控。"
                },
                {
                    "en": "Disaster management focused on long-term [[survival]], helping residents [[survive]] harsh winter conditions. Vulnerable groups were particularly [[susceptible]] to flu, prompting authorities to [[suspend]] public gatherings. Police began to [[suspect]] illicit activities, harboring deep [[suspicion]] toward a [[suspicious]] network. Efforts to [[sustain]] relief operations continued as a [[swarm]] of volunteers arrived.",
                    "zh": "灾难管理专注于长期生存，帮助居民在严酷的冬季条件下生存。脆弱群体特别容易遭受流感侵袭，促使当局暂停公共聚集。警方开始怀疑非法活动，对一个可疑网络怀有深切怀疑。随着一群志愿者的到来，维持救灾行动的努力得以持续。"
                }
            ]
        },
        {
            "id": "s2",
            "en": "Progressive Programs and Promising Futures",
            "zh": "渐进的项目与前景广阔的未来",
            "theme": "经济 / 项目",
            "ps": [
                {
                    "en": "Officials took an oath to [[swear]] allegiance to public duty. As rivers began to [[swell]] after heavy rains, engineers used a mechanical [[swing]] to [[switch]] emergency generators on.",
                    "zh": "官员们宣誓效忠公共职责。随着暴雨后河水开始上涨膨胀，工程师们使用机械摇摆臂切断并转换应急发电机。"
                },
                {
                    "en": "They initiated an ambitious infrastructure [[project]] designed to generate sustainable [[profit]] for [[profitable]] local enterprises. The research brought [[profound]] insights, laying the foundation for a training [[program]] to foster [[progressive]] social development.",
                    "zh": "他们启动了一项雄心勃勃的基础设施项目，旨在为有盈利能力的当地企业创造可持续的利润。研究带来了深刻的见解，为培养渐进式社会发展的培训项目奠定了基础。"
                },
                {
                    "en": "Regulators moved to [[prohibit]] harmful practices and avoid attempts to [[prolong]] legal disputes. A [[prominent]] scientist made a firm [[promise]], outlining a [[promising]] career path to [[promote]] clean technology and ensure [[prompt]] emergency responses.",
                    "zh": "监管者采取行动禁止有害行为，并避免延长法律争议的企图。一位杰出的科学家做出了坚定的承诺，勾勒出一条前景广阔的职业道路，以推广清洁技术并确保迅速的应急响应。"
                }
            ]
        },
        {
            "id": "s3",
            "en": "Resilience, Resources, and Responsibility",
            "zh": "韧性、资源与责任",
            "theme": "社会 / 责任",
            "ps": [
                {
                    "en": "Requiring solid [[proof]] before making a formal [[reservation]], managers set aside a financial [[reserve]] to [[resist]] market volatility. Community [[resistance]] remained strong, making infrastructure [[resistant]] to severe weather as [[resilient]] workers rebuilt damaged facilities.",
                    "zh": "在做出正式保留预约前需要坚实的证据，管理者留出了一笔财务储备以抵御市场波动。社区抵御力保持强大，使基础设施能够抵抗恶劣天气，因为有韧性的工人重建了受损设施。"
                },
                {
                    "en": "They decided to [[resort]] to emergency funds, allocating every available [[resource]] with deep [[respect]] for [[respective]] local needs.",
                    "zh": "他们决定采取诉诸应急资金的办法，在深切尊重各自地方需求的情况下分配所有可用资源。"
                },
                {
                    "en": "Spokespersons promised to [[respond]] quickly, issuing an official [[response]] that affirmed corporate [[responsibility]]. Appointing a [[responsible]] leader, they managed to [[succeed]] in stabilizing market confidence, leading to remarkable commercial [[success]].",
                    "zh": "发言人承诺快速回应，出台了一份确认公司责任的官方回应。任命一位负责任的领导者，他们成功地稳定了市场信心，带来了显著的商业成功。"
                }
            ]
        },
        {
            "id": "s4",
            "en": "Succession and Superiority",
            "zh": "继承与卓越",
            "theme": "管理 / 成功",
            "ps": [
                {
                    "en": "Following a [[successful]] campaign, the executive board oversaw a smooth leadership [[succession]] through [[successive]] quarterly milestones. A worthy [[successor]] was chosen to lead the firm, warning competitors not to [[suck]] vital capital away.",
                    "zh": "在一场成功的运动之后，执行董事会在连续的季度里程碑中督导了平稳的领导继承。一位有价值的继任者被选出来领导公司，警告竞争对手不要吮吸吸走关键资金。"
                },
                {
                    "en": "Victims threatened to [[sue]] fraudulent entities, refusing to [[suffer]] further financial losses. Current measures will [[suffice]] to maintain [[sufficient]] liquidity across operations.",
                    "zh": "受害者威胁要起诉欺诈实体，拒绝遭受进一步的财务损失。当前措施将足以维持整个运营中充分的流动性。"
                },
                {
                    "en": "Advisors chose to [[suggest]] a thoughtful [[suggestion]] to resolve a complex legal [[suit]], warning that reckless actions would be corporate [[suicide]]. They selected a [[suitable]] venue for a [[super]] event, celebrating [[superb]] artistic achievements that avoided [[superficial]] vanity.",
                    "zh": "顾问提出了有帮助的建议，针对解决复杂的法律诉讼提出了深思熟虑的建议。他们为一个超级盛会选择了合适的场地，庆祝避免了浅薄虚荣的卓越艺术成就。"
                }
            ]
        },
        {
            "id": "s5",
            "en": "Council Guidance and Exploration",
            "zh": "委员会指导与探索",
            "theme": "科学 / 探索",
            "ps": [
                {
                    "en": "Removing [[superfluous]] regulations, the court affirmed its [[superior]] legal standing and established clear [[superiority]] over regional tribunals. Senior partners met to [[supervise]] compliance, taking care not to [[trigger]] sudden market panic during their victory [[triumph]].",
                    "zh": "移除多余累赘的规定，法院确认了其优越的法定地位，并确立了对区域审判庭的明确优势。资深合伙人开会监督合规，注意在胜利的赞歌中不触发突然的市场恐慌。"
                },
                {
                    "en": "Executives moved to [[assure]] investors, providing solid [[assurance]] that continued innovation would [[astonish]] global markets. Under a calm academic [[atmosphere]], the advisory [[council]] gathered to provide expert [[counsel]].",
                    "zh": "高管们采取行动向投资者保证，提供坚实的保证，即持续创新将使全球市场惊叹。在平静的学术氛围下，咨询委员会聚集在一起提供专家建议。"
                },
                {
                    "en": "They staged a compelling historical [[drama]], capturing [[dramatic]] shifts in societal values as scientists chose to [[exploit]] natural resource reserves and [[explore]] unknown frontiers.",
                    "zh": "他们上演了一幕吸引人的历史戏剧，捕捉了社会价值观中的剧烈转变，因为科学家们选择开发自然资源储备并探索未知的前沿领域。"
                }
            ]
        }
    ],
    "words": [
        {"w": "rule", "ipa": "ruːl", "pos": "n. / v.", "s": "s1", "zh": "规则", "exam": "规则；统治；裁决", "c": ["break the rule 违反规则", "rule over 统治"], "syn": ["regulation", "law", "govern"], "fam":["ruler n. 统治者；直尺"], "dif": "rule 指明确制定的行为规则、规定，或政治统治。 ", "pat": "Everyone must strictly follow the safety rules in the laboratory.", "patZh": "每个人在实验室里都必须严格遵守安全规则。"},
        {"w": "ruler", "ipa": "ˈruːlə", "pos": "n.", "s": "s1", "zh": "统治者", "exam": "统治者；直尺", "c": ["absolute ruler 专制统治者", "measuring ruler 量尺"], "syn": ["monarch", "sovereign", "straightedge"], "fam":["rule v. 统治"], "dif": "ruler 可指国家统治者，也可指测量长度用的直尺。", "pat": "The historic ruler introduced sweeping administrative reforms across the empire.", "patZh": "这位历史上的统治者在整个帝国范围内推行了彻底的行政改革。"},
        {"w": "surname", "ipa": "ˈsɜːneɪm", "pos": "n.", "s": "s1", "zh": "姓氏", "exam": "姓；姓氏", "c": ["family surname 家族姓氏", "maiden surname 婚前姓氏"], "syn": ["last name", "family name"], "fam":["name n. 名字"], "dif": "surname 特指个人的家族姓氏（与 first name 相对）。", "pat": "Please write your official surname clearly on the registration form.", "patZh": "请在登记表上清晰书写您的官方姓氏。"},
        {"w": "surpass", "ipa": "səˈpɑːs", "pos": "vt.", "s": "s1", "zh": "超越", "exam": "超越；胜过", "c": ["surpass expectations 超出期望", "surpass competitors 胜过竞争对手"], "syn": ["exceed", "outdo", "excel"], "fam":["surpassing adj. 胜过的"], "dif": "surpass 侧重在质量、成就、数量上超过前人或预期。 ", "pat": "Her remarkable test scores managed to surpass all previous records.", "patZh": "她显著的测试分数成功超越了以往所有的记录。"},
        {"w": "surplus", "ipa": "ˈsɜːpləs", "pos": "n. / adj.", "s": "s1", "zh": "剩余", "exam": "过剩；剩余；盈余；过剩的", "c": ["trade surplus 贸易顺差", "budget surplus 预算盈余"], "syn": ["excess", "remainder", "extra"], "fam":["surplus adj. 剩余的"], "dif": "surplus 侧重在需求满足后剩下的过剩物资或资金盈余。", "pat": "The country recorded a huge trade surplus in electrical exports.", "patZh": "该国在电力出口方面创下了巨大的贸易顺差。"},
        {"w": "surprise", "ipa": "səˈpraɪz", "pos": "n. / vt.", "s": "s1", "zh": "惊奇", "exam": "惊奇；令人惊奇的事；使惊奇", "c": ["in surprise 惊奇地", "take by surprise 使措手不及"], "syn": ["astonishment", "amaze", "startle"], "fam":["surprising adj. 令人惊奇的"], "dif": "surprise 侧重由于意想不到的情况而产生的惊奇感。 ", "pat": "The unexpected news of his promotion came as a pleasant surprise.", "patZh": "他升职的出人意料的消息带来了一个令人高兴的惊奇。"},
        {"w": "survey", "ipa": "ˈsɜːveɪ", "pos": "n. / vt.", "s": "s1", "zh": "调查", "exam": "调查；测量；勘测；审视", "c": ["conduct a survey 进行民意调查", "land survey 土地勘测"], "syn": ["poll", "inspection", "scrutinize"], "fam":["surveyor n. 测量员"], "dif": "survey 侧重全面搜集数据的民意调查或地形勘测。 ", "pat": "The company launched an online survey to gather customer feedback.", "patZh": "该公司发起了一项在线调查以收集客户反馈。"},
        {"w": "surveillance", "ipa": "sɜːˈveɪləns", "pos": "n.", "s": "s1", "zh": "监控", "exam": "监视；监控", "c": ["video surveillance 视频监控", "under surveillance 处于监视之下"], "syn": ["monitoring", "observation", "supervision"], "fam":["survey v. 勘测"], "dif": "surveillance 专指警方、保安对特定区域或嫌犯的持续暗中监视。 ", "pat": "Security cameras maintain round-the-clock surveillance over the vault.", "patZh": "安全摄像头对金库保持全天候的监控。"},
        {"w": "survival", "ipa": "səˈvaɪvl", "pos": "n.", "s": "s1", "zh": "生存", "exam": "生存；幸存；残存物", "c": ["survival rate 生存率", "struggle for survival 生存挣扎"], "syn": ["existence", "endurance", "continuance"], "fam":["survive v. 生存"], "dif": "survival 指从危险极端的环境中艰难幸存、维持生存。 ", "pat": "Basic medical supplies are essential for the survival of earthquake victims.", "patZh": "基础医疗用品对于地震受害者的生存至关重要。"},
        {"w": "survive", "ipa": "səˈvaɪv", "pos": "v.", "s": "s1", "zh": "幸存", "exam": "幸免于；幸存；比…活得长", "c": ["survive the crash 在车祸中幸存", "survive on 靠…活下来"], "syn": ["outlast", "endure", "persist"], "fam":["survivor n. 幸存者"], "dif": "survive 指经历灾难疾病后活下来，或生命长于他人。 ", "pat": "Only a few rare plant species can survive in desert climates.", "patZh": "只有极少数稀有植物物种能在沙漠气候中存活下来。"},
        {"w": "susceptible", "ipa": "səˈseptəbl", "pos": "adj.", "s": "s1", "zh": "易受影响的", "exam": "易受影响的；易感染的", "c": ["susceptible to disease 易感染疾病的", "susceptible to influence 易受影响的"], "syn": ["vulnerable", "prone", "sensitive"], "fam":["susceptibility n. 易感性"], "dif": "susceptible 强调由于缺乏抵抗力而极易受疾病、情绪影响。 ", "pat": "Elderly individuals are particularly susceptible to winter lung infections.", "patZh": "老年人特别容易受到冬季肺部感染的影响。"},
        {"w": "suspend", "ipa": "səˈspend", "pos": "vt.", "s": "s1", "zh": "暂停", "exam": "悬挂；暂停；推迟；中止", "c": ["suspend judgment 暂缓判决", "suspend operations 暂停运营"], "syn": ["intermit", "halt", "hang"], "fam":["suspension n. 暂停；悬挂"], "dif": "suspend 指暂时停止某项活动、职位，或物理上的悬挂。 ", "pat": "The airline was forced to suspend flights during the severe blizzard.", "patZh": "在严重暴风雪期间航空公司被迫暂停航班。"},
        {"w": "suspect", "ipa": "səˈspekt", "pos": "v. / n. / adj.", "s": "s1", "zh": "怀疑", "exam": "怀疑；猜想；犯罪嫌疑人；可疑的", "c": ["suspect foul play 怀疑有诈", "prime suspect 主要嫌疑人"], "syn": ["distrust", "surmise", "dubious"], "fam":["suspicion n. 怀疑"], "dif": "suspect 作动词指推测某种坏事可能为真；作名词指犯罪嫌疑人。 ", "pat": "Detectives began to suspect that the burglary was an inside job.", "patZh": "侦探们开始怀疑这起盗窃案是内部人员所为。"},
        {"w": "suspicion", "ipa": "səˈspɪʃn", "pos": "n.", "s": "s1", "zh": "怀疑", "exam": "怀疑；猜疑；微量", "c": ["under suspicion 受到怀疑", "above suspicion 无可置疑"], "syn": ["distrust", "doubt", "misgiving"], "fam":["suspicious adj. 可疑的"], "dif": "suspicion 指对某人某事持有的怀疑态度或直觉猜疑。 ", "pat": "His vague answers aroused deep suspicion among board members.", "patZh": "他含糊的回答引发了董事会成员的深切怀疑。"},
        {"w": "suspicious", "ipa": "səˈspɪʃəs", "pos": "adj.", "s": "s1", "zh": "可疑的", "exam": "可疑的；猜疑的；多疑的", "c": ["suspicious package 可疑包裹", "be suspicious of 对…起疑"], "syn": ["dubious", "questionable", "distrustful"], "fam":["suspicion n. 怀疑"], "dif": "suspicious 描写行为迹象反常可疑，或性格多疑。 ", "pat": "Security guards called police after spotting a suspicious package near the entrance.", "patZh": "保安人员在入口附近发现可疑包裹后报警。"},
        {"w": "sustain", "ipa": "səˈsteɪn", "pos": "vt.", "s": "s1", "zh": "维持", "exam": "保持；维持；支撑；经受", "c": ["sustain growth 维持增长", "sustain injuries 遭受创伤"], "syn": ["maintain", "support", "uphold"], "fam":["sustainable adj. 可持续的"], "dif": "sustain 强调长时间给与支撑以维持生存或增长状态。 ", "pat": "The ecosystem can no longer sustain heavy industrial pollution.", "patZh": "该生态系统已无法再承受沉重的工业污染。"},
        {"w": "swarm", "ipa": "swɔːm", "pos": "n. / vi.", "s": "s1", "zh": "一群", "exam": "一大群；蜂群；蜂拥", "c": ["swarm of bees 一群蜜蜂", "swarm into 蜂拥而入"], "syn": ["flock", "horde", "throng"], "fam":["swarm v. 蜂拥"], "dif": "swarm 特指昆虫、人群蜂拥聚集的大群。 ", "pat": "A large swarm of mosquitoes descended upon the camp at dusk.", "patZh": "黄昏时分一大群蚊子袭击了营地。"},

        {"w": "swear", "ipa": "sweə", "pos": "v.", "s": "s2", "zh": "发誓", "exam": "发誓；诅咒；咒骂", "c": ["swear in 宣誓就职", "swear an oath 宣誓"], "syn": ["pledge", "vow", "curse"], "fam":["swearer n. 发誓者"], "dif": "swear 指庄严发誓承诺，或口出粗言诅咒。 ", "pat": "The witness had to swear to tell the whole truth in court.", "patZh": "证人在法庭上必须发誓说出全部事实。"},
        {"w": "swell", "ipa": "swel", "pos": "v. / n.", "s": "s2", "zh": "膨胀", "exam": "（使）膨胀；（使）肿胀；增加", "c": ["swell up 肿胀起来", "ground swell 巨浪/涌浪"], "syn": ["expand", "inflate", "bulge"], "fam":["swelling n. 肿块"], "dif": "swell 指因充水、充气或发炎而体积增大膨胀。 ", "pat": "His sprained ankle began to swell rapidly after the match.", "patZh": "比赛后他扭伤的脚踝开始迅速肿胀起来。"},
        {"w": "swing", "ipa": "swɪŋ", "pos": "v. / n.", "s": "s2", "zh": "摇摆", "exam": "（使）摇摆；摆动；秋千；大幅改变", "c": ["swing mood 情绪摇摆", "swing into action 立即行动"], "syn": ["sway", "oscillate", "pendulum"], "fam":["swinger n. 摆动者"], "dif": "swing 指像摆锤一样悬挂着左右摆动。 ", "pat": "Children love to swing higher and higher in the playground.", "patZh": "孩子们喜欢在游乐场里把秋千荡得越来越高。"},
        {"w": "switch", "ipa": "swɪtʃ", "pos": "v. / n.", "s": "s2", "zh": "转换", "exam": "开关；转换；改变；转变", "c": ["switch off 关掉", "switch jobs 换工作"], "syn": ["change", "shift", "toggle"], "fam":["switchable adj. 可切换的"], "dif": "switch 侧重按开关改变状态，或方向轨道的直接切换。 ", "pat": "Companies should switch to green energy to reduce carbon emissions.", "patZh": "公司应当转向使用绿色能源以减少碳排放。"},
        {"w": "project", "ipa": "ˈprɒdʒekt", "pos": "n. / v.", "s": "s2", "zh": "项目", "exam": "方案；项目；工程；投影；预测", "c": ["research project 研究项目", "project image 塑造形象"], "syn": ["scheme", "plan", "forecast"], "fam":["projection n. 预测；投影"], "dif": "project 作名词指规划的项目工程，作动词指投射或预测。 ", "pat": "The government launched a major project to build new affordable housing.", "patZh": "政府启动了一项建设新型保障房的重大项目。"},
        {"w": "profit", "ipa": "ˈprɒfɪt", "pos": "n. / v.", "s": "s2", "zh": "利润", "exam": "利润；收益；获利；受益", "c": ["net profit 净利润", "profit from 从…获利"], "syn": ["gain", "earnings", "benefit"], "fam":["profitable adj. 有利润的"], "dif": "profit 特指商业经营中扣除成本后的净利润或实际好处。 ", "pat": "The company reported a sharp increase in annual net profit.", "patZh": "公司报告年度净利润大幅增加。"},
        {"w": "profitable", "ipa": "ˈprɒfɪtəbl", "pos": "adj.", "s": "s2", "zh": "有利润的", "exam": "有利可图的；有利润的；有益的", "c": ["profitable investment 有成效的投资", "highly profitable 高利润的"], "syn": ["lucrative", "remunerative", "fruitful"], "fam":["profit n. 利润"], "dif": "profitable 指能带来可观财务利润或有实质益处。 ", "pat": "Expanding into international markets proved to be a highly profitable decision.", "patZh": "事实证明向国际市场扩张是一项高利润的决定。"},
        {"w": "profound", "ipa": "prəˈfaʊnd", "pos": "adj.", "s": "s2", "zh": "深刻的", "exam": "深刻的；深奥的；巨大的", "c": ["profound impact 深刻的影响", "profound knowledge 深奥的知识"], "syn": ["deep", "insightful", "far-reaching"], "fam":["profoundly adv. 深刻地"], "dif": "profound 指影响极其深远、思想极具深度或感情强烈。 ", "pat": "The scientific discovery had a profound impact on modern physics.", "patZh": "这项科学发现对现代物理学产生了深刻的影响。"},
        {"w": "program", "ipa": "ˈprəʊɡræm", "pos": "n. / vt.", "s": "s2", "zh": "项目", "exam": "程序；项目；节目；编制程序", "c": ["training program 培训项目", "computer program 计算机程序"], "syn": ["schedule", "plan", "curriculum"], "fam":["programmer n. 程序员"], "dif": "program 指一系列有计划的行动方案、节目或计算机代码程序。 ", "pat": "The university launched a specialized exchange program for international students.", "patZh": "该大学为国际学生推出了一项专门的交流项目。"},
        {"w": "progressive", "ipa": "prəˈɡresɪv", "pos": "adj.", "s": "s2", "zh": "渐进的", "exam": "进步的；渐进的；革新的", "c": ["progressive policy 进步的政策", "progressive decline 渐进式下降"], "syn": ["advanced", "gradual", "forward-looking"], "fam":["progress n. 进步"], "dif": "progressive 指思想开放进步革新的，或事物循序渐进发展的。 ", "pat": "The municipality adopted progressive measures to tackle urban pollution.", "patZh": "该市政当局采取了渐进的措施来解决城市污染。"},
        {"w": "prohibit", "ipa": "prəˈhɪbɪt", "pos": "vt.", "s": "s2", "zh": "禁止", "exam": "禁止；阻止", "c": ["strictly prohibit 严格禁止", "prohibit A from doing 禁止A做B"], "syn": ["forbid", "ban", "bar"], "fam":["prohibition n. 禁止"], "dif": "prohibit 侧重通过法律、官方命令明确宣布禁止做某事。 ", "pat": "School rules strictly prohibit smoking anywhere on campus premises.", "patZh": "学校规定严格禁止在校园内任何地方吸烟。"},
        {"w": "prolong", "ipa": "prəˈlɒŋ", "pos": "vt.", "s": "s2", "zh": "延长", "exam": "延长；拉长；拖延", "c": ["prolong life 延长寿命", "prolong a conflict 拖延冲突"], "syn": ["extend", "lengthen", "protract"], "fam":["prolongation n. 延长"], "dif": "prolong 侧重使原本有限的时间、生命或状态延续更久。 ", "pat": "Medical treatments helped prolong the patient's life by several years.", "patZh": "医疗手段帮助将患者的寿命延长了数年。"},
        {"w": "prominent", "ipa": "ˈprɒmɪnənt", "pos": "adj.", "s": "s2", "zh": "杰出的", "exam": "突出的；杰出的；显著的", "c": ["prominent figure 杰出人物", "prominent position 显眼的位置"], "syn": ["famous", "distinguished", "conspicuous"], "fam":["prominently adv. 显眼地"], "dif": "prominent 指地位显赫杰出的，或地理物理上引人注目的。 ", "pat": "She became a prominent figure in the international human rights movement.", "patZh": "她成为了国际人权运动中的杰出人物。"},
        {"w": "promise", "ipa": "ˈprɒmɪs", "pos": "v. / n.", "s": "s2", "zh": "承诺", "exam": "允诺；答应；预示；承诺；希望", "c": ["keep a promise 遵守承诺", "show promise 展现出希望"], "syn": ["pledge", "guarantee", "potential"], "fam":["promising adj. 前景广阔的"], "dif": "promise 既指做出的口头书面保证，也可指发展潜质希望。 ", "pat": "The politician failed to keep his campaign promise after taking office.", "patZh": "这位政治家在上任后未能兑现其竞选承诺。"},
        {"w": "promising", "ipa": "ˈprɒmɪsɪŋ", "pos": "adj.", "s": "s2", "zh": "前景广阔的", "exam": "有希望的；前景广阔的", "c": ["promising future 前景广阔的未来", "promising student 有前途的学生"], "syn": ["encouraging", "auspicious", "bright"], "fam":["promise n. 前景"], "dif": "promising 描写人或事物展现出良好的成功发展势头与希望。 ", "pat": "The initial clinical trials yielded promising results for cancer patients.", "patZh": "初步临床试验为癌症患者带来了令人鼓舞的前景广阔的结果。"},
        {"w": "promote", "ipa": "prəˈməʊt", "pos": "vt.", "s": "s2", "zh": "推广", "exam": "促进；提升；推广；晋升", "c": ["promote growth 促进增长", "be promoted to 被晋升为"], "syn": ["foster", "advance", "encourage"], "fam":["promotion n. 促进；晋升"], "dif": "promote 侧重促进事物发展、宣传推广产品或提升职位。 ", "pat": "The campaign aims to promote environmental awareness among school children.", "patZh": "该运动旨在在学童中推广环保意识。"},
        {"w": "prompt", "ipa": "prɒmpt", "pos": "adj. / vt. / n.", "s": "s3", "zh": "迅速的", "exam": "迅速的；敏捷的；促使；提示", "c": ["prompt action 迅速的行动", "prompt response 快速回复"], "syn": ["immediate", "swift", "trigger"], "fam":["promptly adv. 迅速地"], "dif": "prompt 作形容词指反应迅速不拖延，作动词指促使激起某行为。 ", "pat": "Emergency teams provided prompt medical care to flood survivors.", "patZh": "应急队伍向洪水幸存者提供了迅速的医疗救护。"},

        {"w": "proof", "ipa": "pruːf", "pos": "n. / adj.", "s": "s3", "zh": "证据", "exam": "证据；证明；检验；防…的", "c": ["solid proof 坚实的证据", "waterproof adj. 防水的"], "syn": ["evidence", "demonstration", "testament"], "fam":["prove v. 证明"], "dif": "proof 指能确定某事为真的确凿证据、证明。 ", "pat": "Scientists required conclusive proof before accepting the revolutionary claims.", "patZh": "科学家们在接受这一革命性断言前需要确凿的证据。"},
        {"w": "reservation", "ipa": "ˌrezəˈveɪʃn", "pos": "n.", "s": "s3", "zh": "保留", "exam": "保留；预订；保护区", "c": ["make a reservation 预订", "have reservations 有所保留"], "syn": ["booking", "misgiving", "sanctuary"], "fam":["reserve v. 预订"], "dif": "reservation 指旅馆座位预订，或对想法方案抱有的疑虑保留。 ", "pat": "It is advisable to make a hotel reservation well in advance during peak season.", "patZh": "在旺季期间最好提前预订酒店。"},
        {"w": "reserve", "ipa": "rɪˈzɜːv", "pos": "vt. / n.", "s": "s3", "zh": "储备", "exam": "保留；预订；储备；保护区；矜持", "c": ["cash reserve 现金储备", "nature reserve 自然保护区"], "syn": ["store", "withhold", "book"], "fam":["reserved adj. 矜持的"], "dif": "reserve 指把资源留在日后使用，或预订场地、保留权利。 ", "pat": "Central banks hold foreign currency reserves to stabilize the national economy.", "patZh": "中央银行持有外汇储备以稳定国家经济。"},
        {"w": "resist", "ipa": "rɪˈzɪst", "pos": "v.", "s": "s3", "zh": "抵抗", "exam": "抵抗；反抗；忍住", "c": ["resist temptation 抵制诱惑", "resist pressure 顶住压力"], "syn": ["oppose", "defy", "withstand"], "fam":["resistance n. 抵抗"], "dif": "resist 侧重抵制某种诱惑、顶住压力反抗进攻。 ", "pat": "Workers joined hands to resist unfair pay cuts imposed by the firm.", "patZh": "工人联手抵抗公司实施的不公平减薪。"},
        {"w": "resistance", "ipa": "rɪˈzɪstəns", "pos": "n.", "s": "s3", "zh": "抵抗", "exam": "抵抗；反抗；阻力；抵抗力", "c": ["meet resistance 遇到阻力", "antibiotic resistance 抗生素耐药性"], "syn": ["opposition", "defiance", "impediment"], "fam":["resistant adj. 有抵抗力的"], "dif": "resistance 指对某种力量的组织反抗或物理生物上的阻力。 ", "pat": "The proposed policy change met strong opposition and political resistance.", "patZh": "提议的政策变更遭到了强烈的反对和政治阻力。"},
        {"w": "resistant", "ipa": "rɪˈzɪstənt", "pos": "adj.", "s": "s3", "zh": "抵抗的", "exam": "有抵抗力的；抵抗的；防…的", "c": ["resistant to change 抵制改变的", "heat-resistant 耐热的"], "syn": ["proof", "impervious", "defiant"], "fam":["resistance n. 抵抗力"], "dif": "resistant 指能够承受恶劣影响、不容易受损害或变质的。 ", "pat": "The new crops are engineered to be highly resistant to severe droughts.", "patZh": "这种新农作物经过基因改造能够高度抗干旱。"},
        {"w": "resilient", "ipa": "rɪˈzɪliənt", "pos": "adj.", "s": "s3", "zh": "有韧性的", "exam": "有弹性的；能复原的；有韧性的", "c": ["resilient economy 有韧性的经济", "resilient spirit 顽强的精神"], "syn": ["flexible", "adaptable", "robust"], "fam":["resilience n. 韧性"], "dif": "resilient 强调在遭受挫折打击后快速复原、适应环境的能力。 ", "pat": "Small businesses demonstrated a resilient capacity to adapt during the economic downturn.", "patZh": "小企业在经济下滑期间展现出了快速适应的复原能力。"},
        {"w": "resort", "ipa": "rɪˈzɔːt", "pos": "vi. / n.", "s": "s3", "zh": "诉诸", "exam": "诉诸；求助；胜地；招数", "c": ["resort to force 诉诸武力", "holiday resort 度假胜地"], "syn": ["turn to", "recourse", "retreat"], "fam":["resort v. 诉诸"], "dif": "resort 搭配 to 表示在无别办法时采取某种手段；作名词指胜地。 ", "pat": "Diplomats worked hard so neither country would resort to armed conflict.", "patZh": "外交官们努力工作以使两国都不至于诉诸武装冲突。"},
        {"w": "resource", "ipa": "rɪˈsɔːs", "pos": "n.", "s": "s3", "zh": "资源", "exam": "资源；财力；谋略", "c": ["natural resources 自然资源", "human resources 人力资源"], "syn": ["asset", "supply", "wealth"], "fam":["resourceful adj. 足智多谋的"], "dif": "resource 指国家或机构拥有的物资、资金、人才等可资利用的资源。 ", "pat": "Efficient management of natural resources is essential for sustainable development.", "patZh": "自然资源的高效管理对于可持续发展至关重要。"},
        {"w": "respect", "ipa": "rɪˈspekt", "pos": "vt. / n.", "s": "s3", "zh": "尊重", "exam": "尊重；尊敬；方面；重视", "c": ["pay respect to 尊敬", "in this respect 在这个方面"], "syn": ["esteem", "reverence", "aspect"], "fam":["respectful adj. 恭敬的"], "dif": "respect 侧重对人品成就的尊敬，或指具体方面细节。 ", "pat": "Students are taught to respect diverse opinions and cultural backgrounds.", "patZh": "学生们被教育要尊重多元的观点和文化背景。"},
        {"w": "respective", "ipa": "rɪˈspektɪv", "pos": "adj.", "s": "s3", "zh": "各自的", "exam": "各自的；分别的", "c": ["respective positions 各自的位置", "respective fields 各自的领域"], "syn": ["individual", "particular", "specific"], "fam":["respectively adv. 各自地"], "dif": "respective 侧重分别归属于各个不同个体的人或事物。 ", "pat": "After the conference ended, delegates returned to their respective countries.", "patZh": "会议结束后代表们返回了他们各自的国家。"},
        {"w": "respond", "ipa": "rɪˈspɒnd", "pos": "vi.", "s": "s3", "zh": "回应", "exam": "回答；响应；作出反应", "c": ["respond to 做出回应", "respond well to 反应良好"], "syn": ["react", "answer", "reply"], "fam":["response n. 回应"], "dif": "respond 侧重对刺激、问题或变化做出具体的行动或语言反应。 ", "pat": "The patient began to respond favorably to the new medical treatment.", "patZh": "患者开始对这种新医疗手段产生良好的回应。"},
        {"w": "response", "ipa": "rɪˈspɒns", "pos": "n.", "s": "s3", "zh": "回应", "exam": "回答；反应；响应", "c": ["in response to 对…做出回应", "emergency response 应急响应"], "syn": ["reaction", "answer", "reply"], "fam":["respond v. 回应"], "dif": "response 指针对询问或情境做出的答复或具体反应。 ", "pat": "The public gave a enthusiastic response to the new charity initiative.", "patZh": "公众对这一新的慈善倡议给予了热烈的回应。"},
        {"w": "responsibility", "ipa": "rɪˌspɒnsəˈbɪləti", "pos": "n.", "s": "s3", "zh": "责任", "exam": "责任；职责；义务", "c": ["take responsibility 承担责任", "sense of responsibility 责任感"], "syn": ["duty", "obligation", "liability"], "fam":["responsible adj. 负责任的"], "dif": "responsibility 指因职位或道德所必须履行的职责后果。 ", "pat": "Parents share the primary responsibility for their children's well-being.", "patZh": "父母共同承担对子女幸福的主要责任。"},
        {"w": "responsible", "ipa": "rɪˈspɒnsəbl", "pos": "adj.", "s": "s3", "zh": "负责任的", "exam": "有责任的；可信赖的；负责的", "c": ["be responsible for 对…负责", "responsible position 负责任的职位"], "syn": ["accountable", "liable", "trustworthy"], "fam":["responsibility n. 责任"], "dif": "responsible 强调对行为、后果负有直接法律或道德义务。 ", "pat": "Engineers are directly responsible for ensuring the structural stability of bridges.", "patZh": "工程师直接负责确保桥梁的结构稳定性。"},
        {"w": "succeed", "ipa": "səkˈsiːd", "pos": "v.", "s": "s3", "zh": "成功", "exam": "成功；继承；接着发生", "c": ["succeed in doing 成功做…", "succeed to the throne 继承王位"], "syn": ["triumph", "inherit", "follow"], "fam":["success n. 成功"], "dif": "succeed 搭配 in 表示达成目标，搭配 to 表示接替继承。 ", "pat": "If you persevere through challenges, you will eventually succeed.", "patZh": "如果你在挑战中坚持不懈，你最终会成功。"},
        {"w": "success", "ipa": "səkˈses", "pos": "n.", "s": "s3", "zh": "成功", "exam": "成功；成就；成功的人或事", "c": ["achieve success 获得成功", "key to success 成功的关键"], "syn": ["triumph", "accomplishment", "victory"], "fam":["successful adj. 成功的"], "dif": "success 指达成目标的圆满结果或具有成功成就的人士。 ", "pat": "Hard work and strategic planning are essential elements of long-term business success.", "patZh": "努力工作和战略规划是长期商业成功的必要要素。"},

        {"w": "successful", "ipa": "səkˈsesfl", "pos": "adj.", "s": "s4", "zh": "成功的", "exam": "成功的；有成就的", "c": ["successful career 成功的职业", "highly successful 非常成功的"], "syn": ["prosperous", "triumphant", "flourishing"], "fam":["success n. 成功"], "dif": "successful 描写计划圆满达成或事业极具成就。 ", "pat": "The entrepreneur built a highly successful tech company within five years.", "patZh": "这位创业者在五年内建立了一家非常成功的科技公司。"},
        {"w": "succession", "ipa": "səkˈseʃn", "pos": "n.", "s": "s4", "zh": "继承", "exam": "连续；继承；接替", "c": ["in succession 连续地", "succession plan 继承计划"], "syn": ["series", "sequence", "inheritance"], "fam":["successive adj. 连续的"], "dif": "succession 指事件的一系列连续发生，或权力的依法接替继承。 ", "pat": "The team won three championship titles in rapid succession.", "patZh": "该团队接连快速赢得了三个冠军头衔。"},
        {"w": "successive", "ipa": "səkˈsesɪv", "pos": "adj.", "s": "s4", "zh": "连续的", "exam": "连续的；相继的", "c": ["successive days 连续的几天", "successive generations 接连的几代"], "syn": ["consecutive", "subsequent", "sequential"], "fam":["succession n. 继承"], "dif": "successive 强调一个接一个毫不中断地接连发生。 ", "pat": "Heavy rainfall continued for four successive days, causing minor flooding.", "patZh": "大雨持续了连续四天，引发了轻度洪水。"},
        {"w": "successor", "ipa": "səkˈsesə", "pos": "n.", "s": "s4", "zh": "继任者", "exam": "继任者；继承人", "c": ["legal successor 合法继承人", "successor to 某人的继任者"], "syn": ["heir", "replacement", "follower"], "fam":["succeed v. 继承"], "dif": "successor 特指接替前任职位、头衔或遗产的人。 ", "pat": "The former CEO worked closely with his designated successor during transition.", "patZh": "前任 CEO 在过渡期间与指定继任者密切合作。"},
        {"w": "suck", "ipa": "sʌk", "pos": "v. / n.", "s": "s4", "zh": "吮吸", "exam": "吸；吮；吸收", "c": ["suck up 吸入", "suck in 卷入/吸引"], "syn": ["sip", "absorb", "draw"], "fam":["sucker n. 吸盘；易受骗者"], "dif": "suck 指用嘴或机械力吸入液体气体。 ", "pat": "Plants suck up water and minerals from the surrounding soil.", "patZh": "植物从周围土壤中吸收水分和矿物质。"},
        {"w": "sue", "ipa": "suː", "pos": "v.", "s": "s4", "zh": "起诉", "exam": "控告；起诉；请求", "c": ["sue for damages 诉请赔偿", "sue A for B 因B起诉A"], "syn": ["prosecute", "litigate", "indict"], "fam":["lawsuit n. 诉讼"], "dif": "sue 侧重在民事法庭上向某人提出起诉控告。 ", "pat": "The injured worker decided to sue the construction company for negligence.", "patZh": "受伤的工人决定因疏忽起诉该建筑公司。"},
        {"w": "suffer", "ipa": "ˈsʌfə", "pos": "v.", "s": "s4", "zh": "遭受", "exam": "遭受；受苦；患病", "c": ["suffer from 患…病/遭受", "suffer losses 遭受损失"], "syn": ["undergo", "endure", "experience"], "fam":["suffering n. 痛苦"], "dif": "suffer 侧重承受身体心理的痛苦或财产损失。 ", "pat": "Many local businesses continue to suffer heavy losses during recession.", "patZh": "许多当地企业在衰退期间继续遭受重大损失。"},
        {"w": "suffice", "ipa": "səˈfaɪs", "pos": "vi.", "s": "s4", "zh": "足够", "exam": "足够；合格", "c": ["suffice it to say 简而言之", "suffice to show 足够表明"], "syn": ["satisfy", "serve", "be enough"], "fam":["sufficient adj. 充分的"], "dif": "suffice 指数量、条件完全满足需要或合格。 ", "pat": "A simple written notice will suffice to cancel the subscription.", "patZh": "一份简单的书面通知就足以取消订阅。"},
        {"w": "sufficient", "ipa": "səˈfɪʃnt", "pos": "adj.", "s": "s4", "zh": "充分的", "exam": "充分的；足够的", "c": ["sufficient evidence 充分的证据", "sufficient funds 足够的资金"], "syn": ["adequate", "ample", "enough"], "fam":["sufficiency n. 充分"], "dif": "sufficient 侧重数量程度完全达到规定标准。 ", "pat": "Ensure you get sufficient rest before taking a high-stakes exam.", "patZh": "请确保在参加高风险考试前获得充分的休息。"},
        {"w": "suggest", "ipa": "səˈdʒest", "pos": "vt.", "s": "s4", "zh": "建议", "exam": "建议；提议；暗示；表明", "c": ["suggest that 建议…", "suggest a solution 提出方案"], "syn": ["propose", "recommend", "hint"], "fam":["suggestion n. 建议"], "dif": "suggest 指提出看法供考虑，或隐晦暗示。 ", "pat": "Medical experts suggest drinking plenty of water daily.", "patZh": "医疗专家建议每天饮用充足的水。"},
        {"w": "suggestion", "ipa": "səˈdʒestʃən", "pos": "n.", "s": "s4", "zh": "建议", "exam": "建议；提议；示意", "c": ["make a suggestion 提出建议", "at the suggestion of 应…的建议"], "syn": ["proposal", "recommendation", "advice"], "fam":["suggest v. 建议"], "dif": "suggestion 指提出的想法看法或微小暗示。 ", "pat": "The manager welcomed every practical suggestion for improving workplace safety.", "patZh": "经理欢迎关于改善工作场所安全的每一条实用建议。"},
        {"w": "suicide", "ipa": "ˈsuːɪsaɪd", "pos": "n.", "s": "s4", "zh": "自杀", "exam": "自杀；自取灭亡的行为", "c": ["commit suicide 自杀", "political suicide 政治上的自取灭亡"], "syn": ["self-destruction", "self-harm"], "fam":["suicidal adj. 自杀的"], "dif": "suicide 指故意结束自己生命或自取灭亡。 ", "pat": "Mental health hotlines offer support to individuals battling suicidal thoughts.", "patZh": "心理健康热线向与自杀念头作斗争的人提供支持。"},
        {"w": "suit", "ipa": "suːt", "pos": "n. / v.", "s": "s4", "zh": "合适", "exam": "西装；诉讼；适合；满足", "c": ["business suit 商务西装", "suit one's needs 适合某人的需求"], "syn": ["fit", "adapt", "outfit"], "fam":["suitable adj. 合适的"], "dif": "suit 指衣着西装，或事物性质适合某人需要。 ", "pat": "The working schedule can be tailored to suit individual personal needs.", "patZh": "工作日程可以量身定制以适合个人需求。"},
        {"w": "suitable", "ipa": "ˈsuːtəbl", "pos": "adj.", "s": "s4", "zh": "合适的", "exam": "合适的；适宜的", "c": ["suitable for 适合…的", "suitable candidate 合适的候选人"], "syn": ["appropriate", "fitting", "proper"], "fam":["suit v. 适合"], "dif": "suitable 侧重符合特定场合条件或用途要求。 ", "pat": "Applicants must hold qualifications suitable for the academic position.", "patZh": "申请人必须具备适合该学术职位的资质。"},
        {"w": "super", "ipa": "ˈsuːpə", "pos": "adj.", "s": "s4", "zh": "超级的", "exam": "极好的；超级的", "c": ["super power 超级大国", "super quality 极佳质量"], "syn": ["excellent", "supreme", "outstanding"], "fam":["superb adj. 极好的"], "dif": "super 指规模水准极大、极其优秀的。 ", "pat": "The country emerged as a global super power in tech innovation.", "patZh": "该国已崛起为科技创新领域的全球超级大国。"},
        {"w": "superb", "ipa": "suːˈpɜːb", "pos": "adj.", "s": "s4", "zh": "极好的", "exam": "极好的；出色的；华丽的", "c": ["superb performance 极好的表演", "superb quality 绝佳品质"], "syn": ["magnificent", "splendid", "outstanding"], "fam":["superbly adv. 出色地"], "dif": "superb 强调品质高超、表现极其出众超群。 ", "pat": "The violinist gave a superb performance that captivated the entire audience.", "patZh": "小提琴家给出了一场令人为之倾倒的极好的表演。"},
        {"w": "superficial", "ipa": "ˌsuːpəˈfɪʃl", "pos": "adj.", "s": "s4", "zh": "浅薄的", "exam": "表面的；肤浅的；浅薄的", "c": ["superficial knowledge 浅薄的知识", "superficial wound 表面伤口"], "syn": ["shallow", "surface", "cursory"], "fam":["superficiality n. 浅薄"], "dif": "superficial 侧重停留在表面、缺乏深度透彻理解。 ", "pat": "Avoid making hasty judgments based on superficial impressions.", "patZh": "避免根据表面的印象做出草率的判断。"},

        {"w": "superfluous", "ipa": "suːˈpɜːfluəs", "pos": "adj.", "s": "s5", "zh": "多余的", "exam": "过剩的；多余的；累赘的", "c": ["superfluous detail 多余的细节", "superfluous words 累赘的言词"], "syn": ["unnecessary", "redundant", "excess"], "fam":["superfluity n. 多余"], "dif": "superfluous 指超出需要、完全没有必要的累赘多余物。 ", "pat": "Edit the report carefully to eliminate all superfluous words.", "patZh": "仔细编辑报告以消除所有多余累赘的字词。"},
        {"w": "superior", "ipa": "suːˈpɪəriə", "pos": "adj. / n.", "s": "s5", "zh": "优越的", "exam": "优良的；较好的；上级的；上级", "c": ["superior quality 优良的品质", "be superior to 优于…"], "syn": ["better", "higher", "senior"], "fam":["superiority n. 优越"], "dif": "superior 指品质地位高于普通水平或竞争对方。 ", "pat": "Our product offers superior quality at a competitive market price.", "patZh": "我们的产品在具有竞争力的市场价格下提供优良的品质。"},
        {"w": "superiority", "ipa": "suːˌpɪəriˈɒrəti", "pos": "n.", "s": "s5", "zh": "优越", "exam": "优越（性）；优势", "c": ["technical superiority 技术优势", "air superiority 空中优势"], "syn": ["advantage", "supremacy", "dominance"], "fam":["superior adj. 优越的"], "dif": "superiority 指在品质能力地位上占据的绝对优势。 ", "pat": "The firm established its market superiority through continuous technological innovation.", "patZh": "该公司通过持续的技术创新确立了其市场优势。"},
        {"w": "supervise", "ipa": "ˈsuːpəvaɪz", "pos": "v.", "s": "s5", "zh": "监督", "exam": "监督；管理；指导", "c": ["supervise staff 监督员工", "supervise work 督导工作"], "syn": ["oversee", "inspect", "direct"], "fam":["supervision n. 监督", "supervisor n. 监督员"], "dif": "supervise 侧重站在管理层角度对人员工作流程实施经常性监督指导。 ", "pat": "Managers are required to supervise daily operations to ensure quality control.", "patZh": "管理者被要求监督日常运营以确保质量控制。"},
        {"w": "trigger", "ipa": "ˈtrɪɡə", "pos": "vt. / n.", "s": "s5", "zh": "触发", "exam": "扳机；触发器；引起；触发", "c": ["trigger a reaction 触发反应", "pull the trigger 扣动扳机"], "syn": ["cause", "spark", "activate"], "fam":["trigger n. 触发器"], "dif": "trigger 侧重像扣动扳机一样引发链式反应或事件。 ", "pat": "Rising food prices could trigger widespread public unrest across the region.", "patZh": "粮食价格上涨可能会触发全地区的广泛公众动荡。"},
        {"w": "triumph", "ipa": "ˈtraɪʌmf", "pos": "n. / vi.", "s": "s5", "zh": "胜利", "exam": "伟大胜利；巨大成功；战胜；得意", "c": ["in triumph 胜利地", "triumph over 战胜"], "syn": ["victory", "win", "conquest"], "fam":["triumphant adj. 胜利的"], "dif": "triumph 指克服重重困难后取得的辉煌成果胜利。 ", "pat": "The team celebrated their triumph after winning the championship trophy.", "patZh": "团队在赢得冠军奖杯后庆祝了他们的伟大胜利。"},
        {"w": "assure", "ipa": "əˈʃʊə", "pos": "vt.", "s": "s5", "zh": "保证", "exam": "使确信；向…保证；确保", "c": ["assure sb of 向某人保证…", "rest assured 尽管放心"], "syn": ["reassure", "guarantee", "ensure"], "fam":["assurance n. 保证"], "dif": "assure 侧重口头或书面向他人做出保证以消除怀疑虑。 ", "pat": "The director stepped forward to assure staff that no lay-offs were planned.", "patZh": "主管走上前去向员工保证没有裁员计划。"},
        {"w": "assurance", "ipa": "əˈʃʊərəns", "pos": "n.", "s": "s5", "zh": "保证", "exam": "保证；确信；自信", "c": ["give assurance 给予保证", "quality assurance 质量保证"], "syn": ["guarantee", "promise", "confidence"], "fam":["assure v. 保证"], "dif": "assurance 指做出的正式保证承诺，或内心的确信自信。 ", "pat": "The government gave full assurance that public safety would be maintained.", "patZh": "政府给出了维持公共安全的全面保证。"},
        {"w": "astonish", "ipa": "əˈstɒnɪʃ", "pos": "vt.", "s": "s5", "zh": "使惊叹", "exam": "使十分惊奇；使惊叹", "c": ["astonish the world 使世界惊叹", "be astonished at 对…感到惊奇"], "syn": ["amaze", "astound", "surprise"], "fam":["astonishing adj. 令人惊叹的", "astonishment n. 惊奇"], "dif": "astonish 强调出乎意料的事物让人感到极度惊奇震惊。 ", "pat": "Her rapid progress in learning languages continues to astonish her teachers.", "patZh": "她在语言学习上的快速进步继续使她的老师们感到惊叹。"},
        {"w": "atmosphere", "ipa": "ˈætməsfɪə", "pos": "n.", "s": "s5", "zh": "氛围", "exam": "大气（层）；空气；气氛；氛围", "c": ["friendly atmosphere 友好的氛围", "earth's atmosphere 地球大气层"], "syn": ["ambiance", "climate", "air"], "fam":["atmospheric adj. 大气的"], "dif": "atmosphere 指围绕地球的气体层，或场所中的特定群体氛围。 ", "pat": "The historic restaurant boasts a cozy and romantic atmosphere.", "patZh": "这家历史悠久的餐厅拥有温馨而浪漫的氛围。"},
        {"w": "council", "ipa": "ˈkaʊnsl", "pos": "n.", "s": "s5", "zh": "委员会", "exam": "理事会；委员会；地方议会", "c": ["city council 市议会", "security council 安全理事会"], "syn": ["board", "committee", "assembly"], "fam":["councillor n. 议员"], "dif": "council 特指依法成立的地方议会、行政或咨询委员会。 ", "pat": "The city council voted unanimously to approve the new park project.", "patZh": "市议会一致投票批准了新公园项目。"},
        {"w": "counsel", "ipa": "ˈkaʊnsl", "pos": "n. / vt.", "s": "s5", "zh": "建议", "exam": "忠告；建议；法律顾问；劝告", "c": ["legal counsel 法律顾问", "counsel sb on 就…劝告某人"], "syn": ["advice", "lawyer", "advise"], "fam":["counselor n. 顾问"], "dif": "counsel 侧重深谋远虑的专业忠告、建议或法庭辩护律师。 ", "pat": "He sought wise counsel from experienced mentors before taking the offer.", "patZh": "在接受报盘前他向有经验的导师寻求了明智的忠告。"},
        {"w": "drama", "ipa": "ˈdrɑːmə", "pos": "n.", "s": "s5", "zh": "戏剧", "exam": "戏剧；剧本；戏剧性事件", "c": ["stage drama 舞台戏剧", "historical drama 历史剧"], "syn": ["play", "theater", "event"], "fam":["dramatic adj. 戏剧性的"], "dif": "drama 指舞台剧本戏剧，或生活中富有跌宕起伏的戏剧性事件。 ", "pat": "She pursued a degree in classical drama at the performing arts academy.", "patZh": "她在表演艺术学院攻读古典戏剧学位。"},
        {"w": "dramatic", "ipa": "drəˈmætɪk", "pos": "adj.", "s": "s5", "zh": "戏剧性的", "exam": "戏剧的；剧烈的；引人注目的", "c": ["dramatic change 剧烈的变化", "dramatic increase 戏剧性的增加"], "syn": ["striking", "spectacular", "drastic"], "fam":["dramatically adv. 戏剧性地"], "dif": "dramatic 强调变化极其剧烈、引人注目或富有戏剧色彩。 ", "pat": "The company experienced a dramatic rise in share prices following the launch.", "patZh": "发布会后该公司经历了股价的剧烈上涨。"},
        {"w": "exploit", "ipa": "ɪkˈsplɔɪt", "pos": "vt. / n.", "s": "s5", "zh": "开发", "exam": "开发；利用；剥削；功绩", "c": ["exploit resources 开发资源", "exploit vulnerabilities 利用漏洞"], "syn": ["utilize", "harness", "feat"], "fam":["exploitation n. 开发；剥削"], "dif": "exploit 指充分开采利用资源，或指不公正剥削他人。 ", "pat": "Engineers sought to exploit geothermal energy for sustainable heating.", "patZh": "工程师们试图开发地热能用于可持续供暖。"},
        {"w": "explore", "ipa": "ɪkˈsplɔː", "pos": "v.", "s": "s5", "zh": "探索", "exam": "勘探；探索；探究", "c": ["explore space 探索太空", "explore possibilities 探究可能性"], "syn": ["investigate", "discover", "examine"], "fam":["exploration n. 探索", "explorer n. 探险家"], "dif": "explore 侧重深入未知领域、问题进行前沿考察探究。 ", "pat": "Scientists launched a space probe to explore distant moons of Jupiter.", "patZh": "科学家们发射了一枚空间探测器去探索木星的遥远卫星。"}
    ]
}

# Unit 26 Data (69 words)
unit26_data = {
    "unit": 26,
    "stories": [
        {
            "id": "s1",
            "en": "Intelligent Design and Restoration",
            "zh": "智能设计与复原",
            "theme": "科技 / 设计",
            "ps": [
                {
                    "en": "Demonstrating high artificial [[intelligence]], an [[intelligent]] system produced [[intelligible]] code summaries that helped developers [[polish]] every key [[point]]. Innovative engines began to [[propel]] automated tools to handle [[proper]] data structures across corporate [[property]].",
                    "zh": "展现出高超的人工智能，智能系统输出了清晰易懂的代码总结，帮助开发人员精雕细琢每一个要点。创新的引擎开始推动自动化工具，跨公司财产处理适当的数据结构。"
                },
                {
                    "en": "Maintaining a balanced [[proportion]] of resources, the board submitted a formal [[proposal]] to [[propose]] a new commercial [[proposition]]. Assessing future market [[prospects|prospect]], [[prospective]] investors followed standard security [[protocol]] to find a [[proximate]] solution and [[restore]] system stability.",
                    "zh": "保持平衡的资源比例，董事会提交了一份正式提案以提出一项新的商业主张。评估未来的市场前景，预期的投资者遵循标准安全协议以寻找切近的解决方案并恢复系统稳定性。"
                }
            ]
        },
        {
            "id": "s2",
            "en": "Restraint and Creative Enterprise",
            "zh": "克制与创意企业",
            "theme": "管理 / 创意",
            "ps": [
                {
                    "en": "Regulators agreed to [[restrain]] impulsive spending, placing strict [[restraint]] on market speculation so as not to [[restrict]] genuine growth. Developers decided to [[attach]] new clauses before competitors launched an [[attack]] on their market share.",
                    "zh": "监管者同意抑制冲动支出，对市场投机施加严格约束，以免限制真实增长。开发商决定在竞争对手对其市场份额发起攻击前附加新条款。"
                },
                {
                    "en": "Striving to [[attain]] excellence, executives made an [[attempt]] to [[attend]] the summit, paying full [[attention]] to policy trends. Adopting a positive [[attitude]], they refused to [[attribute]] success purely to luck.",
                    "zh": "努力取得卓越，高管们尝试参加峰会，全神贯注于政策趋势。采取积极的态度，他们拒绝将成功纯粹归因于运气。"
                },
                {
                    "en": "Appearing before the supreme [[court]], attorneys acted with flawless [[courtesy]]. They moved to [[cover]] risk, [[create]] new jobs, foster a [[creative]] team, and earn international [[credit]].",
                    "zh": "出庭最高法院，律师们表现出无可挑剔的谦恭礼貌。他们采取行动规避涵盖风险、创造新岗位、培养有创意的团队并赢得国际声誉信用。"
                }
            ]
        },
        {
            "id": "s3",
            "en": "Humanitarian Crisis and Policy Exposure",
            "zh": "人道主义危机与政策暴露",
            "theme": "社会 / 人道",
            "ps": [
                {
                    "en": "During a sudden financial [[crisis]], leaders took action to [[drive]] economic reform and restrict illicit [[drug]] trade. Expanding foreign [[exports|export]], analysts warned against policies that [[expose]] domestic markets to excessive [[exposure]].",
                    "zh": "在突然的金融危机期间，领导人采取行动驱动经济改革并限制非法毒品交易。扩大对外出口，分析师警告不要采取使国内市场暴露出过度风险暴露的政策。"
                },
                {
                    "en": "Officials wished to [[express]] deep concern through a formal [[expression]]. They sought to [[extend]] aid networks, plan an [[extension]] of services, conduct an [[extensive]] review, and measure the full [[extent]] of damages.",
                    "zh": "官员们希望通过正式声明表达深切关切。他们试图延伸救援网络，规划服务拓展，开展广泛的审查，并测量全部损害程度。"
                },
                {
                    "en": "Preserving basic [[human]] dignity, the global campaign served all [[humanity]] with a [[humble]] attitude, fully [[intending|intend]] to realize its noble [[intention]].",
                    "zh": "维护基本的人类尊严，这项全球运动以谦逊的态度服务于全人类，完全意图实现其高尚的意图。"
                }
            ]
        },
        {
            "id": "s4",
            "en": "International Relations and Lucrative Ties",
            "zh": "国际关系与丰厚回报",
            "theme": "国际 / 合作",
            "ps": [
                {
                    "en": "Faced with [[intense]] competition, researchers raised the [[intensity]] of their [[intensive]] study to [[interact]] smoothly through international [[intercourse]]. Driven by genuine [[interest]], they renovated the [[interior]] space to support [[internal]] operational needs across an [[international]] network.",
                    "zh": "面对激烈的竞争，研究人员提升了集中精细研究的强度，以通过国际交流顺畅互动。在真实兴趣的驱动下，他们整修了内部空间，以支持国际网络中的内部运营需求。"
                },
                {
                    "en": "Scholars gathered to [[interpret]] complex legal codes without fearing to [[lose]] face or suffer financial [[loss]]. Even when market rates reached a [[low]] point, managers chose to [[lower]] entry costs to launch a [[lucrative]] business model.",
                    "zh": "学者们聚集在一起解读复杂的法律法规，而不必担心丢面子或遭受财务损失。即使在市场利率跌至低点时，管理者仍选择降低进入成本以推出盈利丰厚的商业模式。"
                },
                {
                    "en": "The high-stakes trial tested every [[nerve]], leaving negotiators [[nervous]], but [[nevertheless]] they reached a historic compromise.",
                    "zh": "这场高风险的审判考验着神经，让谈判代表感到紧张不安，但尽管如此他们依然达成了历史性的妥协。"
                }
            ]
        }
    ],
    "words": [
        {"w": "intelligence", "ipa": "ɪnˈtelɪdʒəns", "pos": "n.", "s": "s1", "zh": "智力", "exam": "智力；智慧；情报；情报人员", "c": ["artificial intelligence 人工智能", "military intelligence 军事情报"], "syn": ["intellect", "mind", "information"], "fam":["intelligent adj. 聪明的"], "dif": "intelligence 指人的智力思维能力，或军事安全部门的情报。 ", "pat": "Artificial intelligence is reshaping modern diagnostic medicine.", "patZh": "人工智能正在重塑现代诊断医学。"},
        {"w": "intelligent", "ipa": "ɪnˈtelɪdʒənt", "pos": "adj.", "s": "s1", "zh": "聪明的", "exam": "聪明的；理智的；智能的", "c": ["intelligent system 智能系统", "intelligent student 聪明的学生"], "syn": ["smart", "clever", "bright"], "fam":["intelligence n. 智力"], "dif": "intelligent 侧重具有高智商、理解力强或具备智能化功能。 ", "pat": "The university recruits highly intelligent students from around the globe.", "patZh": "该大学从全球招募智商极高的聪明学生。"},
        {"w": "intelligible", "ipa": "ɪnˈtelɪdʒəbl", "pos": "adj.", "s": "s1", "zh": "清晰易懂的", "exam": "可理解的；明白易懂的", "c": ["intelligible explanation 清晰的解释", "easily intelligible 简单易懂的"], "syn": ["understandable", "clear", "comprehensible"], "fam":["intelligibility n. 可理解性"], "dif": "intelligible 侧重语言、文理清晰表达明确容易听懂理解。 ", "pat": "The professor made complex quantum concepts easily intelligible to beginners.", "patZh": "教授使复杂的量子概念对初学者来说简单易懂。"},
        {"w": "polish", "ipa": "ˈpɒlɪʃ", "pos": "vt. / n.", "s": "s1", "zh": "擦亮", "exam": "磨光；擦亮；润色；擦光剂", "c": ["polish shoes 擦鞋", "polish a draft 润色草案"], "syn": ["shine", "refine", "buff"], "fam":["polisher n. 抛光器"], "dif": "polish 指物理上擦亮抛光，或对文章言论精雕细琢润色。 ", "pat": "She spent hours attempting to polish her academic thesis before submission.", "patZh": "她在提交前花了数小时试图润色她的学术论文。"},
        {"w": "point", "ipa": "pɔɪnt", "pos": "n. / v.", "s": "s1", "zh": "要点", "exam": "要点；核心；观点；尖端；指", "c": ["key point 核心要点", "point out 指出"], "syn": ["dot", "detail", "indicate"], "fam":["pointer n. 指针；教鞭"], "dif": "point 指具体的要点、分数、尖端，或用手指指方向。 ", "pat": "The speaker raised a valid point during the parliamentary debate.", "patZh": "演讲者在议会辩论期间提出了一个有效的要点。"},
        {"w": "propel", "ipa": "prəˈpel", "pos": "vt.", "s": "s1", "zh": "推进", "exam": "推进；推动；驱使", "c": ["propel forward 向前推进", "propel growth 推动增长"], "syn": ["drive", "push", "impel"], "fam":["propeller n. 螺旋桨"], "dif": "propel 侧重施加机械力或动力推着物体前进。 ", "pat": "Strong winds helped propel the sailboat across the turbulent bay.", "patZh": "强风有助于推进帆船穿过动荡的海湾。"},
        {"w": "proper", "ipa": "ˈprɒpə", "pos": "adj.", "s": "s1", "zh": "适当的", "exam": "正确的；适当的；特有的", "c": ["proper way 适当的方式", "proper care 妥善的照料"], "syn": ["appropriate", "suitable", "fitting"], "fam":["properly adv. 适当地"], "dif": "proper 指符合规范礼仪、标准或特定场合要求的。 ", "pat": "Wearing proper safety gear is mandatory inside the construction site.", "patZh": "在施工现场内部穿戴适当的安全装备是强制性的。"},
        {"w": "property", "ipa": "ˈprɒpəti", "pos": "n.", "s": "s1", "zh": "财产", "exam": "财产；资产；房地产；性质", "c": ["private property 私有财产", "intellectual property 知识产权"], "syn": ["possessions", "estate", "attribute"], "fam":["proprietor n. 业主"], "dif": "property 指依法拥有的地产财产，或物质的物理化学性质。 ", "pat": "Protecting intellectual property is essential for encouraging innovation.", "patZh": "保护知识产权对于鼓励创新至关重要。"},
        {"w": "proportion", "ipa": "prəˈpɔːʃn", "pos": "n.", "s": "s1", "zh": "比例", "exam": "比例；部分；均衡", "c": ["in proportion to 与…成比例", "large proportion 很大比例"], "syn": ["ratio", "share", "percentage"], "fam":["proportional adj. 成比例的"], "dif": "proportion 指整体中各部分所占的数量比例关系。 ", "pat": "A high proportion of the company's revenue is reinvested in research.", "patZh": "公司收入的很大比例被重新投资于研究。"},
        {"w": "proposal", "ipa": "prəˈpəʊzl", "pos": "n.", "s": "s1", "zh": "提案", "exam": "提议；提案；求婚", "c": ["submit a proposal 提交提案", "business proposal 商业提案"], "syn": ["suggestion", "scheme", "bid"], "fam":["propose v. 提议"], "dif": "proposal 指正式书面提交供讨论审议决定的提议方案。 ", "pat": "The committee reviewed the budget proposal submitted by the department.", "patZh": "委员会审查了该部门提交的预算提案。"},
        {"w": "propose", "ipa": "prəˈpəʊz", "pos": "v.", "s": "s1", "zh": "提议", "exam": "提议；建议；打算；求婚", "c": ["propose a plan 提议一个计划", "propose a toast 提议干杯"], "syn": ["suggest", "advocate", "intend"], "fam":["proposition n. 主张"], "dif": "propose 指正式提出方案看法，或向人求婚。 ", "pat": "The government plans to propose new legislation on renewable energy.", "patZh": "政府计划就可再生能源提出新立法。"},
        {"w": "proposition", "ipa": "ˌprɒpəˈzɪʃn", "pos": "n.", "s": "s1", "zh": "主张", "exam": "主张；命题；提议；交易", "c": ["business proposition 商业主张", "testing a proposition 检验命题"], "syn": ["premise", "hypothesis", "proposal"], "fam":["propose v. 提议"], "dif": "proposition 侧重在逻辑论证或商业谈判中陈述的论题主张。 ", "pat": "The entrepreneur presented an attractive business proposition to investors.", "patZh": "创业者向投资者展示了一项极具吸引力的商业主张。"},
        {"w": "prospect", "ipa": "ˈprɒspekt", "pos": "n. / v.", "s": "s1", "zh": "前景", "exam": "前景；前途；期望；勘探", "c": ["bright prospects 光明的前景", "prospect for oil 勘探石油"], "syn": ["outlook", "possibility", "explore"], "fam":["prospective adj. 预期的"], "dif": "prospect 指对未来发展的期望前途，或地质勘探。 ", "pat": "Job prospects for software engineers remain exceptionally strong.", "patZh": "软件工程师的就业前景依然格外强劲。"},
        {"w": "prospective", "ipa": "prəˈspektɪv", "pos": "adj.", "s": "s1", "zh": "预期的", "exam": "预期的；未来的；可能的", "c": ["prospective buyers 预期的买家", "prospective student 准学生"], "syn": ["potential", "future", "upcoming"], "fam":["prospect n. 前景"], "dif": "prospective 指在将来有可能成为客户、买家或学生的。 ", "pat": "The real estate agent invited prospective buyers to inspect the house.", "patZh": "房地产经纪人邀请预期的买家看房。"},
        {"w": "protocol", "ipa": "ˈprəʊtəkɒl", "pos": "n.", "s": "s1", "zh": "协议", "exam": "礼仪；外交协议；网络协议", "c": ["diplomatic protocol 外交礼仪", "network protocol 网络协议"], "syn": ["convention", "etiquette", "procedure"], "fam":["protocol n. 协议"], "dif": "protocol 指外交场合的正式礼仪规则，或计算机网络通信协议。 ", "pat": "Strict diplomatic protocol was observed during the presidential reception.", "patZh": "在总统招待会期间遵循了严格的外交礼仪。"},
        {"w": "proximate", "ipa": "ˈprɒksɪmət", "pos": "adj.", "s": "s1", "zh": "切近的", "exam": "最接近的；切近的；直接的", "c": ["proximate cause 直接原因", "proximate location 切近的位置"], "syn": ["adjacent", "nearest", "direct"], "fam":["proximity n. 接近"], "dif": "proximate 指在时间、空间或因果关系上最切近直接的。 ", "pat": "Careless driving was determined as the proximate cause of the collision.", "patZh": "疏忽驾驶被认定为碰撞的直接原因。"},
        {"w": "restore", "ipa": "rɪˈstɔː", "pos": "vt.", "s": "s1", "zh": "恢复", "exam": "恢复；修复；归还", "c": ["restore order 恢复秩序", "restore confidence 恢复信心"], "syn": ["reinstate", "renew", "refurbish"], "fam":["restoration n. 恢复"], "dif": "restore 侧重使受损、破坏的状态或信心重新回到原先的良好水平。 ", "pat": "The new policy helped restore public confidence in the banking system.", "patZh": "新政策有助于恢复公众对银行体系的信心。"},

        {"w": "restrain", "ipa": "rɪˈstreɪn", "pos": "vt.", "s": "s2", "zh": "抑制", "exam": "抑制；克制；制止；扣留", "c": ["restrain anger 抑制怒火", "restrain sb from doing 制止某人做…"], "syn": ["suppress", "check", "curb"], "fam":["restraint n. 克制"], "dif": "restrain 侧重用意志力或物理手段强制压制情绪或行为。 ", "pat": "Police worked quickly to restrain the unruly crowd at the stadium.", "patZh": "警方迅速采取行动制止体育场内失控的人群。"},
        {"w": "restraint", "ipa": "rɪˈstreɪnt", "pos": "n.", "s": "s2", "zh": "克制", "exam": "克制；抑制；约束措施", "c": ["exercise restraint 保持克制", "financial restraint 财务约束"], "syn": ["self-control", "restriction", "moderation"], "fam":["restrain v. 抑制"], "dif": "restraint 指保持沉着冷静的自我约束克制，或管束措施。 ", "pat": "Diplomats urged all parties to exercise maximum restraint during crisis.", "patZh": "外交官们敦促各方在危机期间保持最大程度的克制。"},
        {"w": "restrict", "ipa": "rɪˈstrɪkt", "pos": "vt.", "s": "s2", "zh": "限制", "exam": "限制；约束；限定", "c": ["restrict access 限制进入", "restrict to 限于…"], "syn": ["limit", "confine", "bound"], "fam":["restriction n. 限制"], "dif": "restrict 侧重依法规制度划定明确界限加以约束限制。 ", "pat": "The regulation aims to restrict access to sensitive military records.", "patZh": "该规定旨在限制对敏感军事记录的调阅。"},
        {"w": "attach", "ipa": "əˈtætʃ", "pos": "vt.", "s": "s2", "zh": "附加", "exam": "系；贴；附加；使依恋", "c": ["attach a file 附加文件", "attach importance to 重视…"], "syn": ["append", "affix", "connect"], "fam":["attachment n. 附件；依恋"], "dif": "attach 指将某物系在或贴在另一物上，或表示重视。 ", "pat": "Remember to attach your updated resume to the job application email.", "patZh": "请记得将您更新后的简历附在求职申请电子邮件中。"},
        {"w": "attack", "ipa": "əˈtæk", "pos": "v. / n.", "s": "s2", "zh": "攻击", "exam": "攻击；进攻；发作", "c": ["under attack 受到攻击", "heart attack 心脏病发作"], "syn": ["assault", "strike", "aggression"], "fam":["attacker n. 攻击者"], "dif": "attack 指武力进攻、言论抨击，或疾病突然发作。 ", "pat": "The army launched a surprise attack on the enemy stronghold.", "patZh": "军队对敌方据点发动了突然袭击。"},
        {"w": "attain", "ipa": "əˈteɪn", "pos": "vt.", "s": "s2", "zh": "取得", "exam": "达到；获得；取得", "c": ["attain a goal 达成目标", "attain mastery 掌握专长"], "syn": ["achieve", "acquire", "gain"], "fam":["attainment n. 成就"], "dif": "attain 侧重经过长期不懈努力达成宏大目标或成就。 ", "pat": "She worked diligently for years to attain a doctorate in astrophysics.", "patZh": "她勤奋工作多年以取得天体物理学博士学位。"},
        {"w": "attempt", "ipa": "əˈtempt", "pos": "vt. / n.", "s": "s2", "zh": "尝试", "exam": "尝试；试图；企图", "c": ["attempt to do 尝试做…", "make an attempt 作出尝试"], "syn": ["try", "endeavor", "effort"], "fam":["attempted adj. 企图的"], "dif": "attempt 侧重付出努力尝试去做具有挑战性的事情。 ", "pat": "The climber made a bold attempt to reach the mountain summit.", "patZh": "登山者做出了攀登山峰顶峰的大胆尝试。"},
        {"w": "attend", "ipa": "əˈtend", "pos": "v.", "s": "s2", "zh": "出席", "exam": "出席；参加；照顾；专心", "c": ["attend a meeting 出席会议", "attend to 处理/照顾"], "syn": ["present", "accompany", "mind"], "fam":["attendance n. 出勤", "attendant n. 服务员"], "dif": "attend 指亲自到场出席活动，或专心照顾某人。 ", "pat": "Delegates from over fifty nations will attend the annual climate conference.", "patZh": "来自五十多个国家的代表将出席年度气候会议。"},
        {"w": "attention", "ipa": "əˈtenʃn", "pos": "n.", "s": "s2", "zh": "注意力", "exam": "注意；关心；立正", "c": ["pay attention to 注意…", "attract attention 吸引注意"], "syn": ["notice", "focus", "regard"], "fam":["attentive adj. 专注的"], "dif": "attention 指将心思精力集中关注于某一特定事物。 ", "pat": "Please pay close attention to the safety demonstration before take-off.", "patZh": "起飞前请密切注意安全示范。"},
        {"w": "attitude", "ipa": "ˈætɪtjuːd", "pos": "n.", "s": "s2", "zh": "态度", "exam": "态度；看法；姿态", "c": ["positive attitude 积极的态度", "attitude towards 对…的态度"], "syn": ["stance", "outlook", "disposition"], "fam":["attitudinal adj. 态度的"], "dif": "attitude 指对人对事所持的心态观点或行为姿态。 ", "pat": "Maintaining a constructive attitude helps resolve workplace disputes quickly.", "patZh": "保持建设性的态度有助于快速解决工作场所的争议。"},
        {"w": "attribute", "ipa": "əˈtrɪbjuːt", "pos": "vt. / n.", "s": "s2", "zh": "归因于", "exam": "把…归因于；属性；品质", "c": ["attribute A to B 把A归因于B", "essential attribute 本质属性"], "syn": ["ascribe", "impute", "trait"], "fam":["attribution n. 归因"], "dif": "attribute 作动词指归因于，作名词指特征属性。 ", "pat": "Scientists attribute global warming largely to human carbon emissions.", "patZh": "科学家们很大程度上把全球变暖归因于人类的碳排放。"},
        {"w": "court", "ipa": "kɔːt", "pos": "n. / vt.", "s": "s2", "zh": "法院", "exam": "法院；法庭；球场；追求", "c": ["supreme court 最高法院", "tennis court 网球场"], "syn": ["tribunal", "bench", "solicit"], "fam":["courtroom n. 法庭"], "dif": "court 指进行审判的民事刑事法庭，或体育球场。 ", "pat": "The case will be presented before the supreme court next Monday.", "patZh": "该案件将于下周一在最高法院出庭审理。"},
        {"w": "courtesy", "ipa": "ˈkɜːtəsi", "pos": "n.", "s": "s2", "zh": "谦恭礼貌", "exam": "礼貌；谦恭；客气", "c": ["by courtesy of 蒙…惠赠/允许", "courtesy visit 礼节性拜访"], "syn": ["politeness", "civility", "manners"], "fam":["courteous adj. 有礼貌的"], "dif": "courtesy 指行为举止中展现的高雅谦恭与文明礼貌。 ", "pat": "Show common courtesy by waiting for others to finish speaking.", "patZh": "通过等待他人说完话来展现基本的谦恭礼貌。"},
        {"w": "cover", "ipa": "ˈkʌvə", "pos": "v. / n.", "s": "s2", "zh": "涵盖", "exam": "覆盖；涵盖；包含；掩盖；封面", "c": ["cover costs 涵盖费用", "front cover 封面"], "syn": ["overlay", "include", "shelter"], "fam":["coverage n. 覆盖率；新闻报道"], "dif": "cover 指物理上遮盖，或在范围上包含涵盖某费用议题。 ", "pat": "The medical insurance policy will cover all hospitalization expenses.", "patZh": "医疗保险单将涵盖所有的住院费用。"},
        {"w": "create", "ipa": "kriˈeɪt", "pos": "vt.", "s": "s2", "zh": "创造", "exam": "创造；创作；产生", "c": ["create jobs 创造就业", "create value 创造价值"], "syn": ["produce", "generate", "invent"], "fam":["creation n. 创造", "creator n. 创造者"], "dif": "create 侧重从无到有建立或构想出新的事物价值。 ", "pat": "The investment initiative aims to create thousands of sustainable jobs.", "patZh": "这项投资倡议旨在创造数以千计的可持续就业机会。"},
        {"w": "creative", "ipa": "kriˈeɪtɪv", "pos": "adj.", "s": "s2", "zh": "有创意的", "exam": "创造性的；有创意的", "c": ["creative thinking 创造性思维", "creative writing 创意写作"], "syn": ["imaginative", "innovative", "original"], "fam":["creativity n. 创造力"], "dif": "creative 描写具有丰富想象力和创新设计思维的。 ", "pat": "Engineers need creative problem-solving skills to overcome complex technical design challenges.", "patZh": "工程师需要有创意的解决问题技能来克服复杂的技术设计挑战。"},
        {"w": "credit", "ipa": "ˈkredɪt", "pos": "n. / vt.", "s": "s2", "zh": "声誉信用", "exam": "信用；信誉；赞扬；学分；归功于", "c": ["credit card 信用卡", "give credit to 赞扬/归功于"], "syn": ["reputation", "trust", "attribute"], "fam":["creditable adj. 值得赞扬的"], "dif": "credit 指财务信用，或对成就的公开赞扬归功。 ", "pat": "Her tireless dedication earned her full credit for the project's success.", "patZh": "她不懈的奉献为她赢得了该项目成功的充分赞扬与归功。"},

        {"w": "crisis", "ipa": "ˈkraɪsɪs", "pos": "n.", "s": "s3", "zh": "危机", "exam": "危机；紧要关头", "c": ["financial crisis 金融危机", "energy crisis 能源危机"], "syn": ["emergency", "dilemma", "climax"], "fam":["critical adj. 关键的"], "dif": "crisis 特指面临严重危险混乱的决定性紧要关头。 ", "pat": "Governments must act decisively during an economic crisis.", "patZh": "政府必须在经济危机期间果断采取行动。"},
        {"w": "drive", "ipa": "draɪv", "pos": "v. / n.", "s": "s3", "zh": "驱动", "exam": "驾驶；驱动；推进；运动；干劲", "c": ["drive growth 驱动增长", "membership drive 招募运动"], "syn": ["propel", "steer", "motivation"], "fam":["driver n. 驾驶员；驱动因素"], "dif": "drive 指驾驶车辆，或在物理力量动机上驱使向前。 ", "pat": "Technological innovation continues to drive economic productivity worldwide.", "patZh": "技术创新继续驱动着全球经济生产力。"},
        {"w": "drug", "ipa": "drʌɡ", "pos": "n. / v.", "s": "s3", "zh": "毒品", "exam": "药物；毒品；用药", "c": ["prescription drug 处方药", "illicit drug 违禁毒品"], "syn": ["medicine", "narcotic", "medicate"], "fam":["druggist n. 药剂师"], "dif": "drug 既指治病用的医学处方药，也指成瘾违禁毒品。 ", "pat": "Strict laws regulate the manufacturing and distribution of prescription drugs.", "patZh": "严格的法律监管着处方药的生产与分销。"},
        {"w": "export", "ipa": "ˈekspɔːt", "pos": "v. / n.", "s": "s3", "zh": "出口", "exam": "出口；输出；出口商品", "c": ["export market 出口市场", "export goods 出口货物"], "syn": ["ship abroad", "trade out"], "fam":["exporter n. 出口商"], "dif": "export 指将本国商品技术销售输出到国外（与 import 相对）。 ", "pat": "Agricultural produce forms a major part of the country's total export volume.", "patZh": "农产品构成了该国总出口量的主要部分。"},
        {"w": "expose", "ipa": "ɪkˈspəʊz", "pos": "vt.", "s": "s3", "zh": "暴露", "exam": "暴露；揭露；使接触", "c": ["expose fraud 揭露欺诈", "expose to danger 使暴露于危险"], "syn": ["uncover", "reveal", "disclose"], "fam":["exposure n. 暴露；曝光"], "dif": "expose 侧重使隐藏的欺诈事实暴露出光，或置于危险中。 ", "pat": "Investigative reporters worked to expose corruption within the regulatory agency.", "patZh": "调查记者致力于揭露监管机构内部的腐败。"},
        {"w": "exposure", "ipa": "ɪkˈspəʊʒə", "pos": "n.", "s": "s3", "zh": "暴露", "exam": "暴露；显露；曝光；报道", "c": ["exposure to radiation 暴露于辐射", "media exposure 媒体曝光"], "syn": ["uncovering", "publicity", "revelation"], "fam":["expose v. 暴露"], "dif": "exposure 指置身于某种环境风险中的状态，或媒体曝光报道。 ", "pat": "Prolonged exposure to direct sunlight can cause skin damage.", "patZh": "长期暴露于阳光直射下会造成皮肤损害。"},
        {"w": "express", "ipa": "ɪkˈspres", "pos": "vt. / adj. / n.", "s": "s3", "zh": "表达", "exam": "表达；表示；特快的；快递", "c": ["express concern 表达关切", "express delivery 快递"], "syn": ["convey", "articulate", "explicit"], "fam":["expression n. 表达"], "dif": "express 作动词指清楚表达想法感情，作形容词指特快明确的。 ", "pat": "The ambassador stepped forward to express sincere condolences to victims.", "patZh": "大使走上前去向受害者表达诚挚的哀悼。"},
        {"w": "expression", "ipa": "ɪkˈspreʃn", "pos": "n.", "s": "s3", "zh": "表达", "exam": "表达；词语；表情", "c": ["facial expression 面部表情", "freedom of expression 表达自由"], "syn": ["utterance", "look", "phrase"], "fam":["express v. 表达"], "dif": "expression 指思想情感的表达方式，或脸上的喜怒表情。 ", "pat": "Art offers a powerful medium for personal emotional expression.", "patZh": "艺术为个人情感表达提供了一种强有力的媒介。"},
        {"w": "extend", "ipa": "ɪkˈstend", "pos": "v.", "s": "s3", "zh": "延伸", "exam": "延伸；扩展；提供；延长", "c": ["extend a deadline 延长截止日期", "extend a welcome 表达欢迎"], "syn": ["expand", "stretch", "prolong"], "fam":["extension n. 延伸；拓展"], "dif": "extend 侧重在长度、时间、空间或范围上的延伸扩展。 ", "pat": "The university decided to extend the application deadline by one week.", "patZh": "大学决定将申请截止日期延长一周。"},
        {"w": "extension", "ipa": "ɪkˈstenʃn", "pos": "n.", "s": "s3", "zh": "延伸", "exam": "延伸；拓展；电话分机；延期", "c": ["phone extension 电话分机", "grant an extension 给予延期"], "syn": ["addition", "expansion", "prolongation"], "fam":["extend v. 延伸"], "dif": "extension 指增加的延伸部分、延定期限或电话分机号。 ", "pat": "He requested a two-day extension to finalize the research paper.", "patZh": "他申请延期两天以完成研究论文。"},
        {"w": "extensive", "ipa": "ɪkˈstensɪv", "pos": "adj.", "s": "s3", "zh": "广泛的", "exam": "广阔的；广泛的；大量的", "c": ["extensive research 广泛的研究", "extensive knowledge 渊博的知识"], "syn": ["broad", "widespread", "vast"], "fam":["extensively adv. 广泛地"], "dif": "extensive 强调覆盖范围辽阔、领域广泛或数量巨大。 ", "pat": "The scientist conducted extensive field trials across three continents.", "patZh": "这位科学家在三大洲开展了广泛的野外试验。"},
        {"w": "extent", "ipa": "ɪkˈstent", "pos": "n.", "s": "s3", "zh": "程度", "exam": "范围；程度；广度", "c": ["to some extent 在某种程度上", "full extent 最大程度"], "syn": ["degree", "range", "scope"], "fam":["extend v. 延伸"], "dif": "extent 侧重影响、损害或范围所达到的具体程度。 ", "pat": "It is difficult to assess the full extent of the storm damage immediately.", "patZh": "很难立即评估风暴损害的全盘程度。"},
        {"w": "human", "ipa": "ˈhjuːmən", "pos": "adj. / n.", "s": "s3", "zh": "人类的", "exam": "人的；人类的；人", "c": ["human nature 人性", "human rights 人权"], "syn": ["mortal", "person", "individual"], "fam":["humanity n. 人类；人性"], "dif": "human 指与人类属性相关的，与动物机器相对。 ", "pat": "Human error was determined as the main factor in the accident.", "patZh": "人为错误被判定为事故的主要因素。"},
        {"w": "humanity", "ipa": "hjuːˈmænəti", "pos": "n.", "s": "s3", "zh": "人类", "exam": "人类；人性；人道；人文科学", "c": ["crimes against humanity 反人类罪", "study of humanity 人文研究"], "syn": ["mankind", "humanness", "compassion"], "fam":["human adj. 人类的"], "dif": "humanity 指全人类的总称，或人道关怀同情心。 ", "pat": "Medical advancements have brought immense benefits to all humanity.", "patZh": "医学进步给全人类带来了巨大福祉。"},
        {"w": "humble", "ipa": "ˈhʌmbl", "pos": "adj. / vt.", "s": "s3", "zh": "谦逊的", "exam": "谦逊的；地位卑微的；使谦逊", "c": ["humble background 卑微的背景", "humble opinion 拙见"], "syn": ["modest", "meek", "unassuming"], "fam":["humbly adv. 谦逊地"], "dif": "humble 侧重虚心谦逊不自傲，或出身普通卑微。 ", "pat": "Despite his brilliant success, he remained a remarkably humble scholar.", "patZh": "尽管取得了辉煌的成功，他依然是一位格外谦逊的学者。"},
        {"w": "intend", "ipa": "ɪnˈtend", "pos": "vt.", "s": "s3", "zh": "打算", "exam": "想要；打算；预求", "c": ["intend to do 打算做…", "be intended for 专供…"], "syn": ["plan", "aim", "designate"], "fam":["intention n. 意图"], "dif": "intend 指心中计划打算达成某种目的或用途。 ", "pat": "We fully intend to complete the software upgrade by next month.", "patZh": "我们完全打算在下个月前完成软件升级。"},
        {"w": "intention", "ipa": "ɪnˈtenʃn", "pos": "n.", "s": "s3", "zh": "意图", "exam": "意图；目的；打算", "c": ["good intentions 良好的意图", "with the intention of 怀着…目的"], "syn": ["purpose", "goal", "aim"], "fam":["intentional adj. 有意的"], "dif": "intention 指行动背后预先设立的具体目的意图。 ", "pat": "He signed the contract with the clear intention of expanding the business.", "patZh": "他签署合同怀有明确拓展业务的意图。"},

        {"w": "intense", "ipa": "ɪnˈtens", "pos": "adj.", "s": "s4", "zh": "激烈的", "exam": "剧烈的；激烈的；强烈的；热情的", "c": ["intense heat 酷热", "intense competition 激烈的竞争"], "syn": ["severe", "fierce", "extreme"], "fam":["intensity n. 强度"], "dif": "intense 强调感情、痛楚、竞争在程度上的剧烈强烈。 ", "pat": "Athletes faced intense heat during the marathon race.", "patZh": "运动员们在马拉松赛跑期间面对酷热。"},
        {"w": "intensity", "ipa": "ɪnˈtensəti", "pos": "n.", "s": "s4", "zh": "强度", "exam": "强烈；剧烈；强度", "c": ["high intensity 高强度", "intensity of light 光照强度"], "syn": ["strength", "force", "power"], "fam":["intense adj. 剧烈的"], "dif": "intensity 物理学或抽象意义上测量的力量、情感强度水平。 ", "pat": "The hurricane increased in intensity as it approached the coast.", "patZh": "当飓风逼近海岸时，其强度不断增加。"},
        {"w": "intensive", "ipa": "ɪnˈtensɪv", "pos": "adj.", "s": "s4", "zh": "集中的", "exam": "集中的；精细的；加强的", "c": ["intensive care 密集护理/ICU", "labor intensive 劳动密集型的"], "syn": ["thorough", "concentrated", "rigorous"], "fam":["intensify v. 加强"], "dif": "intensive 侧重短时间内投入大量资源开展的精细集中行动。 ", "pat": "Students completed an intensive course in business English before traveling.", "patZh": "学生们在出行前完成了一门商务英语集训课程。"},
        {"w": "interact", "ipa": "ˌɪntərˈækt", "pos": "vi.", "s": "s4", "zh": "互动", "exam": "相互作用；相互影响；交流", "c": ["interact with 与…互动", "interact socially 社交互动"], "syn": ["engage", "mingle", "interrelate"], "fam":["interaction n. 互动"], "dif": "interact 指两者或多方之间产生互相交流影响。 ", "pat": "Teachers encourage students to interact actively during class discussions.", "patZh": "老师鼓励学生在课堂讨论期间积极互动。"},
        {"w": "intercourse", "ipa": "ˈɪntəkɔːs", "pos": "n.", "s": "s4", "zh": "交流", "exam": "交流；往来；交际", "c": ["social intercourse 社交往来", "commercial intercourse 商业往来"], "syn": ["communication", "dealings", "contact"], "fam":["intercourse n. 往来"], "dif": "intercourse 指社会、国家、思想之间的正式往来交流。 ", "pat": "Freedom of trade promotes peaceful commercial intercourse between nations.", "patZh": "贸易自由促进国家之间和平的商业往来。"},
        {"w": "interest", "ipa": "ˈɪntrest", "pos": "n. / vt.", "s": "s4", "zh": "兴趣", "exam": "兴趣；利益；利息；使感兴趣", "c": ["in the interest of 为了…利益", "interest rate 利率"], "syn": ["curiosity", "benefit", "stake"], "fam":["interesting adj. 有趣的"], "dif": "interest 作名词指兴趣求知欲、商业利益或贷款利息。 ", "pat": "Central banks raised the interest rate to curb runaway inflation.", "patZh": "中央银行提高了利率以遏制失控的通胀。"},
        {"w": "interior", "ipa": "ɪnˈtɪəriə", "pos": "n. / adj.", "s": "s4", "zh": "内部", "exam": "内部；内地；内部的；内陆的", "c": ["interior design 室内设计", "interior ministry 内政部"], "syn": ["inside", "inward", "inner"], "fam":["interior adj. 内部的"], "dif": "interior 指建筑物、机构内部空间，或国家内陆地区（与 exterior 相对）。 ", "pat": "The interior design of the hotel combines modern and traditional elements.", "patZh": "该酒店的室内设计融合了现代与传统元素。"},
        {"w": "internal", "ipa": "ɪnˈtɜːnl", "pos": "adj.", "s": "s4", "zh": "内部的", "exam": "内部的；国内的；体内的", "c": ["internal audit 内部审计", "internal organs 体内器官"], "syn": ["inner", "domestic", "inside"], "fam":["internally adv. 在内部"], "dif": "internal 强调机构、身体或系统内部的结构功能。 ", "pat": "The executive board ordered a thorough internal audit of financial accounts.", "patZh": "执行董事会下令对财务账户进行彻底的内部审计。"},
        {"w": "international", "ipa": "ˌɪntəˈnæʃnəl", "pos": "adj.", "s": "s4", "zh": "国际的", "exam": "国际的；世界性的", "c": ["international trade 国际贸易", "international community 国际社会"], "syn": ["global", "worldwide", "transnational"], "fam":["internationally adv. 在国际上"], "dif": "international 涉及两个或多个国家之间的交流关系。 ", "pat": "The summit brought together leaders from across the international community.", "patZh": "峰会汇聚了来自整个国际社会的领导人。"},
        {"w": "interpret", "ipa": "ɪnˈtɜːprɪt", "pos": "v.", "s": "s4", "zh": "解读", "exam": "解释；说明；口译；把…理解为", "c": ["interpret data 解读数据", "interpret for 替…口译"], "syn": ["explain", "translate", "construe"], "fam":["interpretation n. 解释；口译"], "dif": "interpret 侧重对数据、法律条文进行学术解说理解，或进行口译。 ", "pat": "Scholars gathered to interpret newly discovered ancient manuscripts.", "patZh": "学者们聚集在一起解读新发现的古代手稿。"},
        {"w": "lose", "ipa": "luːz", "pos": "v.", "s": "s4", "zh": "失去", "exam": "失去；输掉；迷失；浪费", "c": ["lose weight 减肥", "lose a job 失去工作"], "syn": ["forfeit", "misplace", "drop"], "fam":["loss n. 损失", "loser n. 失败者"], "dif": "lose 侧重失去物品、比赛输掉或迷失方向。 ", "pat": "Companies stand to lose valuable clients if service quality declines.", "patZh": "如果服务质量下降，公司面临失去宝贵客户的风险。"},
        {"w": "loss", "ipa": "lɒs", "pos": "n.", "s": "s4", "zh": "损失", "exam": "丧失；损失；亏损", "c": ["financial loss 财务亏损", "at a loss 茫然不知所措"], "syn": ["deficit", "deprivation", "harm"], "fam":["lose v. 失去"], "dif": "loss 指失去某物、亲人离世，或财务上的亏损赤字。 ", "pat": "Insurance covered the full financial loss caused by the factory fire.", "patZh": "保险涵盖了由工厂火灾造成的全部财务损失。"},
        {"w": "low", "ipa": "ləʊ", "pos": "adj. / adv. / n.", "s": "s4", "zh": "低下的", "exam": "低的；矮的；低下的；低价", "c": ["low temperature 低温", "low cost 低成本"], "syn": ["short", "modest", "depressed"], "fam":["lower v. 降低"], "dif": "low 侧重位置矮、数量少、程度或价格低下。 ", "pat": "Engineers designed an energy-efficient home with extremely low power consumption.", "patZh": "工程师设计了一栋具有极低功耗的节能住宅。"},
        {"w": "lower", "ipa": "ˈləʊə", "pos": "vt. / adj.", "s": "s4", "zh": "降低", "exam": "降低；减少；较低的", "c": ["lower prices 降低价格", "lower risk 减少风险"], "syn": ["reduce", "decrease", "lessen"], "fam":["low adj. 低的"], "dif": "lower 作动词指使高度、价格、音量降低变小。 ", "pat": "The bank voted to lower interest rates to stimulate business borrowing.", "patZh": "银行投票决定降低利率以刺激企业借贷。"},
        {"w": "lucrative", "ipa": "ˈluːkrətɪv", "pos": "adj.", "s": "s4", "zh": "盈利丰厚的", "exam": "赚钱的；盈利丰厚的", "c": ["lucrative contract 盈利丰厚的合同", "lucrative market 高利润市场"], "syn": ["profitable", "remunerative", "gainful"], "fam":["lucre n. 利润"], "dif": "lucrative 特指能产生巨额金钱利润的商业活动或合同。 ", "pat": "He abandoned his law practice to pursue a lucrative career in investment banking.", "patZh": "他放弃了法律执业去从事投资银行这一盈利丰厚的职业。"},
        {"w": "nerve", "ipa": "nɜːv", "pos": "n. / vt.", "s": "s4", "zh": "神经", "exam": "神经；勇气；胆量；鼓起勇气", "c": ["have the nerve 有勇气", "nerve center 神经中枢"], "syn": ["courage", "bravery", "grit"], "fam":["nervous adj. 紧张的"], "dif": "nerve 指生理神经系统，或内心的胆量勇气。 ", "pat": "It takes immense nerve to step onto the international stage alone.", "patZh": "独自走上国际舞台需要巨大的勇气。"},
        {"w": "nervous", "ipa": "ˈnɜːvəs", "pos": "adj.", "s": "s4", "zh": "紧张不安的", "exam": "神经紧张的；焦虑不安的；神经的", "c": ["feel nervous 感到紧张", "nervous system 神经系统"], "syn": ["anxious", "apprehensive", "edgy"], "fam":["nerve n. 神经"], "dif": "nervous 描写因担心、恐惧而产生的心理紧张不安。 ", "pat": "She felt extremely nervous right before presenting her speech to the board.", "patZh": "在向董事会展示演讲前她感到极其紧张不安。"},
        {"w": "nevertheless", "ipa": "ˌnevəðəˈles", "pos": "adv.", "s": "s4", "zh": "尽管如此", "exam": "然而；尽管如此", "c": ["nevertheless, he agreed 尽管如此，他同意了", "nevertheless, he persevered 尽管如此，他仍坚持"], "syn": ["however", "nonetheless", "still"], "fam":["nevertheless adv. 尽管如此"], "dif": "nevertheless 作转折副词，强调即使存在某种情况，后面的事实依然成立。 ", "pat": "The task was extraordinarily difficult; nevertheless, the team completed it on schedule.", "patZh": "任务极其困难；尽管如此，团队依然按时完成了任务。"}
    ]
}

os.makedirs(story_dir, exist_ok=True)

with open(os.path.join(story_dir, "Unit25.json"), "w", encoding="utf-8") as f:
    json.dump(unit25_data, f, ensure_ascii=False, indent=2)

with open(os.path.join(story_dir, "Unit26.json"), "w", encoding="utf-8") as f:
    json.dump(unit26_data, f, ensure_ascii=False, indent=2)

print("Saved Unit25.json and Unit26.json successfully.")
