import re
from analysis import Analyser

class GFP(Analyser):
    def __init__(self):
        self.pattern_parent = '<li class="game-live-item" gid="3203">([\s\S]*?)</li>' 
        self.pattern_num = '<i class="js-num">([\s\S]*?)</i>'
        self.pattern_name = '<i class="nick" title="([\s\S]*?)">'
    
    def analysis(self, htmls):
        root_htmls = re.findall(self.pattern_parent, htmls)
        anchors = []
        for html in root_htmls:
            num = re.findall(self.pattern_num, html)
            name = re.findall(self.pattern_name, html)
            anchor = {'name': name, 'number': num}
            anchors.append(anchor)
        
        anchors = self.__refine(anchors)
        anchors = self.__sort(anchors)
        self.__show(anchors)
    
    def __refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
        }

        return map(l, anchors)

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall('[1-9]\d*\.?\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('rank ' +  str(rank + 1)
            + '  :  ' + anchors[rank]['name']
            + '  :  ' + anchors[rank]['number'])