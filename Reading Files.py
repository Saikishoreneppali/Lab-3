with open("/home/skneppali/Desktop/Modran robotics/sensor_data.txt", "r") as file:
    # now iterate over each line
    for line in file:
        # split the line into timestamp and temprature:
        timestamp, temprature = line.strip().split(", ")

        # now we can process the data
        print("Timestamp: ", timestamp)
        print("Temprature: ", temprature)