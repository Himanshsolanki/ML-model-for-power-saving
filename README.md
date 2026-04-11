# 🏙️ Smart City AI Dashboard (Streamlit)

A real-time **Smart City Simulation Dashboard** built using **Streamlit**, showcasing how AI-driven systems can manage urban infrastructure like traffic, hospitals, malls, parking, and homes.

---

## 🚀 Overview

This project simulates a **smart governance system** where AI dynamically controls:

- 🚦 Traffic & street lighting
- 🏥 Hospital power management
- 🅿️ Parking systems
- 🏬 Mall energy optimization
- 🌫️ Mist cooling systems
- 🏠 Smart home automation

The system uses **simulated sensor data + decision logic** to optimize energy usage and improve efficiency.

---

## ⚙️ Key Features

### 🧠 AI Decision System
- Automatically adjusts systems based on:
  - Light intensity (LDR)
  - Motion detection (PIR)
  - Humidity
  - Wi-Fi device density
  - Distance sensors

---

### 🚨 Emergency Mode
- Overrides all logic for:
  - Hospitals
  - Traffic systems
- Ensures **maximum power & priority handling**

---

### 🛠️ Sensor Calibration (New Zero Concept)
- Fix faulty sensors using:
  - "🔧 Fix All Sensors" button
- Applies **offset correction** to eliminate noise/drift

---

### ⚠️ Fault Detection System
- Randomly simulates:
  - Sensor failures
  - Data inconsistencies
- Displays real-time alerts

---

### 🕹️ Manual Override
Each system can be controlled manually:
- AI Enable (default)
- Full Power
- Power Off

---

## 🧩 System Modules

### 🚦 Street / Traffic
- Controls:
  - Traffic signals
  - Street light brightness (PWM)
- Logic:
  - Bright daylight → lights OFF
  - Night + activity → FULL brightness
  - Empty roads → DIM mode

---

### 🏥 Hospital
- Dynamic power allocation:
  - Critical rooms → 100%
  - Occupied → stable power
  - Empty → eco mode
- Emergency → full power everywhere

---

### 🅿️ Parking System
- Uses:
  - Ultrasonic sensor + LDR
- Provides:
  - Smart lighting
  - Spot detection

---

### 🏬 Mall System
- Multi-sensor decision:
  - Crowd (Wi-Fi + PIR)
  - Lighting conditions
- Controls:
  - Lighting + ventilation

---

### 🌫️ Mist Cooling System
- Activates only when:
  - People are present
- Saves:
  - Water
  - Energy

---

### 🏠 Smart Home
- Uses:
  - Lock direction (inside/outside)
  - Humidity
- Logic:
  - Outside → shutdown mode
  - Inside → active appliances

---

## 📊 Real-Time Dashboard

Displays:
- Live system status (metrics)
- AI reasoning for decisions
- Sensor health monitoring
- Offset calibration values

---

## 📂 Code Reference

Main file:  
👉 :contentReference[oaicite:0]{index=0}

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install streamlit
