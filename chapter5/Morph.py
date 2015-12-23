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

    def __init__(self, surface, base, pos, pos1):
        """コンストラクタ

        keyword argumets:
        surface - 表層系
        base - 基本形
        pos - 品詞
        pos1 - 品詞細分類1
        """
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
