import tkinter as tk
from datetime import date

def calculate_donation():
    #today's date and day of the year
    today = date.today()
    day_of_year = today.timetuple().tm_yday  # Day of the year
    
    #today's donation and total saved so far
    donation_today = day_of_year
    total_saved = (day_of_year * (day_of_year + 1)) // 2
    
    # Update the labels with today's details
    date_label.config(text=f"Today's Date: {today}")
    day_label.config(text=f"Day of the Year: {day_of_year}")
    donation_label.config(text=f"Donation for Today: Ksh {donation_today}")
    total_label.config(text=f"Total Saved So Far: KSh {total_saved}")

#main application window
root = tk.Tk()
root.title("Daily Donation Reminder")
root.geometry("400x250")

#labels for displaying information
date_label = tk.Label(root, text="", font=("Helvetica", 12))
date_label.pack(pady=5)

day_label = tk.Label(root, text="", font=("Helvetica", 12))
day_label.pack(pady=5)

donation_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
donation_label.pack(pady=5)

total_label = tk.Label(root, text="", font=("Helvetica", 12))
total_label.pack(pady=5)

#button to calculate the donation details
calculate_button = tk.Button(root, text="Show Today's Donation", command=calculate_donation, font=("Helvetica", 12))
calculate_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Helvetica", 12))
exit_button.pack(pady=10)

root.mainloop()
#to be modified laters