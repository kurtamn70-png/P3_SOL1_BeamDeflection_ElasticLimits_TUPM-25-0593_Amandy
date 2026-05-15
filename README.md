# ✈️ Aircraft Wing Spar: Structural Health Monitoring
> **Validation of Elastic Limits using Node 19 Telemetry**

---

## 📖 About the Project
This project implements a data-driven pipeline to monitor the structural health of an aircraft wing spar. By analyzing the relationship between aerodynamic load factors and vertical deflection, we verify the material's structural integrity against theoretical elastic limits.

## 🚀 Key Features
* **Data Cleaning:** Automated removal of sensor noise and handling of missing telemetry packets.
* **Statistical Validation:** Calculation of the Pearson Correlation Coefficient ($r = 0.9998$).
* **Digital Twin Visualization:** Dynamic Plotly animations showing real-time deflection.
* **Optimized Deployment:** Lightweight HTML outputs hosted via GitHub Pages.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas, NumPy, Plotly
* **Version Control:** Git & GitHub Actions
* **Documentation:** IEEE Standard formatting

## 📂 Repository Structure
* `data/`: Contains the raw `.csv` telemetry.
* `outputs/`: Stores the generated GIF and interactive HTML models.
* `main.py`: The core processing script.
* `requirements.txt`: Project dependencies.

---

## 📊 Results Summary
The analysis confirms a strictly linear response, proving that the wing spar operates safely within the **Proportional Limit**. No plastic deformation was detected in the tested load range.

**Student:** Kurt Andrew Amandy  
**ID:** TUPM-25-0593