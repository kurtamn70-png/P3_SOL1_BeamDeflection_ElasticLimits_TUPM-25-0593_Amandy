# Aircraft Wing Spar: Structural Health Monitoring
> **Data-Driven Analysis of Beam Deflection and Elastic Limits**

![Wing Spar Animation](./outputs/structural_response.gif)

## Project Overview
This repository contains a computational pipeline for monitoring the structural health of an aircraft wing spar. By processing telemetry from **Node 19**, the system validates the proportional relationship between aerodynamic load factors (G) and structural deflection (mm), ensuring the airframe operates within safe mechanical limits.

## Key Features
* **Automated Data Cleaning:** Handles missing sensor packets and isolates specific node telemetry.
* **Statistical Validation:** Verified a Pearson Correlation Coefficient (r) of **0.9998**.
* **Dynamic Visualization:** Interactive Plotly models optimized for web deployment.
* **Performance Optimization:** Implemented data decimation to reduce HTML payload for GitHub Pages.

---

## Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-222222?style=for-the-badge&logo=GitHub&logoColor=white)

---

## Repository Structure
* `data/`: Raw CSV telemetry dataset.
* `outputs/`: Generated GIF, static plots, and interactive HTML models.
* `main.py`: Core logic for data processing and analysis.
* `requirements.txt`: Environment dependencies.

---

## Live Simulation
Access the interactive digital twin here:  
[View Live Wing Spar Animation](https://kurtamn70-png.github.io/EDS_TUPM-25-0593_Amandy/outputs/animation_structural_response.html)

---

**Student:** Kurt Andrew Amandy  
**Student ID:** TUPM-25-0593  
**Institution:** Technological University of the Philippines - Manila