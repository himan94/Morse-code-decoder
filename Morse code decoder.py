"""
FIT9133 ASSIGNMENT 2 Building a Morse Code Decoder
with Python Classes
Semester 1 2018
STUDENT ID – 29389089
NAME – HIMANSHU SONI
"""

class decoder:
    def __init__(self):
        self.dict1 =    { '01' :'A' ,   '11' :'M'  ,   '1011' :'Y' ,
                         '1000' :'B' ,   '10' :'N'  ,   '1100' :'Z' ,
                         '1010' :'C' ,  '111' :'O'  ,  '11111' :'0' ,
                         '100'  :'D' , '0110' :'P'  ,  '01111' :'1' ,
                           '0'  :'E' , '1101' :'Q'  ,  '00111' :'2' ,
                         '0010' :'F' ,  '010' :'R'  ,  '00011' :'3' ,
                         '110'  :'G' ,  '000' :'S'  ,  '00001' :'4' ,
                         '0000' :'H' ,    '1' :'T'  ,  '00000' :'5' ,
                         '00'   :'I' ,  '001' :'U'  ,  '10000' :'6' ,
                         '0111' :'J' , '0001' :'V'  ,  '11000' :'7' ,
                         '101'  :'K' ,  '011' :'W'  ,  '11100' :'8' ,
                         '0100' :'L' , '1001' :'X'  ,  '11110' :'9' ,
                         '010101' : '.','110011': ',' ,'001100':'?' 
                          }
    def __str__(self):

        st=""
        for key,val in self.dict1.items():
            st = st + str(key) +':'+ str(val) + "\n"
        return st

    def decode(self,morse_code1):
        self.final_list = []
        pre_final_list = []
        ind_list = []
        for j1 in morse_code1:
            morse_code = j1.split('***')
            #print(morse_code)
            for seq_no,elem in enumerate(morse_code):         # ENUMERATES TAKES THE INDEX AS WELL AS ELEMENT IN A LIST
                for ind_str in elem:                       # TAKES INDIVISUAL CHARACTERS
                    if ind_str  == '1' or ind_str =='0' or ind_str =='*':       # CHECKS TO SEE IF IT'S VALID OR NOT
                        pass
                    else:
                        print ("Sequence number "+str(seq_no+1)+" rejected because of presence of invalid character: "+str(ind_str))
                        ind_list.append(seq_no)                # APPENDS THE INDEXES OF REJECTED ELEMENTS IN LIST seq_no
                        break


            for pop_seq in ind_list[::-1]:              # Loop in reversed to pop out the biggest index first
                ip_list.pop(pop_seq)                    # REMOVES ALL THE REJECTED ELEMENTS FROM THE LIST
            #print ("Correct sequences that were accepted are", morse_code)

            n = 0
            final_list = []
            
            for elem_in_iplist in morse_code:                # TAKES ONE ELEMENT AT A TIME FROM IP_LIST
                join_interim_list    = []                 # TWO INTERIM LIST WHERE THE JOINING PROCESS TAKES PLACE
                unjoint_interim_list = []
                after_split = elem_in_iplist.split('*')   # LIST CREATED AFTER SPLITTING WITH RESPECT TO *
                print (after_split)
                for elem2 in after_split:                 # TAKING ONE ELEMENT AT A TIME 
                    if elem2 not in self.dict1.keys():
                        print ("sequence rejected because of incorrect code entered:"+str(elem2))  # REJECTING ELEMENTS WHICH ARE NOT IN DICTIONARY
                        n = 1
                    else:
                        unjoint_interim_list.append(self.dict1[elem2])       # APPENDING VALID VALUE CORRESPONDING TO THE KEY     
                join_interim_list.append(''.join(unjoint_interim_list))  # JOINING ALL CHARACTERS AND APPENDING TO A DIFFERENT LIST
                final_list.append(join_interim_list[0])            # APPENDING THE RESULT AFTER JOINING TO THE FINAL LIST(ANSWER)
                join_interim_list = []                          # EMPTYING THE LIST SO THAT THE PROCESS CAN BE DONE FOR THE NEW STRING
                unjoint_interim_list = []

            if n == 0:
                pre_final_list.append(' '.join(final_list))
            else:
                pass
            
        #print(pre_final_list) 
        for q1 in pre_final_list:
            if q1[-1] in ['?','.',',']: 
                self.final_list.append(q1)
            else:
                print ("Sentence cannot end with "+ q1[-1])

        reject_list = []

        # creating a reject list which stores the indexes to reject
        
        for seq_q3,comp_q4 in enumerate(self.final_list):       #checking to see if punctuations occur one after other in one sentence (ex - ,?)
            for q2 in range(0,len(comp_q4)-1):                   
                if (comp_q4[q2] in ['?','.',','] and comp_q4[q2+1] in ['?','.',',']):
                    reject_list.append(seq_q3)

        for seq_q5,comp_q6 in enumerate(self.final_list):       #checking to see if punctuations occur in one sentence one after other with space in between (ex - , ?)
            for q5 in range(0,len(comp_q6)-2):
                if (comp_q6[q5] in ['?','.',','] and comp_q6[q5+2] in ['?','.',',']):
                    reject_list.append(seq_q5)

        reject_list.sort(reverse = True)
        for j1 in reject_list:
            del self.final_list[j1]
        
        return self.final_list
        
# TASK 2 BEGINS

class CharacterAnalyser(decoder):
    def __init__(self):
        decoder.__init__(self)
        self.count = {}
    def __str__(self):
        st=""
        for key,val in self.count.items():
            st = st + str(key) +':'+ str(val) + "\n"
        return st
    def analyse_characters(self, decoded_sequence):
    
        mid = {}
        from collections import Counter    #COUNTER IS USED TO MEASURE THE OCCURANCE OF EACH CHARACTER IN THE FORM OF A DICTIONARY

        for elem3 in self.final_list:           # TAKES ONE ELEMENT FROM THE LIST AT A TIME
            c1 = Counter(elem3)            # CREATES A DICTIONARY INDICATING THE OCCURANCE OF EACH CHARACTER
            for keys1 in c1:
                if keys1 in mid:            # checks if key is in dictionary, if yes increase count as per value in c1
                    mid[keys1] = mid[keys1] + c1[keys1]
                else:
                    mid[keys1] = c1[keys1]
        for keys2 in mid:
            self.count[keys2] = mid[keys2]
        return self.count

# TASK 3 BEGINS

class WordAnalyser(CharacterAnalyser):
    def __init__(self):
        CharacterAnalyser.__init__(self)
        self.wordcount = {}

    def __str__(self):
        st=""
        for key,val in self.wordcount.items():
            st = st + str(key) +':'+ str(val) + "\n"
        return st
    
    def analyse_words(self, decoded_sequence):

        mid1 = {}

        from collections import Counter    #COUNTER IS USED TO MEASURE THE OCCURANCE OF EACH CHARACTER IN THE FORM OF A DICTIONARY
        for sequence in self.final_list:
            countword = Counter(sequence.split(' '))   # COUNTER MODULE USED WITH THE WHOLE SEQUENCE PASSED AS INPUT
            for keys3 in countword:
                if keys3 in mid1:        # IF WORD FOUND THEN INCREASE COUNT AS PER THE VALUE
                    mid1[keys3] = mid1[keys3] + countword[keys3]
                else:
                    mid1[keys3] = countword[keys3]
        for keys4 in mid1:
            self.wordcount[keys4] = mid1[keys4]
        return self.wordcount

# TASK 4 BEGINS

class SentenceAnalyser(decoder):

    def __init__(self):
        decoder.__init__(self)
        self.sentencetype = {}

    def __str__(self):

        st=""
        for key,val in self.sentencetype.items():
            st = st + str(key) +':'+ str(val) + "\n"
        return st

    def analyse_sentences(self,decoded_sequence):

        #initializing all sentence types to zero
        self.sentencetype['questions'] = 0
        self.sentencetype['sentences'] = 0
        self.sentencetype['clauses'] = 0
        
        for sequences in self.final_list:
            for a_sequence in sequences:

                #increment count if the particular punctuation is found
                
                if a_sequence == '?':
                    self.sentencetype['questions'] += 1    
                elif a_sequence == '.':
                    self.sentencetype['sentences'] += 1
                elif a_sequence == ',':
                    self.sentencetype['clauses'] += 1
                else:
                    pass

        return self.sentencetype

# TASK 5 BEGINS

def main():

    # initializing objects
    
    decoder_op = decoder()
    character_op = CharacterAnalyser()
    word_op = WordAnalyser()
    sentence_op = SentenceAnalyser()

    ip_list = []              # CREATING AN EMPTY LIST TO STORE INPUTS FROM USER
    flag1 = 'Y'             # CREATING AN INITIAL FLAG(LOOP CONTINUES UNTIL FLAG VALUE IS CHANGED)
    while(flag1 == 'Y'):
    
        user_ip = input("Enter the desired morse code:")     # PROMPTING INPUT FROM USER
        if len(user_ip)> 0:                                  # ONLY APPENDING TO THE LIST IF IT'S LENGTH > 0
            ip_list.append(user_ip)
        else:
            print ("length should be greater than ZERO")
        
        flag2 = input("PRESS 'Y' or 'y' and enter key if there's another code,Press anything else and enter key if no other code:")
        flag1 = flag2.upper()

    reject_list1 = []
    
    for seq_no,a_seq in enumerate(ip_list):
        if '***' in a_seq:
            pass
        else:
            print('Sequence number: '+str(seq_no)+ 'rejected because of no *** in sequence')
            reject_list1.append(seq_no)

    reject_list1.sort(reverse = True)
    for comp1 in reject_list1:
        del ip_list[comp1]
                        
    flag3 = 'Y'             # CREATING AN INITIAL FLAG(LOOP CONTINUES UNTIL FLAG VALUE IS CHANGED)
    
    while(flag3 == 'Y'):    # second while loop to take to perform the choice operation
        
        choice = int(input(" Chosse 1 for morse code decoding , 2 for character count, 3 for word count and 4 for sentence type count: "))

        if choice == 1:
            print(decoder_op.decode(ip_list))
        elif choice == 2:
            q2 = character_op.decode(ip_list)       # creating an object of decoded sequence to be used aS input for analysing
            print(character_op.analyse_characters(q2))
        elif choice == 3:
            q3 = word_op.decode(ip_list)
            print(word_op.analyse_words(q3))
        elif choice == 4:
            q4 = sentence_op.decode(ip_list)
            print(sentence_op.analyse_sentences(q4))
        else:
            print("options should be between 1 and 4")

        flag4 = input("PRESS 'Y' or 'y' and enter key if there's another choice,Press anything else and enter key if no other choice:")
        flag3 = flag4.upper()

if  __name__ == '__main__':
    main()
