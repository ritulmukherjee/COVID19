#!/usr/bin/env python
# coding: utf-8

# In[2]:


def covid():
    if (((Input2>=60) or (Input2<=10) or (Input=='Y')) & ((Input13=='Y') or (Input14=='Y') or
                                                          (Input15=='Y')) & (Input3=='Y') & (Input4=='Y') & (Input5=='Y')):
        print("As you come in the category of critical age group or have travelled recently or have serious symptoms, Rush to doctor!")
    elif((Input3=='Y') &(Input4=='Y') &(Input5=='Y')):
        print("You have common symptoms. It can be COVID or flu. Take care!")
    elif((Input6=='Y') & (Input7=='Y') & (Input8=='Y') & (Input9=='Y') & (Input10=='Y') & (Input11=='Y') & (Input12=='Y')):
        print("You have mild symptoms. Home quarantine is advised.")
    else:
        print("NEXT")
        


# In[ ]:


for i in range(1,3):
    print("Patient No :{}".format(i))
    Input1=input("Enter your name:")
    Input2=int(input("Enter your age:"))
    Input=input("Have you travelled from abroad recently? (Y/N)")
    Input3=input("Do you have fever? (Y/N)")
    Input4=input("Do you have dry cough? (Y/N)")
    Input5=input("Do you have tiredness? (Y/N)")
    Input6=input("Do you have aches and pains in any part of the body? (Y/N)")
    Input7=input("Are you having sore throat (Y/N)")
    Input8=input("Are you suffering from diarrhoea? (Y/N)")
    Input9=input("Do you have conjunctivitis (Y/N)")
    Input10=input("Are you having continuous headache? (Y/N)")
    Input11=input("Are you suffering from the loss of taste or smell? (Y/N)")
    Input12=input("Are you having rashes anywhere on the skin? (Y/N)")
    Input13=input("Are you having difficulty in breathing? (Y/N)")
    Input14=input("Are you suffering from chest pain (Y/N)")
    Input15=input("Are you suffering from the loss of speech or movement (Y/N)")
    covid()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




