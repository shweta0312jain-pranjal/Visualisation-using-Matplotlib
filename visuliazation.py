import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Company Sales Data.csv")

plt.figure()
plt.plot(df['month_number'], df['total_profit'],
         linestyle='dotted', marker='o',
         color='red', linewidth=3,
         markerfacecolor='black')

plt.title("Month-wise Company Profit")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.show()


plt.figure()
plt.plot(df['month_number'], df['facecream'], marker='o', linewidth=3, label='Face Cream')

plt.plot(df['month_number'], df['facewash'], marker='o', linewidth=3, label='Face Wash')

plt.plot(df['month_number'], df['toothpaste'], marker='o', linewidth=3, label='Toothpaste')

plt.plot(df['month_number'], df['bathingsoap'], marker='o', linewidth=3, label='Bathing Soap')

plt.plot(df['month_number'], df['shampoo'], marker='o', linewidth=3, label='Shampoo')

plt.plot(df['month_number'], df['moisturizer'], marker='o', linewidth=3, label='Moisturizer')

plt.title("Sales Data of All Products")
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.legend()
plt.show()



plt.figure()
plt.bar(df['month_number'], df['facecream'], label='Face Cream')

plt.bar(df['month_number'], df['facewash'], label='Face Wash')

plt.title("Face Cream and Face Wash Sales Comparison")
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.legend()
plt.show()
