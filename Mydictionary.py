print("Enter the word which you find the meaning of:",end="\n\n")
print("Following is the list of words select any one word for its meaning:",end="\n\n")
MyDict={"Set":"Collection of well defined objects","Mutable":"Can be changed","Immutable":"Can not be changed.","Immunity":"1.the ability of an organism to resist a particular infection or toxin by the action of specific antibodies or sensitized white blood cells, 2.protection or exemption from something, especially an obligation or penaltyb the rebels were given immunity from prosecution","precisely":"1.exactly   2.exactly (used to emphasize the complete accuracy or truth of a statement)."}
words=["Set","Mutable","Immutable","Immunity","precisely"]
print(words)
choice=str(input())
print(MyDict[choice])