# -*- coding: utf-8 -*-

def delete_tag(tag):
    git push --delete origin $1
    git tag -d $1
