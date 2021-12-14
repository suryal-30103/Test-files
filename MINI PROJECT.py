state_dict= { "andhra pradesh": "Tirupati , Vizag , Vijaywada , Amravathi , Kakinada , Rajahmundry , Chitoor , Kadapa , Nellore , Rajole , Gudur",
"arunachal pradesh": "Tawang , Zero , Itanagar , Bomdila , Pasighat", 
"assam": "Guwahati , Silchar , Dibrugarh , Jorhat , Nagaon", 
"bihar": "Patna , Gaya , Bhagalpur , Muzzafarpur , Dharbhanga",
"chattisgarh": "Raipur , Bilaspur , Durg , Janjgir-Champa , Rajnandgaon ",
"goa": "Panaji , Madgaon , Mormugao , Mapuca , Ponda",
"gujurat" : "Gandhi nagar , Ahmedabad , Surat , Vadodara , Rajkot , Bhavnagar",
"haryana" : "Faridabad , Gurugram , Chandigarh , Panipat , Ambala , Yamunanagar",
"himachal pradesh" : "Shimla , Solan , Kullu, Baddi , Mandi",
"jharkand" : "Jamshedpur , DhanbadRanchi , Bokaro Steel City , Deoghar",
"karnataka" : "Bengaluru, Hubballi-Dharwad , Mysuru , Davangere , Mangaluru, Tumkur, Chikkamagaluru ",
"kerala" : "Thiruvananthapuram, Kozhikode, Kochi, Kollam, Thrissur, Kannur",
"madhya pradesh" : "Indore, Bhopal, Jabalpur, Gwalior, Ujjain, Sagar",
"maharashtra" : "Mumbai, Pune, Nagpur, Thane, Nashik, Amravati, Nashik,",
"manipur": "Imphal, Imphal, Bishnupur, Senapati, Chandel, Tamenglong, Ukhrul",
"meghalaya": "Shillong, Cherrapunji, Guwahait, Tura, Baghamra, Nongstoin, Garo hills, ",
"mizoram": "Aizawl, Champhai, Kolasib, Lawngtlai, Lunglei, Mamit, Saiha, Serchhip",
"nagaland":"Dimapur, Kohima, Soma, Tuensang",
"odisha" : "Bhubaneswar, Cuttack, Rourkela, Berhampur, Sambalpur, Puri, Balasore",
"punjab": "Amritsar, Ludhiana, Jalandhar, Patiala, Bathinda, ,Mohali",
"rajasthan": "Jaipur, Ajmer, Jodhpur, Kota, Bhiwadi, Bikaner,Udaipur",
"sikkim": " Gangtok, Pelling, Lachung, Lachung, Yuksom, ",
"tamil nadu": "Chennai, Coimbatore, Madurai, Tiruchirappalli, Salem, Tirunelveli, Tiruppur, Vellore, Thoothukkudi",
"telangana": "Hyderabad, Warangal, Nizamabad, Khammam, Karimnagar, Peddapalli, Suryapet",
"tripura": "Agartala, Dharmanagar, Udaipur, Kailashahar, Bishalgarh, ",
"uttar pradesh": "Kanpur, Lucknow, Ghaziabad, Agra, Meerut, Varanasini, Prayagraj",
"uttarakhand": "Dehradun, Haridwar, Roorkee, Rudrapur, Kashipur",
"west bengal": "Kolkata , Asansol, Siliguri, Durgapur, Bardhaman, Malda, Baharampur"}

print("Welcome to know important cities of all states in India")
def state():
    name=str(input("Enter state of india to know its important cities(in lower cases only):-"))
    if name in state_dict.keys():
        print('Important cities of the state',name,'are--->',state_dict.get(name))
    
        cont=input('Do you want to know for other states?(type Y/N):-')
        if cont=='Y':
            state()
        elif cont=='N':
            print('Thank you!!!')
    else:
        print('Given name does not exist')
        
        cont=input('Do you want to know for other states?(type Y/N):-')
        if cont=='Y':
            state()
        elif cont=='N':
            print('Thank you!!!')
       
        
state()
    
