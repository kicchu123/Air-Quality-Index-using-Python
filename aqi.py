def get_aqi(concentration, breakpoints):
    for bp in breakpoints:
        if bp["C_low"] <= concentration <= bp["C_high"]:
            I_low = bp["I_low"]
            I_high = bp["I_high"]
            C_low = bp["C_low"]
            C_high = bp["C_high"]
            aqi = ((I_high - I_low) / (C_high - C_low)) * (concentration - C_low) + I_low
            return round(aqi)
    return None

def get_health_effects(aqi):
    if aqi is None:
        return "Invalid AQI"
    elif aqi <= 50:
        return "Good - Air quality is considered satisfactory."
    elif aqi <= 100:
        return "Moderate - Acceptable, but there may be a concern for some pollutants."
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups - People with lung disease, older adults, and children should limit outdoor exertion."
    elif aqi <= 200:
        return "Unhealthy - Everyone may begin to experience health effects."
    elif aqi <= 300:
        return "Very Unhealthy - Health alert: everyone may experience more serious health effects."
    else:
        return "Hazardous - Serious health effects and emergency conditions."

# Breakpoints for PM2.5 (24-hour avg) in µg/m³
pm25_breakpoints = [
    {"C_low": 0.0, "C_high": 12.0, "I_low": 0, "I_high": 50},
    {"C_low": 12.1, "C_high": 35.4, "I_low": 51, "I_high": 100},
    {"C_low": 35.5, "C_high": 55.4, "I_low": 101, "I_high": 150},
    {"C_low": 55.5, "C_high": 150.4, "I_low": 151, "I_high": 200},
    {"C_low": 150.5, "C_high": 250.4, "I_low": 201, "I_high": 300},
    {"C_low": 250.5, "C_high": 500.4, "I_low": 301, "I_high": 500},
]

# Breakpoints for PM10 (24-hour avg) in µg/m³
pm10_breakpoints = [
    {"C_low": 0, "C_high": 54, "I_low": 0, "I_high": 50},
    {"C_low": 55, "C_high": 154, "I_low": 51, "I_high": 100},
    {"C_low": 155, "C_high": 254, "I_low": 101, "I_high": 150},
    {"C_low": 255, "C_high": 354, "I_low": 151, "I_high": 200},
    {"C_low": 355, "C_high": 424, "I_low": 201, "I_high": 300},
    {"C_low": 425, "C_high": 604, "I_low": 301, "I_high": 500},
]

def main():
    print("Enter pollutant concentrations (24-hour average):")
    pm25 = float(input("PM2.5 (µg/m³): "))
    pm10 = float(input("PM10 (µg/m³): "))

    aqi_pm25 = get_aqi(pm25, pm25_breakpoints)
    aqi_pm10 = get_aqi(pm10, pm10_breakpoints)

    overall_aqi = max(filter(None, [aqi_pm25, aqi_pm10]))

    print("\n--- AQI Report ---")
    print(f"PM2.5 AQI: {aqi_pm25} -> {get_health_effects(aqi_pm25)}")
    print(f"PM10 AQI: {aqi_pm10} -> {get_health_effects(aqi_pm10)}")
    print(f"\nOverall AQI: {overall_aqi} -> {get_health_effects(overall_aqi)}")

if __name__ == "__main__":
    main()
