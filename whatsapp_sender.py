import pandas as pd
import pywhatkit as kit
import time

# Read Excel file
data = pd.read_excel("C:\\Users\\kumar\\Desktop\\phone_numbers.xlsx")

for index, row in data.iterrows():
    phone = f"+{row['Phone Number']}"
    name = row['Name']
    message_template = row['Message Template']
    
    # Personalize the message
    personalized_msg = message_template.replace("{name}", name)

    # Send message - this schedules message 1 minute ahead (you can adjust)
    kit.sendwhatmsg(
        phone_no=phone,
        message=personalized_msg,
        time_hour=time.localtime().tm_hour,
        time_min=time.localtime().tm_min + 1,
        wait_time=10,
        tab_close=True
    )

    print(f"Scheduled message to {name} at {phone}")
    time.sleep(15)  # Wait a bit before sending the next one
