


f=open ("Card_0001.txt","r")



txt = (f.readline())
#print(txt.split("/"))
print
#
FIRST=(txt.split("/"))
#print (FIRST[0] + FIRST[1] + FIRST[2]+ FIRST[3])
Page1=(FIRST[0].replace("^", chr(13) + "2. "))
Page2=(FIRST[1].replace("^", chr(13) + "4. "))
Page4=(FIRST[2].replace("^", chr(13) + "8. "))
Page8=FIRST[3]
#
txt = (f.readline())
SECOND=(txt.split("/"))
#print (SECOND[2]+ SECOND[3]);
hack= (SECOND[2].split("^"))
Page4= Page4 + chr(13) + "9. "+(hack[1])
Page9=(SECOND[3])
#
txt=(f.readline())
THIRD=(txt.split("/"))
hack=(THIRD[1].split("^"))
Page2=Page2+chr(13)+"5. " + (hack[1])
Page5=(THIRD[2].replace("^", chr(13)+"10. "))
PageA=(THIRD[3])
#
txt=(f.readline())
FOURTH=(txt.split("/"))
hack=(FOURTH[2].split("^"))
Page5=Page5+chr(13)+"11. " + (hack[1])
PageB=(FOURTH[3])
#
txt=(f.readline())
FIFTH=(txt.split("/"))
hack=(FIFTH[0].split("^"))
Page1=Page1+chr(13)+ "3. "+(hack[1])
Page3=(FIFTH[1].replace("^", chr(13) + "6. "))
Page6=(FIFTH[2].replace("^", chr(13) +"12. "))
PageC=FIFTH[3]
#
txt=(f.readline())
SIXTH=(txt.split("/"))
hack= (SIXTH[2].split("^"))
Page6= Page6 + chr(13) +  "13. " + (hack[1])
PageD=(SIXTH[3])
#
txt=(f.readline())
SEVENTH=(txt.split("/"))
hack=(SEVENTH[1].split("^"))
Page3=Page3+chr(13)+ "7. "+ (hack[1])
Page7=(SEVENTH[2].replace("^", chr(13) + "14. "))
PageE=(SEVENTH[3])
#
txt = (f.readline())
EIGHTH=(txt.split("/"))
print (EIGHTH[2]+ EIGHTH[3]);
hack= (EIGHTH[2].split("^"))
Page7= Page7 + chr(13) + "15. "+ (hack[1])
PageF=(EIGHTH[3])



#
print "1. " + Page1;
print
print "2. " + Page2;
print
print "3. " + Page3; 
print
print "4. " + Page4;
print
print "5. " + Page5;
print
print "6. " + Page6;
print
print "7. " + Page7; 
print
print "8. " + Page8;
print
print "9. " + Page9;
print
print "10. " + PageA;
print
print "11. " + PageB;
print
print "12. " + PageC;
print
print "13. " + PageD;
print
print "14. " + PageE;
print 
print "15. " + PageF; 