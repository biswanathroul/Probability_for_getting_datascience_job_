r1name=input("Enter your name: ")
r1mob=input("Enter your mobile number: ")
r1email=input("Enter your email id: ")
#10th section
r2medium=input("In 10th, which board did you studied? ")
r2sub10th=input("Enter your all subjects including all electives in small letters and separated by comma: ")
if r2sub10th in ["cs", "computer science", "computer" , "programming" , "programming language"] :
   r2sub10thmemoryproglang=input("what programming language do you know?")
    r2sub10thmemory=input("Do you still remember the basics of programming language? yes or no: ")
r2sub10thmathpercentae=input("Enter your percentage in maths: ")
#12th section
r3sub12th=input("In 12th, which stream did you choosed?")
if r3sub12th in ["arts", "ARTs", "Arts" , "art", "ART", "Art"] :
    r3sub12thmemory=input("Do you have any of these electives or majors in your 12th, Economics or Computer science or mathematics? Answer in yes or no: ")
    if r3sub12thmemory in ["yes", "Yes", "YES"]:
        r3sub12thmemorysub=input("which subject?")
#graduation section
r4subgrad=input("In graduation, which stream did you choosed? like bsc, bcom, bba, bca, btech, bba")
if r4subgrad in ["arts", "ARTs", "Arts" , "art", "ART", "Art"] :
    r4subgradmemory=input("Do you have any of these electives or majors in your graduation, Economics or Computer science or mathematics? Answer in yes or no: ")
    if r4subgradmemory in ["yes", "Yes", "YES"]:
        r4subgradmemorysub=input("which subject?")

#masters section
r5submasters=input("In masters, which stream did you choosed? like msc, mcom, mba, mca, mtech, mba")
if r5submasters in ["arts", "ARTs", "Arts" , "art", "ART", "Art"] :
