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
                    "en": "In the industrial heartland, engineers had a gloomy [[outlook]] regarding factory [[output]], as obsolete machinery kept worker communities in [[poverty]]. To break this cycle, the state granted clean energy [[power]] to a [[practical]] workshop where innovative [[practice|practices]] were tested. Mechanical [[practitioner|practitioners]] were encouraged to [[practise]] advanced automated techniques rather than just [[preach]] theoretical ideals.",
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
                    "zh": "勘测员仔细保存了一座数百年古庙的剩余部分，同时将古代遗迹编目以供博物馆展出。发掘组长提出了一个可持续的补救方法，以保护废墟免受风雨侵蚀。"
                },
                {
                    "en": "Scholars still [[remember]] how Elders used to [[remind]] youth that historical memory could [[render]] a community resilient against modern disruptions. Ultimately, the highway was rerouted around the site.",
                    "zh": "学者们依然记得长老们过去如何提醒年轻人：历史记忆能够使一个社区在面对现代冲击时保持韧性。最终，公路被绕道开设在遗址周围。"
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
                    "en": "When a major supplier attempted to breach a binding [[contract]], auditors proved that its claims [[contradict|contradicted]] basic accounting facts. On the [[contrary]] to public belief, the company's internal reports showed a sharp [[contrast]] between advertised ethics and actual practices. In response, leadership pursued [[diverse]] investment strategies as a temporary [[diversion]] to [[divert]] public attention away from the lawsuit.",
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
                    "en": "A public leader must [[exemplify]] integrity whenever they [[exert]] authority over civic institutions. Pushing staff to the point of total [[exhaust|exhaustion]] can endanger the very [[exist|existence]] of a public healthcare system. Analysts noticed that [[exotic]] management models imported from abroad often clashed with local [[moral]] values and professional [[morality]].",
                    "zh": "一位公共管理者在对公民机构行使职权时必须树立诚信的典范。将员工推到彻底精疲力竭的地步可能会危及公共医疗体系的生存。分析人士注意到，从国外引进的具有异国情调的管理模式往往与当地的道德价值观和职业道德规范相冲突。"
                },
                {
                    "en": "[[Moreover]], hospital staff were [[mostly]] concerned that policy updates occurred without [[prior]] consultation. They demanded that patient care be given top [[priority]], ensuring that patient [[privacy]] and [[private]] medical records were safeguarded against unauthorized access.",
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
    "words": []
}

print(f"Stories written: {len(unit_data['stories'])}")
