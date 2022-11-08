#!/usr/bin/python
def tamgiaccan(n):
    i = 1
    while (i <= 2*n-1):
            a = str()
            if (i <= n):
                    j = 1
                    while (j <= i):
                            a = a + '* '
                            j += 1
                    print a
            else:
                    j = 2*n - i
                    while (j > 0):
                            a = a + '* '
                            j -= 1
                    print a
            i += 1
