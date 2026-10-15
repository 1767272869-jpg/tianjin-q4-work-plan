# -*- coding: utf-8 -*-
from pathlib import Path
import base64, html, json
from diagrams import schematic
ROOT=Path(__file__).resolve().parent
def esc(s): return html.escape(str(s))
def table(headers, rows, cls=''):
 return '<div class="table-wrap '+cls+'"><table><thead><tr>'+''.join('<th scope="col">'+h+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+c+'</td>' for c in r)+'</tr>' for r in rows)+'</tbody></table></div>'
EV={
'E1':('数据参考','客源结构与装修需求：面积是线索，需求还需确认',
 table(['范围','可引用的事实','解释范围'],[
 ['天津市内六区二手市场','成交占比46.5%；平均面积约66.8㎡（表中取整67㎡）；≥70㎡占比38.8%','说明交易资源的面积结构，不直接证明装修意愿或消费能力。'],
 ['天塔，2026年1—9月','按二手签约时间统计客源6,362条；＜50㎡1,397条、50—70㎡1,410条、≥70㎡3,555条；≥50㎡合计78.0%','与城市整体范围不同。原图“50平+”在口径说明中指≥50㎡。'],
 ]), '来源：城市市场结构截图；四中心报告1.1、1.9及口径说明。学区政策文字仅作为当时的业务背景，本稿不据此说明现行政策。', ['market']),
'E2':('数据参考','天塔的接触规模与装修产出',
 table(['指标','2026年1—9月','应如何使用'],[
 ['客源／带展／草签／正签','线索时间口径客源6,370条；同期带展1,282、草签98、正签78','各阶段按自身时间归期，不是同一批客户的逐层流失。'],
 ['同期数量比','带展÷客源20.13%；正签÷客源1.22%','用于提出后续分析问题，不能当作同批客户真实转化率。'],
 ['草签合同额及配套','草签合同额约1,077.3万元；草签单均约10.99万元；定软电配比19.6%','合同额不等于收入、回款或利润；配比需结合需求、产品和成本解释。'],
 ]), '来源：四中心报告2.9、3.8、口径说明。客源按编码统计，同一二手协议可能关联多个客源；6,362与6,370的时间口径不同。', ['center','finance','definitions']),
'E3':('数据参考','天塔门店资源集中，可以先明确经营优先级',
 '<p>天塔689家门店有二手签约记录，按中心内客源量排序取头部30%，共207家，贡献5,261条，占82.7%。这里的“有签约”指二手签约，不能解释为这些门店均有装修成交。</p><p>支持先摸排重点门店；实际维护顺序还需结合装修需求、合作意愿、既有反馈及承接情况。</p>',
 '来源：四中心报告4.1。207家为689×30%向上取整。', ['doors']),
'E4':('个案参考','需求、预算及承诺交接的具体问题',
 table(['案例／反馈','能够支持的判断'],[
 ['7月4日客户访谈：收纳需求未充分进入方案；定制预算约3.3万元变为4.8万元，部分附加费用未提前说明','有必要检查需求记录、预算范围和变化确认；不能据单例估算问题发生率。'],
 ['7月5日客户反馈：设计师曾承诺处理窗户移位，施工时却需客户自行找人；更换设计师后重新沟通需求','交接和承诺留痕值得改善，需回看合同、方案、变更及责任记录。'],
 ['9月28日四真培训：展厅介绍、道具使用及客户服务方式存在差异','可作为服务流程与角色访谈的入口，不能直接判定差异造成多少流失。'],
 ]), '来源：关键挑战截图中记录的客户访谈及培训摘要。日期按原文保留，案例明细尚未在本次独立核查。', ['challenge']),
'E5':('战略要求','展厅要把体验转成客户自己家的方案与预算',
 '<p>家装签约中心2.0展厅利用购房交易的近场服务机会，通过场景、产品、选材及工具辅助决策；围绕客户户型确认布局、风格、配置、预算和保障。</p><p>“四真”对应保障、适配、落地、透明。要求需求有记录，方案与预算经过深化，承诺能够交接。服务效果需要通过客户记录与反馈验证。</p>',
 '来源：两类物理场地与四真标准截图。此处引用家装展厅及服务要求。', ['service']),
'E6':('业务反馈','经营方式为什么需要调整',
 '<p>开城初期希望利用签约中心见客、展厅及自身服务完成转化，并避免订单增长超过承接能力。运行后发现签约经理精力有限，家装团队与门店联系不足；从Q3开始推动直接联动，并开放部分项目资源。资源已提供，但联动效果仍需进一步了解。</p><p>这是对经营背景和调整思路的整理；门店关系对成交的具体影响、资源开放效果，需要后续明细和访谈验证。</p>',
 '', []),
'E7':('工作记录','客服和定责已经发现的流程问题',
 '<p>例会反复涉及：定制设计及反补、对客预期与承诺、配送安装排期、跨岗位信息不互通、问题上报及定责等待、漏水及收尾处理、线下下单手续遗漏。</p><p>拟与客服、定责、设计及交付伙伴复核案例，将可预防问题转成节点检查项。同一事件可能连续多期出现，不能把周报提及次数当发生量；责任结论及规则由专业伙伴确认。</p>',
 '来源：《【品策】中心例会汇报》，重点参考10.1—10.11及9月相关记录。', []),
'E8':('产品记录','MOMA已有成果与正式能力的边界',
 '<p>依据10月12日V4方案及最新交接：已有产品方案、可操作HTML原型、来源映射与构建交接。共17个组件登记，其中15个可见组件取得查询引用，2个备用组件待补。引用登记不代表正式取数已接通。</p><p>原型的计划保存在本机，结果需人工录入；正式取数、自由日期、真实同批转化、等待客户、自动通知及多人协作尚需验收。实际接入、使用和收益按后续验收记录。</p>',
 '来源：《经营罗盘V4·业务诊断与数据映射》《应用构建交接_最新要求与验收》，2026-10-12。', []),
'E9':('口径核查','两版天塔9月数据暂不能混用',
 table(['字段','9月线上看板截图','四中心1—9月报告中的9月'],[
 ['客源／集签','月全量集签477','二手签约时间口径580；线索时间口径568'],
 ['装修数量','委托366；到店141；草签14；正签15','带展153；草签14；正签17'],
 ['金额','月草签业绩流水224.4万；草签合同额目标229万','另一数据范围；本稿不与前列金额相除'],
 ]), '来源：新发9月线上看板与四中心报告。截止日期、目标单、区域、状态及到店／带展定义尚未对齐，不能据此判定哪份错误，亦不能拼成漏斗。', ['month'])
}
def evidence(*ids):
 out='<div class="evidence-group">'
 for id in ids:
  tag,title,body,source,ims=EV[id]
  out+=f'<details class="evidence" id="{id}"><summary><span class="source-tag">{tag} · {id}</span><span>{title}</span><span class="chevron">＋</span></summary><div class="evidence-body">{body}'+(f'<p class="source-note">{source}</p>' if source else '')
  out+='</div></details>'
 return out+'</div>'
def section(id,no,title,lead,body):return f'<section id="{id}" class="section"><div class="section-head"><span class="section-num">{no}</span><div><h2>{title}</h2><p class="lead">{lead}</p></div></div>{body}</section>'

centers=[['天塔',366,141,14,15,477],['中海',190,35,5,6,452],['晨景',297,25,8,6,572],['富裕广场',107,18,5,4,219],['鼓楼',244,73,7,3,386],['中北新城市',154,18,2,3,307],['诺德',167,21,6,1,357],['北辰红郡雅苑',205,13,1,1,374]]
EV['E1']=('数据参考','城市与各中心的客源结构不同，需求要进一步识别',
 table(['范围','数据','支持什么思考'],[
 ['天津市内六区二手市场','成交占比46.5%；平均面积约66.8㎡；≥70㎡占比38.8%。','交易集中不等于当期装修需求集中；需要了解购房用途和装修时间。'],
 ['四中心，2026年1—9月','≥50㎡客源占比：天塔78.0%、中海84.4%、海教96.9%、富裕广场58.7%。','中心间客群结构差异明显，不能直接用一个转化标准解释全部中心。'],
 ]), '来源：城市市场结构截图、四中心报告1.9。城市与四中心范围不同，不直接比较高低；面积不等于意愿或预算。学区文字仅保留为当时背景。', ['market','areas'])
EV['E2']=('数据参考','四中心都有客源、带展与签约，比例差异需要回到客户核查',
 table(['中心','客源（线索时间）','同期带展','同期草签','同期正签'],[
 ['天塔','6,370','1,282','98','78'],['中海','5,261','260','40','37'],['海教','2,886','57','3','2'],['富裕广场','2,769','133','27','23']
 ])+'<p>这组数据支持把“资源进入、接触服务、签约产出”放在一起观察。它提示需要研究的环节，不能据差额统计流失，也不能直接认定服务能力或需求是唯一原因。</p>',
 '来源：四中心报告2.9，2026年1—9月历史口径。各阶段按自身日期统计，客源按编码计数，不是独立二手合同数。本版9月经营观察另用E9新口径，不与本表拼接。', ['center','definitions'])
EV['E3']=('数据参考','四中心共同特点：约三成门店贡献超过八成二手签约客源',
 table(['中心','有二手签约记录门店','头部30%门店','头部门店贡献'],[
 ['天塔','689家','207家','82.7%'],['中海','601家','181家','84.4%'],['海教','440家','132家','84.7%'],['富裕广场','440家','132家','84.2%']
 ])+'<p>支持优先摸排重点门店、明确负责人，再结合装修需求、合作意愿和客户反馈安排维护。这里不是装修成交门店统计；同一门店可能跨中心出现，各中心家数不作为城市去重门店数相加。</p>',
 '来源：四中心报告4.1。各中心按客源贡献排序取前30%，数量向上取整。', ['doors'])
EV['E9']=('新口径数据','9月八个签约中心：已放开目标单限制，可用于本版经营观察',
 table(['中心','月全量集签','月委托','月到店','月草签','月正签','同期到店÷委托'],[
 [x[0]+'签约中心',str(x[5]),str(x[1]),str(x[2]),str(x[3]),str(x[4]),f'{x[2]/x[1]*100:.2f}%'] for x in centers
 ])+'<p><b>可以看到的共性：</b>八个中心的同期月到店数都少于月委托数，到店与委托的数量比为6.3%—38.5%。只看委托量，不能了解实际到店规模和后续推进；各中心都需要补上客户过程跟踪。</p><p><b>进一步分析：</b>数量差额可能涉及跨期、客户需求、邀约安排或记录口径，不能直接认定为流失；需要关联同一客户查看其当前阶段、最近跟进和下一次安排。</p><p><b>9月口径：</b>已放开目标单限制，可用于当期经营观察。各中心表现不同，差异原因需另行核查。</p><p>月到店÷月委托为同期数量比，不能直接解释同批客户转化。近三月数据用于补充观察，必须另列期间；不能与本月分母混算变化。草签业绩流水与合同额目标不是同一金额口径，不直接相除。</p>',
 '来源：9月签约中心线上看板，已放开目标单限制。与1—9月历史数据分别使用，正式分析注明截止日期和计数粒度。', ['month'])

chart='<figure><figcaption>9月各中心委托与到店数量</figcaption><div class="legend"><span>蓝色：月委托</span><span>绿色：月到店</span><span>统一按0—400展示</span></div>'
for x in centers:
 chart+=f'<div class="center-row"><b>{x[0]}</b><div><div class="bar"><i style="width:{x[1]/4}%"></i></div><div class="bar accent"><i style="width:{x[2]/4}%"></i></div></div><span>{x[1]} / {x[2]}</span></div>'
chart+='<p class="small">月到店÷月委托为同期数量比，差额不是流失人数。需关联同一批客户、固定观察期后判断真实转化。</p></figure>'
tag,title,body,source,ims=EV['E9']
EV['E9']=(tag,'各中心都需要跟踪委托后的到店与签约推进（9月新口径）',chart+body,source,ims)

parts=[]
b=schematic('reasoning')+'<h3 class="subhead first-sub">客户和业务分别面临什么难点</h3>'
b+=table(['思考路径','从客户需求角度的思考','从业务盈利角度的思考'],[
 ['需求','根据自己家的布局、喜好的风格得到适配的产品，了解整体预算与服务保障，交钱后拿到预期的装修交付，住进理想中的家。','找准合适的客户群体，而不是一味扩大获客量，把当下的服务能力转成有效订单，完成交付，再通过口碑带来新客户。'],
 ['目前的难点','<b>1. 装修意图难确认。</b>客户在房产成交时，可能还拿不准是否装修、什么时候装修，获客和跟进容易反复。<br><br><b>2. 需求难表达、难理解。</b>有装修意图的客户，对空间、设计、品质和省心服务要求高，却不容易说清具体需求与标准；历史方案、工地案例也难以持续用于帮助客户理解和促成选择。<br><br><b>3. 需求和承诺难持续传递。</b>设计、报价、选材、施工、售后涉及多人、多次交接，重复沟通、变更确认和信息遗漏增加服务成本。','<b>1. 获客增长与承接能力可能不匹配。</b>渠道短时间带来大量订单，设计、服务和交付可能跟不上；只追求成交、承接不足，可能带来客户不满。<br><br><b>2. 获取推荐和客户信任的竞争加大。</b>AI和搜索让客户能从更多渠道了解、比较装修公司；经纪人也有其他推荐选择。依赖渠道导流取得客户，再建立信任拿到订单，面临更大竞争。'],
], 'thinking-table')
b+=evidence('E1','E4')
b+='<h3 class="subhead">当前采取什么动作，解决了什么，还面临什么问题</h3>'
b+=table(['解决问题的动作','预期带来的收益','仍然面临的问题与约束'],[
 ['<b>选择“签约中心＋展厅”</b><br>利用签约中心的客户接触机会，用展厅、产品和服务完成转化；同时先建设承接能力，让增长与服务能力相匹配。','帮助客户发现装修意图、获得风格灵感，通过参考物说清需求和标准，减少前期理解与沟通成本。<br><br>签约经理与经纪人联系较紧密，希望借助其对客户的了解促进沟通。','签约经理精力有限，在签约过程中何时插入装修推荐也需要把握；家装团队与经纪人关系基础较弱，协作难推进；竞品也在争取经纪人推荐，因此我们并非其必须推荐的选择。'],
 ['<b>增加门店、经纪人建联与激励</b><br>家装团队主动走进门店，讲清服务和激励规则，跟进客户并反馈进展。','补充签约经理难以持续覆盖的协作，争取更多推荐机会，建立合作信任；激励宣发也是客户经理建联的一种方式。','联动仍受资源结构影响：二手交易量大，但部分区域小面积、高购房支出及非即时居住需求，限制当期整装机会。增加建联后还要继续识别需求。'],
 ['<b>挖掘更多适配客户</b><br>经营经纪人手上的非当期二手交易客户、新房现房客户，以及未锁盘、已向家装团队开放的项目资源。','使家装团队有机会经营开渠团队未覆盖、已向家装开放的项目，扩大可接触的客户范围。','前期较少开展门店联动，关系和能力尚需建设；即使开放项目，没有经纪人联系和后续承接，也难以获得委托、形成结果。'],
])
b+=evidence('E5','E6','E3')
parts.append(section('understanding','01','收获与反思：业务为什么这样开展','先从客户需求和业务盈利两边找难点，再看当前经营动作的作用与后续问题。',b))

b='<p class="reasoning-intro">前面的经营调整，一方面需要把经纪人合作做深，另一方面需要提高客户承接与服务能力。沿着这两点，进一步拆解部门需要提供的支持，以及我能承担的工作。</p>'
b+=table(['综合来看业务需要的支持','从我方部门角度思考支持','人角度todo','预期带来的收益'],[
 ['<b>如何与经纪人建立长久紧密合作的联系</b>','建立竞赛与积分激励机制，围绕方案宣发、过程跟进、结果公示和奖励发放形成完整运营流程，让经纪人清楚规则、及时了解进度、看见参与收益。<br><br>客户经理到门店宣发激励规则，也是有效建联的方式。','1. 将激励规则转化为统一的数据计算口径，搭建激励看板，保障积分、排名和奖励计算准确、更新及时。<br><br>2. 支持进度同步与结果核对，跟踪参与和持续荐客情况，评估激励效果，为方案调整提供依据。','降低经纪人理解规则和查询进度的成本，通过透明结果与及时兑现增强参与意愿和合作信任，促进持续荐客。'],
 ['<b>如何减少“毛线索→委托→带展→草签→正签”各环节的可避免流失，提高转化效率</b>','组织沉淀客户异议、流失原因和客诉原因，将部分预警前置到交易环节。<br><br>沉淀优秀成交案例，从优秀人员怎样成交中提炼可用方法，支持一线赋能。','1. 统一各环节指标口径，跟踪同源客户的阶段转化、流转时长和流失情况，定位主要卡点。<br><br>2. 按营销中心、经营部提供看板及客户明细，支持业务排查。','帮助业务发现并挽回可避免的流失，减少跟进遗漏和协同延误，提高承接效率，促进有效委托向签约推进。'],
 ['<b>如何及时发现店、经营部的经营问题</b>','建立经营监测、问题核查、行动跟进和复盘机制，让管理者明确优先解决什么、由谁推动、如何验证。','用MOMA建设经营罗盘，集成看板、数据、指标口径和业务规则。<br><br>围绕目标进度、同批客户转化、阶段停滞和回访时效预警，并通知对应责任人。<br><br>AI结合数据证据整理待核实原因与行动建议，支持客户下钻、待办和复盘报告。','减少人工找数、对口径和整理报告的时间，提高发现与处理效率，让管理动作落实到具体客户和环节。'],
 ['<b>如何判断资源投向哪里，使获客投入与服务能力匹配</b>','综合客户机会、渠道产出和承接能力，评估重点门店、项目及激励方案的投入优先级，通过试点复盘调整。','在罗盘中整合渠道投入、有效客户、后续成交及接待、设计、交付负荷。<br><br>由AI辅助整理差异与核查线索，支持不同投入方案的情景测算，并跟踪调整后的表现。','提高资源配置针对性，减少低效投入和机会浪费，降低集中获客超过服务能力的风险。'],
 ['<b>如何提高团队各环节的沟通与转化能力，给人赋能</b>','组织销冠案例复盘与心得分享，结合真实沟通过程，沉淀需求挖掘、邀约带展、价值讲解、异议处理和签约推进方法，由业务骨干审核。<br><br>建立分享内容换取奖励的机制。','利用智能工牌录音结合心得分享，提炼“客户场景—关键问题—判断依据—有效做法—话术示例”。<br><br>建立按阶段和客户诉求分类的案例库，支持接待前学习、沟通后复盘与模拟练习。','降低优秀经验传递和新人学习成本，帮助一线理解有效做法及适用条件，提高沟通质量与服务稳定性。'],
 ['<b>如何结合客户差异提供有针对性的沟通与服务</b>','持续沉淀客户需求和画像标签，区分所处阶段、核心诉求与主要顾虑，形成差异化跟进策略。','1. 从沟通记录、业务档案提取待确认的装修时间、预算、风格、居住需求、决策人及顾虑标签。<br><br>2. 按客户阶段匹配销冠案例、提问建议、话术和产品材料，生成接待准备及下一步建议，结合人员反馈更新。<br><br>3. 根据客户情况及带展录音，由AI生成带展报告。','<b>对我方：</b>提高需求理解和服务匹配程度，更有效地回应顾虑，促进阶段推进。<br><br><b>对客户：</b>帮助确认装修意图和需求，理解方案差异及我们与竞品的差异和优势；通过报告链接回看，巩固理解。'],
], 'support-table')
b+='<p class="small">以上包含部门支持思路与岗位建设方向。毛线索至正签用于梳理业务节点，实际客户可能跨期、重复服务或走不同路径；同批转化需关联同一客户并固定观察窗口。</p>'
b+=evidence('E9','E2')
b+='<h3 class="subhead">季度重点一：基础数据建设</h3><p>围绕激励管理和客户转化，完善指标口径、数据看板及明细支持，让数据准确、及时、可核查；在日常交付中，逐步形成解释业务问题的能力。</p>'
b+=table(['工作内容','具体做什么','产出与作用'],[
 ['<b>激励数据支持</b>','将规则转成统一计算口径，明确参与范围、周期、人员归属、去重和退单处理；保障积分、排名和奖励计算准确。','计算口径、激励看板和核对明细；支持规则解释、进度同步与结果核对。'],
 ['<b>客户转化跟踪</b>','统一委托、带展、量房、签约等节点定义；跟踪同一批客户的阶段转化、流转时长和流失情况。','环节指标及客户过程明细；为查找卡点提供依据。'],
 ['<b>经营看板与明细支持</b>','按营销中心、经营部等维度提供看板和可追溯明细，支持进度查看、异常核查和具体客户跟进。','日常看板、取数和问题核查记录；减少反复找数与确认。'],
])
b+='<h3 class="subhead">激励工作：持续运维、运营支持与结算核对</h3>'
b+=schematic('incentive')
b+=table(['阶段','个人工作与协同','希望解决什么'],[
 ['<b>日常运维</b>','持续维护激励看板、计算规则和名单，检查更新及计算异常；响应业务查数、规则答疑和结果核对需求，保留问题处理记录。','让规则、榜单和明细持续可用，减少数据异常影响参与和信任。'],
 ['<b>过程运营</b>','输出阶段结果，支持参与进度同步、结果公示和答疑；结合阶段表现，协同开展社群氛围运营，持续提醒参与者关注进度和收益。','让经纪人看见参与收益，保持参与热度和合作黏性。'],
 ['<b>周期结算</b>','结算前核对计算范围、积分、排名和奖励名单，排查归属、重复、退单等差异；支持结算说明与兑现进度核对。','保障激励发放公平公正，减少核对和兑现争议。'],
 ['<b>效果复盘</b>','先确保计算准确，再看激励对象的产出、持续荐客、有效客户和后续转化，输出阶段结果，为激励与运营调整提供依据。','让优秀业务人员更有动力，推动经纪人持续合作；效果结合实际反馈验证。'],
])
b+='<h3 class="subhead">从交付数据到解释业务问题</h3><p>在看板和日常取数的基础上，逐步形成“看结果—拆变化—找环节—查对象—跟行动”的分析习惯。从具体、范围较小的问题入手，例如某个中心带展下降，或激励参与人员持续荐客不足，练习完整的分析与复盘。</p>'
b+='<div class="steps">'+''.join(f'<div><span>{i+1:02}</span><b>{a}</b><small>{c}</small></div>' for i,(a,c) in enumerate([('看结果','发现进度或指标变化'),('拆变化','拆中心、来源和人员'),('找环节','判断变化集中在哪一步'),('查对象','查客户记录，与业务核实'),('跟行动','跟踪执行与后续表现')]))+'</div>'
b+=table(['层次','希望形成的价值'],[
 ['日常交付','口径稳定、数据易核查，同类需求处理更快。'],
 ['业务判断','说明变化由什么构成、可能涉及哪些环节、还需要什么证据，缩小排查范围。'],
 ['经营改善','持续跟踪行动和结果，判断哪些做法保留、哪些调整；成交与转化改善由数分和业务共同验证。'],
])
parts.append(section('work','02','部门支持与基础数据建设','先明确部门和个人能提供的支持，再落实基础数据、日常运维和分析工作。',b))
b='<p>经营罗盘目前设计了6个主模块，其中“经营诊断”包含3个子模块，并提供贯穿各模块的分析报告功能。使用过程是：先看经营重点 → 查看问题依据 → 核查原因 → 安排行动 → 跟踪执行 → 复盘结果。</p>'
b+='<h3 class="subhead">主模块：做什么、为什么这样设计</h3>'
b+=table(['模块','功能','设计思路与预期收益'],[
 ['今日重点','汇总目标进度、核心业务量、需要关注的问题及进行中事项。','帮助经营者先明确关注重点。'],
 ['经营诊断','查看目标达成、业务量与转化、阶段时效；点击指标查看原值、公式、参考标准、数据缺口、待核实原因和下一步建议。','不仅展示红黄绿，还要解释为什么提示、还缺什么证据。'],
 ['行动台账','记录对象、负责人、具体动作、期限、执行证据、受阻情况、验收及后续观察。','让问题能落实到人和具体事项，并跟踪执行。'],
 ['数据协同','记录缺数、口径、范围和归属问题，安排核查与反馈。','减少因数据问题造成的反复确认和误判。'],
 ['数据来源／AI接口','管理数据来源、字段、期间、口径和导入导出。','让指标和分析有来源，便于核对及后续接入。'],
 ['使用说明','说明操作流程、数据状态和使用限制。','让使用者理解功能与数据的适用范围。'],
])
b+='<h3 class="subhead">经营诊断：重点分析哪三类问题</h3>'
b+=table(['子模块','要回答的问题','分析思路'],[
 ['目标进度','当前进度与计划差多少，接下来需要关注什么？','结合目标、实际完成和时间进度判断；计划线需说明依据。'],
 ['业务量与转化','哪些环节的量发生变化，有效客户是否继续推进？','先看阶段业务量，再用同一批客户的过程记录分析转化；同期数量比不代替同批转化。'],
 ['阶段时效','客户在哪一步等待，跟进和交接是否及时？','区分已完成客户的流转时长与仍在等待的客户，结合具体对象核查。'],
])
b+='<h3 class="subhead">报告与AI：把分析连接到行动</h3><p>希望AI能帮助负责人看清：哪些数据有变化、涉及哪些客户、应该先查什么。负责人查清情况后，再决定由谁跟进、怎么处理。后续把处理过程和客户进展记下来，复盘时就能看到做了什么、有没有改善。</p>'
b+=schematic('ai-granularity')
b+='<h3 class="subhead">当前进展与卡点</h3>'
b+=table(['方面','目前情况','接下来需要解决什么'],[
 ['<b>已有进展</b>','已有产品方案、HTML交互原型及数据映射、构建交接材料，已形成从查看问题到行动、复盘的产品思路。','按实际接入和使用情况确认完成度，原型演示与正式可用分开说明。'],
 ['<b>需求粒度：指标视角与经营者盘客需求有差距</b>','原方案主要从数分角度组织指标、阈值和经营诊断；经营者还需要知道具体是哪位客户、由谁跟进、卡在哪里、最近沟通了什么、下一步如何安排。','结合经营者逐单盘客的方式，重新梳理页面和客户明细；让汇总指标能下钻到具体客户与跟进事项。'],
 ['<b>数据支撑：汇总数据还不能直接变成客户待办</b>','现有看板和来源映射提供了基础，但客户、交易、订单、负责人及过程记录的关联还需核实。正式取数、日期筛选和同批转化等能力需要按实际结果验证。','明确每项判断所需字段、统计范围和来源；缺失项保留缺口，不用汇总量推造客户名单。'],
 ['<b>判断与行动：能提示异常，还需要知道如何核查</b>','只有指标偏低或时长偏长，不能直接判断客户流失原因；预警要能指向对象和待核实问题。','结合实际业务记录完善规则，保留“依据—核查—动作—反馈”，再判断建议是否有用。'],
])
b+='<h3 class="subhead">季度重点二：AI应用建设</h3>'
b+=table(['改进重点','围绕当前卡点开展的工作','产出'],[
 ['经营者实际使用需求','结合逐单盘客场景，确认角色需要看什么、查什么、如何安排跟进；对比现有方案的粒度差距。','需求差异清单、页面与客户明细调整方案。'],
 ['数据与功能衔接','梳理客户关联、过程字段、指标口径和规则来源，逐项核对现有能力与缺口。','数据需求及映射说明、功能状态与问题清单。'],
 ['核心过程验证','围绕“查看问题—核查客户—安排行动—跟踪复盘”验证可用性，收集使用反馈后调整。','可操作版本、核查与使用反馈、后续迭代清单。'],
])
parts.append(section('ai','03','AI应用进展及案例','围绕现有经营罗盘，保留产品思路、实际进展和当前卡点，再明确下一步建设。',b))
b='<p class="planning-note">Q4围绕“基础数据建设”和“AI应用建设”两部分推进。激励、客户转化和看板运维同属基础数据建设；AI从当前使用需求与数据卡点出发完善。</p>'
b+=schematic('priorities')
b+=table(['目标 O','关键结果 KR','验收依据'],[
 ['<b>O1 完善基础数据建设，让日常交付准确、及时、可核查，并逐步支持业务分析</b>','<b>KR1 数据交付：</b>完善负责范围内的激励、客户转化及经营看板口径，提供可追溯明细，记录版本及范围变化。<br><br><b>KR2 激励运维与运营支持：</b>按约定节奏维护看板和名单，支持阶段结果同步、答疑、社群氛围运营；结算前完成数据核对，跟踪差异处理及兑现进度。<br><br><b>KR3 分析与复盘：</b>围绕具体业务问题，形成“变化拆解—环节定位—对象核查—行动跟踪”的分析记录；跟踪激励对象产出、持续荐客、有效客户及后续转化。','口径说明、看板和明细；运维及答疑记录；阶段结果、结算核对和差异处理记录；业务分析与行动复盘。'],
 ['<b>O2 完善经营罗盘，使指标诊断更贴合经营者的客户跟进与管理需求</b>','<b>KR1 需求对齐：</b>梳理经营者逐单盘客的使用流程，明确现有指标视角与实际使用需求的差距，形成调整方案。<br><br><b>KR2 数据与能力核查：</b>明确核心场景的客户关联、字段、来源和口径，记录已具备、待补及受阻项，不把原型能力视为正式接入。<br><br><b>KR3 核心过程验证：</b>围绕问题查看、客户核查、行动安排和复盘验证可用性，记录反馈及改进结果，形成后续迭代清单。','角色与场景需求、原型调整；数据和功能核查记录；可操作版本、使用反馈及迭代清单。'],
])
b+='<h3 class="subhead">10—12月工作安排</h3>'
b+=table(['重点','10月：梳理与对齐','11月：持续支持与完善','12月：复盘与沉淀'],[
 ['<b>基础数据建设</b>','梳理激励规则、客户节点和看板口径；持续做好看板运维、阶段结果同步和核对支持，整理常见问题。','持续维护与答疑，支持社群运营；跟踪荐客、有效客户和后续转化，从具体业务问题开展分析。','按激励实际周期支持结算前核对及兑现跟踪；复盘参与和客户推进，沉淀口径、运维步骤及分析方法。'],
 ['<b>AI应用建设</b>','对比现有产品方案与经营者逐单盘客需求，梳理客户字段、关联和现有能力缺口。','根据核查结果完善页面、数据和规则衔接，验证核心使用流程，记录受阻项与反馈。','复盘可用功能和使用反馈，区分已完成与未解决问题，确定后续迭代重点。'],
])
b+='<h3 class="subhead">持续沉淀的机制</h3>'
b+=table(['机制','怎么运行','价值'],[
 ['数据交付与运维','口径、来源、版本和更新问题留痕；日常查数、答疑与异常处理持续跟进。','提高日常交付稳定性，减少重复核对。'],
 ['激励过程与结算','规则宣发、阶段结果、社群运营、结算核对和兑现跟踪按分工协作。','让参与者看清规则和收益，维护公平与合作信任。'],
 ['分析、行动与复盘','围绕具体问题核查客户、确认动作、记录反馈和结果，再调整判断或做法。','让分析能服务实际跟进，并持续积累有效方法。'],
])
b+='<div class="value-grid"><article><span>公司价值</span><h3>支持有效获客与客户承接</h3><p>提供可靠依据，帮助业务减少可避免的遗漏；经营增量结合行动与结果验证。</p></article><article><span>组织价值</span><h3>稳定交付，沉淀方法</h3><p>减少重复核对，维护激励公正，积累可复用的口径、运维与分析方法。</p></article><article><span>个人价值</span><h3>从交付数据到解释问题</h3><p>在日常支持和产品建设中，提升业务理解、问题拆解、分析与结果跟踪能力。</p></article></div>'
parts.append(section('plan','04','Q4 OKR与工作安排','对应基础数据建设与AI应用建设，明确工作、产出和复盘安排。',b))
css='''
:root{--ink:#142c48;--muted:#607189;--blue:#175dcc;--teal:#168a81;--line:#dce5f0;--paper:#fff;--bg:#f3f6fa;--light:#eaf1fc;--gold:#ad6b22}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:90px}body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;font-size:15px;line-height:1.8}button,a,summary{-webkit-tap-highlight-color:transparent}button,summary{cursor:pointer}button{font:inherit}.top{background:#102e51;color:#fff;padding:36px max(28px,calc((100vw - 1220px)/2)) 30px;border-bottom:4px solid #5593e6}.topline{display:flex;justify-content:space-between;gap:20px;align-items:center;font-size:12px;color:#c4d7ed;letter-spacing:1px}.top h1{font-size:36px;line-height:1.3;margin:22px 0 10px;font-weight:750;letter-spacing:1px}.top p{margin:0;color:#d1deed;font-size:16px}.hero-meta{display:flex;gap:12px;margin-top:21px;flex-wrap:wrap}.hero-meta span{font-size:12px;border:1px solid #53708e;padding:3px 11px;border-radius:4px}.sticky{position:sticky;top:0;background:rgba(255,255,255,.97);backdrop-filter:blur(10px);z-index:10;border-bottom:1px solid var(--line)}.nav{max-width:1276px;margin:auto;display:flex;gap:22px;align-items:center;padding:12px 28px}.nav a{font-size:13px;white-space:nowrap;color:var(--muted);text-decoration:none;padding:3px 0}.nav a.active{color:var(--blue);box-shadow:0 2px var(--blue)}.nav-tools{margin-left:auto;display:flex;gap:8px;white-space:nowrap}.nav-tools button{background:#fff;border:1px solid var(--line);border-radius:5px;padding:4px 10px;color:var(--ink);font-size:12px}.nav-tools button:hover{border-color:var(--blue)}main{max-width:1276px;margin:auto;padding:0 28px 60px}.section{margin-top:32px;padding:30px;background:var(--paper);border:1px solid var(--line);border-radius:10px;box-shadow:0 5px 20px #12385d04}.section-head{display:flex;gap:16px;margin-bottom:23px;align-items:flex-start}.section-num{background:var(--light);color:var(--blue);font-size:14px;font-weight:700;min-width:42px;height:42px;display:grid;place-items:center;border-radius:7px}.section h2{font-size:24px;line-height:1.4;margin:1px 0 6px}.lead{margin:0;color:var(--muted);font-size:14px}.perspectives{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:24px}.perspectives article{border-left:3px solid var(--blue);padding:8px 20px;background:#f8faff}.eyebrow{font-size:12px;color:var(--blue);font-weight:700;letter-spacing:1px}h3{font-size:17px;line-height:1.6;margin:8px 0}p{margin:8px 0}.perspectives p{color:var(--muted);font-size:14px}.table-wrap{width:100%;overflow:auto;border:1px solid var(--line);border-radius:6px}table{border-collapse:collapse;width:100%;text-align:left;font-size:14px}th{background:#edf3fb;font-weight:650;color:#234b77;font-size:13px;white-space:normal}td,th{padding:14px 16px;vertical-align:top;border-bottom:1px solid var(--line);border-right:1px solid #e6edf5}td:first-child{font-weight:600;min-width:135px}td{min-width:150px}th:last-child,td:last-child{border-right:0}tr:last-child td{border-bottom:0}tbody tr:nth-child(even){background:#fbfcfe}.note{border-left:3px solid #d8a54a;background:#fffbf3;padding:12px 16px;margin:18px 0;color:#685331;font-size:13px}.subhead{margin:25px 0 12px;font-size:18px}.evidence-group{margin-top:16px}.evidence{border:1px solid #dfe7f0;border-radius:6px;margin-top:8px;background:#fafcff}.evidence>summary{display:flex;gap:12px;align-items:center;list-style:none;padding:12px 15px;font-size:13px}.evidence>summary::-webkit-details-marker{display:none}.source-tag{font-size:11px;color:#4b7199;border:1px solid #cfdfef;background:#edf4fb;white-space:nowrap;padding:1px 7px;border-radius:3px}.chevron{margin-left:auto;color:var(--blue);font-weight:bold;font-size:17px}.evidence[open] .chevron{transform:rotate(45deg)}.evidence-body{padding:0 18px 18px;border-top:1px dashed #dfe7f0;font-size:14px}.evidence-body>p:first-child{margin-top:15px}.evidence-body .table-wrap{margin-top:15px}.source-note{font-size:12px;color:var(--muted);margin:14px 0 0}.original{margin-top:12px}.original summary{color:var(--blue);font-size:12px}.original img{max-width:100%;height:auto;display:block;margin:12px auto;background:#fff;border:1px solid var(--line)}.data-intro{display:grid;grid-template-columns:1.2fr 1fr;gap:30px;padding:22px;background:#f5f9ff;border-radius:8px}.data-intro p{font-size:14px}.metric-pair{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:20px}.metric-pair>div{border-left:1px solid #d6e2f0;padding-left:22px}.metric-pair b{font-size:39px;display:block;line-height:1.3;color:var(--blue)}.metric-pair b span{font-size:20px}.metric-pair small{font-size:12px;color:var(--muted)}.small{font-size:12px!important;color:var(--muted)}.chart-grid{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin:22px 0}figure{margin:0;border:1px solid var(--line);padding:18px 20px;border-radius:7px}figcaption{font-size:15px;font-weight:650;margin-bottom:15px}.bar-label{display:flex;justify-content:space-between;gap:15px;font-size:12px;margin:10px 0 4px}.bar{height:12px;background:#edf2f7;border-radius:3px;overflow:hidden}.bar i{display:block;height:100%;background:var(--blue)}.bar.accent i{background:var(--teal)}.stack{height:36px;display:flex;border-radius:4px;overflow:hidden;margin-top:25px}.stack i:nth-child(1){background:#bccbdc}.stack i:nth-child(2){background:#80a9e2}.stack i:nth-child(3){background:#175dcc}.legend{display:flex;gap:16px;flex-wrap:wrap;margin-top:8px;font-size:12px;color:var(--muted)}.steps{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}.steps>div{padding:14px;background:#f2f6fc;border-radius:5px}.steps span{font-size:12px;color:#7294bc;display:block}.steps b{display:block;margin:2px 0}.steps small{font-size:12px;color:var(--muted)}.ai-banner{padding:17px 20px;background:#f0f7f6;border:1px solid #d6e7e3;margin-bottom:20px;border-radius:6px}.ai-banner p{font-size:14px;margin:10px 0 0}.pill{display:inline-block;background:#dcf0e9;color:#1c7065;font-size:12px;padding:3px 9px;border-radius:4px;margin-right:8px}.pill.pending{background:#f8ecd5;color:#8b6328}.workflow{display:flex;gap:12px;align-items:center;justify-content:space-between;margin:20px 0;flex-wrap:wrap}.workflow span{background:#edf3fb;padding:7px 13px;border-radius:4px;font-size:13px}.workflow b{color:#8aa2be}.planning-note{font-size:13px;color:var(--muted);margin-top:-4px}.value-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:24px}.value-grid article{border-top:3px solid #81a8db;padding:14px;background:#f8faff}.value-grid span{font-size:12px;color:var(--blue)}.value-grid p{font-size:13px;color:var(--muted)}footer{font-size:12px;color:var(--muted);padding:24px 2px 0}.key{color:var(--blue)}a{color:var(--blue)}:focus-visible{outline:3px solid #ffbd47;outline-offset:4px}.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);padding:10px 18px;background:#102e51;color:#fff;border-radius:6px;z-index:30;font-size:13px;display:none}
@media(max-width:850px){.top{padding:28px 20px}.top h1{font-size:28px}.topline{letter-spacing:0}.nav{gap:16px;overflow-x:auto;padding:10px 16px}.nav-tools{gap:5px}main{padding:0 12px 40px}.section{padding:20px 16px;margin-top:18px}.section h2{font-size:20px}.perspectives,.data-intro,.chart-grid{grid-template-columns:1fr}.steps{grid-template-columns:repeat(2,1fr)}.value-grid{grid-template-columns:1fr}.metric-pair{padding:8px 0}.evidence>summary{flex-wrap:wrap;gap:6px}.evidence>summary>span:nth-child(2){flex:1;min-width:150px}.section-head{gap:10px}.section-num{min-width:34px;height:34px}.nav-tools button{padding:3px 7px}.table-wrap table{min-width:620px}.support-table table{min-width:1120px}}
@media print{@page{size:A4 landscape;margin:12mm}html{scroll-padding:0}body{background:#fff;font-size:11px;line-height:1.6;-webkit-print-color-adjust:exact;print-color-adjust:exact}.top{padding:16px 20px}.top h1{font-size:25px;margin:12px 0}.sticky,.toast{display:none}main{max-width:none;padding:0}.section{border:0;box-shadow:none;padding:18px 0;margin:0;break-before:page}.section:first-child{break-before:auto}.section h2{font-size:20px}.section-head{margin-bottom:12px}table{font-size:11px}td,th{padding:8px;min-width:0!important}th{font-size:11px}tr{break-inside:avoid}thead{display:table-header-group}.table-wrap{overflow:visible}.evidence:not([open]){display:none}.original{display:none}.steps>div{padding:9px}.value-grid{gap:12px}.data-intro{padding:14px}.chart-grid{gap:12px}.note,.evidence>summary,.perspectives{break-inside:avoid}.topline{font-size:10px}.hero-meta{margin-top:10px}}
'''

nav=[('understanding','业务思考'),('work','基础数据建设'),('ai','AI进展'),('plan','OKR与安排')]
script='''const allDetails=()=>[...document.querySelectorAll('details.evidence')];document.querySelector('#expand').addEventListener('click',()=>{allDetails().forEach(d=>d.open=true);show('已展开全部事实依据');});document.querySelector('#collapse').addEventListener('click',()=>{document.querySelectorAll('details').forEach(d=>d.open=false);show('已收起全部事实依据');});document.querySelector('#print').addEventListener('click',()=>window.print());function show(t){const e=document.querySelector('#toast');e.textContent=t;e.style.display='block';clearTimeout(window.toastTimer);window.toastTimer=setTimeout(()=>e.style.display='none',2200)}const observer=new IntersectionObserver(entries=>{for(const en of entries)if(en.isIntersecting){document.querySelectorAll('.nav a').forEach(a=>a.classList.toggle('active',a.hash==='#'+en.target.id));}},{rootMargin:'-15% 0px -65% 0px'});document.querySelectorAll('section').forEach(s=>observer.observe(s));'''
css+='\n.thinking-table th:first-child{width:9%}.thinking-table th:nth-child(2){width:47%}.thinking-table th:nth-child(3){width:44%}.thinking-table td:first-child{min-width:80px}.thinking-table td:not(:first-child){font-weight:400}.reasoning-intro{margin:0 0 18px;font-size:14px;color:var(--muted)}.evidence-body figure{margin-top:16px}\n.support-table th:nth-child(1){width:17%}.support-table th:nth-child(2){width:27%}.support-table th:nth-child(3){width:33%}.support-table th:nth-child(4){width:23%}.first-sub{margin-top:0}.reasoning{background:#f5f8fd;padding:14px 20px;border-left:3px solid #175dcc}.reasoning p{font-size:14px;margin:12px 0}.center-row{display:grid;grid-template-columns:105px 1fr 90px;gap:14px;align-items:center;margin:12px 0}.center-row>b{font-size:13px}.center-row>span{font-size:12px;color:#607189;text-align:right}.center-row .bar{height:9px;margin:5px 0}.metric-pair b{font-size:29px}@media(max-width:600px){.center-row{grid-template-columns:75px 1fr 70px;gap:8px}.metric-pair b{font-size:24px}}'
css+='''.schematic{margin:22px 0 28px;padding:20px;background:linear-gradient(135deg,#f8fbff,#fff);border:1px solid #cdddee;border-radius:12px;overflow:hidden}.schematic figcaption{display:flex;align-items:center;gap:12px;font-size:17px;line-height:1.5;margin:0 0 15px}.schematic figcaption span{font-size:11px;font-weight:600;letter-spacing:1px;color:#416b96;background:#eaf2fc;border:1px solid #cfdfef;border-radius:4px;padding:3px 8px;white-space:nowrap}.schematic-canvas{overflow-x:auto}.schematic svg{display:block;width:100%;height:auto}.schematic svg text{font-kerning:normal}@media(max-width:850px){.schematic{padding:14px 10px}.schematic figcaption{align-items:flex-start;font-size:15px;gap:8px}.schematic svg{min-width:820px}}@media print{.schematic{background:#fff;padding:10px;break-inside:avoid;page-break-inside:avoid}.schematic svg{min-width:0}.schematic figcaption{font-size:13px}.schematic-canvas{overflow:visible}}'''
page='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>薛晴 · 2026 Q4工作规划</title><meta name="description" content="整装业务理解、事实参考、AI应用进展与Q4工作安排"><style>'+css+'</style></head><body><header class="top"><div class="topline"><span>整装业务 · 数据分析</span><span>薛晴 / 2026年第四季度</span></div><h1>Q4工作规划</h1><p>业务思考、基础数据建设与AI应用建设。</p><div class="hero-meta"><span>收获与反思</span><span>经营罗盘</span><span>OKR与月度安排</span><span>2026.10.16 · 修订版</span></div></header><div class="sticky"><nav class="nav" aria-label="章节导航">'+''.join(f'<a href="#{id}">{title}</a>' for id,title in nav)+'<div class="nav-tools"><button id="expand">展开依据</button><button id="collapse">收起依据</button><button id="print">打印 / PDF</button></div></nav></div><main>'+''.join(parts)+'<footer><b>阅读说明</b>　参考依据默认收起，可逐项或全部展开。数据表、图表及事实解读均可折叠，保留来源与统计说明。<br>9月经营数据采用放开目标单限制的新口径；1—9月历史数据独立说明范围。</footer></main><div id="toast" class="toast" role="status" aria-live="polite"></div><script>'+script+'</script></body></html>'
out=ROOT/'index.html';out.write_text(page,encoding='utf-8')
print(json.dumps({'html':str(out),'bytes':out.stat().st_size},ensure_ascii=False))
