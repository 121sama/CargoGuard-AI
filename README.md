# 🚀 ELEVATIA – AI-Powered Cargo Inspection System

An advanced AI/ML-based web application designed for customs and border security to detect suspicious, misdeclared, or prohibited objects in cargo X-ray images.

---

## 📌 Problem Statement
Manual cargo inspection is slow, error-prone, and inefficient when dealing with large volumes of containers. Detecting hidden threats like weapons, drugs, or illegal items is challenging due to overlapping objects and complex cargo structures.

---

## 💡 Solution
ELEVATIA uses a hybrid AI pipeline combining Object Detection + Anomaly Detection to automatically analyze cargo images and identify potential threats in real time.

---

## 🧠 Key Features

- Object Detection (YOLOv8)  
- Anomaly Detection (Autoencoder)  
- Risk Scoring System (Low / Medium / High)  
- X-ray Visualization with bounding boxes  
- AI Chatbot Assistant  
- Role-Based Login System  
- Inspection Logs  

---

## 🏗️ System Architecture

User → Web App (React)  
→ Backend API (FastAPI)  
→ AI Model (YOLOv8 + Autoencoder)  
→ Risk Scoring Engine  
→ Database  
→ Chatbot  
→ Dashboard  

---

## ⚙️ Tech Stack

- Frontend: React.js  
- Backend: FastAPI (Python)  
- AI Models: YOLOv8, Autoencoder  
- Database: MongoDB / PostgreSQL  
- Authentication: JWT  

---

## 💻 How It Works

1. User logs in  
2. Upload cargo image  
3. AI processes image  
4. Objects detected  
5. Risk score generated  
6. Results shown with chatbot explanation  

![CargoGuard AI](https://github.com/user-attachments/assets/bf1d69b4-c946-423d-8ea8-143870c52055)




![CargoGuard AI2](https://github.com/user-attachments/assets/0117fd64-1cb1-4fcd-aab4-54b9a33cf1cd)
