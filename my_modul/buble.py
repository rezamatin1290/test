
#this is for buble sort for small to tall


def input_list():
        ls_1.append(input("enter a name: "))
        ls_2.append(float(input("enter a number:")))#if user Enter a number Error
        sort_wills()

def sort_wills():
        if (len(ls_1))!=1:
                for x in range((len(ls_2)-1), 0, -1):
                        if ls_2[x] < ls_2[x-1]:
                                temp = ls_2[x-1]
                                ls_2[x-1] = ls_2[x]
                                ls_2[x] = temp
                                temp = ls_1[x-1]
                                ls_1[x-1] = ls_1[x]
                                ls_1[x] = temp
                                del temp
                        else:
                                break
                        
                                



                """if ls_2[-1]<ls_2[-2]:
                        temp=ls_2[-1]
                        ls_2[-1]=ls_2[-2]
                        ls_2[-2]=temp
                        temp=ls_1[-1]
                        ls_1[-1]=ls_1[-2]
                        ls_1[-2]=temp
                        del temp

        """
ls_1 = []
ls_2 = []
for x in range(8):
        input_list()
        print(ls_1)
        print(ls_2)
