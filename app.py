import streamlit as st
import random
import time

# 1. Setup the Page
st.set_page_config(page_title="Smart City Dashboard", layout="wide")
st.title("🏙️ Smart City AI: Simple Governance Dashboard")
st.markdown("---")

# Initialize Calibration Offsets for "New Zero"
if 'offsets' not in st.session_state:
    st.session_state.offsets = {"ldr": 0, "pir": 0}
if 'sensor_fault' not in st.session_state:
    st.session_state.sensor_fault = False

# 2. Sidebar: Tools & Diagnostic Alert
st.sidebar.header("🛠️ Tools")
emergency_mode = st.sidebar.toggle("🚨 Emergency Mode (Hospital/Traffic)", value=False)
st.sidebar.divider()

# Logic for "New Zero" Calibration
if st.sidebar.button("🔧 Fix All Sensors", type="primary"):
    with st.spinner("Recalibrating for New Zero Baseline..."):
        time.sleep(1.5) 
        st.session_state.sensor_fault = False
        # Capturing current "noise" as the new baseline offset
        st.session_state.offsets["ldr"] = random.randint(1, 5) 
        st.session_state.offsets["pir"] = random.randint(1, 3)
        st.session_state.diag_msg = "✅ Success: Established 'New Zero' baseline. Sensors recalibrated."
    st.toast(st.session_state.diag_msg)
    st.sidebar.success("Sensors re-aligned to baseline!")
else:
    if 'diag_msg' not in st.session_state:
        st.session_state.diag_msg = "System Healthy."

st.sidebar.divider()
st.sidebar.warning(f"🔔 **Diagnostic Alert**\n\n{st.session_state.diag_msg}")

# 3. Main Display Grid
st.header("What's Happening in the City?")
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1: street_ui = st.empty()
with col2: hosp_ui = st.empty()
with col3: park_ui = st.empty()
with col4: mall_ui = st.empty()
with col5: mist_ui = st.empty()
with col6: house_ui = st.empty()

st.divider()

# 4. Detailed Solution & Reasoning (LOCKED LAYOUT)
st.header("📋 Why did the AI choose this?")
bottom_reasoning = st.empty()

st.divider()

# 5. Sensor Health Check (NEW OFFSET METRICS)
st.header("🩺 Are the Sensors Working?")
health_ui = st.empty()

# 6. Manual Controls
st.header("🕹️ Take Control Manually")
m_col1, m_col2, m_col3 = st.columns(3)
m_col4, m_col5, m_col6 = st.columns(3)

options = ["AI Enable", "Full Power", "Power Off"]
mode_street = m_col1.selectbox("Traffic/Street", options, index=0)
mode_hosp = m_col2.selectbox("Hospital Power", options, index=0)
mode_park = m_col3.selectbox("Parking Lights", options, index=0)
mode_mall = m_col4.selectbox("Mall Lights", options, index=0)
mode_mist = m_col5.selectbox("Mist System", options, index=0)
mode_house = m_col6.selectbox("Home Appliances", options, index=0)

# 7. The Main Loop
while True:
    if random.random() < 0.05 and not st.session_state.sensor_fault: 
        st.session_state.sensor_fault = True
        st.session_state.diag_msg = "⚠️ ALERT: Inconsistent data! Drift detected in LDR/PIR."
        st.toast(st.session_state.diag_msg)

    if st.session_state.sensor_fault:
        ldr, people_count, wifi_devices, us_dist, hum = 0, 0, 0, 0, 0
        occ_rooms, empty_rooms, crit_rooms = 0, 0, 0
        pwm_val, signal_status = 0, "RED"
        lock_side = "N/A"
    else:
        # Applying the "New Zero" offset subtraction
        raw_ldr = random.randint(0, 100)
        raw_pir = random.randint(0, 50)
        ldr = max(0, raw_ldr - st.session_state.offsets["ldr"])
        people_count = max(0, raw_pir - st.session_state.offsets["pir"])
        
        wifi_devices = random.randint(0, 150) 
        us_dist = random.randint(20, 300) 
        hum = random.randint(30, 95)
        lock_side = random.choice(["Inside", "Outside"])
        
        # Hospital Criteria Logic
        crit_rooms = 5 
        occ_rooms = min(20, int(people_count / 2)) 
        empty_rooms = max(0, 25 - occ_rooms - crit_rooms)

    def get_status(mode, auto_act, auto_sol, auto_why, auto_proc):
        if mode == "Full Power":
            return "Full Power", "Human Override", "You forced this to be ON.", "AI bypassed."
        elif mode == "Power Off":
            return "Power Off", "Human Override", "You forced this to be OFF.", "Power cut completely."
        return auto_act, auto_sol, auto_why, auto_proc

    # 1. STREET Logic
    signal_status = "Green" if people_count > 10 else "Red"
    if ldr > 75:
        s_a, s_s, pwm_val = "Off", "Daylight Mode", 0
        s_w = f"Lights: {pwm_val}% (LDR: {ldr}%) | Signal: {signal_status}"
    elif people_count > 5:
        s_a, s_s, pwm_val = "Full", "Night Active", 100
        s_w = f"Lights: {pwm_val}% (PIR: {people_count}) | Signal: {signal_status}"
    else:
        s_a, s_s, pwm_val = "Dim", "Night Eco", 30
        s_w = f"Lights: {pwm_val}% (Empty) | Signal: {signal_status}"
    s_act, s_sol, s_why, s_proc = get_status(mode_street, s_a, s_s, s_w, "Managing Signal Phasing & PWM Dimming.")

    # 2. HOSPITAL Logic
    h_a = "Max Power" if (emergency_mode or occ_rooms > 12) else "Zone Governance"
    h_s = "Life Saving Mode" if h_a == "Max Power" else "Zone Governance"
    h_w = f"Rooms: {occ_rooms} Occ, {empty_rooms} Eco, {crit_rooms} Crit."
    h_p = "Critical zones locked at 100%. Occupied wards at Stable Power. Empty wards on 30% Eco dimming."
    h_act, h_sol, h_why, h_proc = get_status(mode_hosp, h_a, h_s, h_w, h_p)

    # 3. PARKING Logic
    p_a = "Bright" if (ldr < 35 and us_dist < 100) else "Eco"
    p_s = "Spot Active" if us_dist < 100 else "Spot Empty"
    p_w = f"US: {us_dist}cm | LDR: {ldr}%"
    p_p = "Providing live spot data to prevent fuel waste from searching."
    p_act, p_sol, p_why, p_proc = get_status(mode_park, p_a, p_s, p_w, p_p)

    # 4. MALL Logic (Multi-Sensor)
    m_a = "Full Light" if (wifi_devices > 80 or people_count > 20 or ldr < 30) else "Econo Mode"
    m_w = f"Wi Fi: {wifi_devices} | PIR: {people_count} | LDR: {ldr}%"
    m_p = "HVAC fans at 100% capacity. Maximum ventilation active."
    m_act, m_sol, m_why, m_proc = get_status(mode_mall, m_a, "Intelligent Mall", m_w, m_p)

    # 5. MIST Logic
    mist_a, mist_s, mist_w = ("Active", "Cooling ON", f"PIR: {people_count} ppl.") if people_count > 10 else ("Standby", "Cooling OFF", "Vacant.")
    mist_p = "Pumps active only for residents. Saves water and power."
    mist_act, mist_sol, mist_why, mist_proc = get_status(mode_mist, mist_a, mist_s, mist_w, mist_p)

    # 6. HOUSE Logic (Directional Lock)
    h_v, h_sol_a, h_why_a = (("Shutdown", "Exit Mode", "LDR: 0% | Lock: Out") if lock_side == "Outside" else (f"ON", "Inside Mode", f"Humid: {hum}% | Lock: In")) if not st.session_state.sensor_fault else ("Error", "Broken", "Sensor Fault")
    house_val, house_sol, house_why, house_proc = get_status(mode_house, h_v, h_sol_a, h_why_a, "Hostel Energy Management.")

    # --- REFRESH SCREEN ---
    with street_ui.container(): st.metric("Street/Traffic", str(s_act).title(), str(s_w))
    with hosp_ui.container(): st.metric("City Hospital", str(h_act).title(), str(h_w))
    with park_ui.container(): st.metric("Parking Lot", str(p_act).title(), str(p_w))
    with mall_ui.container(): st.metric("Urban Malls", str(m_act).title(), str(m_w))
    with mist_ui.container(): st.metric("Mist System", str(mist_act).title(), str(mist_w))
    with house_ui.container(): st.metric("Home Sector", str(house_val).title(), str(h_why_a))

    # Reasoning Section (LOCKED)
    with bottom_reasoning.container():
        b1, b2 = st.columns(2)
        with b1:
            st.info(f"**Street:** {s_sol}\n\n**Reason:** {s_why}\n\n**Action Plan:**\n{s_proc}")
            st.success(f"**Hospital:** {h_sol}\n\n**Reason:** {h_w}\n\n**Action Plan:**\n{h_p}")
            st.info(f"**Parking:** {p_sol}\n\n**Reason:** {p_w}\n\n**Action Plan:**\n{p_p}")
        with b2:
            st.info(f"**Mall:** {m_sol}\n\n**Reason:** {m_why}\n\n**Action Plan:**\n{m_p}")
            st.info(f"**Mist:** {mist_sol}\n\n**Reason:** {mist_w}\n\n**Action Plan:**\n{mist_p}")
            st.warning(f"**House:** {house_sol}\n\n**Reason:** {house_why}\n\n**Action Plan:**\n{house_proc}")

    with health_ui.container():
        h1, h2, h3, h4, h5 = st.columns(5)
        # Displaying active offsets for technical proof
        h1.metric("Light", f"{ldr}%", f"Offset: {st.session_state.offsets['ldr']}")
        h2.metric("Motion", f"{people_count} ppl", f"Offset: {st.session_state.offsets['pir']}")
        h3.metric("Ultrasonic", f"{us_dist}cm")
        h4.metric("Humidity", f"{hum}%")
        h5.metric("Wi Fi", f"{wifi_devices} ids")

    time.sleep(2)