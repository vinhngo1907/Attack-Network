#!/usr/bin/python
def sortdict(dictionary):
    sort = sorted(dictionary.items(), key = lambda k: k[1])
    sort_reverse = sorted(dictionary.items(), key = lambda k: k[1], reverse=True)
    print 'Sap xep tang dan: ', sort
    print 'Sap xep giam dan: ', sort_reverse
