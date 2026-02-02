import csv
import json

INPUT_CSV = "fleet_data.csv"
OUTPUT_JSON = "battery_filtered_data.json"

battery_0_10 = []
battery_10_20 = []
battery_20_30 = []
battery_30_40 = []
battery_40_50 = []
battery_50_60 = []
battery_60_70 = []
battery_70_80 = []
battery_80_90 = []
battery_90_100 = []


with open(INPUT_CSV, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        battery = int(row["battery"])

        vehicle_data = {
            "vehicle_id": row["vehicle_id"],
            "model": row["model"],
            "battery": battery,
            "status": row["status"],
            "hub": row["hub"],
            "vehicle_type": row["vehicle_type"]
        }

        if 0 <= battery < 10:
            battery_0_10.append(vehicle_data)

        elif 10 <= battery < 20:
            battery_10_20.append(vehicle_data)

        elif 20 <= battery < 30:
            battery_20_30.append(vehicle_data)

        elif 30 <= battery < 40:
            battery_30_40.append(vehicle_data)

        elif 40 <= battery < 50:
            battery_40_50.append(vehicle_data)

        elif 50 <= battery < 60:
            battery_50_60.append(vehicle_data)

        elif 60 <= battery < 70:
            battery_60_70.append(vehicle_data)

        elif 70 <= battery < 80:
            battery_70_80.append(vehicle_data)

        elif 80 <= battery < 90:
            battery_80_90.append(vehicle_data)

        elif 90 <= battery <= 100:
            battery_90_100.append(vehicle_data)


final_data = {
    "battery_0_10": battery_0_10,
    "battery_10_20": battery_10_20,
    "battery_20_30": battery_20_30,
    "battery_30_40": battery_30_40,
    "battery_40_50": battery_40_50,
    "battery_50_60": battery_50_60,
    "battery_60_70": battery_60_70,
    "battery_70_80": battery_70_80,
    "battery_80_90": battery_80_90,
    "battery_90_100": battery_90_100
}

with open(OUTPUT_JSON, "w") as json_file:
    json.dump(final_data, json_file, indent=4)


with open(OUTPUT_JSON, "w") as json_file:
    json.dump(final_data, json_file, indent=4)

