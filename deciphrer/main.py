import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.text import FontContextManager

class MyGrid(Widget):
    message = ObjectProperty(None)
    combinations = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 'qn', 'py', 'cc', 'ej', 'rr', 'az', 'rh', 'ir', 'cd', 'jp', 'px', 'io', 'pj', 'bp', 'uy', 'iq', 'na', 'q', 'ma', 'gu', 'sx', 'hg', 'za', 'un', 'uj', 'cm', 'kr', 'cv', 'ib', 'am', 'i', 'sg', 'es', 'cu', 'qe', 'bh', 'wt', 'bu', 'fg', 'eq', 'wn', 'xi', 'do', 'cj', 'np', 'yk', 'hk', 'zf', 'rb', 'xl', 'vx', 'tw', 'aw', 'gb', 'ah', 'ud', 'zs', 'rg', 'on', 'xn', 'kx', 'gl', 'oi', 't', 'li', 'sh', 'gm', 'ef', 'gg', 'cr', 'mt', 'kp', 'hu', 'lb', 'k', 'ht', 'we', 'ee', 'pq', 'xz', 'if', 'xy', 'ca', 'ka', 'sn', 'bt', 'pf', 'ml', 'fz', 'kk', 'nh', 'vh', 'sp', 'er', 'fi', 'cn', 'vm', 'eh', 'mp', 'pi', 'zy', 'ek', 'wj', 'du', 'zm', 'ky', 'c', 'ph', 'wv', 'hy', 'ii', 'vl', 'mj', 'st', 'cz', 'hq', 'he', 'ip', 'ch', 'wz', 'ue', 'nz', 'gk', 'tj', 'uq', 'zw', 'jh', 'td', 'qh', 'nw', 'nx', 'bi', 'sv', 'eu', 'ts', 'hx', 'yw', 'je', 'cs', 'rk', 'e', 'dn', 'il', 'ay', 'ks', 'ql', 'ai', 'hb', 'xa', 'gh', 'no', 'mg', 'om', 'mn', 'vq', 'au', 'bz', 'su', 'qm', 'nv', 'dr', 'kz', 'ax', 'md', 'hj', 'de', 'se', 'lk', 'sb', 'yx', 'ny', 'tf', 'tv', 'ot', 'ug', 'hr', 'vj', 'yg', 'xk', 'zn', 'sr', 'vd', 'xm', 'id', 'gi', 'pz', 'kl', 'th', 'oj', 'tx', 'qp', 'pt', 'r', 'qc', 'xv', 'kw', 'yo', 'ys', 'ed', 'uk', 'go', 'ga', 'le', 'by', 'gy', 'zt', 'uu', 'ci', 'fa', 'wa', 'dg', 'br', 'ra', 'ix', 'ng', 'up', 'tb', 'qu', 'tu', 'vk', 'lm', 'sq', 'ti', 'ty', 's', 'wb', 'um', 'd', 'si', 'qs', 'lp', 'bf', 'tq', 'jf', 'nc', 'ln', 'lj', 'fr', 'sj', 'dm', 'tc', 'da', 'hi', 'of', 'fc', 'ig', 'fq', 'ki', 'xt', 'yr', 'sa', 'rl', 'kg', 'dl', 'bq', 'dj', 'rp', 'rx', 'rm', 'jj', 'bk', 'ea', 'gt', 'rf', 'qb', 'oe', 'ex', 'cy', 'yy', 'lr', 'oh', 'vu', 'cg', 'dv', 'pr', 'ri', 'dk', 'pe', 'gn', 'bl', 'fm', 'x', 'zb', 'ob', 'vt', 'fw', 'jl', 'cp', 'iy', 'is', 'ut', 'a', 'yp', 'cq', 'dd', 'xx', 'at', 'bv', 'yq', 'ih', 'os', 'ak', 'xo', 'ps', 'ux', 'ez', 'yt', 'zx', 'kb', 'ym', 'tk', 'kh', 'uh', 'vo', 'uo', 'lo', 'zi', 'sk', 'qw', 'qj', 'gq', 'co', 'ft', 'yi', 'mz', 'ko', 'j', 'ew', 'kq', 'fs', 'rj', 'jg', 'nd', 'mc', 'hp', 'o', 'po', 'jw', 'pn', 'it', 'yd', 'bn', 'qy', 'gv', 'wk', 'ie', 'yl', 'ep', 'gs', 'ub', 'mw', 'ru', 'ok', 'ss', 'qg', 'oc', 'ff', 'ta', 'uf', 'mk', 'pd', 'ey', 'kv', 'db', 'me', 'zz', 'iv', 'nt', 'od', 'vv', 'eg', 'ol', 'pc', 'll', 'mi', 'xd', 'xq', 'ho', 'ba', 'zg', 'wm', 'bm', 'nm', 'wp', 'yv', 'nf', 'yf', 'jr', 'zl', 'ns', 'tp', 'hh', 'gp', 'xg', 'nk', 'w', 'p', 'fb', 'wy', 'kc', 'pu', 'el', 'kj', 'qi', 'fu', 'n', 'qk', 'nq', 'wl', 'di', 'ce', 'mr', 'yj', 'ao', 'ne', 'ap', 'fd', 'zh', 'aj', 'ld', 'ow', 'uc', 'vn', 'hn', 'kn', 'ct', 'vr', 'vp', 'ae', 'tl', 'ua', 'al', 'ad', 'fy', 'dq', 'qz', 've', 'hf', 'g', 'hm', 'pm', 'qv', 'zk', 'wd', 'jo', 'oa', 'tg', 'hs', 'lx', 'ag', 'h', 'vc', 'xe', 'dt', 'pa', 'va', 'zj', 'av', 'mh', 'yn', 'so', 'ei', 'bo', 'gc', 'iu', 'bc', 'vy', 'xf', 'bs', 'jc', 'in', 'ur', 'ws', 'oo', 'bx', 'en', 'gj', 'ji', 'im', 'jy', 'cx', 'sz', 'gw', 'zv', 'hw', 'tr', 'yu', 'bd', 'lt', 'hv', 'ic', 'z', 'ge', 'us', 'vi', 'fx', 'xs', 'te', 'vw', 'iw', 'mx', 'ev', 'fh', 'ya', 'wq', 'jn', 'yz', 'rc', 'nb', 'pk', 'gx', 'ni', 'aq', 'xr', 'lu', 'lf', 'ou', 'dh', 'b', 'sm', 'my', 'uv', 'xp', 'zu', 'ls', 'kt', 'xb', 'wf', 'vb', 'rv', 'zo', 'fo', 'la', 'pv', 'fn', 'tt', 'wx', 'wc', 'ds', 'wo', 'tn', 'sw', 'lz', 'lg', 'fl', 'af', 'y', 'jz', 'rt', 'mf', 'lc', 'wi', 'hl', 'ul', 'jv', 'yb', 'mu', 'lh', 'hz', 'qx', 'wu', 'ze', 'ui', 'xu', 'dy', 're', 'ry', 'eb', 'jm', 'to', 'v', 'bg', 'rs', 'qa', 'dz', 'dw', 'iz', 'mb', 'tz', 'oq', 'gd', 'ju', 'ec', 'hc', 'lq', 'vz', 'ia', 'qf', 'jt', 'zp', 'sf', 'rd', 'ye', 'lv', 'ab', 'og', 'nj', 'xw', 'ku', 'ww', 'ms', 'xh', 'fv', 'bw', 'et', 'df', 'hd', 'cf', 'jk', 'op', 'jd', 'fe', 'ij', 'nn', 'tm', 'ov', 'pw', 'cb', 'kf', 'jx', 'qo', 'ro', 'cw', 'qt', 'zd', 'sl', 'eo', 'be', 'pg', 'ac', 'mq', 'oy', 'xc', 'm', 'kd', 'sc', 'xj', 'l', 'as', 'vs', 'nl', 'ke', 'fp', 'zr', 'aa', 'ja', 'fj', 'zc', 'oz', 'ox', 'lw', 'yc', 'nr', 'jb', 'pl', 'dp', 'uz', 'bj', 'pb', 'cl', 'pp', 'nu', 'f', 'qr', 'ly', 'mo', 'km', 'jq', 'rq', 'wh', 'qq', 'gf', 'qd', 'fk', 'bb', 'wg', 'vf', 'dc', 'gz', 'yh', 'dx', 'ck', 'mm', 'uw', 'rn', 'gr', 'rz', 'wr', 'vg', 'sd', 'em', 'ar', 'sy', 'ha', 'u', 'js', 'ik', 'zq', 'mv', 'an', 'or', 'rw', 'õ', 'ä', 'ö', 'ü', "š", "ž"]
    characters = ["我", "们", "他", "在", "个", "会", "什", "说", "能", "了", '兹', '颗', '课', '盖', '鲍', '插', '晨', '触', '遍', '潜', '姑', '帅', '镜', '列', '货', '踢', '末', '罢', '胎', '归', '犹', '商', '拼', '掌', '摔', '库', '矶', '丹', '瞧', '毫', '操', '杜', '笨', '输', '项', '缺', '按', '皮', '鼓', '售', '杉', '皇', '凶', '拳', '喊', '丑', '租', '虫', '饿', '耍', '严', '钻', '网', '憾', '降', '阵', '盯', '乔', '仔', '剩', '虚', '灯', '纹', '土', '盒', '滑', '泡', '爽', '烂', '圈', '研', '疼', '障', '镇', '抽', '汉', '善', '胖', '磨', '孕', '隐', '寄', '叔', '俱', '迟', '临', '惹', '销', '零', '梅', '疗', '典', '承', '鲁', '宇', '旅', '弱', '仍', '暴', '香', '竟', '股', '硬', '豪', '执', '搭', '响', '胜', '珍', '暗', '丈', '检', '熟', '莉', '臭', '搬', '政', '挥', '载', '啡', '吹', '占', '厨', '络', '策', '赌', '户', '鲜', '介', '散', '织', '豆', '摇', '顺', '亡', '鞋', '愚', '箱', '搜', '苏', '席', '南', '厂', '菲', '符', '熊', '扫', '环', '劳', '刀', '猎', '笔', '伟', '魂', '敏', '埋', '财', '辆', '旦', '欠', '敬', '闲', '乡', '糊', '黎', '奶', '招', '树', '例', '闪', '咬', '余', '委', '聚', '兵', '签', '雅', '吻', '钥', '景', '迈', '既', '慈', '批', '铁', '丧', '订', '寓', '狂', '骑', '育', '雨', '坚', '纪', '默', '牢', '莎', '速', '丢', '露', '互', '漫', '佳', '社', '毛', '森', '技', '盘', '鸡', '剪', '蒙', '导', '翻', '石', '墙', '浪', '砸', '致', '围', '隔', '聪', '构', '墨', '妙', '协', '净', '裤', '诚', '暂', '糖', '桑', '句', '困', '啤', '遗', '推', '蜜', '贵', '著', '腿', '沙', '迫', '灰', '逼', '赖', '春', '草', '艺', '彩', '轮', '伴', '梯', '雇', '塔', '补', '低', '赞', '椅', '核', '档', '键', '冠', '躺', '群', '秒', '汤', '角', '剂', '忠', '绪', '辩', '压', '纸', '毕', '汽', '判', '雪', '淘', '陆', '震', '奏', '斗', '恭', '稍', '岛', '洲', '仇', '阻', '势', '丝', '黄', '脏', '羊', '姻', '碎', '略', '摩', '摸', '敲', '古', '营', '叛', '魔', '富', '帽', '途', '窗', '爬', '祷', '限', '怨', '哭', '愉', '银', '偏', '浴', '创', '帐', '曲', '嫁', '吵', '悔', '弗', '伦', '兽', '娜', '郎', '凯', '贴', '尊', '党', '匙', '型', '农', '状', '编', '吓', '野', '闭', '宫', '闹', '欺', '优', '彼', '傲', '微', '依', '采', '罚', '健', '擦', '借', '尾', '胡', '曼', '设', '形', '援', '肉', '悲', '率', '嫌', '细', '裂', '祈', '卧', '河', '彻', '尺', '敌', '沃', '换', '顶', '霍', '青', '额', '吐', '卷', '登', '耳', '绿', '袋', '献', '冒', '妇', '睛', '乌', '葬', '汰', '短', '态', '巨', '雄', '审', '抢', '左', '频', '胸', '锁', '烈', '范', '绑', '座', '胁', '寻', '挂', '述', '季', '纯', '颜', '木', '败', '洁', '伯', '守', '甜', '九', '洞', '偶', '竞', '圾', '奖', '移', '粉', '盗', '羞', '桌', '猫', '鼻', '戒', '骨', '琳', '佩', '祖', '骄', '爆', '撞', '刑', '贺', '蹈', '瓶', '灭', '挖', '厅', '俄', '惨', '勒', '虽', '祝', '允', '评', '征', '款', '朗', '涂', '摄', '赏', '猪', '甲', '增', '恨', '朝', '充', '饼', '阳', '怜', '拖', '启', '恋', '遭', '怒', '巧', '茶', '尉', '烤', '播', '尝', '孤', '惧', '损', '躲', '菜', '训', '层', '醉', '陷', '挑', '牌', '残', '莫', '施', '伍', '堂', '抗', '懂', '鸟', '授', '泰', '境', '摆', '蓝', '娃', '掩', '惯', '广', '序', '池', '防', '般', '夏', '透', '双', '质', '症', '避', '拒', '邮', '八', '素', '攻', '欲', '督', '秀', '章', '副', '谓', '肥', '拥', '驾', '温', '省', '龙', '握', '拾', '升', '谎', '引', '忍', '估', '姓', '享', '村', '冰', '佛', '端', '幻', '洋', '慢', '染', '瓜', '源', '邦', '爷', '较', '括', '府', '辞', '宣', '撤', '尖', '废', '埃', '恢', '七', '描', '域', '尤', '奋', '荒', '怖', '替', '辣', '累', '忆', '努', '讯', '乖', '购', '扎', '垃', '谅', '材', '烟', '康', '幕', '李', '丁', '千', '稳', '劲', '惜', '址', '宁', '侵', '侦', '良', '效', '扮', '沉', '封', '舒', '软', '宾', '折', '旧', '婊', '劫', '勇', '辈', '牙', '尚', '访', '塞', '蠢', '匹', '武', '屋', '爵', '唯', '刻', '逮', '痴', '族', '印', '堆', '瓦', '徒', '誓', '啥', '邀', '扔', '扯', '诊', '乘', '堡', '嘘', '概', '妮', '喔', '初', '邻', '旁', '究', '测', '夺', '帕', '减', '翰', '抛', '庆', '婆', '异', '申', '禁', '北', '挡', '泳', '酷', '刺', '坦', '绍', '童', '盛', '鼠', '赚', '右', '供', '捕', '若', '免', '逊', '欧', '纽', '附', '仪', '园', '举', '咖', '厉', '尿', '辛', '称', '邪', '配', '属', '烧', '诞', '扰', '袭', '胆', '液', '版', '荣', '痕', '阴', '拯', '获', '迹', '智', '航', '违', '针', '以', '事', '样', '下', '做', '出']

    
    def encrypt_button(self):
        final = ""
        sonum = self.message.text.replace(" ", "").lower()
        
        for n in range(0, len(sonum)-1, 2):
            silp = sonum[n:n+2]
            
            if silp not in self.combinations:
                if silp[0] not in self.combinations and silp[1] not in self.combinations:
                    final += silp
                elif silp[0] in self.combinations and silp[1] in self.combinations:
                    final += self.characters[self.combinations.index(silp[0])] + self.characters[self.combinations.index(silp[1])]
                elif silp[0] in self.combinations:
                    final += self.characters[self.combinations.index(silp[0])] + silp[1]
                else:
                    final += silp[0] + self.characters[self.combinations.index(silp[1])]
            else:
                final += self.characters[self.combinations.index(silp)]
                
        if len(sonum) % 2 != 0:
            if sonum[-1] not in self.combinations:
                final += sonum[-1]
            else:
                final += characters[self.combinations.index(silp)]
        self.output.text = final
    
    def decrypt_button(self):      
        final = ""
        sonum = self.message.text.replace(" ", "").lower()
        
        for letter in sonum:
            if letter not in self.characters:
                final += letter
            else:
                final += self.combinations[self.characters.index(letter)]

        self.output.text = final
        
class KripteerijaApp(App):
    def build(self):
        return MyGrid()
    
if __name__ == "__main__":
    KripteerijaApp().run()