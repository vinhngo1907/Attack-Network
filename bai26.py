#!/usr/bin/python
def print_pascal(n):
     def pascal(n):
          if n == 1:
               list_pascal = [[1]]
               return list_pascal
          else:
               list_pascal = pascal(n-1)
               p = list_pascal[n-2]
               temp = list()
               temp.append(1)
               i = 0;
               while (i < len(p)-1):
                    t = int(p[i]) + int(p[i+1])
                    temp.append(t)
                    i = i + 1
               temp.append(1)
               list_pascal.append(temp)
               return list_pascal

     for line in pascal(n):
                i = 0
                s = str()
                while (i <= len(line)-1):
                        s = s + str(line[i]) + '\t'
                        i += 1
                print s
                
