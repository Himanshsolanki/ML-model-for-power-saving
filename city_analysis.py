import random
import time
import os

# --- SYSTEM STATE ---
sensor_fault = False
diag_msg = "System Healthy."

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    print("🏙️  CITY ANALYSIS ENGINE: DATA GATHERING & ML INFERENCE")
    print("="*65)

    # 1. RAW SENSOR INPUTS (MATCHING APP.PY)
    if random.random() < 0.05 and not sensor_fault:
        sensor_fault = True
        diag_msg = "⚠️ ALERT: Inconsistent data! Fans/Street lights may be stuck."

    if sensor_fault:
        ldr, people_count, wifi_ids, us_dist, hum = 0, 0, 0, 0, 0
        occ_rooms, empty_rooms, crit_rooms = 0, 0, 0
        lock_side = "N/A"
        pwm_val, signal_status = 0, "RED"
    else:
        ldr = random.randint(0, 100)
        people_count = random.randint(0, 50)
        wifi_ids = random.randint(0, 150)
        us_dist = random.randint(20, 300)
        hum = random.randint(30, 95)
        lock_side = random.choice(["Inside", "Outside"])
        
        # Hospital Room Logic
        crit_rooms = 5
        occ_rooms = min(20, int(people_count / 2))
        empty_rooms = max(0, 25 - occ_rooms - crit_rooms)

    # 2. SECTOR ANALYSIS (WHY DID THE AI CHOOSE THIS?)

    # STREET & TRAFFIC SEPARATION
    signal_status = "GREEN" if people_count > 10 else "RED"
    if ldr > 75:
        s_act, s_pwm, s_plan = "OFF", 0, "Lights OFF (0% PWM). Solar energy sufficient."
    elif people_count > 5:
        s_act, s_pwm, s_plan = "FULL", 100, "100% PWM. AI suppressed red light to prevent Idling Waste."
    else:
        s_act, s_pwm, s_plan = "DIM", 30, "30% PWM to save battery. Presence sensors active."

    # HOSPITAL ZONES
    h_act = "MAX_POWER" if occ_rooms > 12 else "ZONE_MODE"
    h_plan = "Critical zones at 100%. Empty wards on 30% Eco-dimming."

    # PARKING (ULTRASOUND + LDR)
    p_act = "BRIGHT" if (ldr < 35 and us_dist < 100) else "ECO"
    p_plan = "Providing live spot data via Ultrasonic sensor to reduce searching."

    # MALL (WIFI + LDR + PIR)
    m_act = "FULL_LIGHT" if (wifi_ids > 80 or people_count > 20 or ldr < 30) else "ECONO_MODE"
    m_plan = "Fusing Wi-Fi and PIR for demand-based HVAC/Lighting."

    # HOUSE (DIRECTIONAL LOCK)
    h_v = "SHUTDOWN" if lock_side == "Outside" else f"ON ({'Fan' if hum > 75 else 'Lights'})"
    h_plan_home = "Total power cut. House empty." if lock_side == "Outside" else "Active for comfort."

    # 3. TERMINAL DISPLAY (ORGANIZED BY SECTOR)
    print(f"[STREET]   Mode: {s_act} | PWM: {s_pwm}% | Signal: {signal_status}")
    print(f"           Data: LDR {ldr}% | People {people_count} | Plan: {s_plan}")
    print("-" * 65)
    print(f"[HOSPITAL] Mode: {h_act} | Occ: {occ_rooms} | Eco: {empty_rooms} | Crit: {crit_rooms}")
    print(f"           Plan: {h_plan}")
    print("-" * 65)
    print(f"[PARKING]  Mode: {p_act} | US Dist: {us_dist}cm | LDR: {ldr}%")
    print(f"           Plan: {p_plan}")
    print("-" * 65)
    print(f"[MALL]     Mode: {m_act} | Wi-Fi: {wifi_ids} | PIR: {people_count} | LDR: {ldr}%")
    print(f"           Plan: {m_plan}")
    print("-" * 65)
    print(f"[HOME]     Mode: {h_v} | Lock: {lock_side} | Humidity: {hum}%")
    print(f"           Plan: {h_plan_home}")
    print("="*65)

    # 4. DIAGNOSTIC FOOTER
    if sensor_fault:
        print(f"DIAGNOSTIC ALERT: {diag_msg}")
    else:
        print("SYSTEM HEALTH: All sensors calibrated (New Zero active).")
    
    time.sleep(2)
