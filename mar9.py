m = lambda n: ['/'.join([str(j) for j in i]) for i in ([list(i) for i in (list(zip([i for i in range(1, n + 1)], [j for j in range(2, n + 2)])))])]

print(m(5))
# ans = [i for i in range(1, n + 1)]
    # ans2 = [j for j in range(2, n + 2)]
    # lol = [list(i) for i in (list(zip(ans, ans2)))]

xd = lambda w: w.split()
print(xd('''步步莲花 碧海青天 白华之怨 冰肌玉骨
败柳残花 冰清玉洁 闭月羞花 楚楚可怜
初发芙蓉 风信年华 粉妆玉琢 国色天香 国色天姿
姑射神人 瓜字初分 皓齿蛾眉 皓齿明眸 诲盗诲淫
红粉青楼 环肥燕瘦 回眸一笑 花容月貌 蕙心兰质
红颜薄命 诲淫诲盗 花颜月貌 巾帼奇才 巾帼须眉
巾帼英雄 巾帼丈夫 惊鸿艳影 及笄年华 嫁鸡随鸡，嫁狗随狗
静如处女，动如脱兔 佳人才子 绝世独立 举止娴雅 旷夫怨女
郎才女貌 罗敷有夫 梨花带雨 路柳墙花 柳絮才高
林下风范 林下风气 怜香惜玉 绿叶成阴 明眸皓齿
明眸善睐 女大十八变 男尊女卑 破瓜之年 飘茵落溷
搔头弄姿 守如处女，出如脱兔 闲花野草 小家碧玉 萧郎陌路
心灵手巧 杏脸桃腮 香消玉殒 惜玉怜香 仙姿玉貌
野草闲花 莺俦燕侣 压良为贱 逾墙钻隙 遇人不淑
冶容诲淫 嫣然一笑 艳如桃李，冷若冰霜 燕瘦环肥 莺声燕语
尤物移人 瘗玉埋香 燕语莺声 秋风团扇 千娇百媚
螓首蛾眉 如花似玉 人老珠黄 软玉温香 扫眉才子
搔头弄姿 守如处女，出如脱兔 上烝下报 天生尤物 投梭折齿
亭亭玉立 天香国色 雾鬓风鬟 雾鬓云鬟 文君新醮
我见犹怜 闲花野草 小家碧玉 萧郎陌路 心灵手巧
杏脸桃腮 香消玉殒 惜玉怜香 仙姿玉貌 野草闲花
莺俦燕侣 压良为贱 逾墙钻隙 遇人不淑 冶容诲淫
嫣然一笑 艳如桃李，冷若冰霜 燕瘦环肥 莺声燕语 尤物移人
瘗玉埋香 燕语莺声 瘗玉埋香 燕语莺声 妍姿艳质
姑射神人 花容月貌 绝世独立 郎才女貌 面如傅粉
面如冠玉 袅袅娉娉 袅袅婷婷 柔枝嫩条 柔枝嫩叶
色衰爱弛 香消玉碎 香消玉损 秀色可餐 夭桃秾李
夭桃穠李 一顾倾城 倚姣作媚 玉碎香残 月貌花容
阿娇金屋 闭月羞花 彩云易散 姹紫嫣红 沉鱼落雁
逞娇呈美 春暖花香 春色满园 春深似海 斗美夸丽
斗艳争辉 蛾眉皓齿 飞阁流丹 国色天香 皓齿蛾眉
皓齿明眸 红颜薄命 胡天胡帝 花颜月貌 金屋娇娘
金屋贮娇 尽态极妍 绝色佳人 姱容修态 兰质蕙心
离魂倩女 落雁沉鱼 落英缤纷 靡颜腻理 明眸皓齿
女貌郎才 琪花瑶草 螓首蛾眉 清词丽句 清辞丽句
清辞丽曲 曲眉丰颊 爽心悦目 水木清华 天生丽质
天香国色 宛转蛾眉 我见犹怜 霞光万道 涎玉沫珠
香消玉殒 小家碧玉 杏脸桃腮 杏腮桃脸 杏雨梨云
雄伟壮观 煦色韶光 妍蚩好恶 艳色绝世 艳紫妖红
宜嗔宜喜 宜喜宜嗔 旖旎风光 瘗玉埋香 余霞成绮
鱼沉雁落 远山芙蓉 章台杨柳 朱唇皓齿 左家娇女'''))