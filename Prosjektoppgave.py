# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:45:15 2025

Prosjektoppgave

@author: EMM
"""

import pandas as pd
import matplotlib.pyplot as plt


# Del a) Lese inn filen support_uke_24.xlsx og poplulere arrayene
##################################################################

df=pd.read_excel('support_uke_24.xlsx')
u_dag=df['Ukedag'].values
kl_slett=df['Klokkeslett'].values
varighet=df['Varighet'].values
score=df['Tilfredshet'].values


# Del b) Lage søylediagram som viser henvendelse pr. ukedag
##################################################################

print('\n',"Del b",'\n',"***************************")

iMandag = iTirsdag = iOnsdag = iTorsdag = iFredag = iLørdag = iSøndag = 0

for sDag in u_dag:
    if sDag == "Mandag":
        iMandag += 1
    elif sDag == "Tirsdag":
         iTirsdag += 1
    elif sDag == "Onsdag":
         iOnsdag += 1
    elif sDag == "Torsdag":
         iTorsdag += 1
    elif sDag == "Fredag":
         iFredag += 1 
    elif sDag == "Lørdag":
         iLørdag += 1
    elif sDag == "Søndag":
         iSøndag += 1 
    else:
         pass
  
sDager = [iMandag, iTirsdag, iOnsdag, iTorsdag, iFredag, iLørdag, iSøndag]  
sNavn = ['Mandag','Tirsdag', 'Onsdag' , 'Torsdag', 'Fredag', 'Lørdag', 'Søndag']
lFarger = ['red','blue','green','orange', 'purple', 'pink','black'] 
plt.bar(sNavn,sDager,color = lFarger)
plt.title('Henvendelser fordelt på dager') 
plt.xlabel('Dager') 
plt.ylabel('Henvendelser')
plt.show()  


# Del c) Finne minste og lengste samtaletid
##################################################################

print('\n','\n',"Del c",'\n',"***************************",'\n')

print("Lengste samtale-varighet:",max(varighet))
print("Korteste samtale-varighet:",  min(varighet))


# Del d) Gjennomsnittlig samtaletid
##################################################################

print('\n','\n',"Del d",'\n',"***************************",'\n')

iTotal = 0
iAntall = 0
for sVarighet in varighet:
    aTid = sVarighet.split(":")
    iTidsekunder = int(aTid[0]) * 60 * 60   + int(aTid[1]) * 60 + int(aTid[2])
    iTotal = iTotal + iTidsekunder
iSnitTid = int(iTotal/len(varighet))

sTekst = "Gjennomsnittlig samtaletid: "
iSnittTidTimer = iSnitTid // (60 * 60)

if iSnittTidTimer >= 1:
    sTekst = sTekst + str(iSnittTidTimer) + " timer "
    iSnitTid = iSnitTid - (iSnittTidTimer * 60 * 60)

sTekst = sTekst + str(iSnitTid // 60) + " minutter " + str(iSnitTid % 60) + " sekunder" 

print(sTekst)


# Del e) Sektordiagram som viser henvendelse i ulike perioder
##################################################################

print('\n','\n',"Del e",'\n',"***************************")

i08_10 = i10_12 = i12_14 = i14_16 = 0

for x in kl_slett:
    ax = x.split(":")
    if int(ax[0]) > 16:
        pass
    elif int(ax[0]) >= 14:
        i14_16 += 1
    elif int(ax[0]) >= 12:
        i12_14 += 1
    elif int(ax[0]) >= 10:
        i10_12 += 1
    elif int(ax[0]) >= 8:
        i08_10 += 1
    else:
        pass    

sLabelTekst = ["08-10", "10-12", "12-14", "14-16" ]
plt.title('Henvendelser fordelt på tidspunkt') 
plt.pie([i08_10, i10_12, i12_14, i14_16], labels=sLabelTekst)
plt.show()


# Del f) Finne kundetilfredshet (NPS = % positive kunder - % negative kunder) 
##################################################################

print('\n','\n',"Del f",'\n',"***************************",'\n')

i1 = i2 = i3 = i4 = i5 = i6 = i7 = i8 = i9 = i10 = 0
iAntall = 0
for x in score:
    if not(pd.isna(x)): # Tar bort kunder som ikke har gitt vurdering
        iAntall +=1
        y = int(x)
        if y == 1:
            i1 += 1
        if y == 2:
            i2 += 1
        if y == 3:
            i3 += 1
        if y == 4:
            i4 += 1
        if y == 5:
            i5 += 1
        if y == 6:
            i6 += 1
        if y == 7:
            i7 += 1
        if y == 8:
            i8 += 1
        if y == 9:
            i9 += 1
        if y == 10:
            i10 += 1    
        
iMisfornøyde = i1 + i2 + i3 + i4 + i5 + i6
iFornøyde = i9 + i10

NPS = ((iFornøyde/iAntall - iMisfornøyde/iAntall) * 100)
print("NPS ",round(NPS,1), "( % Fornøyde:", round(iFornøyde/iAntall * 100,1) , "- % Misfornøyde", round(iMisfornøyde/iAntall * 100,1), ")" )


