Here is a **clean, professional, and beginner-friendly README.md** for your AQI Calculator project.
You can copy-paste directly into GitHub.

---

# 🌫️ Air Quality Index (AQI) Calculator

A simple Python program that calculates the **Air Quality Index (AQI)** based on **PM2.5** and **PM10** pollutant concentrations (24-hour average).
It uses official U.S. EPA breakpoints to compute AQI and provides corresponding **health effect messages**.

---

## 📌 Features

* Calculates **AQI for PM2.5**
* Calculates **AQI for PM10**
* Computes **Overall AQI**
* Provides **health impact descriptions** based on AQI range
* Uses official **EPA AQI breakpoints**
* Clean and easy-to-understand Python code

---

## 📁 Project Structure

```
AQI-Calculator/
│
├── aqi_calculator.py   # Main Python program
└── README.md           # Documentation
```

---

## 🧮 How It Works

The AQI is calculated using the formula:

```
AQI = ((I_high - I_low) / (C_high - C_low)) * (Concentration - C_low) + I_low
```

Where:

* `I_low` and `I_high` → AQI category range
* `C_low` and `C_high` → pollutant concentration range
* Breakpoints are defined for PM2.5 and PM10.

---

## 🚀 How to Run the Program

### **1. Clone the repository**

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### **2. Run the Python script**

```bash
python aqi_calculator.py
```

### **3. Enter inputs when prompted**

Example:

```
PM2.5 (µg/m³): 80
PM10 (µg/m³): 120
```

---

## 📝 Sample Output

```
--- AQI Report ---
PM2.5 AQI: 164 -> Unhealthy - Everyone may begin to experience health effects.
PM10 AQI: 95 -> Moderate - Acceptable, but there may be a concern for some pollutants.

Overall AQI: 164 -> Unhealthy - Everyone may begin to experience health effects.
```

## 🩺 AQI Health Categories

| AQI Range | Category                       | Description                              |
| --------- | ------------------------------ | ---------------------------------------- |
| 0–50      | Good                           | Air quality is satisfactory              |
| 51–100    | Moderate                       | Acceptable air quality                   |
| 101–150   | Unhealthy for Sensitive Groups | Affects children, elderly, lung patients |
| 151–200   | Unhealthy                      | Health effects for everyone              |
| 201–300   | Very Unhealthy                 | Serious health effects                   |
| 301–500   | Hazardous                      | Emergency conditions                     |

---

## 🛠️ Technologies Used

* **Python 3**
* AQI Breakpoints (U.S. EPA Standard)

---

## 🤝 Contributions

Pull requests are welcome.
If you want to add support for additional pollutants (CO, SO₂, NO₂, O₃), feel free to contribute!

