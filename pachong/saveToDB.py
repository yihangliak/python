#coding=utf-8
import pymysql

db = pymysql.connect(host='localhost', user='root', password='wo@NI123',
                     port=3306, db='alex')
cursor = db.cursor()
# create_table = 'CREATE TABLE IF NOT EXISTS zhihu(question VARCHAR(255) NOT NULL, author VARCHAR (255) NOT NULL, age VARCHAR (500) NOT NULL, PRIMARY KEY (question))'
# cursor.execute(create_table)


data = {'question': '如何评价第四届汉唐杯大陆健力纪录赛？',
        'author': '王衡爱健身',
        'answer': '谢毛神 @毛晨雨 邀请。这是我第四次参加大陆健力记录赛了，加上大陆健力记录赛的前身比赛，我总共参与了六届比赛，还是有点发言权的。我是亲眼看着比赛一届一届越来越好，越来越正规的，虽然每届比赛进步升级的地方不多，但每一届都有进步，就是这些持续不断的小进步最终带来了赛事规模和赛事体验的大突破。尤其是今年的药检流程，真的是国内力量举赛事的一次重大突破。\n今年在比赛器械方面，也进步了不少，使用的比赛架子和杠铃片都是毛神 @毛晨雨 自主研发的器械品牌「汉龙体育」生产的。（因为是毛神做的杠铃片，简称「毛片」！）下图是汉龙体育生产的专业级力量举钢片，设计非常赏心悦目，使用起来感觉也相当好，比赛亲测！我相信每个力量举爱好者的梦想之一就是能用专业级的钢片训练。如果各位老板想采购这些专业的力量训练设备，可以和毛神 @毛晨雨 联系。每届比赛都有新人进来，也有很多老人离去，但不得不承认，大陆健力赛确实启蒙和带出了一些明星力量举选手。对于我个人而言，每年的比赛更是检验自己训练水平是否进步的最好证明，有一个比赛目标的话，训练会更有规划，也更容易进步。如果你想对自己的训练水平有一个真实的了解，想检验下自己的训练计划是否合理，不妨准备个比赛试试，我相信比完赛回来你会对力量举有一个更深刻的认识。晚上和唐哥一起吃饭的时候，唐哥也说，国内力量举圈这几年沧海桑田，和以前真是大不一样了，进步非常大，我混圈子时间也不短了，对这番话也是深有感触。酒过三巡，讲到兴起，唐哥直接现场示范，讲解起动作细节。对力量举这事儿的激情真不是我们年轻人能比的。最后简单介绍下我这次的比赛情况。这届比赛依然参加的105kg级，体重依然是102kg，区别是去年赛前基本不敢吃东西，称重称了个102，今年是赛前胡吃海塞，最后“撑”了个102 （我其实就想说我瘦了点！莱维！）。最终的比赛成绩只比我平时训练成绩低了2.5kg，个人还是非常满意的，训练水平基本都发挥出来了。\n深蹲定格第二把190kg（训练最好成绩），第三把要了195kg，被压了个瓷实。\n第二把190kg视频\nhttps://www.zhihu.com/video/971792198169280512\n卧推定格第二把117.5kg，本来的策略是第一把110kg，第二把115kg，第三把120kg的，后来杨老师观察到我110kg秒起，建议我第二把要117.5kg，同样起的没啥黏滞，于是第三把直接建议我加到125kg，试一下。可惜的是，125kg平衡没了，最终还是压了个瓷实，我平时训练卧推最好成绩是120kg，但底部停顿时间应该不够。\n卧推第二把117.5kg视频\nhttps://www.zhihu.com/video/971792944735449088\n卧推第三把125kg失败视频\nhttps://www.zhihu.com/video/971793029854572544\n硬拉同样定格第二把210kg，第三把要了215kg，可惜最后伸髋没锁住。\n硬拉第二把210kg视频\nhttps://www.zhihu.com/video/971793482968506368\n硬拉第三把215kg失败视频\nhttps://www.zhihu.com/video/971793550850088960\n最终我的成绩是\n深蹲190kg，比去年10月提高5kg\n卧推117.5kg，比去年10月提高7.5kg\n硬拉210kg，比去年提高5kg\n总成绩517.5kg，比去年提高17.5kg\n这说明我这半年也算没白练……\n今年下半年的训练目标是降重比93kg级别，同时试着提高成绩，希望能上540+。\n最后，祝比赛越办越好！\n时光不老，我们不散！'

}
table = 'zhihu'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
insert_sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
cursor.execute(insert_sql, tuple(data.values()))
print('ok')
db.commit()
# except:
#     print('faild')
#     db.rollback()
db.close()