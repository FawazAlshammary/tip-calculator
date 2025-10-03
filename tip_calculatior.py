print(مرحبًا بك في برنامج تقسيم الفاتورة ! ")
bill = float(input("كم مبلغ الفاتورة ؟ "))
tip = int(input("كم تريد ان تعطي بقشيش 0 , 5 , 10 , 12 , 15 الخ ؟ "))
persons = int(input("كم عددكم ؟ "))
Calc_tip = tip / 100
Total_Calc_tip = bill * Calc_tip
Calc_Bill_tip = (bill + Total_Calc_tip ) /  persons
final_Bill = round(Calc_Bill_tip, 2)
print(f"الحسبة على كل واحد {final_Bill} ")



