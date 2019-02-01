def cenvert_c_to_f(temp_C):
    temp_F = temp_C * 1.8 + 32 
    return temp_F

def main():
    temp_C_str = input("enter temp in degC: ")
    temp_C = float(temp_C_str)
    temp_F = temp_C * 1.8 + 32
    print('this is the temp in C',temp_C,'and in F',temp_F)

def fever_detection(temp_list):
    for tempurature in temp_list 
        if type(tempurature) == str:
            number_temp = float(tempurature)
        else:
            number_temp = tempurature
    for tempurature in temp_list :
        if number_temp > fever threshhold:
            is_fever = true 
        return is_fever 

if __name__ == "__main__":
    main()

