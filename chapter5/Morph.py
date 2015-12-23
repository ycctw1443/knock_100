#!/usr/bin/env python
# -- coding:utf-8 -*-

"""形態素を表すクラスの実装

100本ノック問40
"""

__author__ = ''
__vertion__ = '0.1'
__date__ = ''


class Morph():
    """
    形態素を表すクラス
    """

    def __init__(self, word):
        """コンストラクタ

        keyword argumets:
        sentence -- 単語
        """
        self.__word = word
        self.surface = self.__word.split()[0]
        self.base = self.__word.split()[1].split(',')[6]
        self.pos = self.__word.split()[1].split(',')[0]
        self.pos1 = self.__word.split()[1].split(',')[1]
