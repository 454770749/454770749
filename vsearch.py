# -*- coding: utf-8 -*-

def search4prepositions_zhs(phrase: str) -> set:
    """Return any prepositions found in a supplied phrase."""
    # Source http://xh.5156edu.com/page/z3033m4876j18636.html
    # Source https://resources.allsetlearning.com/chinese/grammar/Preposition
    PREPOSITION_zhs = set('北京市 京''上海市 沪''天津市 津''重庆市 渝''黑龙江省 黑''吉林省 吉''辽宁省 辽''内蒙古 内蒙古''河北省 冀''新疆 疆''甘肃省 甘''青海省 青''陕西省 陕''宁夏 宁''河南省 豫''山东省 鲁''山西省 晋''安徽省 皖''湖北省 鄂''湖南省 湘''江苏省 苏''四川省 川''贵州省 黔''云南省 滇''广西省 桂''西藏 藏''浙江省 浙''江西省 赣''广东省 粤''福建省 闽''台湾省 台''海南省 琼''香港 港''澳门 澳')
    return PREPOSITION_zhs.intersection(set(phrase))

def search4letters(phrase: str='省份', letters: str='普及率') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
