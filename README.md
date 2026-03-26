# 🚀 AI-Powered Cargo Inspection System (ELEVATIA)

An intelligent web-based application designed for **customs and border security** to automatically detect **suspicious, misdeclared, or prohibited objects** in cargo X-ray images using advanced **AI/ML and Deep Learning techniques**.

---

## 🎯 Project Overview

Manual cargo inspection is slow and error-prone. Our system uses **Computer Vision + Deep Learning** to automate the detection process and improve accuracy, speed, and security.

---

## 🧠 Key Features

* 🔍 **Object Detection (YOLOv8)**
  Detects multiple objects in cargo images with bounding boxes

* ⚠️ **Suspicious Item Detection**
  Identifies prohibited or unusual items

* 📊 **Risk Scoring System**
  Classifies cargo as **Low / Medium / High Risk**

* 🖼️ **X-ray Style Visualization**
  Displays results like real cargo scanners with bounding boxes

* 🤖 **AI Chatbot Assistant**
  Explains detection results and answers user queries

* 🔐 **Role-Based Authentication**

  * Student (limited access)
  * Government Officer (full access)
  * Admin (control panel)

* 📁 **Inspection Logs**
  Stores past scan results for analysis

---

## 🏗️ System Architecture

```
User → Web App (React)
     → Upload Image
     → Backend API (FastAPI)
     → AI Model (YOLOv8 + Autoencoder)
     → Risk Scoring Engine
     → Database (Logs)
     → Chatbot System
     → Dashboard Output
```

---

## ⚙️ Tech Stack

* **Frontend:** React.js
* **Backend:** FastAPI (Python)
* **AI Models:** YOLOv8, Autoencoder
* **Database:** MongoDB / PostgreSQL
* **Authentication:** JWT (JSON Web Tokens)
* **Deployment:** Docker / Cloud

---

## 💻 How It Works

1. User logs in (role-based access)
2. Upload cargo X-ray image
3. AI model processes the image
4. Objects are detected and highlighted
5. Risk score is generated
6. Results displayed on dashboard
7. Chatbot provides explanation

---

## 🔐 Security Features

* Role-Based Access Control (RBAC)
* Secure authentication using JWT
* Protected APIs
* Audit logs

---

## ⚠️ Challenges & Risks

* Limited labeled X-ray datasets
* False positives / false negatives
* Complex cargo images (overlapping objects)
* Adversarial hiding techniques
* Chatbot hallucination risk

---

## 🚀 Future Enhancements

* Multi-modal AI (image + text data)
* Real-time CCTV integration
* Mobile application
* Advanced anomaly detection

![CargoGuard AI](https://github.com/user-attachments/assets/64213b77-68bc-4470-8c42-e024ad37a7fe)

![CargoGuard AI](https://github.com/user-attachments/assets/5e67b9e3-d884-4e86-90cb-61d84345e019)


