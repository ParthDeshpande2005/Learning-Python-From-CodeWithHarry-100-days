Questions=[
"Who was the first person to win two Nobel Prizes in different sciences? \n1. Albert Einstein \n2. Marie Curie \n3. Linus Pauling \n4. Richard Feynman"
,"Which Indian ruler defeated Alexander’s general Seleucus Nicator? \n1. Chandragupta Maurya \n2. Ashoka  \n3. Samudragupta  \n4. Bindusara" 
,"What is the term for a star that suddenly increases in brightness due to an explosion?  \n1. Pulsar  \n2. Supernova   \n3. Quasar  \n4. Neutron Star"  
,"In which year did ISRO launch its first satellite, Aryabhata?  \n1. 1969  \n2. 1975  \n3. 1980  \n4. 1991"  
,"Who wrote *The Origin of Species*?  \n1. Gregor Mendel  \n2. Charles Darwin   \n3. Louis Pasteur  \n4. Alfred Wallace"
,"Which chemical element was named after a scientist?  \n1. Einsteinium   \n2. Polonium  \n3. Radium  \n4. Uranium" 
,"The Bermuda Triangle is located in which ocean?  \n1. Indian Ocean  \n2. Atlantic Ocean   \n3. Pacific Ocean  \n4. Arctic Ocean"  
,"The Nobel Peace Prize is awarded in which city?  \n1. Stockholm  \n2. Geneva  \n3. Oslo  \n4. Vienna" 
,"In which year did the French Revolution begin?  \n1. 1765  \n2. 1789  \n3. 1815  \n4. 1848"
,"Which country borders both the Caspian Sea and the Persian Gulf?  \n1. Turkey  \n2. Iran   \n3. Kazakhstan  \n4. Saudi Arabia"  
,"Which Indian state has the highest number of international borders?  \n1. Arunachal Pradesh  \n2. Sikkim  \n3. Assam  \n4. West Bengal" 
,"The Treaty of Versailles ended which war?  \n1. World War I  \n2. World War II  \n3. Napoleonic Wars  \n4. Cold War" 
,"Who was the first Indian to travel to space?  \n1. Kalpana Chawla  \n2. Sunita Williams  \n3. Rakesh Sharma  \n4. Vikram Sarabhai"  
,"What is the SI unit of electric resistance?  \n1. Coulomb  \n2. Ohm   \n3. Tesla  \n4. Ampere" 
,"Which is the deepest point in the Earth's oceans?  \n1. Mariana Trench   \n2. Tonga Trench  \n3. Java Trench  \n4. Puerto Rico Trench"  
,"What was the codename of India’s first nuclear test in 1974?  \n1. Operation Vijay  \n2. Operation Smiling Buddha \n3. Operation Trident  \n4. Operation Shakti"] 

correctanswer=[2,1,2,2,2,1,2,3,2,2,4,1,3,2,1,2]
Prize=["0k","1k","2k","3k","5k","10k","20k","40k","80k","160k","320k","640k","1250k","2500k","5000k","1cr","7cr"]   


print("WELCOME TO KBC".center(150))

for i in range (16):
   if(i/5==1 or i/5==2 or i/5==3):
            print("You have reach a checkpoint.If any answer is wrong until next check point you will recive the checkpoint prize.which is",Prize[i])
   print("Your",i+1,"question is on screen")
   print(i+1,".",Questions[i])
   ans=int(input("Enter your answer: "))
   if(ans==correctanswer[i]):
        print("Your answer is correct!!!")    
        print("You have won Rs",Prize[i+1],"!!!")
        if(i==15):
            print("You have completed the Game.Thank You")
        else:
            print("lets move to the next Question")
   else:
       print("Your answer is incorrect")
       if(i+1<5):
        print("your final Prize is",Prize[i])
       else:
           print("your final Prize is",Prize[i//5*5])
       print("Thank You")
       break

   