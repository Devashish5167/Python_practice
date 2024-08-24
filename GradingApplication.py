# Grading Application using If Else

m_maths = int(input("Enter maths marks: "))
m_physics = int(input("Enter Physics marks: "))
m_Chemistry = int(input("Enter chemistry marks: "))
if(m_maths>=35 and m_physics>=35 and m_physics>=35):
    print("Pass")
    
    avg=(m_maths+m_physics+m_Chemistry)/3
    print(avg)
    
    if(avg<=59):
        print("Grade C")
    elif(avg<=69):
        print("Grade B")
    else:
        print("Grade A")
        
else:
    print("Fail")