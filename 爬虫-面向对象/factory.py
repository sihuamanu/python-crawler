from analyser.gfp import *

class CategoryFactory():

    @staticmethod
    def get_category(flag):
        if flag == 'GFP':
            return GFP()