import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os
import time

load_dotenv()

my_token = os.getenv("AQI_API_TOKEN")

def get_health_label(aqi):
    try:
        aqi = int(aqi)
    except ValueError:
        return None
    
    if aqi is None:
        return "Unknown"
    if aqi <= 50:
        return "Low"
    elif aqi <= 100:
        return "Medium"
    else:
        return "High"


def fetch_aqi(city):
    url = f"https://api.waqi.info/feed/{city}/?token={my_token}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        if data["status"]=="ok":
            aqi_only = data["data"].get("aqi")
            aqi_data = data["data"]["iaqi"]
            dt = datetime.now()
            return{
                "City": city,
                "DateTime": dt,
                "AQI": aqi_only,
                "PM2.5": aqi_data.get("pm25", {}).get("v"),
                "PM10": aqi_data.get("pm10", {}).get("v"),
                "CO": aqi_data.get("co", {}).get("v"),
                "NO2": aqi_data.get("no2", {}).get("v"),
                "SO2": aqi_data.get("so2", {}).get("v"),
                "O3": aqi_data.get("o3", {}).get("v"),
                "Temp": aqi_data.get("t", {}).get("v"),
                "Humidity": aqi_data.get("h", {}).get("v"),
                "Wind": aqi_data.get("w", {}).get("v"),
                "Health_Risk": get_health_label(aqi_only)
            }
        else:
            return None
    else:
        print("HTTP Request Failed",res.status_code)


cities = ['Adoni', 'Amaravati', 'Anantapur', 'Chandragiri', 'Chittoor', 'Dowlaiswaram', 'Eluru', 'Guntur', 'Kadapa', 'Kakinada', 'Kurnool', 'Machilipatnam', 'Nagarjunakoṇḍa', 'Rajahmundry', 'Srikakulam', 'Tirupati', 'Vijayawada', 'Visakhapatnam', 'Vizianagaram', 'Yemmiganur', 'Arunachal Pradesh', 'Itanagar', 'Assam', 'Dhuburi', 'Dibrugarh', 'Dispur', 'Guwahati', 'Jorhat', 'Nagaon', 'Sivasagar', 'Silchar', 'Tezpur', 'Tinsukia', 'Bihar', 'Ara', 'Barauni', 'Begusarai', 'Bettiah', 'Bhagalpur', 'Bihar Sharif', 'Bodh Gaya', 'Buxar', 'Chapra', 'Darbhanga', 'Dehri', 'Dinapur Nizamat', 'Gaya', 'Hajipur', 'Jamalpur', 'Katihar', 'Madhubani', 'Motihari', 'Munger', 'Muzaffarpur', 'Patna', 'Purnia', 'Pusa', 'Saharsa', 'Samastipur', 'Sasaram', 'Sitamarhi', 'Siwan', 'Chandigarh (union territory)', 'Chandigarh', 'Chhattisgarh', 'Ambikapur', 'Bhilai', 'Bilaspur', 'Dhamtari', 'Durg', 'Jagdalpur', 'Raipur', 'Rajnandgaon', 'Dadra and Nagar Haveli and Daman and Diu (union territory)', 'Daman', 'Diu', 'Silvassa', 'Delhi (national capital territory)', 'Delhi', 'New Delhi', 'Goa', 'Madgaon', 'Panaji', 'Gujarat', 'Ahmadabad', 'Amreli', 'Bharuch', 'Bhavnagar', 'Bhuj', 'Dwarka', 'Gandhinagar', 'Godhra', 'Jamnagar', 'Junagadh', 'Kandla', 'Khambhat', 'Kheda', 'Mahesana', 'Morbi', 'Nadiad', 'Navsari', 'Okha', 'Palanpur', 'Patan', 'Porbandar', 'Rajkot', 'Surat', 'Surendranagar', 'Valsad', 'Veraval', 'Haryana', 'Ambala', 'Bhiwani', 'Chandigarh', 'Faridabad', 'Firozpur Jhirka', 'Gurugram', 'Hansi', 'Hisar', 'Jind', 'Kaithal', 'Karnal', 'Kurukshetra', 'Panipat', 'Pehowa', 'Rewari', 'Rohtak', 'Sirsa', 'Sonipat', 'Himachal Pradesh', 'Bilaspur', 'Chamba', 'Dalhousie', 'Dharmshala', 'Hamirpur', 'Kangra', 'Kullu', 'Mandi', 'Nahan', 'Shimla', 'Una', 'Jammu and Kashmir (union territory)', 'Anantnag', 'Baramula', 'Doda', 'Gulmarg', 'Jammu', 'Kathua', 'Punch', 'Rajouri', 'Srinagar', 'Udhampur', 'Jharkhand', 'Bokaro', 'Chaibasa', 'Deoghar', 'Dhanbad', 'Dumka', 'Giridih', 'Hazaribag', 'Jamshedpur', 'Jharia', 'Rajmahal', 'Ranchi', 'Saraikela', 'Karnataka', 'Badami', 'Ballari', 'Bengaluru', 'Belagavi', 'Bhadravati', 'Bidar', 'Chikkamagaluru', 'Chitradurga', 'Davangere', 'Halebid', 'Hassan', 'Hubballi-Dharwad', 'Kalaburagi', 'Kolar', 'Madikeri', 'Mandya', 'Mangaluru', 'Mysuru', 'Raichur', 'Shivamogga', 'Shravanabelagola', 'Shrirangapattana', 'Tumakuru', 'Vijayapura', 'Kerala', 'Alappuzha', 'Vatakara', 'Idukki', 'Kannur', 'Kochi', 'Kollam', 'Kottayam', 'Kozhikode', 'Mattancheri', 'Palakkad', 'Thalassery', 'Thiruvananthapuram', 'Thrissur', 'Ladakh (union territory)', 'Kargil', 'Leh', 'Madhya Pradesh', 'Balaghat', 'Barwani', 'Betul', 'Bharhut', 'Bhind', 'Bhojpur', 'Bhopal', 'Burhanpur', 'Chhatarpur', 'Chhindwara', 'Damoh', 'Datia', 'Dewas', 'Dhar', 'Dr. Ambedkar Nagar (Mhow)', 'Guna', 'Gwalior', 'Hoshangabad', 'Indore', 'Itarsi', 'Jabalpur', 'Jhabua', 'Khajuraho', 'Khandwa', 'Khargone', 'Maheshwar', 'Mandla', 'Mandsaur', 'Morena', 'Murwara', 'Narsimhapur', 'Narsinghgarh', 'Narwar', 'Neemuch', 'Nowgong', 'Orchha', 'Panna', 'Raisen', 'Rajgarh', 'Ratlam', 'Rewa', 'Sagar', 'Sarangpur', 'Satna', 'Sehore', 'Seoni', 'Shahdol', 'Shajapur', 'Sheopur', 'Shivpuri', 'Ujjain', 'Vidisha', 'Maharashtra', 'Ahmadnagar', 'Akola', 'Amravati', 'Aurangabad', 'Bhandara', 'Bhusawal', 'Bid', 'Buldhana', 'Chandrapur', 'Daulatabad', 'Dhule', 'Jalgaon', 'Kalyan', 'Karli', 'Kolhapur', 'Mahabaleshwar', 'Malegaon', 'Matheran', 'Mumbai', 'Nagpur', 'Nanded', 'Nashik', 'Osmanabad', 'Pandharpur', 'Parbhani', 'Pune', 'Ratnagiri', 'Sangli', 'Satara', 'Sevagram', 'Solapur', 'Thane', 'Ulhasnagar', 'Vasai-Virar', 'Wardha', 'Yavatmal', 'Manipur', 'Imphal', 'Meghalaya', 'Cherrapunji', 'Shillong', 'Mizoram', 'Aizawl', 'Lunglei', 'Nagaland', 'Kohima', 'Mon', 'Phek', 'Wokha', 'Zunheboto', 'Odisha', 'Balangir', 'Baleshwar', 'Baripada', 'Bhubaneshwar', 'Brahmapur', 'Cuttack', 'Dhenkanal', 'Kendujhar', 'Konark', 'Koraput', 'Paradip', 'Phulabani', 'Puri', 'Sambalpur', 'Udayagiri', 'Puducherry (union territory)', 'Karaikal', 'Mahe', 'Puducherry', 'Yanam', 'Punjab', 'Amritsar', 'Batala', 'Chandigarh', 'Faridkot', 'Firozpur', 'Gurdaspur', 'Hoshiarpur', 'Jalandhar', 'Kapurthala', 'Ludhiana', 'Nabha', 'Patiala', 'Rupnagar', 'Sangrur', 'Rajasthan', 'Abu', 'Ajmer', 'Alwar', 'Amer', 'Barmer', 'Beawar', 'Bharatpur', 'Bhilwara', 'Bikaner', 'Bundi', 'Chittaurgarh', 'Churu', 'Dhaulpur', 'Dungarpur', 'Ganganagar', 'Hanumangarh', 'Jaipur', 'Jaisalmer', 'Jalor', 'Jhalawar', 'Jhunjhunu', 'Jodhpur', 'Kishangarh', 'Kota', 'Merta', 'Nagaur', 'Nathdwara', 'Pali', 'Phalodi', 'Pushkar', 'Sawai Madhopur', 'Shahpura', 'Sikar', 'Sirohi', 'Tonk', 'Udaipur', 'Sikkim', 'Gangtok', 'Gyalshing', 'Lachung', 'Mangan', 'Tamil Nadu', 'Arcot', 'Chengalpattu', 'Chennai', 'Chidambaram', 'Coimbatore', 'Cuddalore', 'Dharmapuri', 'Dindigul', 'Erode', 'Kanchipuram', 'Kanniyakumari', 'Kodaikanal', 'Kumbakonam', 'Madurai', 'Mamallapuram', 'Nagappattinam', 'Nagercoil', 'Palayamkottai', 'Pudukkottai', 'Rajapalayam', 'Ramanathapuram', 'Salem', 'Thanjavur', 'Tiruchchirappalli', 'Tirunelveli', 'Tiruppur', 'Thoothukudi', 'Udhagamandalam', 'Vellore', 'Telangana', 'Hyderabad', 'Karimnagar', 'Khammam', 'Mahbubnagar', 'Nizamabad', 'Sangareddi', 'Warangal', 'Tripura', 'Agartala', 'Uttar Pradesh', 'Agra', 'Aligarh', 'Amroha', 'Ayodhya', 'Azamgarh', 'Bahraich', 'Ballia', 'Banda', 'Bara Banki', 'Bareilly', 'Basti', 'Bijnor', 'Bithur', 'Budaun', 'Bulandshahr', 'Deoria', 'Etah', 'Etawah', 'Faizabad', 'Farrukhabad-cum-Fatehgarh', 'Fatehpur', 'Fatehpur Sikri', 'Ghaziabad', 'Ghazipur', 'Gonda', 'Gorakhpur', 'Hamirpur', 'Hardoi', 'Hathras', 'Jalaun', 'Jaunpur', 'Jhansi', 'Kannauj', 'Kanpur', 'Lakhimpur', 'Lalitpur', 'Lucknow', 'Mainpuri', 'Mathura', 'Meerut', 'Mirzapur-Vindhyachal', 'Moradabad', 'Muzaffarnagar', 'Partapgarh', 'Pilibhit', 'Prayagraj', 'Rae Bareli', 'Rampur', 'Saharanpur', 'Sambhal', 'Shahjahanpur', 'Sitapur', 'Sultanpur', 'Tehri', 'Varanasi', 'Uttarakhand', 'Almora', 'Dehra Dun', 'Haridwar', 'Mussoorie', 'Nainital', 'Pithoragarh', 'West Bengal', 'Alipore', 'Alipur Duar', 'Asansol', 'Baharampur', 'Bally', 'Balurghat', 'Bankura', 'Baranagar', 'Barasat', 'Barrackpore', 'Basirhat', 'Bhatpara', 'Bishnupur', 'Budge Budge', 'Burdwan', 'Chandernagore', 'Darjeeling', 'Diamond Harbour', 'Dum Dum', 'Durgapur', 'Halisahar', 'Haora', 'Hugli', 'Ingraj Bazar', 'Jalpaiguri', 'Kalimpong', 'Kamarhati', 'Kanchrapara', 'Kharagpur', 'Cooch Behar', 'Kolkata', 'Krishnanagar', 'Malda', 'Midnapore', 'Murshidabad', 'Nabadwip', 'Palashi', 'Panihati', 'Purulia', 'Raiganj', 'Santipur', 'Shantiniketan', 'Shrirampur', 'Siliguri', 'Siuri', 'Tamluk', 'Titagarh']


records_list = []

for city in cities:
    records = fetch_aqi(city)
    if records:
        records_list.append(records)
        print(f"Data saved for {city}")
    else:
        print(f"data doesn't get saved for {city}...")

df = pd.DataFrame(records_list)

df.to_csv("weather_data.csv",index=False)
