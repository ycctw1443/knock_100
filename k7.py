#!/usr/bin/env python
#-- coding:utf-8 -*-

def xyz(x,y,z):
    return str(x) + '時の' + y + 'は' + str(z)

def main():
    x = 12
    y ='気温'
    z = 22.4
    print(xyz(x,y,z))

if __name__ == '__main__':
    main()
