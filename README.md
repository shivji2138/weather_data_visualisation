🌦️ Weather Data Visualization App\
🧠 Overview

This Python GUI application visualizes weather data (from a CSV file) using CustomTkinter, Matplotlib, and Pandas.
It allows users to explore weather insights like precipitation trends, temperature variations, and weather type distribution — all in a beautiful, modern interface.

🚀 Features

✅ Interactive GUI built with CustomTkinter
✅ Graphs rendered dynamically using Matplotlib
✅ Three visualizations:

🌧 Precipitation Trend – Plots precipitation vs. date

☁ Weather Type Distribution – Pie chart of weather categories

🌡 Minimum Temperature Trend – Shows temperature variation per day

✅ Blue-themed UI with rounded buttons
✅ CSV-driven — easy to update data without changing the code

🧩 Tech Stack -Component	Library \
GUI	-customtkinter \
Data Handling-	pandas \
Plotting-	matplotlib \
📂 Project Structure
📁 Weather-Data-Visualization
 ┣ 📜 weather_jan24.csv
 ┣ 📜 main.py
 ┗ 📜 README.md

⚙️ Installation & Setup

1️⃣ Clone this repo

git clone https://github.com/<your-username>/Weather-Data-Visualization.git
cd Weather-Data-Visualization


2️⃣ Install dependencies

pip install pandas matplotlib customtkinter


3️⃣ Add your dataset
Make sure weather_jan24.csv is present in the same directory.
Example CSV format:

date,precipitation,temp_min,weather
2024-01-01,12.5,21,Sunny
2024-01-02,8.3,19,Rainy
2024-01-03,0.0,23,Cloudy


4️⃣ Run the app

python main.py

🖼️ Screenshots

<img width="1118" height="845" alt="Screenshot 2025-10-28 201742" src="https://github.com/user-attachments/assets/12da9d6c-d0a7-4d8e-a25b-3a757581ee51" />
<img width="844" height="639" alt="Screenshot 2025-10-28 201801" src="https://github.com/user-attachments/assets/31251f71-8884-4fd7-839b-6f3f30877b48" />
<img width="845" height="627" alt="Screenshot 2025-10-28 201817" src="https://github.com/user-attachments/assets/22450368-720f-46be-b069-7a967376e882" />

 <img width="850" height="642" alt="image" src="https://github.com/user-attachments/assets/02c63fa5-35f7-4112-acf9-d08d588ff4a0" />


💡 Future Enhancements

Add month selector for dynamic data filtering

Export graphs as images

Add max temperature visualization

Integrate real-time weather API

👨‍💻 Author

Shiva Akash R
📍 SRM Institute of Science and Technology
💻 B.Tech Information Technology | 2025–2029
⭐ Aiming for creative, data-driven, and visually interactive Python apps
