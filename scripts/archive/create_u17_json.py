import json
import os

unit_data = {
    "unit": 17,
    "stories": [
        {
            "id": "s1",
            "en": "The Precision Revolution",
            "zh": "精密的革命",
            "theme": "科技 / 环境",
            "ps": [
                {
                    "en": "In the industrial heartland, engineers had a gloomy [[outlook]] regarding factory [[output]], as obsolete machinery kept worker communities in [[poverty]]. To break this cycle, the state granted clean energy [[power]] to a [[practical]] workshop where innovative [[practices|practice]] were tested. Mechanical [[practitioners|practitioner]] were encouraged to [[practise]] advanced automated techniques rather than just [[preach]] theoretical ideals.",
                    "zh": "在工业心脏地带，工程师们对工厂产出的前景持悲观态度，因为陈旧的机械使工人社区陷入贫困。为了打破这一循环，国家向一家实用车间提供了清洁能源电力，在那里测试创新实践。机械从业人员被鼓励去实际操练先进的自动化技术，而不仅仅是宣扬理论理想。"
                },
                {
                    "en": "Safety inspections must [[precede]] any full-scale assembly. As a [[precaution]], technicians established a legal [[precedent]] by reviewing failure logs from the [[preceding]] decade. They realized that [[precious]] raw components required extremely [[precise]] measurements to maintain quality.",
                    "zh": "安全检查必须在任何大规模组装之前进行。作为一项预防措施，技术人员通过复盘前十年的故障日志创下了法律先例。他们意识到，宝贵的原材料构件需要极精确的测量来保证质量。"
                },
                {
                    "en": "By deploying sensors of unprecedented [[precision]], the plant eliminated micro-defects entirely. Within a year, total productivity doubled, transforming the region into a model of modern manufacturing.",
                    "zh": "通过部署前所未有精密度的传感器，工厂彻底清除了微小瑕疵。一年之内，总生产力翻倍，将该地区重塑为现代制造业的典范。"
                }
            ]
        },
        {
            "id": "s2",
            "en": "What Remains of the Heritage",
            "zh": "遗产所存",
            "theme": "学术 / 认知",
            "ps": [
                {
                    "en": "Architects faced immense [[stress]] when trying to [[stretch]] a narrow highway across a [[remote]] mountain valley. Local villagers urged authorities to [[remove]] heavy excavators, fearing that the [[removal]] of ancient soil would destroy sacred ground. Archeologists insisted that historic structures must [[remain]] intact during construction.",
                    "zh": "在尝试将一条狭窄公路延伸穿越偏僻的山谷时，建筑师们面临着巨大的压力。当地村民敦促当局移开重型挖掘机，担心古老土层的移除会毁坏圣地。考古学家坚持要求历史结构在施工期间必须完好保留。"
                },
                {
                    "en": "Surveyors carefully preserved the [[remainder]] of a centuries-old stone temple, while ancient [[remains]] were cataloged for museum display. The excavation leader proposed a sustainable [[remedy]] to protect the ruins from weather damage.",
                    "zh": "勘测员仔细保存了一座数百年古庙的剩余部分，同时将古代遗迹编目以供博物馆展出。发掘组辩提出了一个可持续的补救方法，以保护废墟免受风雨侵蚀。"
                },
                {
                    "en": "Scholars still [[remember]] how Elders used to [[remind]] youth that historical memory could [[render]] a community resilient against modern disruptions. Ultimately, the highway was rerouted around the site.",
                    "zh": "学者们依然记得长老们过去如何提醒年轻人：历史记忆能够使一个社区在面对现代冲击时保持韧性。最终，公路被绕道开设在遗迹周围。"
                }
            ]
        },
        {
            "id": "s3",
            "en": "The Corporate Contest",
            "zh": "企业风云",
            "theme": "法律 / 社会",
            "ps": [
                {
                    "en": "In [[contemporary]] corporate law, executives who treat environmental regulations with [[contempt]] often find themselves in severe legal trouble. A board member who was not [[content]] with misleading reports decided to [[contend]] for full financial transparency. She entered a fierce leadership [[contest]], placing her reform agenda into a broader social [[context]].",
                    "zh": "在现代公司法中，蔑视环保法规的高管往往发现自己陷入严重的法律麻烦。一位不满于误导性报告的董事会成员决定争取完全的财务透明。她进入了一场激烈的领导权争夺，将她的改革议程置于更广泛的社会语境中。"
                },
                {
                    "en": "When a major supplier attempted to breach a binding [[contract]], auditors proved that its claims [[contradicted|contradict]] basic accounting facts. On the [[contrary]] to public belief, the company's internal reports showed a sharp [[contrast]] between advertised ethics and actual practices. In response, leadership pursued [[diverse]] investment strategies as a temporary [[diversion]] to [[divert]] public attention away from the lawsuit.",
                    "zh": "当一家主要供应商试图违反具有约束力的合同时，审计人员证明其主张与基本会计事实相矛盾。与公众信念相反，该公司内部报告显示出所宣传的道德与实际做法之间的鲜明对比。作为回应，领导层采取了多样的投资策略作为临时分心手段，以转移公众对诉讼的注意力。"
                },
                {
                    "en": "To [[divide]] financial risk, the board voted to distribute an annual [[dividend]] to shareholders while creating a new compliance [[division]]. Legal teams prepared every required [[document]], filmed a comprehensive [[documentary]] of internal reforms, and tasked the chief [[executive]] to [[execute]] the restructuring plan immediately.",
                    "zh": "为了分散财务风险，董事会投票向股东分配年度红利，同时建立了一个新的合规部门。法律团队准备了每一份所需的文件，制作了一部关于内部改革的全景纪录片，并指派首席高管立即执行重组计划。"
                }
            ]
        },
        {
            "id": "s4",
            "en": "The Prudent Guardian",
            "zh": "审慎的守卫者",
            "theme": "人物 / 社会",
            "ps": [
                {
                    "en": "A public leader must [[exemplify]] integrity whenever they [[exert]] authority over civic institutions. Pushing staff to the point of total [[exhaustion|exhaust]] can endanger the very [[existence]] of a public healthcare system. Analysts noticed that [[exotic]] management models imported from abroad often clashed with local [[moral]] values and professional [[morality]]. Public welfare institutions [[exist]] to serve vulnerable populations across the country.",
                    "zh": "一位公共管理者在对公民机构行使职权时必须树立诚信的典范。将员工推到彻底精疲力竭的地步可能会危及公共医疗体系的生存。分析人士注意到，从国外引进的具有异国情调的管理模式往往与当地的道德价值观和职业道德规范相冲突。公共福利机构的存在是为了服务全国范围内的弱势群体。"
                },
                {
                    "en": "[[Moreover|moreover]], hospital staff were [[mostly]] concerned that policy updates occurred without [[prior]] consultation. They demanded that patient care be given top [[priority]], ensuring that patient [[privacy]] and [[private]] medical records were safeguarded against unauthorized access.",
                    "zh": "此外，医院员工主要担心政策更新是在未经事先咨询的情况下进行的。他们要求将患者护理置于最高优先事项，确保患者的隐私和私人医疗记录得到保护，免受未经授权的查阅。"
                },
                {
                    "en": "Holding a public [[privilege]] requires leaders to remain [[prudent]] in every expenditure and policy decision.",
                    "zh": "拥有公共特权要求领导者在每一项支出和政策决定中保持审慎。"
                }
            ]
        },
        {
            "id": "s5",
            "en": "Substantial Reforms",
            "zh": "实质性改革",
            "theme": "教育 / 职场",
            "ps": [
                {
                    "en": "When reform committees [[submit]] proposal drafts, [[subordinate]] officials are expected to [[subscribe]] to the core principles outlined for [[subsequent]] implementation. The genuine [[substance]] of the reform lies in delivering [[substantial]] improvements to public education rather than offering a flimsy [[substitute]].",
                    "zh": "当改革委员会提交提案草案时，下级官员应当赞同为后续实施概述的核心原则。改革的真正实质在于为公共教育带来实质性的改善，而不是提供一个劣质的替代品。"
                },
                {
                    "en": "Navigating [[subtle]] differences in regional needs, policymakers must [[associate]] with veteran teachers and form an educational [[association]] to [[amend]] outdated curricula. Working [[amongst]] experienced scholars, they evaluated the vast [[amount]] of student data collected across schools.",
                    "zh": "在应对区域需求中的微妙差异时，政策制定者必须与资深教师建立联系，并组成教育协会来修改过时的课程。在资深学者之中工作，他们评估了跨学校收集的大量学生数据。"
                },
                {
                    "en": "With [[ample]] funding provided by local foundations, the committee organized interactive programs designed to [[amuse]] young learners while cultivating critical thinking skills.",
                    "zh": "凭借当地基金会提供的充足资金，委员会组织了旨在逗乐幼龄学习者同时培养临界思维能力的互动项目。"
                }
            ]
        }
    ],
    "words": [
        # s1 words
        {
            "w": "outlook", "ipa": "ˈaʊtlʊk", "pos": "n.", "s": "s1", "zh": "前景", "exam": "观点；前景",
            "c": ["a gloomy outlook 悲观的前景", "an optimistic outlook 乐观的展望"],
            "syn": ["perspective", "prospect", "viewpoint"],
            "fam": ["look v. 看；看顾"],
            "dif": "outlook 指对未来发展的前景或看法；insight 指深入的洞察力。",
            "pat": "Economists hold an optimistic outlook regarding the recovery of green industries.",
            "patZh": "经济学家对绿色产业的复苏持乐观态度。"
        },
        {
            "w": "output", "ipa": "ˈaʊtpʊt", "pos": "n.", "s": "s1", "zh": "产出", "exam": "产量",
            "c": ["industrial output 工业产量", "economic output 经济产出"],
            "syn": ["yield", "production", "volume"],
            "fam": ["input n. 输入"],
            "dif": "output 侧重指制造或生产出来的实际总量；yield 侧重指收益或农作物收成。",
            "pat": "The new factory automation significantly increased total monthly output.",
            "patZh": "工厂的新自动化设备显著提升了每月总产量。"
        },
        {
            "w": "poverty", "ipa": "ˈpɒvəti", "pos": "n.", "s": "s1", "zh": "贫困", "exam": "贫穷；贫困",
            "c": ["alleviate poverty 缓解贫困", "poverty line 贫困线"],
            "syn": ["indigence", "hardship", "penury"],
            "fam": ["poor adj. 贫穷的"],
            "dif": "poverty 强调缺少生活必需品的缺乏状态；hardship 强调生活中的艰难困苦。",
            "pat": "Targeted education programs are essential to break the cycle of generational poverty.",
            "patZh": "精准教育项目对于打破代际贫困循环至关重要。"
        },
        {
            "w": "power", "ipa": "ˈpaʊə", "pos": "n.", "s": "s1", "zh": "电力", "exam": "动力；权势；权力；提供动力",
            "c": ["clean energy power 清洁能源电力", "purchasing power 购买力"],
            "syn": ["energy", "authority", "strength"],
            "fam": ["powerful adj. 强有力的", "powerless adj. 无能为力的"],
            "dif": "power 指物理上的能量/动力或行政统治上的权力；authority 侧重合法掌管权。",
            "pat": "Solar panels generate clean power for remote communities during winter.",
            "patZh": "太阳能电池板在冬季为偏远社区提供清洁电力。"
        },
        {
            "w": "practical", "ipa": "ˈpræktɪkl", "pos": "adj.", "s": "s1", "zh": "实用的", "exam": "实际的",
            "c": ["practical experience 实际经验", "practical advice 实用建议"],
            "syn": ["pragmatic", "feasible", "functional"],
            "fam": ["practice n. 实践", "practically adv. 几乎；实际上"],
            "dif": "practical 强调切合实际或注重动手能力；pragmatic 强调讲求实效、不尚空谈。",
            "pat": "The workshop provided students with practical skills needed in modern manufacturing.",
            "patZh": "该车间为学生提供了现代制造业所需的实用技能。"
        },
        {
            "w": "practice", "ipa": "ˈpræktɪs", "pos": "n.", "s": "s1", "zh": "实践", "exam": "练习；实践；业务",
            "c": ["in practice 在实践中", "best practice 最佳做法"],
            "syn": ["implementation", "exercise", "custom"],
            "fam": ["practise v. 练习", "practitioner n. 从业者"],
            "dif": "practice 在美式英语中兼作名词与动词，在英式英语中多专指名词（动词写作 practise）。",
            "pat": "Theory must be combined with practice to achieve meaningful technical progress.",
            "patZh": "理论必须与实践相结合，才能取得有意义的技术进步。"
        },
        {
            "w": "practise", "ipa": "ˈpræktɪs", "pos": "v.", "s": "s1", "zh": "实际操练", "exam": "实施；练习；执业",
            "c": ["practise law 从事法律执业", "practise techniques 操练技术"],
            "syn": ["rehearse", "exercise", "perform"],
            "fam": ["practice n. 练习"],
            "dif": "practise 是英式拼写动词形式（美式常用 practice），指反复练习或从事专业职业。",
            "pat": "Young engineers were encouraged to practise new assembly methods under supervision.",
            "patZh": "鼓励年轻工程师在指导下操练新的组装方法。"
        },
        {
            "w": "practitioner", "ipa": "prækˈtɪʃənə", "pos": "n.", "s": "s1", "zh": "从业人员", "exam": "从业者",
            "c": ["medical practitioner 医疗从业人员", "experienced practitioner 资深从业者"],
            "syn": ["professional", "specialist", "expert"],
            "fam": ["practice n. 业务；实践"],
            "dif": "practitioner 特指从事某种专门职业（如医生、律师、工程师）的人员；expert 指专家。",
            "pat": "Senior practitioners shared their technical expertise during the regional conference.",
            "patZh": "资深从业者在区域会议期间分享了他们的专业技术。"
        },
        {
            "w": "preach", "ipa": "priːtʃ", "pos": "v.", "s": "s1", "zh": "宣扬", "exam": "宣扬",
            "c": ["preach tolerance 宣扬包容", "preach what one practices 言行一致"],
            "syn": ["advocate", "proclaim", "sermonize"],
            "fam": ["preacher n. 传教士；倡导者"],
            "dif": "preach 指说教、宣扬信仰或道德原则；advocate 侧重公开提倡政策或观点。",
            "pat": "Leaders should practice the ethical principles that they preach to their followers.",
            "patZh": "领导者应当身体力行他们向追随者宣扬的道德原则。"
        },
        {
            "w": "precede", "ipa": "prɪˈsiːd", "pos": "vt.", "s": "s1", "zh": "在…之前", "exam": "在…之前",
            "c": ["precede in time 先于时间发生", "precede in order 在顺序上居先"],
            "syn": ["antedate", "pioneer", "lead"],
            "fam": ["preceding adj. 先前的", "precedent n. 先例"],
            "dif": "precede 侧重时间、空间或顺序上的领先；proceed 指继续前进。",
            "pat": "A thorough risk analysis must precede any major capital investment.",
            "patZh": "任何重大资本投资之前都必须进行彻底的风险分析。"
        },
        {
            "w": "precaution", "ipa": "prɪˈkɔːʃn", "pos": "n.", "s": "s1", "zh": "预防措施", "exam": "预防；预防措施",
            "c": ["take precautions 采取预防措施", "safety precaution 安全防范措施"],
            "syn": ["safeguard", "preventative", "measure"],
            "fam": ["cautious adj. 谨慎的"],
            "dif": "precaution 强调为防范潜在危险而事先采取的具体行动或措施。",
            "pat": "Wearing protective gear is an essential precaution when operating high-voltage gear.",
            "patZh": "在操作高压设备时佩戴防护装备是一项必要的安全措施。"
        },
        {
            "w": "precedent", "ipa": "ˈpresɪdənt", "pos": "n. / adj.", "s": "s1", "zh": "先例", "exam": "先例；在先的",
            "c": ["set a precedent 树立先例", "without precedent 无先例的"],
            "syn": ["benchmark", "model", "criterion"],
            "fam": ["unprecedented adj. 史无前例的"],
            "dif": "precedent 特指可作为以后类似情况判例或依据的前例；president 是总统/总裁。",
            "pat": "The court ruling set a significant legal precedent for environmental protection cases.",
            "patZh": "该法院判决为环境保护案件树立了重要的法律先例。"
        },
        {
            "w": "preceding", "ipa": "prɪˈsiːdɪŋ", "pos": "adj.", "s": "s1", "zh": "在前的", "exam": "在先的；在前的",
            "c": ["the preceding chapter 上一章", "preceding years 前几年"],
            "syn": ["previous", "prior", "former"],
            "fam": ["precede v. 先于"],
            "dif": "preceding 指紧接在前的；previous 泛指时间上更早发生的。",
            "pat": "The report compared data from the current quarter with that of the preceding year.",
            "patZh": "该报告将本季度的数据与前一年的数据进行了对比。"
        },
        {
            "w": "precious", "ipa": "ˈpreʃəs", "pos": "adj.", "s": "s1", "zh": "宝贵的", "exam": "宝贵的",
            "c": ["precious metals 贵金属", "precious time 宝贵的时间"],
            "syn": ["valuable", "priceless", "cherished"],
            "fam": ["preciousness n. 珍贵"],
            "dif": "precious 强调因稀少、亲情或价值高而极其珍贵；valuable 侧重经济价值或实用价值。",
            "pat": "Engineers worked around the clock to avoid wasting precious technical resources.",
            "patZh": "工程师们昼夜不停地工作，以避免浪费宝贵的技术资源。"
        },
        {
            "w": "precise", "ipa": "prɪˈsaɪs", "pos": "adj.", "s": "s1", "zh": "精确的", "exam": "精确的",
            "c": ["precise measurement 精确测量", "precise location 准确位置"],
            "syn": ["exact", "accurate", "meticulous"],
            "fam": ["precision n. 精确度", "precisely adv. 精确地"],
            "dif": "precise 侧重细节上的极其准确无误；exact 强调完全相符、一字不差。",
            "pat": "The robotic arm requires precise instructions to position tiny electronic chips.",
            "patZh": "机械臂需要精确的指令来放置微小的电子芯片。"
        },
        {
            "w": "precision", "ipa": "prɪˈsɪʒn", "pos": "n.", "s": "s1", "zh": "精密度", "exam": "精确，精密",
            "c": ["high precision 高精度", "precision instrument 精密仪器"],
            "syn": ["accuracy", "exactness", "refinement"],
            "fam": ["precise adj. 精确的"],
            "dif": "precision 强调工艺、测量或思维上的高度精确与重复一致性。",
            "pat": "Modern optical instruments demand an exceptionally high level of manufacturing precision.",
            "patZh": "现代光学仪器要求极高的制造精度。"
        },

        # s2 words
        {
            "w": "stress", "ipa": "stres", "pos": "n. / vt.", "s": "s2", "zh": "压力", "exam": "压力；强调",
            "c": ["under stress 在压力下", "stress the importance of 强调…的重要性"],
            "syn": ["pressure", "strain", "emphasize"],
            "fam": ["stressful adj. 充满压力的"],
            "dif": "stress 作名词指身心压力或物力应力，作动词指强调某事。",
            "pat": "The architect stressed the need to preserve cultural heritage despite commercial pressure.",
            "patZh": "建筑师强调，尽管面临商业压力，仍需保护文化遗产。"
        },
        {
            "w": "stretch", "ipa": "stretʃ", "pos": "v. / n.", "s": "s2", "zh": "延伸", "exam": "伸展；拉长；延伸；一段时间",
            "c": ["stretch across 延伸穿越", "a long stretch of highway 一长段公路"],
            "syn": ["extend", "expand", "span"],
            "fam": ["stretchy adj. 有弹性的"],
            "dif": "stretch 强调拉长、伸展空间或时间长度；extend 指扩大范围或延续时间。",
            "pat": "The proposed bridge will stretch over the mountain gorge to connect the remote villages.",
            "patZh": "拟建的大桥将延伸跨越山谷，连接偏远村庄。"
        },
        {
            "w": "remote", "ipa": "rɪˈməʊt", "pos": "adj.", "s": "s2", "zh": "偏僻的", "exam": "遥远的；偏僻的",
            "c": ["remote area 偏远地区", "remote control 遥控器"],
            "syn": ["distant", "isolated", "faraway"],
            "fam": ["remotely adv. 遥远地"],
            "dif": "remote 指地理位置远离中心或微小的可能性；distant 泛指距离远。",
            "pat": "Constructing infrastructure in remote mountainous regions poses significant engineering challenges.",
            "patZh": "在偏远山区建设基础设施带来了重大的工程挑战。"
        },
        {
            "w": "remove", "ipa": "rɪˈmuːv", "pos": "v.", "s": "s2", "zh": "移开", "exam": "移开；除去",
            "c": ["remove obstacle 清除障碍", "remove from office 免职"],
            "syn": ["eliminate", "detach", "clear"],
            "fam": ["removal n. 移动；消除"],
            "dif": "remove 指将某物从原位置挪开或消除；delete 特指删除文字或文件。",
            "pat": "Workers used heavy machinery to remove fallen rocks from the blocked highway.",
            "patZh": "工人使用重型机械清除了被封锁公路上落下的巨石。"
        },
        {
            "w": "removal", "ipa": "rɪˈmuːvl", "pos": "n.", "s": "s2", "zh": "移除", "exam": "移动；去除",
            "c": ["removal of trash 垃圾的清除", "snow removal 积雪清除"],
            "syn": ["elimination", "dislodgement", "clearance"],
            "fam": ["remove v. 移开"],
            "dif": "removal 指搬迁、移动或根除的过程。",
            "pat": "The prompt removal of hazardous chemical waste prevented environmental contamination.",
            "patZh": "及时清除有害化学废料防止了环境污染。"
        },
        {
            "w": "remain", "ipa": "rɪˈmeɪn", "pos": "v.", "s": "s2", "zh": "保留", "exam": "剩下；留存；依然是",
            "c": ["remain intact 保持完好", "remain silent 保持沉默"],
            "syn": ["stay", "persist", "endure"],
            "fam": ["remainder n. 剩余部分", "remains n. 遗迹"],
            "dif": "remain 作为系动词指保持某种状态，作为不及物动词指留下。",
            "pat": "Ancient temple structures must remain untouched during the road expansion project.",
            "patZh": "古庙建筑在道路拓宽工程期间必须保持完好无损。"
        },
        {
            "w": "remainder", "ipa": "rɪˈmeɪndə", "pos": "n.", "s": "s2", "zh": "剩余部分", "exam": "剩余物；其余人员",
            "c": ["the remainder of the year 这一年的其余时间", "for the remainder of 在其余时间里"],
            "syn": ["rest", "surplus", "residue"],
            "fam": ["remain v. 留下"],
            "dif": "remainder 强调整体中扣除一部分后剩下的具体数量或部分。",
            "pat": "The team spent the remainder of the afternoon cataloging newly discovered artifacts.",
            "patZh": "团队把下午剩余的时间用来将新发现的文物编目。"
        },
        {
            "w": "remains", "ipa": "rɪˈmeɪnz", "pos": "n.", "s": "s2", "zh": "遗迹", "exam": "遗迹；遗体",
            "c": ["historic remains 历史遗迹", "human remains 人类遗骸"],
            "syn": ["ruins", "relics", "vestiges"],
            "fam": ["remain v. 剩余"],
            "dif": "remains 复数形式专门指古代建筑废墟遗迹或人畜遗骨。",
            "pat": "Archaeologists uncovered the ancient remains of a Roman settlement near the valley.",
            "patZh": "考古学家在山谷附近发掘出了古罗马定居点的历史遗迹。"
        },
        {
            "w": "remedy", "ipa": "ˈremədi", "pos": "n. / vt.", "s": "s2", "zh": "补救方法", "exam": "补救方法；药品；治疗",
            "c": ["effective remedy 有效的补救方法", "remedy the situation 补救局势"],
            "syn": ["solution", "cure", "redress"],
            "fam": ["remedial adj. 补救的；矫正的"],
            "dif": "remedy 既可指治疗疾病的药物，更常指解决棘手问题的纠正补救手段。",
            "pat": "Installing modern filtration systems offered a swift remedy for water contamination.",
            "patZh": "安装现代过滤系统为水污染提供了快速的补救方法。"
        },
        {
            "w": "remember", "ipa": "rɪˈmembə", "pos": "v.", "s": "s2", "zh": "记得", "exam": "记得；记住",
            "c": ["remember to do 记得要去做", "remember doing 记得做过"],
            "syn": ["recall", "recollect", "retain"],
            "fam": ["remembrance n. 记忆；怀念"],
            "dif": "remember 指脑海中保持记忆或想起；remind 指使他人想起。",
            "pat": "Citizens must remember their historical roots to build a cohesive collective identity.",
            "patZh": "公民必须记住自己的历史根基，以构建有凝聚力的集体认同感。"
        },
        {
            "w": "remind", "ipa": "rɪˈmaɪnd", "pos": "vt.", "s": "s2", "zh": "提醒", "exam": "提醒；使想起",
            "c": ["remind sb of sth 提醒某人某事", "remind sb to do 提醒某人去做"],
            "syn": ["prompt", "admonish", "warn"],
            "fam": ["reminder n. 提醒物；提示"],
            "dif": "remind 用于主动引发某人的回忆或注意，句型常接 of 或不定式。",
            "pat": "Museum exhibits serve to remind visitors of the cultural heritage preserving their past.",
            "patZh": "博物馆展品旨在提醒参观者注意保护他们过去的文化遗产。"
        },
        {
            "w": "render", "ipa": "ˈrendə", "pos": "v.", "s": "s2", "zh": "使成为", "exam": "致使；提供",
            "c": ["render harmless 使无害", "render service 提供服务"],
            "syn": ["make", "cause", "provide"],
            "fam": ["rendering n. 翻译；效果图"],
            "dif": "render 接形容词表示“使处于某种状态”，比 make 更具正式书面色彩。",
            "pat": "Continuous maintenance helps ensure that extreme weather will not render roads impassable.",
            "patZh": "持续的维护有助于确保极端天气不会使道路无法通行。"
        },

        # s3 words
        {
            "w": "contemporary", "ipa": "kənˈtemprəri", "pos": "adj. / n.", "s": "s3", "zh": "现代的", "exam": "当代；现代的",
            "c": ["contemporary society 当代社会", "contemporary art 现代艺术"],
            "syn": ["modern", "current", "present-day"],
            "fam": ["contemporaneous adj. 同时代的"],
            "dif": "contemporary 指发生在当今时代或与某人处于同一时代的。",
            "pat": "Contemporary legal systems must evolve rapidly to address novel digital disputes.",
            "patZh": "当代法律体系必须快速演进，以解决新型数字纠纷。"
        },
        {
            "w": "contempt", "ipa": "kənˈtempt", "pos": "n.", "s": "s3", "zh": "蔑视", "exam": "蔑视",
            "c": ["contempt of court 藐视法庭", "hold in contempt 对…表示轻蔑"],
            "syn": ["scorn", "disdain", "disrespect"],
            "fam": ["contemptuous adj. 蔑视的"],
            "dif": "contempt 指对人或规则极度轻视、看不起的态度；scorn 强调嘲弄式的轻蔑。",
            "pat": "Treating regulatory standards with contempt can result in severe legal and financial penalties.",
            "patZh": "蔑视监管标准会导致严重的法律和财务处罚。"
        },
        {
            "w": "content", "ipa": "ˈkɒntent", "pos": "n. / adj.", "s": "s3", "zh": "不满于", "exam": "内容；满足的",
            "c": ["be content with 满意于", "table of contents 目录"],
            "syn": ["satisfied", "substance", "fulfilled"],
            "fam": ["contentment n. 满足"],
            "dif": "content 作名词指内容/容量，重音在第一音节；作形容词指满足的，重音在第二音节。",
            "pat": "Shareholders were not content with ambiguous disclosures and demanded full audit reports.",
            "patZh": "股东们不满于含糊不清的信息披露，要求出具完整的审计报告。"
        },
        {
            "w": "contend", "ipa": "kənˈtend", "pos": "vi.", "s": "s3", "zh": "争取", "exam": "竞争；争论",
            "c": ["contend for 争夺", "contend that 主张/坚称…"],
            "syn": ["compete", "assert", "strive"],
            "fam": ["contender n. 竞争者", "contention n. 争论"],
            "dif": "contend 指在斗争中竞争，或坚决声称某种论点。",
            "pat": "Several candidates decided to contend for the chief executive position within the firm.",
            "patZh": "几名候选人决定在公司内部争夺首席高管职位。"
        },
        {
            "w": "contest", "ipa": "ˈkɒntest", "pos": "n. / v.", "s": "s3", "zh": "争夺", "exam": "竞赛；争论",
            "c": ["leadership contest 领导权争夺", "contest a decision 对决定提出质疑"],
            "syn": ["competition", "challenge", "dispute"],
            "fam": ["contestant n. 参赛者"],
            "dif": "contest 作名词重音在前指比赛；作动词重音在后指驳斥、质询合法性。",
            "pat": "Dissident shareholders launched a proxy contest to challenge board decisions.",
            "patZh": "异见股东发起了代理人争夺战，以质疑董事会的决定。"
        },
        {
            "w": "context", "ipa": "ˈkɒntekst", "pos": "n.", "s": "s3", "zh": "语境", "exam": "上下文；语境；背景",
            "c": ["in the context of 在…背景下", "historical context 历史背景"],
            "syn": ["background", "environment", "setting"],
            "fam": ["contextual adj. 语境的"],
            "dif": "context 指文章前后文语境或事件发生的整体历史/社会背景。",
            "pat": "Legal agreements should always be interpreted in the context of relevant corporate statutes.",
            "patZh": "法律协议应当始终在相关公司法规的背景下进行解释。"
        },
        {
            "w": "contract", "ipa": "ˈkɒntrækt", "pos": "n. / v.", "s": "s3", "zh": "合同", "exam": "合同；契约；收缩；缔结",
            "c": ["sign a contract 签订合同", "breach of contract 违约"],
            "syn": ["agreement", "pact", "shrink"],
            "fam": ["contractor n. 承包商", "contraction n. 收缩"],
            "dif": "contract 作名词指协议合同；作动词指肌肉/经济收缩，或感染疾病。",
            "pat": "Both parties agreed to abide by the terms specified in the binding commercial contract.",
            "patZh": "双方均同意遵守具有约束力的商业合同中规定的条款。"
        },
        {
            "w": "contradict", "ipa": "ˌkɒntrəˈdɪkt", "pos": "v.", "s": "s3", "zh": "相矛盾", "exam": "与…矛盾",
            "c": ["contradict oneself 自相矛盾", "contradict evidence 与证据矛盾"],
            "syn": ["gainsay", "refute", "counter"],
            "fam": ["contradiction n. 矛盾", "contradictory adj. 矛盾的"],
            "dif": "contradict 指陈述或事实与另一事物直接相反、互为矛盾。",
            "pat": "Auditors found that the firm's financial statements contradict its official tax returns.",
            "patZh": "审计人员发现该公司的财务报表与其官方税务申报自相矛盾。"
        },
        {
            "w": "contrary", "ipa": "ˈkɒntrəri", "pos": "adj. / n.", "s": "s3", "zh": "相反的", "exam": "相反的；相反",
            "c": ["on the contrary 相反地", "contrary to popular belief 与普遍观点相反"],
            "syn": ["opposite", "conflicting", "adverse"],
            "fam": ["contrarily adv. 相反地"],
            "dif": "contrary 表示性质完全相反，常构成固定短语 on the contrary。",
            "pat": "Contrary to market expectations, the startup generated substantial profit in its first year.",
            "patZh": "与市场预期相反，这家初创企业在第一年就产生了丰厚的利润。"
        },
        {
            "w": "contrast", "ipa": "ˈkɒntrɑːst", "pos": "v. / n.", "s": "s3", "zh": "对比", "exam": "使形成对比；对比",
            "c": ["in contrast to 与…形成对比", "sharp contrast 鲜明对比"],
            "syn": ["comparison", "difference", "differentiate"],
            "fam": ["contrasting adj. 形成对比的"],
            "dif": "contrast 侧重对照显现出两者之间的差异性。",
            "pat": "The new manager's open style stood in sharp contrast to the rigid culture of the past.",
            "patZh": "新经理开放的风格与过去僵化的文化形成了鲜明对比。"
        },
        {
            "w": "diverse", "ipa": "daɪˈvɜːs", "pos": "adj.", "s": "s3", "zh": "多样的", "exam": "多样的",
            "c": ["diverse background 多元背景", "diverse portfolio 多元化投资组合"],
            "syn": ["varied", "assorted", "heterogeneous"],
            "fam": ["diversity n. 多样性", "diversify v. 使多样化"],
            "dif": "diverse 强调种类繁多且各具特色、性质不同。",
            "pat": "The company recruits experts from diverse disciplines to drive technological innovation.",
            "patZh": "该公司招募来自不同学科领域的专家以推动技术创新。"
        },
        {
            "w": "diversion", "ipa": "daɪˈvɜːʃn", "pos": "n.", "s": "s3", "zh": "分心手段", "exam": "转移；转移注意力；娱乐",
            "c": ["traffic diversion 交通改道", "create a diversion 制造转移注意力的手段"],
            "syn": ["distraction", "detour", "amusement"],
            "fam": ["divert v. 转移"],
            "dif": "diversion 侧重指方向的偏转、注意力的分散或休闲消遣活动。",
            "pat": "Management created a publicity campaign as a temporary diversion from bad earnings news.",
            "patZh": "管理层策划了一场宣传活动，作为转移对盈利不佳新闻注意力的临时手段。"
        },
        {
            "w": "divert", "ipa": "daɪˈvɜːt", "pos": "vt.", "s": "s3", "zh": "转移", "exam": "转移；使转向；改变用途",
            "c": ["divert attention 转移注意力", "divert funds 挪用/改变资金用途"],
            "syn": ["redirect", "reroute", "distract"],
            "fam": ["diversion n. 转移"],
            "dif": "divert 指改变流向、资金用途或注意力转向。",
            "pat": "The board decided to divert extra capital toward emergency research and development.",
            "patZh": "董事会决定将额外资金转移用于应急研发。"
        },
        {
            "w": "divide", "ipa": "dɪˈvaɪd", "pos": "v. / n.", "s": "s3", "zh": "分散", "exam": "分配；划分；使产生分歧",
            "c": ["divide into 划分为", "digital divide 数字鸿沟"],
            "syn": ["separate", "split", "partition"],
            "fam": ["division n. 部门；划分", "divisible adj. 可分割的"],
            "dif": "divide 指把整体切开拆分，或使看法产生分歧分裂。",
            "pat": "Executives opted to divide operational tasks among specialized cross-functional teams.",
            "patZh": "高管们选择在专门的跨职能团队之间分散分配运营任务。"
        },
        {
            "w": "dividend", "ipa": "ˈdɪvɪdend", "pos": "n.", "s": "s3", "zh": "红利", "exam": "股息；红利",
            "c": ["pay a dividend 派发股息", "demographic dividend 人口红利"],
            "syn": ["payout", "bonus", "gain"],
            "fam": ["divide v. 分割"],
            "dif": "dividend 特指公司向股东分配的利润股息，或长期努力带来的红利回报。",
            "pat": "The firm announced an increased annual dividend following a highly profitable quarter.",
            "patZh": "在一季度实现高额盈利后，该公司宣布提高年度股息。"
        },
        {
            "w": "division", "ipa": "dɪˈvɪʒn", "pos": "n.", "s": "s3", "zh": "部门", "exam": "划分；部门；分歧",
            "c": ["sales division 销售部门", "division of labor 劳工分工"],
            "syn": ["department", "section", "split"],
            "fam": ["divide v. 分割"],
            "dif": "division 可以指大型企业中的分支部门，也可以指意见的分歧割裂。",
            "pat": "The regional division met all sales targets despite challenging macroeconomic conditions.",
            "patZh": "尽管宏观经济条件充满挑战，区域部门仍完成了所有销售目标。"
        },
        {
            "w": "document", "ipa": "ˈdɒkjumənt", "pos": "n. / vt.", "s": "s3", "zh": "文件", "exam": "文件；文献；记录",
            "c": ["official document 官方文件", "document progress 记录进度"],
            "syn": ["record", "file", "archive"],
            "fam": ["documentary n. 纪录片", "documentation n. 文件资料"],
            "dif": "document 作名词指公文案卷，作动词指用文字或视频记录事实。",
            "pat": "Attorneys advised the corporation to document every transaction involving foreign partners.",
            "patZh": "律师建议公司记录与外国合作伙伴相关的每一笔交易。"
        },
        {
            "w": "documentary", "ipa": "ˌdɒkjuˈmentri", "pos": "adj. / n.", "s": "s3", "zh": "纪录片", "exam": "文献的；纪录的；纪录片",
            "c": ["documentary film 纪录片", "documentary evidence 兼据/书证"],
            "syn": ["chronicle", "report", "factual"],
            "fam": ["document n. 文件"],
            "dif": "documentary 作为名词特指纪实影片，作为形容词指有文献记录依据的。",
            "pat": "An investigative journalist produced a compelling documentary on industrial compliance.",
            "patZh": "一名调查记者制作了一部关于工业合规性的引人注目的纪录片。"
        },
        {
            "w": "execute", "ipa": "ˈeksɪkjuːt", "pos": "vt.", "s": "s3", "zh": "执行", "exam": "实施；执行",
            "c": ["execute a plan 执行计划", "execute a contract 履行合同"],
            "syn": ["perform", "implement", "enforce"],
            "fam": ["execution n. 执行", "executive n. 高管"],
            "dif": "execute 侧重贯彻落实既定计划、法令或执行特定法律手续。",
            "pat": "The management team worked tirelessly to execute the company's strategic realignment.",
            "patZh": "管理团队不知疲倦地工作，以执行公司的战略重组。"
        },
        {
            "w": "executive", "ipa": "ɪɡˈzekjətɪv", "pos": "n. / adj.", "s": "s3", "zh": "高管", "exam": "高管；主管人；执行的",
            "c": ["chief executive 首席执行官", "executive board 执行董事会"],
            "syn": ["administrator", "manager", "director"],
            "fam": ["execute v. 执行"],
            "dif": "executive 指机构中拥有最高决策或执行权的高层管理人员。",
            "pat": "Senior executives agreed that environmental compliance must be prioritized in corporate goals.",
            "patZh": "高级高管们一致认为，环境合规必须列为公司目标的首要任务。"
        },

        # s4 words
        {
            "w": "exemplify", "ipa": "ɪɡˈzemplɪfaɪ", "pos": "vt.", "s": "s4", "zh": "树立典范", "exam": "是…的典范；举例说明",
            "c": ["exemplify leadership 展现领导力典范", "exemplify the spirit 体现精神"],
            "syn": ["illustrate", "embody", "epitomize"],
            "fam": ["example n. 例子", "exemplary adj. 模范的"],
            "dif": "exemplify 指通过自身表现典型地展现或成为某品质的代表。",
            "pat": "Her selfless dedication during the crisis served to exemplify genuine public leadership.",
            "patZh": "她在危机期间的无私奉献成为了真正公共领导力的典范。"
        },
        {
            "w": "exert", "ipa": "ɪɡˈzɜːt", "pos": "vt.", "s": "s4", "zh": "行使", "exam": "运用；使用；施加",
            "c": ["exert pressure 施加压力", "exert influence 行使影响"],
            "syn": ["exercise", "wield", "apply"],
            "fam": ["exertion n. 努力；施加"],
            "dif": "exert 指积极运用权力、影响力或付出极大体能精力。",
            "pat": "Regulators must exert authority strictly to prevent financial market manipulation.",
            "patZh": "监管机构必须严格行使权力，以防止金融市场操纵。"
        },
        {
            "w": "exhaust", "ipa": "ɪɡˈzɔːst", "pos": "v. / n.", "s": "s4", "zh": "精疲力竭", "exam": "使精疲力竭；耗尽",
            "c": ["exhaust resources 耗尽资源", "exhaust fumes 汽车废气"],
            "syn": ["deplete", "drain", "fatigue"],
            "fam": ["exhaustion n. 耗尽；衰竭", "exhaustive adj. 详尽的"],
            "dif": "exhaust 指体力或资源彻底用尽、消耗殆尽。",
            "pat": "Overworking staff will inevitably exhaust their energy and reduce long-term quality.",
            "patZh": "让员工过度劳累必然会耗尽他们的精力并降低长期质量。"
        },
        {
            "w": "exist", "ipa": "ɪɡˈzɪst", "pos": "vi.", "s": "s4", "zh": "生存", "exam": "存在",
            "c": ["cease to exist 不复存在", "exist peacefully 和平共处"],
            "syn": ["be", "prevail", "subsist"],
            "fam": ["existence n. 存在", "existent adj. 现存的"],
            "dif": "exist 指客观实体在现实中的实际存在或维持基本的生存状态。",
            "pat": "Public welfare institutions exist to serve vulnerable populations across the country.",
            "patZh": "公共福利机构的存在是为了服务全国范围内的弱势群体。"
        },
        {
            "w": "existence", "ipa": "ɪɡˈzɪstəns", "pos": "n.", "s": "s4", "zh": "生存", "exam": "存在；生存",
            "c": ["come into existence 产生", "in existence 现存的"],
            "syn": ["presence", "being", "continuation"],
            "fam": ["exist v. 存在"],
            "dif": "existence 强调客观存在的事实或生命维持的状态。",
            "pat": "The law threatened the very existence of unregulated small lending companies.",
            "patZh": "该法律威胁到了未经监管的小额贷款公司的生存。"
        },
        {
            "w": "exotic", "ipa": "ɪɡˈzɒtɪk", "pos": "adj.", "s": "s4", "zh": "异国情调的", "exam": "异国情调的",
            "c": ["exotic plants 异国植物", "exotic culture 异域文化"],
            "syn": ["foreign", "alien", "unusual"],
            "fam": ["exoticism n. 异国情调"],
            "dif": "exotic 强调源自外国、带有新奇吸引力的异彩风情。",
            "pat": "Importing exotic management tools without local adaptation often leads to internal conflict.",
            "patZh": "在没有本地化调适的情况下引进具有异国情调的管理工具往往会导致内部冲突。"
        },
        {
            "w": "moral", "ipa": "ˈmɒrəl", "pos": "adj. / n.", "s": "s4", "zh": "道德的", "exam": "道德的；品行",
            "c": ["moral standard 道德标准", "moral obligation 道德义务"],
            "syn": ["ethical", "upright", "virtuous"],
            "fam": ["morality n. 道德", "morally adv. 道德上地"],
            "dif": "moral 指符合人类社会的善恶道德准则，或故事的寓意。",
            "pat": "Business leaders have a moral obligation to consider the environmental impact of their choices.",
            "patZh": "商业领袖有道德义务去考虑其选择对环境产生的影响。"
        },
        {
            "w": "morality", "ipa": "məˈræləti", "pos": "n.", "s": "s4", "zh": "职业道德", "exam": "道德；规范",
            "c": ["public morality 公共道德", "professional morality 职业道德"],
            "syn": ["ethics", "integrity", "righteousness"],
            "fam": ["moral adj. 道德的"],
            "dif": "morality 抽象指社会或个人的道德品质、伦理准则框架。",
            "pat": "Maintaining high standards of professional morality builds trust between institutions and the public.",
            "patZh": "保持高水平的职业道德能在机构与公众之间建立信任。"
        },
        {
            "w": "moreover", "ipa": "mɔːrˈəʊvə", "pos": "adv.", "s": "s4", "zh": "此外", "exam": "此外；而且",
            "c": ["moreover, it is clear 此外，显而易见的是", "moreover, research shows 而且，研究表明"],
            "syn": ["furthermore", "besides", "in addition"],
            "fam": ["more adj. / adv. 更多"],
            "dif": "moreover 为正式递进连接副词，表示对前面观点的进一步重要补充。",
            "pat": "The project was completed on schedule; moreover, it stayed well within the allocated budget.",
            "patZh": "该项目按时完成；此外，它还很好地控制在分配的预算之内。"
        },
        {
            "w": "mostly", "ipa": "ˈməʊstli", "pos": "adv.", "s": "s4", "zh": "主要地", "exam": "完全地；主要地；大部分",
            "c": ["mostly composed of 主要由…组成", "mostly true 大体真实"],
            "syn": ["chiefly", "mainly", "predominantly"],
            "fam": ["most adj. / adv. 最多"],
            "dif": "mostly 侧重频次或数量上的“绝大部分”、“主要地”。",
            "pat": "The target audience for the civic education initiative consists mostly of young adults.",
            "patZh": "公民教育倡议的目标受众主要由青年人组成。"
        },
        {
            "w": "prior", "ipa": "ˈpraɪə", "pos": "adj.", "s": "s4", "zh": "事先的", "exam": "在前的；优先的",
            "c": ["prior notice 事先通知", "prior engagement 事先约会"],
            "syn": ["previous", "preceding", "earlier"],
            "fam": ["priority n. 优先事项"],
            "dif": "prior 常指时间上在先的，搭配 to 表示在…之前。",
            "pat": "The policy update required prior approval from the board of directors before release.",
            "patZh": "政策更新在发布前需要获得董事会的事先批准。"
        },
        {
            "w": "priority", "ipa": "praɪˈɒrəti", "pos": "n.", "s": "s4", "zh": "最高优先事项", "exam": "优先权；首要事项",
            "c": ["top priority 最高优先事项", "give priority to 优先考虑"],
            "syn": ["precedence", "preference", "urgency"],
            "fam": ["prior adj. 在前的"],
            "dif": "priority 强调由于重要性或紧急性而享有的优先受考虑地位。",
            "pat": "Ensuring patient health and safety must remain the top priority of hospital staff.",
            "patZh": "确保患者健康和安全必须始终是医院员工的最高优先事项。"
        },
        {
            "w": "privacy", "ipa": "ˈprɪvəsi", "pos": "n.", "s": "s4", "zh": "隐私", "exam": "隐私",
            "c": ["privacy policy 隐私政策", "right to privacy 隐私权"],
            "syn": ["seclusion", "confidentiality", "solitude"],
            "fam": ["private adj. 私人的"],
            "dif": "privacy 指个人生活、信息不受打扰或未经授权披露的隐秘状态。",
            "pat": "Data protection laws strictly enforce user privacy online against unauthorized surveillance.",
            "patZh": "数据保护法严格执行在线用户隐私权，防范未经授权的监视。"
        },
        {
            "w": "private", "ipa": "ˈpraɪvət", "pos": "adj.", "s": "s4", "zh": "私人", "exam": "私人的；私营的",
            "c": ["private sector 私营部门", "private property 私人财产"],
            "syn": ["personal", "confidential", "individual"],
            "fam": ["privacy n. 隐私", "privately adv. 私下地"],
            "dif": "private 与 public（公共的）相对，指归个人所有或非公开的。",
            "pat": "Medical records contain sensitive personal details and must be kept strictly private.",
            "patZh": "医疗记录包含敏感的个人明细，必须严格保密。"
        },
        {
            "w": "privilege", "ipa": "ˈprɪvəlɪdʒ", "pos": "n.", "s": "s4", "zh": "特权", "exam": "特权；荣幸",
            "c": ["special privilege 特殊特权", "an honor and privilege 荣幸"],
            "syn": ["prerogative", "advantage", "entitlement"],
            "fam": ["privileged adj. 享特权的"],
            "dif": "privilege 特指特定阶层或岗位享有的独有特权、特殊待遇。",
            "pat": "Serving as a public servant is a solemn duty rather than a personal privilege.",
            "patZh": "担任公职是一项庄严的职责，而不是个人的特权。"
        },
        {
            "w": "prudent", "ipa": "ˈpruːdnt", "pos": "adj.", "s": "s4", "zh": "审慎", "exam": "审慎的",
            "c": ["prudent decision 审慎的决定", "prudent investor 审慎的投资者"],
            "syn": ["cautious", "judicious", "wise"],
            "fam": ["prudence n. 审慎", "prudently adv. 审慎地"],
            "dif": "prudent 强调因远见卓识和深谋远虑而采取谨慎、明智的态度。",
            "pat": "Fiscal managers advocated for a prudent spending policy during turbulent economic periods.",
            "patZh": "在动荡的经济时期，财政管理者主张采取审慎的支出政策。"
        },

        # s5 words
        {
            "w": "submit", "ipa": "səbˈmɪt", "pos": "v.", "s": "s5", "zh": "提交", "exam": "提交；呈递",
            "c": ["submit a proposal 提交提案", "submit to authority 服从权威"],
            "syn": ["present", "tender", "surrender"],
            "fam": ["submission n. 提交；屈服"],
            "dif": "submit 既可指向上级或机构提交文件，也可指屈服归顺。",
            "pat": "Researchers were asked to submit their final progress report by the end of the month.",
            "patZh": "研究人员被要求在月底前提交他们的最终进度报告。"
        },
        {
            "w": "subordinate", "ipa": "səˈbɔːdɪnət", "pos": "adj. / n.", "s": "s5", "zh": "下级", "exam": "下级的",
            "c": ["subordinate staff 下级员工", "subordinate position 次要地位"],
            "syn": ["secondary", "inferior", "assistant"],
            "fam": ["subordination n. 顺从；次要"],
            "dif": "subordinate 指地位、级别较低的人员或次要的事物。",
            "pat": "Good leaders empower subordinate employees rather than micromanaging every task.",
            "patZh": "好的领导者会向下级员工赋能，而不是微观管理每一项任务。"
        },
        {
            "w": "subscribe", "ipa": "səbˈskraɪb", "pos": "v.", "s": "s5", "zh": "赞同", "exam": "赞同；签署",
            "c": ["subscribe to a view 赞同某观点", "subscribe to a journal 订阅期刊"],
            "syn": ["endorse", "agree", "support"],
            "fam": ["subscriber n. 订阅者", "subscription n. 订阅"],
            "dif": "subscribe 搭配 to 表示赞同某种理念，或付费定期订阅报刊服务。",
            "pat": "Many educators subscribe to the view that experiential learning builds stronger skills.",
            "patZh": "许多教育工作者赞同体验式学习能培养更强技能这一观点。"
        },
        {
            "w": "subsequent", "ipa": "ˈsʌbsɪkwənt", "pos": "adj.", "s": "s5", "zh": "后续", "exam": "随后的",
            "c": ["subsequent events 随后发生的事件", "subsequent developments 后续发展"],
            "syn": ["following", "succeeding", "later"],
            "fam": ["subsequently adv. 随后"],
            "dif": "subsequent 强调时间或顺序上接着某事之后发生的。",
            "pat": "The preliminary discovery paved the way for subsequent breakthroughs in cancer therapy.",
            "patZh": "初步发现为癌症治疗随后的突破铺平了道路。"
        },
        {
            "w": "substance", "ipa": "ˈsʌbstəns", "pos": "n.", "s": "s5", "zh": "实质", "exam": "实质；实体",
            "c": ["toxic substance 有毒物质", "substance of reform 改革的实质"],
            "syn": ["matter", "essence", "core"],
            "fam": ["substantial adj. 实质的"],
            "dif": "substance 既可指具体的物理物质，也可指讲话或政策的核心实质内涵。",
            "pat": "Voters demanded real substance in candidate speeches instead of empty political promises.",
            "patZh": "选民要求候选人演讲具有真实实质，而不是空洞的政治承诺。"
        },
        {
            "w": "substantial", "ipa": "səbˈstænʃl", "pos": "adj.", "s": "s5", "zh": "实质性的", "exam": "实质的；大量的",
            "c": ["substantial increase 大幅增长", "substantial evidence 充分的证据"],
            "syn": ["considerable", "significant", "sizeable"],
            "fam": ["substantially adv. 实质上地；大幅地"],
            "dif": "substantial 强调数量、程度巨大或内容切实重要。",
            "pat": "The foundation provided a substantial grant to fund rural educational facilities.",
            "patZh": "基金会提供了一笔数额巨大的拨款，用于资助农村教育设施。"
        },
        {
            "w": "substitute", "ipa": "ˈsʌbstɪtjuːt", "pos": "n. / v.", "s": "s5", "zh": "替代品", "exam": "替代品；替代",
            "c": ["substitute for 替代", "sugar substitute 代糖"],
            "syn": ["replacement", "alternative", "surrogate"],
            "fam": ["substitution n. 替代"],
            "dif": "substitute 指用来代替另一事物的人或物，或执行替代动作。",
            "pat": "Virtual simulations serve as a practical substitute when laboratory equipment is unavailable.",
            "patZh": "当无法获得实验室设备时，虚拟仿真可作为实用的替代品。"
        },
        {
            "w": "subtle", "ipa": "ˈsʌtl", "pos": "adj.", "s": "s5", "zh": "微妙的", "exam": "微妙的；细微的",
            "c": ["subtle difference 微妙的区别", "subtle hint 暗示"],
            "syn": ["delicate", "nuanced", "understated"],
            "fam": ["subtlety n. 微妙；精妙"],
            "dif": "subtle 强调隐约、不易察觉但至关重要的细微差别。",
            "pat": "Translators must pay attention to subtle nuances in order to convey the precise original tone.",
            "patZh": "译者必须注意微妙的细微差别，以传达精准的原本语气。"
        },
        {
            "w": "associate", "ipa": "əˈsəʊʃieɪt", "pos": "v. / n.", "s": "s5", "zh": "建立联系", "exam": "使联系；使结合；伙伴",
            "c": ["associate with 与…建立联系/交往", "business associate 商务伙伴"],
            "syn": ["connect", "link", "partner"],
            "fam": ["association n. 协会；联系"],
            "dif": "associate 动词指将两者在思想上联系起来，名词指业务同事伙伴。",
            "pat": "People often associate high productivity with effective time management strategies.",
            "patZh": "人们往往将高生产力与有效的时间管理策略建立联系。"
        },
        {
            "w": "association", "ipa": "əˌsəʊʃiˈeɪʃn", "pos": "n.", "s": "s5", "zh": "协会", "exam": "协会；结合；联系",
            "c": ["in association with 与…联合", "trade association 行业协会"],
            "syn": ["organization", "alliance", "connection"],
            "fam": ["associate v. 联系"],
            "dif": "association 可以指专门成立的社团协会，也可以指观念上的联想联系。",
            "pat": "The national teachers association published new guidelines to support inclusive classroom design.",
            "patZh": "全国教师协会发布了新指南，以支持包容性课堂设计。"
        },
        {
            "w": "amend", "ipa": "əˈmend", "pos": "vt.", "s": "s5", "zh": "修改", "exam": "修改；修订",
            "c": ["amend the law 修改法律", "amend a contract 修改合同"],
            "syn": ["revise", "modify", "alter"],
            "fam": ["amendment n. 修正案"],
            "dif": "amend 专门指通过正式法定程序对法律、条款或公文进行修改订正。",
            "pat": "Parliament voted to amend the labor law to strengthen worker safety protections.",
            "patZh": "议会投票决定修改劳动法，以加强工人安全保护。"
        },
        {
            "w": "amongst", "ipa": "əˈmʌŋst", "pos": "prep.", "s": "s5", "zh": "在…之中", "exam": "在…之中",
            "c": ["amongst other things 其中包括", "amongst the crowd 在人群中"],
            "syn": ["among", "amidst", "surrounded by"],
            "fam": ["among prep. 在…之中"],
            "dif": "amongst 是 among 的英式文学表达形式，三者以上之中。",
            "pat": "Debates arose amongst scholars concerning the long-term societal impact of artificial intelligence.",
            "patZh": "学者们之中引发了关于人工智能长期社会影响的辩论。"
        },
        {
            "w": "amount", "ipa": "əˈmaʊnt", "pos": "n. / vi.", "s": "s5", "zh": "数量", "exam": "数量；总计",
            "c": ["amount to 总计达/相当于", "a vast amount of 大量的"],
            "syn": ["quantity", "total", "sum"],
            "fam": ["amount v. 总计达"],
            "dif": "amount 搭配不可数名词；number 搭配可数名词复数。",
            "pat": "The reform initiative raised a vast amount of funding to upgrade educational technology.",
            "patZh": "改革倡议筹集了大量资金来升级教育技术。"
        },
        {
            "w": "ample", "ipa": "ˈæmpl", "pos": "adj.", "s": "s5", "zh": "充足的", "exam": "充足的",
            "c": ["ample evidence 充分的证据", "ample time 充裕的时间"],
            "syn": ["abundant", "plentiful", "sufficient"],
            "fam": ["amplification n. 扩大"],
            "dif": "ample 侧重空间、时间或资源宽裕充沛、绰绰有余。",
            "pat": "The research team was granted ample time to complete comprehensive field trials.",
            "patZh": "研究团队获得了充裕的时间来完成全面的野外试验。"
        },
        {
            "w": "amuse", "ipa": "əˈmjuːz", "pos": "vt.", "s": "s5", "zh": "逗乐", "exam": "逗乐；提供娱乐",
            "c": ["amuse oneself 自娱自乐", "amuse the audience 逗乐观众"],
            "syn": ["entertain", "delight", "divert"],
            "fam": ["amusement n. 娱乐", "amusing adj. 引人发笑的"],
            "dif": "amuse 侧重提供轻松愉快的娱乐、使人发笑或得到遣怀。",
            "pat": "The interactive educational software was designed to amuse young students while teaching basic math.",
            "patZh": "这款互动教育软件旨在逗乐幼年学生的同时教授基础数学。"
        }
    ]
}

out_json = r'd:\xinyi\codespace\WowStory\单词故事本\Unit17.json'
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(unit_data, f, ensure_ascii=False, indent=2)

print(f"Saved {out_json} with {len(unit_data['words'])} words and {len(unit_data['stories'])} stories.")
