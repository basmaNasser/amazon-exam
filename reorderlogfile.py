def reorderLogFiles(self, logs: List[str]) -> List[str]:
         letterLog = []
         digitLog = []

         for i in logs:
             logtype = i.split()[1]

             if logtype.isdigit():
                 digitLog.append(i)

             else:
                 letterLog.append(i)

         letterLog.sort(key=lambda x: (x.split()[1:], x.split()[0]))

         # OR
         # for l in letterLog:
         #   sortedletter=sorted(letterLog,key=lambda x: (x.split(' ',1)[1], x.split(' ',1)[0]))

         # return(sortedletter+digitLog)
         return (letterLog + digitLog)
