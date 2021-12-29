import csv
def write_to_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Sr.no", "Name", "Age", "Class", "Roll.no"])
        writer.writerow(info_list)
if __name__ == '__main__':
    Sr_no=1
    condition=True
    while condition:
        Student_name=input("\nEnter name of student " +str(Sr_no)+ " : ")
        Student_age=input("Enter age of student " +str(Sr_no)+ " : ")
        Student_class=input("Enter class of student " +str(Sr_no)+ " : ")
        Student_roll_no=input("Enter roll no of student " +str(Sr_no)+ " : ")
        Student_info=(Sr_no, Student_name, Student_age, Student_class, Student_roll_no)
        print("\nEntered details of student "+ str(Sr_no) +" are: \n" + Student_info[1], Student_info[2], Student_info[3], Student_info[4])
        info_check=input("\nCheck if the details are correct? (y/n): ")
        if info_check=='y':
            write_to_csv(Student_info)
            condition_check=input("\nDo you want to continue ? (y/n) : ")
            if condition_check=="y":
                Sr_no+=1
                condition=True
            else:
                condition=False
                break
        else:
            print("\nPlease enter the details again")
            condition=True