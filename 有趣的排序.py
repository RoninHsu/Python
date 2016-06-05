List = []
Alist = []
Ap = []
Blist = []
Bp = []
Frist = []
Cp = []
List=[int(a) for a in raw_input().split(" ")]
num=len(List)
for i in range(num):
  if ((i+1)%2)==0 and ((i+1)%3)!=0:
    Alist.append(List[i])
    Ap.append(i)
  elif ((i+1)%3)==0:
      Blist.append(List[i])
      Bp.append(i)
Alist.sort()
Blist.sort(reverse=True)
Anum = len(Ap)
Bnum = len(Bp)
for s_A in range(Anum):
  List[Ap[s_A]]=Alist[s_A]
for s_B in range(Bnum):
  List[Bp[s_B]]=Blist[s_B]
for s_C in range(num):
  print List[s_C],
