all = ["John","Mary","Tina","Fiona","Claire","Eva","Ben","Bill","Bert"]
engpass = ["John","Mary","Fiona","Claire","Ben","Bill"]
mathpass = ["Mary","Fiona","Claire","Eva","Ben"]
enp = []
mnp = []
allpass = []
epmnp = []
for i in range(len(all)):
    if all[i] not in engpass :
        enp.append(all[i])
    if all[i] not in mathpass:
        mnp.append(all[i])
    if all[i] in engpass and all[i] in mathpass:
        allpass.append(all[i])
    if all[i] in engpass and all[i] not in mathpass:
        epmnp.append(all[i])
print("英文與數學都及格:"+str(allpass))
print("數學不及格:"+str(mnp))
print("英文及格但數學不及格:"+str(epmnp))