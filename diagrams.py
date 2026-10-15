# -*- coding: utf-8 -*-
from html import escape
from pathlib import Path

FONT='-apple-system, BlinkMacSystemFont, PingFang SC, Microsoft YaHei, sans-serif'

def text(x,y,content,size=18,color='#173650',weight=400,anchor='start'):
 return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(content)}</text>'
def box(x,y,w,h,title,lines=(),tone='blue',center=False):
 colors={'blue':('#edf4ff','#a9c5eb','#1555a1'),'teal':('#edf8f4','#a4d5c8','#1b7162'),'gold':('#fff8ec','#e6cca2','#906223'),'white':('#ffffff','#d5e1ee','#173650')}
 bg,stroke,ink=colors[tone]
 out=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{bg}" stroke="{stroke}"/>'
 tx=x+w/2 if center else x+22;anchor='middle' if center else 'start'
 out+=text(tx,y+33,title,20,ink,650,anchor)
 for i,line in enumerate(lines):out+=text(tx,y+61+i*25,line,16,'#506a80',400,anchor)
 return out

def arrow(key,path):
 return f'<path d="{path}" fill="none" stroke="#849eb6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#{key}-arrow)"/>'
def svg(key,height,body,title,desc):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 {height}" role="img" aria-labelledby="{key}-title {key}-desc"><title id="{key}-title">{escape(title)}</title><desc id="{key}-desc">{escape(desc)}</desc><defs><marker id="{key}-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M1 1 L7 4.5 L1 8" fill="none" stroke="#849eb6" stroke-width="1.5"/></marker></defs>{body}</svg>'

DIAGRAMS={}
k='reasoning'
b=box(30,15,510,100,'客户要什么',('适配自家的方案，清楚的预算与保障','装修交付符合预期'),tone='blue')
b+=box(580,15,510,100,'业务要什么',('找准合适客户，把服务能力转成有效订单','完成交付，积累口碑'),tone='teal')
b+=arrow(k,'M285 115 V140 H560 V160')+arrow(k,'M835 115 V140 H560')
b+=box(230,164,660,85,'先找难点',('意图和需求难确认；推荐竞争、承接与多人交接有约束',),tone='white',center=True)
b+=arrow(k,'M560 249 V280')
b+=box(30,284,1060,85,'再看当前动作解决了什么，还留下什么问题',('签约中心＋展厅　／　门店建联与激励　／　拓展适配客户与项目',),tone='gold',center=True)
b+=arrow(k,'M560 369 V397 H145 V418')
nodes=[('部门支持','业务需要哪些支持'),('人角度todo','个人能做什么'),('两项季度重点','基础数据＋AI应用'),('OKR与安排','明确工作和产出')]
for i,(a,c) in enumerate(nodes):
 x=30+i*280;b+=box(x,422,220,86,a,(c,),tone='white',center=True)
 if i<3:b+=arrow(k,f'M{x+220} 465 H{x+272}')
DIAGRAMS[k]=('从业务思考到季度工作的推导过程',svg(k,530,b,'从业务思考到季度工作','客户需求与业务盈利两方面的难点，推导经营动作、部门支持、个人todo、两项季度重点及OKR。'))

k='incentive'
b=''
data=[('01','规则口径','范围、积分与奖励','先把规则算清楚'),('02','日常运维','更新、异常与答疑','让数据持续可用'),('03','过程运营','同步、公示与社群','让参与者看见收益'),('04','结算核对','名单、差异与兑现','维护公平与信任'),('05','效果复盘','荐客、有效客户、转化','为调整提供依据')]
for i,(n,a,c,d) in enumerate(data):
 x=18+i*222
 b+=box(x,34,196,123,a,(c,d),tone='teal' if i==2 else 'blue',center=True)
 b+=text(x+12,22,n,12,'#7994af',650)
 if i<4:b+=arrow(k,f'M{x+196} 95 H{x+214}')
b+=arrow(k,'M1004 158 V206 H116 V166')
b+=text(560,235,'日常运维贯穿全过程；复盘结果用于调整规则与运营',17,'#506a80',400,'middle')
DIAGRAMS[k]=('激励支持是一项持续运转的工作',svg(k,260,b,'激励支持全过程','规则口径、日常运维、过程运营、结算核对和效果复盘形成持续反馈，运维贯穿全过程。'))

k='ai-granularity'
b=box(25,20,300,190,'原方案：从指标发现问题',('目标进度','业务量与同批转化','阶段时效','知道哪里值得进一步核查'),tone='blue')
b+=arrow(k,'M325 115 H389')
b+=box(399,20,310,190,'需要补上的一层',('关联客户、交易、订单与人员','补齐阶段、最近沟通与约定','核实数据来源与统计口径','把指标连接到具体跟进对象'),tone='gold')
b+=arrow(k,'M709 115 H773')
b+=box(783,20,312,190,'经营者：围绕具体客户安排',('是哪位客户？由谁跟进？','卡在哪里？最近聊了什么？','下一步做什么、何时推进？','执行后，客户进展怎样？'),tone='teal')
b+=text(560,253,'当前卡点：指标诊断与实际盘客所需的信息粒度还有差距',19,'#173650',650,'middle')
b+=f'<rect x="25" y="277" width="1070" height="61" rx="10" fill="#f4f7fb"/>'
b+=text(560,315,'对齐使用需求　→　补齐数据与明细　→　验证核心流程　→　根据反馈调整',18,'#506a80',400,'middle')
DIAGRAMS[k]=('AI要补齐从指标诊断到具体客户跟进的过程',svg(k,360,b,'AI当前需求粒度卡点','原方案的指标诊断，需要补齐客户关联、过程字段与口径，才能满足经营者逐单盘客和安排行动的需求。该图表示建设思路。'))

k='priorities'
b=box(25,20,1070,127,'季度重点一：基础数据建设',(),tone='blue')
b+=text(49,89,'激励支持与持续运维',18,'#1555a1',600)
b+=text(398,89,'客户转化跟踪',18,'#1555a1',600)
b+=text(731,89,'经营看板与明细支持',18,'#1555a1',600)
b+=text(49,119,'规则、更新、运营、核对',16,'#506a80')
b+=text(398,119,'同批客户、环节与时效',16,'#506a80')
b+=text(731,119,'准确、及时、可核查',16,'#506a80')
b+=arrow(k,'M560 147 V194')
b+=text(585,178,'提供口径、明细和待核查的业务问题',15,'#506a80')
b+=box(25,204,1070,127,'季度重点二：AI应用建设',(),tone='teal')
b+=text(49,273,'对齐经营者使用需求',18,'#1b7162',600)
b+=text(398,273,'核查数据与功能缺口',18,'#1b7162',600)
b+=text(731,273,'验证核心过程与反馈',18,'#1b7162',600)
b+=text(49,303,'从汇总指标到逐单盘客',16,'#506a80')
b+=text(398,303,'已有、待补、受阻分别记录',16,'#506a80')
b+=text(731,303,'发现、核查、行动、复盘',16,'#506a80')
DIAGRAMS[k]=('两项季度重点如何衔接',svg(k,351,b,'两项季度重点','基础数据建设包含激励支持、客户转化和经营看板；AI应用在此基础上对齐经营者需求、核查缺口并验证核心过程。'))

def schematic(key):
 title,image=DIAGRAMS[key]
 return f'<figure class="schematic" data-schematic="{key}"><figcaption><span>思路示意</span>{title}</figcaption><div class="schematic-canvas">{image}</div></figure>'

if __name__=='__main__':
 folder=Path(__file__).parent/'diagrams';folder.mkdir(exist_ok=True)
 for key,(_,image) in DIAGRAMS.items():(folder/(key+'.svg')).write_text(image)
 print('Exported 4 standalone SVG diagrams.')
