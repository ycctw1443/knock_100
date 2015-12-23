#!/usr/bin/env python
# -- coding:utf-8 -*-

"""文節を表すクラスの実装

100本ノック問41
"""

__author__ = ''
__vertion__ = '0.1'
__date__ = ''


class Chunk():
    """
    文節を表すクラス
    """

    def __init__(self, morphs, dst, srcs):
        """コンストラクタ

        keyword argumets:
        morphs -- 形態素のリスト
        dst -- 係り先文節インデックス番号
        srcs -- 係り元文節インデックス番号のリスト
        """
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
