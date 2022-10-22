
def getHeaviestPackage(packageWeights):
        # Write your code here
        new_pkg=new_lst(packageWeights)
        while len(new_pkg)>=2 :
            new_pkg=new_lst(packageWeights)
            if len(new_pkg)==3:
                    break
        print (max(new_pkg))

def new_lst(pkg):
        smm=0
        p1=0
        p2=0
        index=0
        for i in range(len(pkg)-1):
            if pkg[i] < pkg[i+1]:
                if smm < pkg[i]+pkg[i+1]:
                    index=i
                    p1=pkg[i]
                    p2=pkg[i+1]
                    smm=p1+p2
        if smm >0:
                    pkg[index] = smm
                    pkg.remove(p2)
        return (pkg)

# #[20,13,8,9]

getHeaviestPackage([2,9,10,3,7])
