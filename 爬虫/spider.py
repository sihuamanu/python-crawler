import urllib.request
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context

class Spider():
    url = 'https://www.huya.com/g/3203'
    pattern_list = '<li class="game-live-item" gid="3203">([\s\S]*?)</li>' 
    pattern_num = '<i class="js-num">([\s\S]*?)</i>'
    pattern_name = '<i class="nick" title="([\s\S]*?)">'

    def __htmls(self):
        with urllib.request.urlopen(Spider.url) as response:
            htmls = response.read()
        return htmls
    
    def __fetch_content(self, htmls):
        result = re.findall(Spider.pattern_list, str(htmls, encoding='utf-8'))
        anchors = []
        for res in result:
            num = re.findall(Spider.pattern_num, res)
            name = re.findall(Spider.pattern_name, res)
            anchor = {'name': name, 'number': num}
            anchors.append(anchor)
    
        return anchors
    
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

    
    def go(self):
       htmls = self.__htmls()
       anchors = self.__fetch_content(htmls)
       anchors = list(self.__refine(anchors))
       anchors = self.__sort(anchors)
       self.__show(anchors)
    

 
spider = Spider()
spider.go()


