import json
import os
import subprocess

story_dir = r"d:\xinyi\codespace\WowStory\单词故事本"
csv_path = r"d:\xinyi\codespace\WowStory\红宝书必考词_全量汇总_清洗版.csv"
validator = r"d:\xinyi\codespace\WowStory\scripts\validate_unit.py"
builder = r"d:\xinyi\codespace\WowStory\scripts\build_md.py"

# Unit 21 (54 words)
unit21_data = {
    "unit": 21,
    "stories": [
        {
            "id": "s1",
            "en": "The Ambition of Art",
            "zh": "艺术的野心",
            "theme": "人物 / 社会",
            "ps": [
                {
                    "en": "When a severe drought threatened to [[pose]] challenges to agricultural communities, a young artist took a [[position]] in the local council to promote [[positive]] change. Although she did not [[possess]] great wealth, her temporary [[possession]] of a community center allowed her to host workshops.",
                    "zh": "当一场严重的旱灾给农业社区带来挑战时，一位年轻的艺术家在当地委员会中担任职务以促进积极的变革。虽然她没有拥有巨额财富，但她临时占有一座社区中心让她得以举办工作坊。"
                },
                {
                    "en": "To show how to [[dilute]] harmful pesticides, she painted a [[dim]] portrait of polluted rivers to warn against ecological [[diminishment|diminish]]. At first, critics dismissed her as a mere [[amateur]], but her ability to [[amaze]] spectators soon dispelled any [[ambiguous]] doubts about her purpose.",
                    "zh": "为了展示如何稀释有害杀虫剂，她画了一副暗淡的污染河流肖像，以警告生态削减。起初，评论家驳斥她只是个单纯的业余爱好者，但她令观众惊叹的能力很快驱散了对其意图的任何模糊疑虑。"
                },
                {
                    "en": "Her ultimate [[ambition]] was to foster an [[ambitious]] youth movement dedicated to environmental stewardship across the region.",
                    "zh": "她的终极野心是培养一场雄心勃勃的青年运动，致力于全地区的环境管理。"
                }
            ]
        },
        {
            "id": "s2",
            "en": "The Business Conference",
            "zh": "商业会议",
            "theme": "商业 / 契约",
            "ps": [
                {
                    "en": "Investors feared that the tech speculation [[bubble]] would burst before the company could finalize its annual [[budget]]. To [[build]] a sustainable enterprise, executives reorganized their core [[business]] model.",
                    "zh": "投资者担心科技投机泡沫会在公司敲定年度预算前破裂。为了建立可持续的企业，高管们重组了他们的核心商业模式。"
                },
                {
                    "en": "Engineers attempted to [[compress]] data processing times, agreeing that the new platform would [[comprise]] advanced cloud services. Rather than make a risky [[compromise]] on security, they chose to [[conceive]] an innovative architecture and [[concentrate]] resources on algorithm optimization.",
                    "zh": "工程师们试图压缩数据处理时间，同意新平台将包含先进的云服务。他们没有在安全方面做出危险的妥协，而是选择构想一种创新架构，并将资源集中在算法优化上。"
                },
                {
                    "en": "The underlying [[concept]] was to transform the original [[conception]] into a practical product. Driven by deep [[concern]] for user privacy, the team drafted a [[concise]] proposal with [[concrete]] steps, which they decided to [[conclude]] with a firm [[conclusion]] during a [[concurrent]] executive summit. They agreed to [[confer]] honorable awards at the annual [[conference]].",
                    "zh": "其底层概念是将原始构想转化为实用产品。在对用户隐私深度关切的驱动下，团队起草了一份包含具体步骤的简明提案，他们决定在并发举行的高管峰会上做出明确结论。他们同意在年度会议上授予荣誉奖项。"
                }
            ]
        },
        {
            "id": "s3",
            "en": "Lessons of the Epoch",
            "zh": "时代的教训",
            "theme": "学术 / 思考",
            "ps": [
                {
                    "en": "Historians will [[confess]] that recording an [[epic]] struggle during a global [[epidemic]] requires immense objectivity. Each historical [[episode]] marks a turning point in a grand [[epoch]].",
                    "zh": "历史学家会坦白，在全局疫情期间记录一场史诗般的挣扎需要极大的客观性。每一个历史片段都标志着伟大时代中的转折点。"
                },
                {
                    "en": "Scholars warned against remaining [[indifferent]] to social inequality. An [[indignant]] public voiced its [[indignation]], demanding access to [[indispensable]] public resources for every [[individual]].",
                    "zh": "学者们警告不要对社会不平等保持漠不关心。义愤填膺的公众表达了他们的愤慨，要求为每一个个人提供不可或缺的公共资源。"
                },
                {
                    "en": "To clear up the bureaucratic [[mess]], the director sent an urgent [[message]] via a trusted [[messenger]]. Reevaluating their research [[method]], [[militant]] activists and [[military]] advisors agreed in [[mind]] that reforms must [[redeem]] past errors, [[reduce]] unnecessary costs, ensure a swift [[reduction]] in pollution, and [[refer]] to historical precedent for reliable [[reference]].",
                    "zh": "为了清理官僚混乱，主管通过信任的邮递员发送了紧急信息。重新评估他们的研究方法，激进的倡导者与军事顾问在思想上达成一致，认为改革必须赎回过去的错误、减少不必要的开支、确保迅速减少污染，并参考历史先例作为可靠依据。"
                }
            ]
        }
    ],
    "words": [
        {"w": "pose", "ipa": "pəʊz", "pos": "v. / n.", "s": "s1", "zh": "带来", "exam": "造成；提出；摆姿势；姿势", "c": ["pose a threat 构成威胁", "pose a question 提出问题"], "syn": ["present", "constitute", "posture"], "fam": ["position n. 位置"], "dif": "pose 侧重指造成困难、提出问题或摆出特定姿势；present 指呈现。", "pat": "Rapid urbanization can pose significant challenges to municipal infrastructure.", "patZh": "快速城市化可能会对市政基础设施造成重大挑战。"},
        {"w": "position", "ipa": "pəˈzɪʃn", "pos": "n. / vt.", "s": "s1", "zh": "职务", "exam": "位置；职位；立场；安置", "c": ["take a position 担任职务/采取立场", "in a position to 处于能够…的地位"], "syn": ["post", "stance", "location"], "fam": ["positive adj. 积极的"], "dif": "position 既可指具体物理位置，也可指工作职位或观点立场。", "pat": "She accepted a senior research position at the university.", "patZh": "她接受了大学里的高级研究职位。"},
        {"w": "positive", "ipa": "ˈpɒzətɪv", "pos": "adj.", "s": "s1", "zh": "积极的", "exam": "积极的；正面的；确信的", "c": ["positive attitude 积极的态度", "positive effect 积极的影响"], "syn": ["constructive", "optimistic", "favorable"], "fam": ["positively adv. 积极地"], "dif": "positive 强调有建设性、乐观或呈阳性反应。", "pat": "Regular exercise produces positive effects on overall mental health.", "patZh": "规律运动对整体心理健康产生积极的影响。"},
        {"w": "possess", "ipa": "pəˈzes", "pos": "vt.", "s": "s1", "zh": "拥有", "exam": "拥有；具有", "c": ["possess wealth 拥有财富", "possess skills 具备技能"], "syn": ["own", "hold", "enjoy"], "fam": ["possession n. 拥有；财产"], "dif": "possess 侧重具备某种品质、技能或依法拥有资产。", "pat": "Candidates must possess strong analytical skills and leadership experience.", "patZh": "候选人必须具备强大的分析技能和领导经验。"},
        {"w": "possession", "ipa": "pəˈzeʃn", "pos": "n.", "s": "s1", "zh": "占有", "exam": "所有；占有；财产", "c": ["in possession of 占有/拥有", "personal possessions 个人财产"], "syn": ["ownership", "belongings", "property"], "fam": ["possess v. 拥有"], "dif": "possession 复数形式特指个人私有物品财产。", "pat": "The historic documents came into the possession of the national archive.", "patZh": "这些历史文件落入了国家档案馆的占有之中。"},
        {"w": "dilute", "ipa": "daɪˈluːt", "pos": "vt. / adj.", "s": "s1", "zh": "稀释", "exam": "稀释；冲淡；稀释了的", "c": ["dilute a solution 稀释溶液", "dilute the impact 冲淡影响"], "syn": ["weaken", "thin", "water down"], "fam": ["dilution n. 稀释"], "dif": "dilute 液体加水稀释，或抽象减弱某种力量效应。", "pat": "Adding too much water will dilute the chemical strength of the mixture.", "patZh": "加入太多的水会稀释该混合物的化学强度。"},
        {"w": "dim", "ipa": "dɪm", "pos": "adj. / v.", "s": "s1", "zh": "暗淡的", "exam": "暗淡的；模糊的；使变暗", "c": ["dim light 昏暗的光线", "dim view of 认为…不大可能"], "syn": ["faint", "shadowy", "obscure"], "fam": ["dimly adv. 昏暗地"], "dif": "dim 指光线微弱暗淡或前景不明朗。", "pat": "The streetlights cast a dim glow through the heavy evening fog.", "patZh": "街灯在沉重的晚雾中投射出暗淡的光晕。"},
        {"w": "diminish", "ipa": "dɪˈmɪnɪʃ", "pos": "v.", "s": "s1", "zh": "削减", "exam": "减少；降低；削减", "c": ["diminish over time 随着时间减少", "diminish power 削弱权力"], "syn": ["decrease", "lessen", "dwindle"], "fam": ["diminution n. 减少"], "dif": "diminish 指数量、重要性或权威逐渐减少变小。", "pat": "Nothing can diminish the profound impact of his groundbreaking discovery.", "patZh": "没有什么能削减他突破性发现的深远影响。"},
        {"w": "amateur", "ipa": "ˈæmətə", "pos": "n. / adj.", "s": "s1", "zh": "业余爱好者", "exam": "业余爱好者；业余的", "c": ["amateur photographer 业余摄影师", "amateur sports 业余体育运动"], "syn": ["nonprofessional", "layman", "novice"], "fam": ["amateurish adj. 业余水平的"], "dif": "amateur 指非出于职业赚钱目的而出于兴趣从事某事的人。", "pat": "The tournament welcomed both professional athletes and talented amateurs.", "patZh": "该锦标赛欢迎职业运动员与有天赋的业余爱好者参加。"},
        {"w": "amaze", "ipa": "əˈmeɪz", "pos": "vt.", "s": "s1", "zh": "使惊叹", "exam": "使惊奇；使惊叹", "c": ["amaze the audience 使观众惊叹", "be amazed at 对…感到惊奇"], "syn": ["astonish", "astound", "surprise"], "fam": ["amazing adj. 令人惊叹的", "amazement n. 惊奇"], "dif": "amaze 强调因出乎意料的高超表现而令人极度惊叹。", "pat": "Her remarkable recovery continues to amaze doctors across the medical community.", "patZh": "她显著的康复继续使整个医疗界的医生感到惊叹。"},
        {"w": "ambiguous", "ipa": "æmˈbɪɡjuəs", "pos": "adj.", "s": "s1", "zh": "模糊的", "exam": "模棱两可的；含糊的", "c": ["ambiguous statement 模棱两可的声明", "ambiguous meaning 模糊的含义"], "syn": ["equivocal", "unclear", "vague"], "fam": ["ambiguity n. 模棱两可"], "dif": "ambiguous 指由于表达不明确而可作多种不同解释。", "pat": "The contract contained ambiguous language that led to a protracted dispute.", "patZh": "该合同包含模棱两可的措辞，导致了长期的争议。"},
        {"w": "ambition", "ipa": "æmˈbɪʃn", "pos": "n.", "s": "s1", "zh": "野心", "exam": "雄心；野心；抱负", "c": ["achieve ambition 实现抱负", "lifelong ambition 终生抱负"], "syn": ["aspiration", "goal", "drive"], "fam": ["ambitious adj. 有雄心的"], "dif": "ambition 中性偏褒义指宏大抱负，也可指过度的权力野心。", "pat": "His ambition was to establish an international research institute.", "patZh": "他的抱负是建立一个国际研究机构。"},
        {"w": "ambitious", "ipa": "æmˈbɪʃəs", "pos": "adj.", "s": "s1", "zh": "雄心勃勃的", "exam": "雄心勃勃的；野心勃勃的", "c": ["ambitious plan 雄心勃勃的计划", "ambitious goal 宏伟的目标"], "syn": ["aspiring", "bold", "enterprising"], "fam": ["ambition n. 抱负"], "dif": "ambitious 描写计划宏大或个人极具进取心。", "pat": "The government launched an ambitious campaign to achieve carbon neutrality.", "patZh": "政府启动了一项旨在实现碳中和的雄心勃勃的运动。"},

        {"w": "bubble", "ipa": "ˈbʌbl", "pos": "n. / vi.", "s": "s2", "zh": "泡沫", "exam": "气泡；泡沫；起泡", "c": ["economic bubble 经济泡沫", "burst the bubble 打破泡沫"], "syn": ["foam", "blister", "illusion"], "fam": ["bubbly adj. 充满气泡的"], "dif": "bubble 指物理气体泡沫，或经济投机膨胀的虚幻泡沫。", "pat": "Financial analysts warned that the housing market bubble could collapse suddenly.", "patZh": "金融分析师警告说，住房市场泡沫可能会突然破裂。"},
        {"w": "budget", "ipa": "ˈbʌdʒɪt", "pos": "n. / v.", "s": "s2", "zh": "预算", "exam": "预算；编制预算", "c": ["annual budget 年度预算", "budget constraint 预算约束"], "syn": ["financial plan", "allocation", "allotment"], "fam": ["budgetary adj. 预算的"], "dif": "budget 指划定的收支预算计划或控制支出的过程。", "pat": "The department managed to complete the infrastructure project well within budget.", "patZh": "该部门成功地在预算之内完成了基础设施项目。"},
        {"w": "build", "ipa": "bɪld", "pos": "v. / n.", "s": "s2", "zh": "建立", "exam": "建造；建立；体格", "c": ["build a reputation 建立声誉", "build confidence 树立信心"], "syn": ["construct", "erect", "establish"], "fam": ["building n. 建筑物", "builder n. 建筑工"], "dif": "build 可指修建实体建筑物，也可指建立抽象关系声誉。", "pat": "Engineers worked together to build a state-of-the-art research facility.", "patZh": "工程师们合作建立了一座最先进的研究设施。"},
        {"w": "business", "ipa": "ˈbɪznəs", "pos": "n.", "s": "s2", "zh": "商业", "exam": "商业；生意；事务；企业", "c": ["business model 商业模式", "on business 出差"], "syn": ["commerce", "trade", "enterprise"], "fam": ["businessman n. 商人"], "dif": "business 指商业活动、企业或个人应管的私事。", "pat": "Adopting sustainable energy is essential for modern business success.", "patZh": "采用可持续能源对于现代商业成功至关重要。"},
        {"w": "compress", "ipa": "kəmˈpres", "pos": "v.", "s": "s2", "zh": "压缩", "exam": "压缩；精简", "c": ["compress data 压缩数据", "compress air 压缩空气"], "syn": ["condense", "squeeze", "compact"], "fam": ["compression n. 压缩", "compressor n. 压缩机"], "dif": "compress 指施加压力使体积缩小，或压缩数据时间。", "pat": "Software algorithms can compress large video files without sacrificing clarity.", "patZh": "软件算法可以在不牺牲清晰度的情况下压缩大型视频文件。"},
        {"w": "comprise", "ipa": "kəmˈpraɪz", "pos": "vt.", "s": "s2", "zh": "包含", "exam": "包含；由…组成", "c": ["be comprised of 由…组成", "comprise several teams 包含几个团队"], "syn": ["consist of", "include", "contain"], "fam": ["comprise v. 包含"], "dif": "comprise 主语可为整体表示包含部分，也可表示部分组成整体。", "pat": "The committee is comprised of distinguished representatives from diverse industries.", "patZh": "该委员会由来自不同行业的高级代表组成。"},
        {"w": "compromise", "ipa": "ˈkɒmprəmaɪz", "pos": "n. / v.", "s": "s2", "zh": "妥协", "exam": "妥协；折中；危害", "c": ["reach a compromise 达成妥协", "compromise security 危害安全"], "syn": ["concession", "settlement", "endanger"], "fam": ["compromise v. 妥协"], "dif": "compromise 既指双方各让一步妥协，也可指损害安全原则。", "pat": "Both parties were willing to reach a reasonable compromise to settle the dispute.", "patZh": "双方都愿意达成合理的妥协来解决争议。"},
        {"w": "conceive", "ipa": "kənˈsiːv", "pos": "v.", "s": "s2", "zh": "构想", "exam": "构想；设想；怀孕", "c": ["conceive an idea 构思创意", "conceive of 设想…"], "syn": ["devise", "imagine", "formulate"], "fam": ["concept n. 概念", "conception n. 构想"], "dif": "conceive 侧重在脑海中孕育出新的构思、理念或方案。", "pat": "Architects managed to conceive a innovative plan for urban renewal.", "patZh": "建筑师们成功地构想出了一项城市更新的创新方案。"},
        {"w": "concentrate", "ipa": "ˈkɒnsntreɪt", "pos": "v. / n.", "s": "s2", "zh": "集中", "exam": "全神贯注；集中；浓缩物", "c": ["concentrate on 专心于", "concentrate resources 集中资源"], "syn": ["focus", "center", "converge"], "fam": ["concentration n. 专心；浓度"], "dif": "concentrate 强调将精神或力量资源汇聚集中于一点。", "pat": "Researchers need to concentrate on collecting reliable empirical evidence.", "patZh": "研究人员需要集中精力收集可靠的经验证据。"},
        {"w": "concept", "ipa": "ˈkɒnsept", "pos": "n.", "s": "s2", "zh": "概念", "exam": "概念；观念", "c": ["basic concept 基本概念", "core concept 核心理念"], "syn": ["notion", "idea", "principle"], "fam": ["conceptual adj. 概念上的", "conceive v. 构想"], "dif": "concept 指经过科学抽象概括出的理性概念法则。", "pat": "The teacher explained the fundamental concept of quantum physics clearly.", "patZh": "老师清晰地解释了量子物理的基本概念。"},
        {"w": "conception", "ipa": "kənˈsepʃn", "pos": "n.", "s": "s2", "zh": "构想", "exam": "概念；构想；受孕", "c": ["original conception 原始构想", "conception of justice 对公正的理解"], "syn": ["perception", "understanding", "formulation"], "fam": ["conceive v. 构想"], "dif": "conception 侧重指思维孕育形成新想法的过程或理解。", "pat": "The design underwent major changes from its original conception to production.", "patZh": "该设计从最初的构想到投产经历了重大改变。"},
        {"w": "concern", "ipa": "kənˈsɜːn", "pos": "n. / vt.", "s": "s2", "zh": "关切", "exam": "关切；关心；涉及；使担忧", "c": ["express concern 表达关切", "be concerned with 涉及/关心"], "syn": ["worry", "anxiety", "pertain to"], "fam": ["concerned adj. 担忧的"], "dif": "concern 指对人或事物的关心挂念，或与其有直接利害关系。", "pat": "Rising healthcare costs remain a major concern for middle-class families.", "patZh": "不断上涨的医疗费用依然是中产阶级家庭的主要关切。"},
        {"w": "concise", "ipa": "kənˈsaɪs", "pos": "adj.", "s": "s2", "zh": "简明的", "exam": "简明的；简练的", "c": ["concise summary 简明的总结", "concise statement 简练的陈述"], "syn": ["succinct", "brief", "compact"], "fam": ["conciseness n. 简明"], "dif": "concise 指语言文字简练明确、毫无废话废字。", "pat": "The executive requested a concise overview of the quarter's financial results.", "patZh": "高管要求对本季度的财务结果作一份简明的概述。"},
        {"w": "concrete", "ipa": "ˈkɒŋkriːt", "pos": "adj. / n.", "s": "s2", "zh": "具体的", "exam": "具体的；混凝土", "c": ["concrete evidence 具体证据", "reinforced concrete 钢筋混凝土"], "syn": ["tangible", "solid", "specific"], "fam": ["concrete adj. 具体的"], "dif": "concrete 与 abstract（抽象的）相对，指具体存在的实物或明确的事实。", "pat": "Investigators must gather concrete proof before filing charges.", "patZh": "调查人员在提出指控前必须收集具体的证据。"},
        {"w": "conclude", "ipa": "kənˈkluːd", "pos": "v.", "s": "s2", "zh": "做出结论", "exam": "推断出；结论；结束；缔结", "c": ["conclude that 推断出…", "conclude a treaty 缔结条约"], "syn": ["infer", "finish", "finalize"], "fam": ["conclusion n. 结论", "conclusive adj. 决定性的"], "dif": "conclude 侧重经推导推理得出结论，或使会议协议圆满结束。", "pat": "After examining the data, scientists concluded that the theory was sound.", "patZh": "在检查数据后，科学家们得出结论认为该理论是可靠的。"},
        {"w": "conclusion", "ipa": "kənˈkluːʒn", "pos": "n.", "s": "s2", "zh": "结论", "exam": "结论；推论；结尾", "c": ["draw a conclusion 得出结论", "in conclusion 总之"], "syn": ["deduction", "inference", "closure"], "fam": ["conclude v. 推断"], "dif": "conclusion 指思考推理得出的最终判断或文章末尾总结。", "pat": "The report reached the conclusion that immediate intervention was necessary.", "patZh": "该报告得出了必须立即干预的结论。"},
        {"w": "concurrent", "ipa": "kənˈkʌrənt", "pos": "adj.", "s": "s2", "zh": "并发的", "exam": "同时发生的；并发的", "c": ["concurrent events 同时发生的事件", "concurrent users 并发用户"], "syn": ["simultaneous", "coinciding", "parallel"], "fam": ["concurrently adv. 同时地"], "dif": "concurrent 强调多个事件在时间上完全同时发生或重合。", "pat": "The server can handle thousands of concurrent requests smoothly.", "patZh": "该服务器可以平稳地处理数以千计的并发请求。"},
        {"w": "confer", "ipa": "kənˈfɜː", "pos": "v.", "s": "s2", "zh": "授予", "exam": "商讨；授予", "c": ["confer with 商讨", "confer an honor on 授予荣誉"], "syn": ["consult", "bestow", "grant"], "fam": ["conference n. 会议"], "dif": "confer 搭配 with 表示协商，搭配 on/upon 表示授予勋章学位。", "pat": "The committee will confer with experts before making a final decision.", "patZh": "委员会在做出决定前将与专家商讨。"},
        {"w": "conference", "ipa": "ˈkɒnfərəns", "pos": "n.", "s": "s2", "zh": "会议", "exam": "会议；研讨会", "c": ["press conference 新闻发布会", "annual conference 年度会议"], "syn": ["symposium", "convention", "meeting"], "fam": ["confer v. 商讨"], "dif": "conference 指正式、大规模的讨论或学术商务会议。", "pat": "Delegates gathered at the international conference to discuss climate policy.", "patZh": "代表们聚集在国际会议上讨论气候政策。"},

        {"w": "confess", "ipa": "kənˈfes", "pos": "v.", "s": "s3", "zh": "坦白", "exam": "供认；坦白；承认", "c": ["confess to doing 供认做了…", "confess one's sins 忏悔罪过"], "syn": ["admit", "acknowledge", "disclose"], "fam": ["confession n. 供认；坦白"], "dif": "confess 侧重承认错误、罪行或内心隐秘真实感受。", "pat": "The suspect eventually decided to confess to the crime during questioning.", "patZh": "嫌疑人在审讯期间最终决定承认罪行。"},
        {"w": "epic", "ipa": "ˈepɪk", "pos": "n. / adj.", "s": "s3", "zh": "史诗般的", "exam": "史诗；史诗般的；壮丽的", "c": ["epic poem 史诗", "epic journey 壮丽的历程"], "syn": ["legendary", "heroic", "grand"], "fam": ["epic adj. 史诗般的"], "dif": "epic 指具有宏大历史、英雄主义色彩的叙事诗或壮丽事件。", "pat": "The film depicts the epic struggle of pioneers building a new nation.", "patZh": "该电影描绘了开拓者建立新国家的史诗般挣扎。"},
        {"w": "epidemic", "ipa": "ˌepɪˈdemɪk", "pos": "n. / adj.", "s": "s3", "zh": "疫情", "exam": "流行病；流行；传染的", "c": ["flu epidemic 流感疫情", "epidemic outbreak 疫情爆发"], "syn": ["plague", "outbreak", "widespread"], "fam": ["pandemic n. 全球大流行病"], "dif": "epidemic 特指在某一地区广泛迅速传播的流行性疾病。", "pat": "Health agencies worked quickly to contain the sudden flu epidemic.", "patZh": "卫生机构迅速行动以控制突发流感疫情。"},
        {"w": "episode", "ipa": "ˈepɪsəʊd", "pos": "n.", "s": "s3", "zh": "片段", "exam": "片段；事件；（剧集的）集", "c": ["brief episode 短暂的片段", "latest episode 最新一集"], "syn": ["incident", "installment", "chapter"], "fam": ["episodic adj. 偶发性的"], "dif": "episode 指连续历史/事件中的独立插曲片段或电视剧集。", "pat": "This traumatic episode shaped his perspective on global public health.", "patZh": "这一创伤性片段塑造了他对全球公共卫生的看法。"},
        {"w": "epoch", "ipa": "ˈiːpɒk", "pos": "n.", "s": "s3", "zh": "时代", "exam": "时代；纪元", "c": ["epoch-making 划时代的", "new epoch 新纪元"], "syn": ["era", "age", "period"], "fam": ["era n. 时代"], "dif": "epoch 侧重指由重大历史变革或新事件开创的新纪元时代。", "pat": "The invention of the steam engine marked the beginning of a industrial epoch.", "patZh": "蒸汽机的发明标志着一个工业时代的开始。"},
        {"w": "indifferent", "ipa": "ɪnˈdɪfrənt", "pos": "adj.", "s": "s3", "zh": "漠不关心的", "exam": "冷漠的；不关心的；平庸的", "c": ["be indifferent to 对…冷漠", "indifferent quality 平庸的质量"], "syn": ["unconcerned", "apathetic", "detached"], "fam": ["indifference n. 冷漠"], "dif": "indifferent 指缺乏兴趣、同情心或关心，也可指质量一般。", "pat": "A civil society cannot afford to remain indifferent to extreme poverty.", "patZh": "公民社会承担不起对极度贫困保持冷漠的后果。"},
        {"w": "indignant", "ipa": "ɪnˈdɪɡnənt", "pos": "adj.", "s": "s3", "zh": "义愤填膺的", "exam": "愤怒的；愤慨的", "c": ["indignant response 愤慨的回应", "feel indignant 感到义愤填膺"], "syn": ["outraged", "incensed", "furious"], "fam": ["indignation n. 愤慨"], "dif": "indignant 特指因出于不公正、冒犯或不公平对待而产生的愤怒。", "pat": "Citizens grew indignant when unfair tax laws were introduced.", "patZh": "当不公平的税法出台时，公民们变得义愤填膺。"},
        {"w": "indignation", "ipa": "ˌɪndɪɡˈneɪʃn", "pos": "n.", "s": "s3", "zh": "愤慨", "exam": "愤怒；愤慨", "c": ["public indignation 公众的愤慨", "arouse indignation 引起愤慨"], "syn": ["outrage", "resentment", "fury"], "fam": ["indignant adj. 愤慨的"], "dif": "indignation 强调出于道德公义对邪恶非正义产生的义愤。", "pat": "The decision sparked widespread public indignation across the nation.", "patZh": "这一决定在全国范围内引发了广泛的公众愤慨。"},
        {"w": "indispensable", "ipa": "ˌɪndɪˈspensəbl", "pos": "adj.", "s": "s3", "zh": "不可或缺的", "exam": "必不可少的；不可或缺的", "c": ["indispensable part 不可或缺的部分", "indispensable to 极宝贵/必不可少的"], "syn": ["essential", "vital", "crucial"], "fam": ["dispense v. 分发"], "dif": "indispensable 强调绝不可缺少、无法被替代或省去。", "pat": "Digital skills have become indispensable for professional career growth.", "patZh": "数字技能已成为职业生涯增长不可或缺的部分。"},
        {"w": "individual", "ipa": "ˌɪndɪˈvɪdʒuəl", "pos": "n. / adj.", "s": "s3", "zh": "个人", "exam": "个人；个体；个别的；独特的", "c": ["individual freedom 个人自由", "individual needs 个别需求"], "syn": ["person", "distinct", "single"], "fam": ["individuality n. 个性"], "dif": "individual 与 collective（集体的）相对，指社会中的单一个人。", "pat": "The policy aims to respect individual rights while protecting public welfare.", "patZh": "该政策旨在保障公共福利的同时尊重个人权利。"},
        {"w": "mess", "ipa": "mes", "pos": "n. / vt.", "s": "s3", "zh": "混乱", "exam": "混乱；脏乱；弄脏", "c": ["in a mess 处于混乱中", "make a mess 搞得一塌糊涂"], "syn": ["disorder", "chaos", "muddle"], "fam": ["messy adj. 混乱的"], "dif": "mess 指物理上的杂乱无章，或局势陷入麻烦混乱。", "pat": "The new manager had to clean up the financial mess left by his predecessor.", "patZh": "新经理不得不清理前任留下的财务混乱。"},
        {"w": "message", "ipa": "ˈmesɪdʒ", "pos": "n.", "s": "s3", "zh": "信息", "exam": "信息；消息；要旨", "c": ["send a message 发送信息", "core message 核心要旨"], "syn": ["communication", "note", "meaning"], "fam": ["messenger n. 邮递员"], "dif": "message 可指具体的书信口信，也可指演讲书刊的核心宗旨。", "pat": "The campaign succeeded in conveying its core environmental message effectively.", "patZh": "该运动成功地有效地传达了其核心环境信息。"},
        {"w": "messenger", "ipa": "ˈmesɪndʒə", "pos": "n.", "s": "s3", "zh": "邮递员", "exam": "送信者；邮递员", "c": ["special messenger 专差", "messenger service 送信服务"], "syn": ["courier", "bearer", "carrier"], "fam": ["message n. 信息"], "dif": "messenger 特指负责传递口信、公文或包裹的专人。", "pat": "The urgent court order arrived via a special messenger late at night.", "patZh": "紧急法院命令深夜由专差送到。"},
        {"w": "method", "ipa": "ˈmeθəd", "pos": "n.", "s": "s3", "zh": "方法", "exam": "方法；办法；条理", "c": ["scientific method 科学方法", "teaching method 教学方法"], "syn": ["approach", "technique", "system"], "fam": ["methodical adj. 有条理的"], "dif": "method 侧重指有系统、有步骤、合乎逻辑的具体工作或研究方法。", "pat": "Adopting a rigid scientific method ensures accurate test results.", "patZh": "采用严密的科学方法可以确保准确的测试结果。"},
        {"w": "militant", "ipa": "ˈmɪlɪtənt", "pos": "adj. / n.", "s": "s3", "zh": "激进的", "exam": "好战的；激进的；激进分子", "c": ["militant group 激进组织", "militant stance 强硬/激进立场"], "syn": ["aggressive", "radical", "belligerent"], "fam": ["militancy n. 激进状态"], "dif": "militant 强调富有斗争性、手段强硬甚至具有武力倾向。", "pat": "The peaceful protest was infiltrated by a small militant group.", "patZh": "和平抗议活动遭到了一个小型激进组织的渗透。"},
        {"w": "military", "ipa": "ˈmɪlətri", "pos": "adj. / n.", "s": "s3", "zh": "军事的", "exam": "军事的；军队的；军队", "c": ["military force 军事力量", "military service 服兵役"], "syn": ["armed", "martial", "soldiery"], "fam": ["militarism n. 军事主义"], "dif": "military 专门与国防、军队武装力量相关。", "pat": "The country maintained strong military defense capabilities along its border.", "patZh": "该国在沿边境保持着强大的军事防御能力。"},
        {"w": "mind", "ipa": "maɪnd", "pos": "n. / v.", "s": "s3", "zh": "思想", "exam": "头脑；思想；介意；照顾", "c": ["keep in mind 牢记", "change one's mind 改变主意"], "syn": ["intellect", "brain", "object"], "fam": ["mindful adj. 留心的"], "dif": "mind 作名词指人的理智、头脑或主意；作动词指介意。", "pat": "Keep in mind that continuous learning is the key to personal growth.", "patZh": "请牢记持续学习是个人成长的关键。"},
        {"w": "redeem", "ipa": "rɪˈdiːm", "pos": "vt.", "s": "s3", "zh": "赎回", "exam": "赎回；弥补；拯救", "c": ["redeem a pledge 履行誓言", "redeem oneself 挽回声誉"], "syn": ["retire", "offset", "recover"], "fam": ["redemption n. 赎回；拯救"], "dif": "redeem 指付代价换回物品，或通过良好表现弥补过失。", "pat": "The manager sought to redeem his reputation by leading a successful project.", "patZh": "经理试图通过领导一个成功的项目来挽回自己的声誉。"},
        {"w": "reduce", "ipa": "rɪˈdjuːs", "pos": "vt.", "s": "s3", "zh": "减少", "exam": "减少；降低；简化", "c": ["reduce costs 降低成本", "reduce risk 减少风险"], "syn": ["decrease", "curtail", "lower"], "fam": ["reduction n. 减少"], "dif": "reduce 泛指使尺寸、数量、程度或价格降低变小。", "pat": "Companies are striving to reduce carbon emissions by using clean energy.", "patZh": "公司正努力通过使用清洁能源来减少碳排放。"},
        {"w": "reduction", "ipa": "rɪˈdʌkʃn", "pos": "n.", "s": "s3", "zh": "减少", "exam": "减少；缩减；降低", "c": ["price reduction 降价", "reduction in pollution 污染减少"], "syn": ["cut", "diminution", "decrease"], "fam": ["reduce v. 减少"], "dif": "reduction 指数量、程度下降或削减的过程与结果。", "pat": "A significant reduction in operational expenses restored profitability.", "patZh": "运营费用的显著减少恢复了盈利能力。"},
        {"w": "refer", "ipa": "rɪˈfɜː", "pos": "v.", "s": "s3", "zh": "参考", "exam": "参考；查阅；涉及；提到", "c": ["refer to 参照/参考/涉及", "refer a case to 移交案件"], "syn": ["allude", "consult", "attribute"], "fam": ["reference n. 参考；提及"], "dif": "refer 搭配 to 可指提及、查阅资料或将问题移交决定。", "pat": "Please refer to the technical manual for detailed installation instructions.", "patZh": "请参考技术手册获取详细的安装说明。"},
        {"w": "reference", "ipa": "ˈrefrəns", "pos": "n.", "s": "s3", "zh": "参考", "exam": "参考；查阅；推荐信；参考书目", "c": ["for future reference 供日后参考", "reference book 参考书"], "syn": ["citation", "recommendation", "allusion"], "fam": ["refer v. 涉及"], "dif": "reference 指查阅资料、推荐信，或文献中的参考引文。", "pat": "Keep this guidebook handy for quick reference during your business trip.", "patZh": "请妥善保存此指南，以便在出差期间快速参考。"}
    ]
}

# Unit 22 (81 words)
unit22_data = {
    "unit": 22,
    "stories": [
        {
            "id": "s1",
            "en": "The Stage of Public Opinion",
            "zh": "舆论的舞台",
            "theme": "心理 / 演艺",
            "ps": [
                {
                    "en": "In modern media, analysts warn against relying on purely [[subjective]] opinions when evaluating public policies. A well-known organization agreed to [[sponsor]] a civic forum to prevent fake news from [[spoiling|spoil]] public trust. Their primary goal was to [[spread]] reliable data and provide a constructive [[spur]] to national reform.",
                    "zh": "在现代媒体中，分析人士警告说，在评估公共政策时不要依赖纯粹的主观观点。一家知名机构同意赞助一个公民论坛，以防止假新闻破坏公众信任。他们的主要目标是传播可靠数据，并对国家改革提供建设性刺激。"
                },
                {
                    "en": "Undercover agents continued to [[spy]] on hostile networks, evaluating whether the government could maintain political [[stability]]. Maintaining a [[stable]] economic climate allowed executive [[staff]] to step onto the national [[stage]] with confidence.",
                    "zh": "卧底特工继续侦察敌对网络，评估政府能否维持政治稳定。保持稳定的经济气候让执行员工能够有信心走上国家舞台。"
                }
            ]
        },
        {
            "id": "s2",
            "en": "Turbulent Transitions",
            "zh": "动荡的转型",
            "theme": "社会 / 动荡",
            "ps": [
                {
                    "en": "A sudden political [[twist]] forced negotiators to dismiss [[trivial]] complaints and [[try]] a bold new diplomatic approach. The stock market began to [[tumble]] during a [[turbulent]] quarter, but leaders managed to [[turn]] the situation around, boosting corporate [[turnover]] significantly.",
                    "zh": "政治上的突发转折迫使谈判代表驳回琐碎的控诉，并尝试一种大胆的新外交方法。股市在动荡的季度中开始跌倒，但领导人成功地扭转局势，大幅提升了企业营业额。"
                },
                {
                    "en": "They identified the [[typical]] pattern of market fluctuations and called for a [[voluntary]] agreement. Every [[volunteer]] was asked to [[vote]] against corrupt measures, ensuring that [[vulgar]] commercial abuses did not hurt [[vulnerable]] social groups.",
                    "zh": "他们识别出市场波动的典型模式，并呼吁达成自愿协议。每一位志愿者被要求投票反对腐败措施，确保粗俗的商业滥用不会伤害脆弱的社会群体。"
                }
            ]
        },
        {
            "id": "s3",
            "en": "The Legal Audit",
            "zh": "法律审计",
            "theme": "法律 / 审计",
            "ps": [
                {
                    "en": "The [[author]] of the compliance guide consulted the highest legal [[authority]] to establish [[auxiliary]] standards. They realized that emergency funds would not [[avail]] unless immediately made [[available]] to regional clinics. A prominent legal [[critic]] voiced sharp [[criticism]], insisting that auditors must [[criticize]] negligence while recognizing [[critical]] safety upgrades.",
                    "zh": "合规指南的作者咨询了最高法律权威以确立辅助标准。他们意识到，除非立即提供给区域诊所，否则应急资金将不起作用。一位著名的法律批评家发表了尖锐的批评，坚持认为审计人员必须批评疏忽，同时认可关键的安全升级。"
                },
                {
                    "en": "A [[crucial]] inquiry was launched to [[culminate]] in a comprehensive trial, seeking to identify the true [[culprit]] behind the financial fraud.",
                    "zh": "一项关键的调查展开了，旨在以一场全面的审判告终，力图指认出财务欺诈背后的真正罪犯。"
                }
            ]
        },
        {
            "id": "s4",
            "en": "Cultivating Growth",
            "zh": "培养增长",
            "theme": "经济 / 文化",
            "ps": [
                {
                    "en": "Local leaders sought to [[cultivate]] a rich civic [[culture]] by promoting [[dual]] educational languages. Resolving [[dubious]] claims regarding [[due]] taxes, the company promised to build [[durable]] public infrastructure for the long [[duration]] of the project. Fulfilling their public [[duty]], they sparked [[dynamic]] economic activity across the region.",
                    "zh": "当地领导人试图通过推广双语教育来培养丰富的公民文化。解决关于到期应缴税款的可疑主张，该公司承诺在项目的长期持续期间建设耐用的公共基础设施。履行他们的公共职责，他们在全地区引发了动态的经济活动。"
                },
                {
                    "en": "Environmentalists feared that endangered species might become [[extinct]] if fires were not quickly [[extinguished|extinguish]]. To prevent loss, experts proposed to [[introduce]] green tech, marking the [[introduction]] of a strategic campaign to [[invest]] capital and boost foreign [[investment]] in sustainable agriculture.",
                    "zh": "环保主义者担心，如果火灾不快速扑灭，濒危物种可能会灭绝。为了防止损失，专家建议引入绿色科技，标志着投入资金并促进外资对可持续农业投资的战略运动的引入。"
                }
            ]
        },
        {
            "id": "s5",
            "en": "The Systematic Investigation",
            "zh": "系统的调查",
            "theme": "科技 / 系统",
            "ps": [
                {
                    "en": "Special agents were assigned to [[investigate]] a [[mysterious]] criminal network, treating the case as a deep [[mystery]] rather than an ancient [[myth]]. Guided by [[noble]] ethics and a strict social [[norm]], they worked toward the [[normalization]] of [[normal]] operational standards.",
                    "zh": "特别特工被指派去调查一个神秘的犯罪网络，将此案视为深奥的谜团，而不是古代的神话。在高尚道德和严格社会规范的指导下，他们致力于使正常运营标准常态化。"
                },
                {
                    "en": "Investigators took careful [[note]] of a troubling [[notion]] that corporate fraud was being hidden from the [[public]]. The [[publication]] and widespread [[publicity]] of their findings forced media outlets to [[publish]] the whole truth, showing that the [[resultant]] reform would [[resume]] public trust.",
                    "zh": "调查人员仔细记录了一种令人不安的观念，即公司欺诈正向公众隐瞒。他们调查结果的出版和广泛宣传迫使媒体机构公布全部事实，表明产生的改革将恢复公众信任。"
                },
                {
                    "en": "The evidence failed to [[reveal]] any secret attempts at [[revenge]], showing instead that state [[revenue]] was used properly to [[supply]] equipment, [[support]] research, [[suppose|supposing]] clear intent to [[suppress]] illegal trade, [[supplement]] healthcare funds, and maintain [[supreme]] standards across a [[systematic]] public [[system]].",
                    "zh": "证据未能揭示任何秘密报复尝试，反倒表明国家财政收入被妥善用于供应设备、支持研究、假设有明确意图以镇压非法交易、补充医疗资金，并在一个系统的公共体系中维持至高无上的标准。"
                }
            ]
        }
    ],
    "words": [
        # Unit 22 81 words
        {"w": "subjective", "ipa": "səbˈdʒektɪv", "pos": "adj.", "s": "s1", "zh": "主观的", "exam": "主观的", "c": ["subjective judgment 主观判断", "subjective view 主观观点"], "syn": ["personal", "biased", "individual"], "fam": ["objectivity n. 客观性"], "dif": "subjective 强调出于个人主观感受或偏见；objective 强调客观公正。", "pat": "Evaluating artistic merit often involves subjective personal taste.", "patZh": "评估艺术价值往往涉及主观的个人品味。"},
        {"w": "spoil", "ipa": "spɔɪl", "pos": "v. / n.", "s": "s1", "zh": "破坏", "exam": "损坏；破坏；宠坏；变质", "c": ["spoil the appetite 破坏食欲", "spoil a child 宠坏孩子"], "syn": ["ruin", "mar", "pamper"], "fam": ["spoilage n. 腐烂；损坏"], "dif": "spoil 可指损坏物品、毁掉心情，也可指过度溺爱溺宠孩子。", "pat": "Extremely high humidity can spoil sensitive electronic components quickly.", "patZh": "极高的湿度会迅速损坏敏感的电子元件。"},
        {"w": "sponsor", "ipa": "ˈspɒnsə", "pos": "n. / vt.", "s": "s1", "zh": "赞助", "exam": "赞助商；主办者；赞助；发起", "c": ["corporate sponsor 企业赞助商", "sponsor an event 赞助一项活动"], "syn": ["patron", "backer", "fund"], "fam": ["sponsorship n. 赞助"], "dif": "sponsor 指为活动出资赞助的厂商，或在议会中发起提案者。", "pat": "The international firm agreed to sponsor the educational scholarship program.", "patZh": "这家国际公司同意赞助该教育奖学金项目。"},
        {"w": "spread", "ipa": "spred", "pos": "v. / n.", "s": "s1", "zh": "传播", "exam": "展开；铺开；传播；蔓延", "c": ["spread rumors 传播谣言", "spread wings 展开翅膀"], "syn": ["disseminate", "extend", "circulation"], "fam": ["widespread adj. 广泛的"], "dif": "spread 侧重从中心向四周扩展分布、传播蔓延。", "pat": "Social media enables news to spread across the globe in seconds.", "patZh": "社交媒体使新闻能在数秒内传播到全球。"},
        {"w": "spur", "ipa": "spɜː", "pos": "n. / vt.", "s": "s1", "zh": "刺激", "exam": "刺激；鼓励；鞭策；马刺", "c": ["spur economic growth 刺激经济增长", "on the spur of the moment 一时冲动"], "syn": ["stimulate", "incentive", "prompt"], "fam": ["spurring n. 刺激激励"], "dif": "spur 原指骑马的马刺，引申为推动某事加速发展的刺激激励物。", "pat": "Tax cuts were introduced to spur private investment in clean energy.", "patZh": "出台减税政策旨在刺激对清洁能源的私人投资。"},
        {"w": "spy", "ipa": "spaɪ", "pos": "n. / v.", "s": "s1", "zh": "侦察", "exam": "间谍；侦察；暗中监视", "c": ["spy on 暗中监视", "industrial spy 工业间谍"], "syn": ["agent", "snoop", "scout"], "fam": ["espionage n. 间谍活动"], "dif": "spy 指暗中刺探情报的人员，或执行暗中侦察监视。", "pat": "Intelligence agencies worked to stop enemy agents spying on secret facilities.", "patZh": "情报机构致力于阻止敌方特工侦察秘密设施。"},
        {"w": "stability", "ipa": "stəˈbɪləti", "pos": "n.", "s": "s1", "zh": "稳定", "exam": "稳定（性）；坚固（性）", "c": ["financial stability 财务稳定", "political stability 政治稳定"], "syn": ["steadiness", "firmness", "constancy"], "fam": ["stable adj. 稳定的"], "dif": "stability 强调结构、情绪或局势处于平稳牢固状态。", "pat": "Maintaining social stability is essential for sustainable economic development.", "patZh": "维持社会稳定对于可持续经济发展至关重要。"},
        {"w": "stable", "ipa": "ˈsteɪbl", "pos": "adj. / n.", "s": "s1", "zh": "稳定的", "exam": "稳定的；沉稳的；马厩", "c": ["stable condition 稳定状况", "stable market 稳定的市场"], "syn": ["steady", "secure", "constant"], "fam": ["stability n. 稳定性"], "dif": "stable 指牢固不易倒塌改变的，或性格情绪沉稳冷静。", "pat": "Doctors reported that the patient was in a stable condition after surgery.", "patZh": "医生报告说手术后患者处于稳定状况。"},
        {"w": "staff", "ipa": "stɑːf", "pos": "n. / vt.", "s": "s1", "zh": "员工", "exam": "全体职工；工作人员；配备人员", "c": ["medical staff 医疗员工", "staffed by 由…配备工作人员"], "syn": ["personnel", "workforce", "employees"], "fam": ["staffing n. 人员配备"], "dif": "staff 作集合名词指机构中的全体工作人员团队。", "pat": "The hospital hired extra staff to handle the seasonal flu outbreak.", "patZh": "医院雇佣了额外员工来应对季节性流感爆发。"},
        {"w": "stage", "ipa": "steɪdʒ", "pos": "n. / vt.", "s": "s1", "zh": "舞台", "exam": "舞台；阶段；上演；举办", "c": ["on stage 在舞台上", "early stage 早期阶段"], "syn": ["phase", "platform", "mount"], "fam": ["staging n. 上演；舞台效果"], "dif": "stage 既指表演的舞台，也指发展过程中的某一特定阶段。", "pat": "The negotiations have reached a critical stage where consensus is required.", "patZh": "谈判已到达需要达成共识的关键阶段。"},
        {"w": "twist", "ipa": "twɪst", "pos": "v. / n.", "s": "s2", "zh": "转折", "exam": "扭转；曲解；转折；拧", "c": ["twist of fate 命运的转折", "twist words 歪曲原话"], "syn": ["turn", "distort", "spin"], "fam": ["twisted adj. 扭曲的"], "dif": "twist 强调用力扭拧或剧情局势发生的意想不到的急转折。", "pat": "An unexpected twist in the investigation revealed the real culprit.", "patZh": "调查中意想不到的转折揭示了真正的罪犯。"},
        {"w": "trivial", "ipa": "ˈtrɪviəl", "pos": "adj.", "s": "s2", "zh": "琐碎的", "exam": "琐碎的；微不足道的", "c": ["trivial matter 琐事", "trivial detail 琐碎细节"], "syn": ["insignificant", "minor", "negligible"], "fam": ["trivia n. 琐事"], "dif": "trivial 强调毫无价值、微不足道、不值得耗费精力关注。", "pat": "Do not waste precious meeting time discussing trivial administrative details.", "patZh": "不要把宝贵的会议时间浪费在讨论琐碎的行政细节上。"},
        {"w": "try", "ipa": "traɪ", "pos": "v. / n.", "s": "s2", "zh": "尝试", "exam": "试图；努力；审讯；尝试", "c": ["try hard 努力尝试", "give it a try 试一试"], "syn": ["attempt", "endeavor", "test"], "fam": ["trial n. 审讯；试验"], "dif": "try 泛指付出努力试图完成某事或试用。", "pat": "Researchers will try a new combination of therapies to boost recovery.", "patZh": "研究人员将尝试一种新的疗法组合来促进康复。"},
        {"w": "tumble", "ipa": "ˈtʌmbl", "pos": "v. / n.", "s": "s2", "zh": "跌倒", "exam": "摔倒；暴跌；跌跤", "c": ["tumble down 跌落", "prices tumble 价格暴跌"], "syn": ["fall", "plummet", "drop"], "fam": ["tumbler n. 翻滚者；杯子"], "dif": "tumble 侧重失去平衡突然跌倒或价格指数猛烈暴跌。", "pat": "Share values began to tumble following the announcement of poor earnings.", "patZh": "在宣布业绩惨淡后股票价值开始暴跌。"},
        {"w": "turbulent", "ipa": "ˈtɜːbjələnt", "pos": "adj.", "s": "s2", "zh": "动荡的", "exam": "动荡的；混乱的；汹涌的", "c": ["turbulent period 动荡时期", "turbulent times 动荡的岁月"], "syn": ["stormy", "chaotic", "unsettled"], "fam": ["turbulence n. 骚乱；气流"], "dif": "turbulent 描写局势骚乱不安或水流气流剧烈翻腾。", "pat": "The company managed to maintain profit margins throughout a turbulent decade.", "patZh": "该公司在整个动荡的十年中成功维持了利润率。"},
        {"w": "turn", "ipa": "tɜːn", "pos": "v. / n.", "s": "s2", "zh": "扭转", "exam": "转动；改变；扭转；轮流", "c": ["turn around 扭转局势", "in turn 依次/反过来"], "syn": ["rotate", "shift", "revert"], "fam": ["turnover n. 营业额"], "dif": "turn 侧重方向的改变、局势的转折或按顺序轮流。", "pat": "Strategic innovation helped the brand turn the crisis into an opportunity.", "patZh": "战略创新帮助该品牌将危机扭转为机遇。"},
        {"w": "turnover", "ipa": "ˈtɜːnəʊvə", "pos": "n.", "s": "s2", "zh": "营业额", "exam": "营业额；人员流动率", "c": ["annual turnover 年度营业额", "staff turnover 人员流动率"], "syn": ["revenue", "sales", "replacement rate"], "fam": ["turn v. 转动"], "dif": "turnover 特指企业一定时期内的总销售营业额或员工换岗率。", "pat": "High staff turnover can negatively affect team productivity and morale.", "patZh": "高员工流动率会给团队生产力和士气带来负面影响。"},
        {"w": "type", "ipa": "taɪp", "pos": "n. / v.", "s": "s2", "zh": "类型", "exam": "类型；样式；打字", "c": ["blood type 血型", "type a letter 打一封信"], "syn": ["kind", "category", "sort"], "fam": ["typical adj. 典型的"], "dif": "type 指具有共同特征的一类事物，或在键盘上打字。", "pat": "What type of technical support does the software provider guarantee?", "patZh": "软件供应商保证提供哪种类型的技术支持？"},
        {"w": "typical", "ipa": "ˈtɪpɪkl", "pos": "adj.", "s": "s2", "zh": "典型的", "exam": "典型的；特有的", "c": ["typical example 典型特征/例子", "be typical of 是…典型的"], "syn": ["characteristic", "representative", "classic"], "fam": ["type n. 类型"], "dif": "typical 强调具备某一类别全部代表性特征。", "pat": "Heavy rainfall is typical of the tropical climate during summer.", "patZh": "强降雨是夏季热带气候的典型特征。"},
        {"w": "voluntary", "ipa": "ˈvɒləntri", "pos": "adj.", "s": "s2", "zh": "自愿的", "exam": "自愿的；志愿的", "c": ["voluntary work 志愿工作", "voluntary organization 志愿者组织"], "syn": ["optional", "willing", "unforced"], "fam": ["volunteer n. 志愿者"], "dif": "voluntary 强调出自个人自由意志而非受胁迫规定。", "pat": "Participation in the wellness program is entirely voluntary for all staff.", "patZh": "所有员工参与该健康项目完全是自愿的。"},
        {"w": "volunteer", "ipa": "ˌvɒlənˈtɪə", "pos": "n. / v.", "s": "s2", "zh": "志愿者", "exam": "志愿者；自愿做", "c": ["community volunteer 社区志愿者", "volunteer to help 自愿帮忙"], "syn": ["helper", "enlist", "offer"], "fam": ["voluntary adj. 自愿的"], "dif": "volunteer 指无偿自愿提供服务的人，或主动承担任务。", "pat": "Many students volunteer at the local shelter during winter holidays.", "patZh": "许多学生在寒假期间在当地救助站当志愿者。"},
        {"w": "vote", "ipa": "vəʊt", "pos": "n. / v.", "s": "s2", "zh": "投票", "exam": "投票；选票；表决", "c": ["vote for 投票赞成", "vote against 投票反对"], "syn": ["ballot", "elect", "poll"], "fam": ["voter n. 投票人"], "dif": "vote 指通过划票、举手等方式表达正式选举或表决意愿。", "pat": "Members met to vote on the proposed amendments to the charter.", "patZh": "成员们开会表决拟议的章程修正案。"},
        {"w": "vulgar", "ipa": "ˈvʌlɡə", "pos": "adj.", "s": "s2", "zh": "粗俗的", "exam": "粗俗的；庸俗的", "c": ["vulgar language 粗俗语言", "vulgar taste 庸俗品味"], "syn": ["crude", "coarse", "tasteless"], "fam": ["vulgarity n. 粗俗"], "dif": "vulgar 强调缺乏教养、言行粗鲁不雅致或趣味低级。", "pat": "The critic condemned the film for its reliance on vulgar humor.", "patZh": "影评人指责该电影依赖粗俗的幽默。"},
        {"w": "vulnerable", "ipa": "ˈvʌlnərəbl", "pos": "adj.", "s": "s2", "zh": "脆弱的", "exam": "脆弱的；易受伤害的", "c": ["vulnerable to 易受…伤害的", "vulnerable group 弱势群体"], "syn": ["susceptible", "fragile", "exposed"], "fam": ["vulnerability n. 脆弱性"], "dif": "vulnerable 强调容易受到物理伤害、攻击或精神创伤打击。", "pat": "Coastal regions are particularly vulnerable to extreme climate events.", "patZh": "沿海地区特别容易受到极端气候事件的伤害。"},

        {"w": "author", "ipa": "ˈɔːθə", "pos": "n. / vt.", "s": "s3", "zh": "作者", "exam": "作者；创始人；撰写", "c": ["best-selling author 畅销书作者", "author a report 撰写报告"], "syn": ["writer", "creator", "originator"], "fam": ["authorship n. 著述身份"], "dif": "author 指书籍文章的著作者，或某项计划方案的始作俑者。", "pat": "The author spent five years researching archives before publishing the biography.", "patZh": "作者在出版该传记前花了五年时间研究档案馆。"},
        {"w": "authority", "ipa": "ɔːˈθɒrəti", "pos": "n.", "s": "s3", "zh": "权威", "exam": "权力；权威；当局；专家", "c": ["local authority 当地政府/当局", "an authority on 某方面的权威"], "syn": ["power", "expert", "jurisdiction"], "fam": ["authorize v. 授权"], "dif": "authority 指合法的行政统治权力，或某一领域的泰斗专家。", "pat": "She is recognized as a leading authority on international maritime law.", "patZh": "她被公认为国际海洋法领域的顶尖权威。"},
        {"w": "auxiliary", "ipa": "ɔːɡˈzɪliəri", "pos": "adj. / n.", "s": "s3", "zh": "辅助的", "exam": "辅助的；备用的；副手", "c": ["auxiliary equipment 辅助设备", "auxiliary verb 助动词"], "syn": ["supplementary", "secondary", "backup"], "fam": ["auxiliary n. 辅助物"], "dif": "auxiliary 强调起协助补充或备用保障作用的设备人员。", "pat": "The hospital switched to auxiliary generators when the main grid failed.", "patZh": "当主电网故障时医院切换到了备用发电机。"},
        {"w": "avail", "ipa": "əˈveɪl", "pos": "v. / n.", "s": "s3", "zh": "起作用", "exam": "有益于；利用；效用", "c": ["to no avail 毫无效果/徒劳", "avail oneself of 利用…"], "syn": ["benefit", "profit", "usefulness"], "fam": ["available adj. 可获得的"], "dif": "avail 常用短语 to no avail 表示徒劳，avail oneself of 表示利用机会。", "pat": "All emergency efforts to restore power were to no avail during the blizzard.", "patZh": "在暴风雪期间恢复供电的所有紧急努力均告徒劳。"},
        {"w": "available", "ipa": "əˈveɪləbl", "pos": "adj.", "s": "s3", "zh": "可获得的", "exam": "可获得的；有空的", "c": ["readily available 容易获得的", "available data 现有的数据"], "syn": ["accessible", "obtainable", "free"], "fam": ["availability n. 可获得性"], "dif": "available 指物品可被取得使用，或人员有时间空闲。", "pat": "Fresh clean water must be made readily available to all disaster victims.", "patZh": "必须向所有灾民随时提供新鲜干净的饮用水。"},
        {"w": "critic", "ipa": "ˈkrɪtɪk", "pos": "n.", "s": "s3", "zh": "批评家", "exam": "批评家；评论家", "c": ["art critic 艺术评论家", "harsh critic 严厉的批评者"], "syn": ["reviewer", "commentator", "detractor"], "fam": ["critical adj. 批判的", "criticism n. 批评"], "dif": "critic 指专职撰写评论分析的评论家，或提出反对批评的人。", "pat": "The theater critic praised the lead actor's powerful dramatic performance.", "patZh": "戏剧评论家赞扬了主角强有力的戏剧表演。"},
        {"w": "critical", "ipa": "ˈkrɪtɪkl", "pos": "adj.", "s": "s3", "zh": "关键的", "exam": "批判的；关键的；危急的", "c": ["critical thinking 批判性思维", "critical role 关键作用"], "syn": ["crucial", "vital", "evaluative"], "fam": ["criticism n. 批评"], "dif": "critical 侧重极其重要决定成败，或带有审查批判态度。", "pat": "Developing critical thinking skills is a fundamental goal of higher education.", "patZh": "培养批判性思维技能是高等教育的根本目标。"},
        {"w": "criticism", "ipa": "ˈkrɪtɪsɪzəm", "pos": "n.", "s": "s3", "zh": "批评", "exam": "批评；评论；责难", "c": ["face criticism 面对批评", "constructive criticism 建设性的批评"], "syn": ["disapproval", "censure", "review"], "fam": ["criticize v. 批评"], "dif": "criticism 指提出的反对批评意见，或对艺术作品的学术评论。", "pat": "The management welcomed constructive criticism to improve customer service.", "patZh": "管理层欢迎建设性的批评意见以改进客户服务。"},
        {"w": "criticize", "ipa": "ˈkrɪtɪsaɪz", "pos": "v.", "s": "s3", "zh": "批评", "exam": "批评；评论", "c": ["criticize sb for 因…批评某人", "severely criticize 严厉批评"], "syn": ["condemn", "blame", "fault"], "fam": ["criticism n. 批评"], "dif": "criticize 指公开指出错误缺点并给以指责或评价。", "pat": "It is easy to criticize policy decisions after knowing the final outcome.", "patZh": "在获知最终结果后去批评政策决定总是容易的。"},
        {"w": "crucial", "ipa": "ˈkruːʃl", "pos": "adj.", "s": "s3", "zh": "关键的", "exam": "至关重要的；决定性的", "c": ["crucial factor 关键因素", "crucial decision 决定性的决定"], "syn": ["pivotal", "decisive", "essential"], "fam": ["crucially adv. 至关重要地"], "dif": "crucial 强调在转折关头起决定成败的生死攸关作用。", "pat": "Timely international aid was crucial to preventing a humanitarian disaster.", "patZh": "及时的国际援助对于防止人道主义灾难至关重要。"},
        {"w": "culminate", "ipa": "ˈkʌlmɪneɪt", "pos": "vi.", "s": "s3", "zh": "以…告终", "exam": "以…告终；达到高潮", "c": ["culminate in 以…达到高潮/告终", "culminate at 达到顶点"], "syn": ["climax", "conclude", "peak"], "fam": ["culmination n. 顶点；高潮"], "dif": "culminate 搭配 in 表示经过长期积累发展后最终达到高潮终点。", "pat": "Years of rigorous research will culminate in a groundbreaking publication.", "patZh": "多年严谨的研究将以一份突破性著作的出版告终。"},
        {"w": "culprit", "ipa": "ˈkʌlprɪt", "pos": "n.", "s": "s3", "zh": "罪犯", "exam": "罪犯；问题的起因/肇事者", "c": ["main culprit 主要肇事者", "catch the culprit 抓获罪犯"], "syn": ["offender", "offending party", "cause"], "fam": ["culprit n. 肇事者"], "dif": "culprit 既指犯罪的罪犯，也指导致不良后果的幕后肇事元凶。", "pat": "Deforestation is the primary culprit behind severe regional soil erosion.", "patZh": "滥砍滥伐是严重区域水土流失背后的主要罪魁祸首。"},

        {"w": "cultivate", "ipa": "ˈkʌltɪveɪt", "pos": "vt.", "s": "s4", "zh": "培养", "exam": "耕作；培养；结交", "c": ["cultivate talent 培养人才", "cultivate relationships 建立关系"], "syn": ["nurture", "foster", "farm"], "fam": ["cultivation n. 培养；耕作"], "dif": "cultivate 指耕耘土地，或通过用心灌溉培育人才品性技巧。", "pat": "Universities aim to cultivate creative talent capable of solving complex problems.", "patZh": "大学旨在培养能够解决复杂问题的创新人才。"},
        {"w": "culture", "ipa": "ˈkʌltʃə", "pos": "n. / vt.", "s": "s4", "zh": "文化", "exam": "文化；文明；教养；培养", "c": ["corporate culture 企业文化", "cultural heritage 文化遗产"], "syn": ["civilization", "customs", "society"], "fam": ["cultural adj. 文化的"], "dif": "culture 指人类社会创造的精神物质文化，或生物细菌培养。", "pat": "Understanding a foreign culture requires open-mindedness and empathy.", "patZh": "理解外域文化需要开放的心态与共情力。"},
        {"w": "dual", "ipa": "ˈdjuːəl", "pos": "adj.", "s": "s4", "zh": "双重的", "exam": "双重的；两部分的", "c": ["dual citizenship 双重国籍", "dual role 双重角色"], "syn": ["double", "twin", "twofold"], "fam": ["duality n. 二元性"], "dif": "dual 强调兼具两种功能、身份或由两部分组成。", "pat": "The manager plays a dual role as both technical leader and mentor.", "patZh": "该经理扮演着技术领导者与导师的双重角色。"},
        {"w": "dubious", "ipa": "ˈdjuːbiəs", "pos": "adj.", "s": "s4", "zh": "可疑的", "exam": "怀疑的；可疑的；不确定的", "c": ["dubious distinction 可疑的头衔", "be dubious about 对…表示怀疑"], "syn": ["doubtful", "suspicious", "questionable"], "fam": ["dubiously adv. 怀疑地"], "dif": "dubious 强调合法性真实性令人生疑、不可靠。", "pat": "Financial regulators questioned the firm's dubious accounting practices.", "patZh": "金融监管机构质疑该公司可疑的会计做法。"},
        {"w": "due", "ipa": "djuː", "pos": "adj. / n.", "s": "s4", "zh": "到期的", "exam": "预期的；到期的；应得的；应付款", "c": ["due to 由于", "in due course 在适当的时候"], "syn": ["expected", "owing", "deserved"], "fam": ["due adj. 应得的"], "dif": "due 表示到期应付的、预期的，短语 due to 表示由于。", "pat": "The final research report is due on the last Friday of the month.", "patZh": "最终研究报告预定于本月最后一个星期五交稿。"},
        {"w": "durable", "ipa": "ˈdjʊərəbl", "pos": "adj.", "s": "s4", "zh": "耐用的", "exam": "耐用的；持久的", "c": ["durable goods 耐用品", "durable peace 持久的和平"], "syn": ["lasting", "sturdy", "enduring"], "fam": ["durability n. 耐用性"], "dif": "durable 强调经久耐用、能经受长期磨损消耗。", "pat": "Constructing durable infrastructure reduces long-term maintenance costs.", "patZh": "建设耐用的基础设施可以降低长期维护成本。"},
        {"w": "duration", "ipa": "djʊˈreɪʃn", "pos": "n.", "s": "s4", "zh": "持续时间", "exam": "持续时间；期间", "c": ["for the duration of 在…期间", "short duration 短暂持续时间"], "syn": ["span", "length", "period"], "fam": ["durable adj. 持久的"], "dif": "duration 强点某一状态或事件在时间轴上持续的长度。", "pat": "Passengers must remain seated for the entire duration of the flight.", "patZh": "在整个飞行持续期间乘客必须保持就座。"},
        {"w": "duty", "ipa": "ˈdjuːti", "pos": "n.", "s": "s4", "zh": "职责", "exam": "职责；义务；关税", "c": ["sense of duty 责任感", "customs duty 关税"], "syn": ["obligation", "responsibility", "tariff"], "fam": ["dutiable adj. 应纳税的"], "dif": "duty 指道德或法律上必须履行的职责，或海关进口税。", "pat": "It is the fiduciary duty of directors to act in the best interest of shareholders.", "patZh": "董事为了股东的最大利益行事是其法定信托职责。"},
        {"w": "dynamic", "ipa": "daɪˈnæmɪk", "pos": "adj. / n.", "s": "s4", "zh": "动态的", "exam": "充满活力的；动态的；动力", "c": ["dynamic market 动态/具活力的市场", "group dynamics 群体动态"], "syn": ["energetic", "vibrant", "active"], "fam": ["dynamism n. 活力"], "dif": "dynamic 强调充满活力能量、不断变化发展。", "pat": "Adapting to a dynamic market environment requires agile leadership.", "patZh": "适应动态的市场环境需要敏捷的领导力。"},
        {"w": "extinct", "ipa": "ɪkˈstɪŋkt", "pos": "adj.", "s": "s4", "zh": "灭绝的", "exam": "灭绝的；绝迹的；熄灭了的", "c": ["become extinct 灭绝", "extinct volcano 死火山"], "syn": ["vanished", "defunct", "died out"], "fam": ["extinction n. 灭绝"], "dif": "extinct 指物种灭绝或火山熄灭、风俗绝迹。", "pat": "Without protection, many endangered species will become extinct within decades.", "patZh": "如果没有保护，许多濒危物种将在几十年内灭绝。"},
        {"w": "extinguish", "ipa": "ɪkˈstɪŋɡwɪʃ", "pos": "vt.", "s": "s4", "zh": "扑灭", "exam": "熄灭；扑灭；使消亡", "c": ["extinguish a fire 扑灭火灾", "extinguish hope 掐灭希望"], "syn": ["quench", "put out", "suppress"], "fam": ["extinguisher n. 灭火器"], "dif": "extinguish 侧重扑灭火火焰，或消灭希望权利。", "pat": "Firefighters worked through the night to extinguish the raging forest fire.", "patZh": "消防员整夜工作以扑灭肆虐的森林火灾。"},
        {"w": "introduce", "ipa": "ˌɪntrəˈdjuːs", "pos": "vt.", "s": "s4", "zh": "引入", "exam": "介绍；引进；提出；采用", "c": ["introduce a policy 引入一项政策", "introduce sb to 介绍某人给…"], "syn": ["present", "launch", "implement"], "fam": ["introduction n. 介绍；引进"], "dif": "introduce 指向他人介绍，或向机构引进新技术政策。", "pat": "The firm plans to introduce automated workflows to increase efficiency.", "patZh": "该公司计划引入自动化工作流来提高效率。"},
        {"w": "introduction", "ipa": "ˌɪntrəˈdʌkʃn", "pos": "n.", "s": "s4", "zh": "引入", "exam": "介绍；引进；引言；导论", "c": ["letter of introduction 介绍信", "introduction to 导论/引进"], "syn": ["preface", "adoption", "presentation"], "fam": ["introduce v. 引进"], "dif": "introduction 指书本的导论前言，或新技术的引进使用。", "pat": "The introduction of solar power reduced reliance on fossil fuels.", "patZh": "太阳能的引入降低了对化石燃料的依赖。"},
        {"w": "invest", "ipa": "ɪnˈvest", "pos": "v.", "s": "s4", "zh": "投资", "exam": "投资；投入（时间/精力）", "c": ["invest in 投资于", "invest time in 在…上投入时间"], "syn": ["fund", "venture", "commit"], "fam": ["investment n. 投资", "investor n. 投资者"], "dif": "invest 搭配 in，指投入资金、金钱或精力和时间。", "pat": "Governments should invest heavily in public education and research.", "patZh": "政府应当在公共教育与科研上加大投资。"},
        {"w": "investment", "ipa": "ɪnˈvestmənt", "pos": "n.", "s": "s4", "zh": "投资", "exam": "投资；投资额；资本", "c": ["foreign investment 外国投资", "return on investment 投资回报率"], "syn": ["capital", "funding", "stake"], "fam": ["invest v. 投资"], "dif": "investment 指投放资金的行为或所投入的资本额。", "pat": "Attracting foreign direct investment is a key goal for regional development.", "patZh": "吸引外商直接投资是区域发展的关键目标。"},

        {"w": "investigate", "ipa": "ɪnˈvestɪɡeɪt", "pos": "v.", "s": "s5", "zh": "调查", "exam": "调查；审查；研究", "c": ["investigate a crime 调查犯罪", "investigate the cause 调查原因"], "syn": ["probe", "examine", "inquire"], "fam": ["investigation n. 调查", "investigator n. 调查员"], "dif": "investigate 强调为了查明真相而有条理地深入调查细节。", "pat": "Authorities formed a special committee to investigate the security breach.", "patZh": "当局成立了一个特别委员会来调查安全漏洞。"},
        {"w": "mutual", "ipa": "ˈmjuːtʃuəl", "pos": "adj.", "s": "s5", "zh": "相互的", "exam": "相互的；共有的", "c": ["mutual respect 相互尊重", "mutual trust 相互信任"], "syn": ["reciprocal", "shared", "joint"], "fam": ["mutually adv. 相互地"], "dif": "mutual 强调两者之间双向对等的相互作用或共同享有。", "pat": "Successful partnership relies on mutual trust and transparent communication.", "patZh": "成功的合作伙伴关系建立在相互信任与透明沟通之上。"},
        {"w": "mysterious", "ipa": "mɪˈstɪəriəs", "pos": "adj.", "s": "s5", "zh": "神秘的", "exam": "神秘的；难以理解的", "c": ["mysterious disappearance 神秘失踪", "mysterious figure 神秘人物"], "syn": ["enigmatic", "secretive", "obscure"], "fam": ["mystery n. 秘密"], "dif": "mysterious 强调充满神秘色彩、难以用常理解释。", "pat": "Detectives looked into the mysterious disappearance of the valuable artwork.", "patZh": "侦探们调查了那件价值连城的艺术品的神秘失踪。"},
        {"w": "mystery", "ipa": "ˈmɪstri", "pos": "n.", "s": "s5", "zh": "谜团", "exam": "神秘；谜；秘密", "c": ["solve a mystery 解开谜团", "remain a mystery 仍是个谜"], "syn": ["puzzle", "riddle", "enigma"], "fam": ["mysterious adj. 神秘的"], "dif": "mystery 指令人困惑不解的事物、秘密或悬疑小说。", "pat": "The exact origin of the ancient text remains a scientific mystery.", "patZh": "这篇古代文献的准确起源仍是一个科学谜团。"},
        {"w": "myth", "ipa": "mɪθ", "pos": "n.", "s": "s5", "zh": "神话", "exam": "神话；荒诞观念", "c": ["ancient myth 古代神话", "dispel the myth 消除误解/神话"], "syn": ["legend", "fable", "fallacy"], "fam": ["mythical adj. 神话的", "mythology n. 神话学"], "dif": "myth 可指古代神话故事，也可指广为流传但并不属实的错误观念。", "pat": "Modern science helped dispel the popular myth about diet pills.", "patZh": "现代科学有助于消除关于减肥药的流行误解。"},
        {"w": "noble", "ipa": "ˈnəʊbl", "pos": "adj. / n.", "s": "s5", "zh": "高尚的", "exam": "高尚的；贵族的；贵族", "c": ["noble cause 高尚的事业", "noble birth 贵族出身"], "syn": ["honorable", "aristocratic", "lofty"], "fam": ["nobility n. 贵族；高尚"], "dif": "noble 侧重指品格高尚崇高，或出身高贵的贵族阶层。", "pat": "Fighting against systemic injustice is a truly noble cause.", "patZh": "同系统性不公作斗争是一项真正高尚的事业。"},
        {"w": "norm", "ipa": "nɔːm", "pos": "n.", "s": "s5", "zh": "规范", "exam": "规范；准则；平均数", "c": ["social norm 社会规范", "above the norm 高于常规标准"], "syn": ["standard", "rule", "benchmark"], "fam": ["normal adj. 正常的", "normalize v. 使正常化"], "dif": "norm 指社会普遍认可遵循的道德行为准则或平均标准。", "pat": "Working remotely has become the accepted norm for tech companies.", "patZh": "远程办公已成为科技公司普遍接受的规范。"},
        {"w": "normal", "ipa": "ˈnɔːml", "pos": "adj. / n.", "s": "s5", "zh": "正常的", "exam": "正常的；普通标准的；正常状态", "c": ["back to normal 恢复正常", "normal procedure 正常程序"], "syn": ["standard", "regular", "ordinary"], "fam": ["normalization n. 正常化"], "dif": "normal 与 abnormal（异常的）相对，指符合常规标准状态。", "pat": "Business operations returned to normal following the end of the strike.", "patZh": "罢工结束后商业运营恢复了正常。"},
        {"w": "normalization", "ipa": "ˌnɔːməlaɪˈzeɪʃn", "pos": "n.", "s": "s5", "zh": "常态化", "exam": "正常化；常态化", "c": ["normalization of relations 关系正常化", "market normalization 市场常态化"], "syn": ["regularization", "standardization", "stabilization"], "fam": ["normalize v. 使正常化"], "dif": "normalization 指从异常无序状态恢复到正常轨道的规制过程。", "pat": "Diplomats worked for the normalization of diplomatic ties between the two nations.", "patZh": "外交官们致力于两国间外交关系的正常化。"},
        {"w": "note", "ipa": "nəʊt", "pos": "n. / vt.", "s": "s5", "zh": "记录", "exam": "笔记；便条；音符；注意；记录", "c": ["take notes 做笔记", "note that 注意到…"], "syn": ["memo", "observation", "observe"], "fam": ["notion n. 观念"], "dif": "note 作动词指留心注意到或做记录；作名词指便条音符。", "pat": "Please note that the deadline for submission is non-negotiable.", "patZh": "请注意到提交截止日期是不容谈判的。"},
        {"w": "notion", "ipa": "ˈnəʊʃn", "pos": "n.", "s": "s5", "zh": "观念", "exam": "概念；观念；想法", "c": ["reject the notion 拒绝这种观念", "preconceived notion 先入为主的观念"], "syn": ["idea", "belief", "concept"], "fam": ["notional adj. 概念上的"], "dif": "notion 侧重指头脑中形成的主观看法、想法或模糊印象。", "pat": "He challenged the outdated notion that failure equals defeat.", "patZh": "他挑战了那种失败即等于彻底被打败的过时观念。"},
        {"w": "public", "ipa": "ˈpʌblɪk", "pos": "adj. / n.", "s": "s5", "zh": "公众", "exam": "公众的；公共的；公众", "c": ["public interest 公众利益", "in public 在公开场合"], "syn": ["civic", "general", "community"], "fam": ["publicity n. 宣传", "publish v. 出版"], "dif": "public 与 private（私人的）相对，指面向大众平民开放的。", "pat": "The government has a duty to protect public health during an outbreak.", "patZh": "政府在疫情爆发期间有职责保护公共健康。"},
        {"w": "publication", "ipa": "ˌpʌblɪˈkeɪʃn", "pos": "n.", "s": "s5", "zh": "出版", "exam": "出版；发表；出版物", "c": ["date of publication 出版日期", "scholarly publication 学术出版物"], "syn": ["printing", "periodical", "release"], "fam": ["publish v. 出版"], "dif": "publication 指书籍期刊等印刷发表的过程或印出的出版物。", "pat": "The professor celebrated the publication of her new textbook.", "patZh": "教授庆祝了她的新教科书的出版。"},
        {"w": "publicity", "ipa": "pʌbˈlɪsəti", "pos": "n.", "s": "s5", "zh": "宣传", "exam": "宣传；关注度；报道", "c": ["gain publicity 获得关注", "publicity campaign 宣传活动"], "syn": ["promotion", "exposure", "media attention"], "fam": ["public adj. 公众的"], "dif": "publicity 强调通过媒体报道引起的公众关注、知名度或促销活动。", "pat": "The event generated massive publicity for the environmental charity.", "patZh": "该活动为环保慈善机构赢得了巨大的公众关注。"},
        {"w": "publish", "ipa": "ˈpʌblɪʃ", "pos": "v.", "s": "s5", "zh": "公布", "exam": "出版；发表；公布", "c": ["publish a report 发表报告", "publish research 公布研究"], "syn": ["print", "issue", "release"], "fam": ["publisher n. 出版商", "publication n. 出版物"], "dif": "publish 指印发图书，或向社会公众正式公布研究数据报告。", "pat": "The laboratory will publish its findings in a peer-reviewed journal.", "patZh": "实验室将在同行评审期刊上发表其研究发现。"},
        {"w": "result", "ipa": "rɪˈzʌlt", "pos": "n. / vi.", "s": "s5", "zh": "结果", "exam": "结果；成果；（in）导致；（from）起因于", "c": ["result in 导致", "result from 起因于"], "syn": ["outcome", "consequence", "effect"], "fam": ["resultant adj. 产生的"], "dif": "result 搭配 in 表示引发某结果，搭配 from 表示由某原因造成。", "pat": "Neglecting routine maintenance can result in sudden mechanical breakdown.", "patZh": "忽视常规维护可能会导致突发的机械故障。"},
        {"w": "resultant", "ipa": "rɪˈzʌltənt", "pos": "adj.", "s": "s5", "zh": "产生的", "exam": "作为结果的；组合的", "c": ["resultant damage 产生的损失", "resultant effect 组合效果"], "syn": ["consequent", "following", "subsequent"], "fam": ["result n. 结果"], "dif": "resultant 侧重因某一具体事件直接引发或导致的后效。", "pat": "The drought and resultant crop failure led to a severe food shortage.", "patZh": "干旱和随之产生的作物减产导致了严重的粮食短缺。"},
        {"w": "resume", "ipa": "rɪˈzjuːm", "pos": "v. / n.", "s": "s5", "zh": "恢复", "exam": "重新开始；恢复；简历（音/ˈrezjuːmeɪ/）", "c": ["resume operations 恢复运营", "resume talk 恢复谈判"], "syn": ["restart", "reopen", "curriculum vitae"], "fam": ["resumption n. 恢复"], "dif": "resume 动词指中断后重新开始；名词读音不同指个人履历简历。", "pat": "Flights will resume normal schedules once the fog clears up.", "patZh": "一旦大雾散去航班将恢复正常时刻表。"},
        {"w": "reveal", "ipa": "rɪˈviːl", "pos": "vt.", "s": "s5", "zh": "揭示", "exam": "揭示；透露；展现", "c": ["reveal secrets 泄露秘密", "reveal the truth 揭示真相"], "syn": ["disclose", "unveil", "expose"], "fam": ["revelation n. 揭示；启示"], "dif": "reveal 侧重揭开原本隐瞒、不为人知的秘密真相或事实。", "pat": "The audit failed to reveal any evidence of illegal transactions.", "patZh": "审计未能揭示出任何非法交易的证据。"},
        {"w": "revelation", "ipa": "ˌrevəˈleɪʃn", "pos": "n.", "s": "s5", "zh": "揭示", "exam": "揭示；透露；出乎意料的事", "c": ["startling revelation 令人震惊的揭露", "revelation of truth 真相的揭示"], "syn": ["disclosure", "unveiling", "discovery"], "fam": ["reveal v. 揭示"], "dif": "revelation 指被揭开公布的惊人事实真相或神圣启示。", "pat": "The journalist's book was packed with shocking revelations about corporate greed.", "patZh": "记者的书里装满了关于公司贪婪的令人震惊的揭露。"},
        {"w": "revenge", "ipa": "rɪˈvendʒ", "pos": "n. / vt.", "s": "s5", "zh": "报复", "exam": "复仇；报复", "c": ["take revenge on 对…进行报复", "exact revenge 实施复仇"], "syn": ["vengeance", "retaliation", "retribution"], "fam": ["revengeful adj. 报复心强的"], "dif": "revenge 强调出于个人怨恨不满而进行的反击报复。", "pat": "Seeking personal revenge will only perpetuate the violent feud.", "patZh": "寻求个人报复只会使暴力宿怨持续下去。"},
        {"w": "revenue", "ipa": "ˈrevənjuː", "pos": "n.", "s": "s5", "zh": "财政收入", "exam": "财政收入；收益；税收", "c": ["tax revenue 税收收入", "annual revenue 年度总收益"], "syn": ["income", "earnings", "proceeds"], "fam": ["revenue n. 税收收入"], "dif": "revenue 特指国家政府的财政税收或公司的营业总收入。", "pat": "The government reported a significant increase in annual tax revenue.", "patZh": "政府报告说年度税收收入有了显著增长。"},
        {"w": "supply", "ipa": "səˈplaɪ", "pos": "n. / vt.", "s": "s5", "zh": "供应", "exam": "供应；补给；必需品；提供", "c": ["supply and demand 供求关系", "water supply 供水"], "syn": ["provide", "furnish", "provision"], "fam": ["supplier n. 供应商"], "dif": "supply 指向需要者提供所需物资装备，或经济供求关系中的供给。", "pat": "The charity worked to supply medical aid to refugees in the camp.", "patZh": "慈善机构致力于向营地里的难民提供医疗援助。"},
        {"w": "support", "ipa": "səˈpɔːt", "pos": "vt. / n.", "s": "s5", "zh": "支持", "exam": "支撑；支持；资助；供养；支持者", "c": ["support a candidate 支持某候选人", "financial support 财务资助"], "syn": ["sustain", "back", "advocate"], "fam": ["supportive adj. 支持的", "supporter n. 支持者"], "dif": "support 强调用体能、金钱或情感道德上撑住、给以有力后盾。", "pat": "Strong public support enabled the government to pass the healthcare bill.", "patZh": "强大的公众支持使政府能够通过该医疗法案。"},
        {"w": "suppose", "ipa": "səˈpəʊz", "pos": "vt.", "s": "s5", "zh": "猜想", "exam": "猜想；假定；认为；（be supposed to）应当", "c": ["be supposed to 应当/被期望", "suppose that 假定…"], "syn": ["assume", "presume", "conjecture"], "fam": ["supposition n. 推测"], "dif": "suppose 表示根据已有迹象进行推测猜想，短语 be supposed to 表示应当履行的职责。", "pat": "Employees are supposed to complete safety training before using the machinery.", "patZh": "员工被要求在操作该机械前完成安全培训。"},
        {"w": "suppress", "ipa": "səˈpres", "pos": "vt.", "s": "s5", "zh": "镇压", "exam": "镇压；压制；抑制；隐瞒", "c": ["suppress a rebellion 镇压叛乱", "suppress emotions 压抑情感"], "syn": ["quell", "stifle", "repress"], "fam": ["suppression n. 镇压"], "dif": "suppress 强调凭借武力、权威或意志强行镇压、封锁或抑制。", "pat": "The dictator used military force to suppress civilian protests across the nation.", "patZh": "独裁者使用军事力量强行镇压全国范围内的平民抗议。"},
        {"w": "supplement", "ipa": "ˈsʌplɪmənt", "pos": "n. / vt.", "s": "s5", "zh": "补充", "exam": "补充；增刊；补给品；增补", "c": ["dietary supplement 膳食补充剂", "supplement income 增加/补充收入"], "syn": ["addition", "add", "complement"], "fam": ["supplementary adj. 补充的"], "dif": "supplement 指为了弥补不足而额外增加的补充物或增刊。", "pat": "Many elderly people take calcium supplements to maintain strong bone health.", "patZh": "许多老年人服用钙补充剂以维持强健骨骼健康。"},
        {"w": "supreme", "ipa": "suːˈpriːm", "pos": "adj.", "s": "s5", "zh": "至高无上的", "exam": "至高无上的；最高的", "c": ["supreme court 最高法院", "supreme commander 最高指挥官"], "syn": ["paramount", "ultimate", "highest"], "fam": ["supremacy n. 至高无上"], "dif": "supreme 强调在权力、地位、品质或重要性上达到最高顶点。", "pat": "The Supreme Court will review the constitutionality of the lower court ruling.", "patZh": "最高法院将审查下级法院判决的合宪性。"},
        {"w": "system", "ipa": "ˈsɪstəm", "pos": "n.", "s": "s5", "zh": "体系", "exam": "系统；体系；制度；方法", "c": ["legal system 法律体系", "solar system 太阳系"], "syn": ["network", "structure", "scheme"], "fam": ["systematic adj. 系统化的"], "dif": "system 指按特定规则有机组合在一起的整体系统制度。", "pat": "Reforming the public education system is vital for future economic growth.", "patZh": "改革公共教育体系对于未来的经济增长至关重要。"},
        {"w": "systematic", "ipa": "ˌsɪstəˈmætɪk", "pos": "adj.", "s": "s5", "zh": "系统的", "exam": "系统化的；有条理的", "c": ["systematic approach 系统的方法", "systematic analysis 系统化的分析"], "syn": ["methodical", "structured", "organized"], "fam": ["system n. 系统", "systematically adv. 有条理地"], "dif": "systematic 强调做事有计划、有条理、按步骤系统推进。", "pat": "A systematic review of internal controls prevented further financial loss.", "patZh": "对内部控制系统的审查防止了进一步的财务损失。"}
    ]
}

# Save JSON
u21_out = os.path.join(story_dir, "Unit21.json")
with open(u21_out, "w", encoding="utf-8") as f:
    json.dump(unit21_data, f, ensure_ascii=False, indent=2)

u22_out = os.path.join(story_dir, "Unit22.json")
with open(u22_out, "w", encoding="utf-8") as f:
    json.dump(unit22_data, f, ensure_ascii=False, indent=2)

print("Saved Unit21.json and Unit22.json.")

for u, j_path in [(21, u21_out), (22, u22_out)]:
    md_path = os.path.join(story_dir, f"Unit{u:02d}.md")
    cmd_val = ["python", validator, "--csv", csv_path, "--unit", str(u), "--json", j_path]
    res_val = subprocess.run(cmd_val, capture_output=True, text=True, encoding="utf-8")
    status = "PASS (ERROR 0)" if res_val.returncode == 0 else "FAIL"
    print(f"Unit {u:02d}: Validation={status}")
    if res_val.returncode != 0:
        print(res_val.stdout)

    cmd_md = ["python", builder, "--json", j_path, "--out", md_path]
    subprocess.run(cmd_md, capture_output=True, text=True, encoding="utf-8")
    print(f"Built {md_path}")
