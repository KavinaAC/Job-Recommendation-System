import sqlite3

# Connect to SQLite database (creates jobs.db if not exists)
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Create jobs table with job type, salary range & certification courses
cursor.execute('''
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    job_type TEXT NOT NULL,
    salary_range TEXT NOT NULL,
    certifications TEXT NOT NULL
)
''')

# Insert jobs only if table is empty
cursor.execute("SELECT COUNT(*) FROM jobs")
if cursor.fetchone()[0] == 0:  
    cursor.executemany('''
    INSERT INTO jobs (title, description, salary_range, certifications) VALUES (?, ?, ?, ?, ?)
    ''', [
        ("Software Engineer", "Looking for Python developer with experience in Flask and APIs.", "$70,000 - $100,000", "Python Developer Certification, AWS Certified Developer"),
        ("Data Scientist", "Requires experience in machine learning, NLP, and Python.", "$80,000 - $120,000", "TensorFlow Developer Certificate, IBM Data Science Professional"),
        ("Web Developer", "Must have skills in HTML, CSS, JavaScript, and React.", "$50,000 - $80,000", "Full Stack Web Developer by Udacity, Google Mobile Web Specialist"),
        ("AI Engineer", "Expert in deep learning, TensorFlow, PyTorch, and AI models.","$90,000 - $150,000", "Deep Learning Specialization (Coursera), AI For Everyone"),
        ("Backend Developer", "Strong experience in Node.js, Express, and databases.", "$75,000 - $110,000", "Node.js Certification, MongoDB Developer Associate"),
        ("Cloud Engineer", "AWS, Azure, Cloud Architecture, Kubernetes, Docker", "$85,000 - $130,000", "AWS Certified Solutions Architect, Google Cloud Professional Cloud Architect"),
        ("Cybersecurity Analyst", "Network Security, Firewalls, Ethical Hacking, SIEM", "$90,000 - $140,000", "Certified Ethical Hacker (CEH), CISSP"),
        ("Mobile App Developer", "Swift, Kotlin, React Native, Flutter, Mobile UI/UX", "$70,000 - $110,000", "Google Associate Android Developer, iOS App Development with Swift"),
        ("Blockchain Developer", "Ethereum, Solidity, Smart Contracts, Hyperledger", "$100,000 - $160,000", "Certified Blockchain Developer, Ethereum Developer Certification"),
        ("DevOps Engineer", "CI/CD, Kubernetes, Docker, Terraform, Jenkins", "$95,000 - $145,000", "Docker Certified Associate, Kubernetes Administrator Certification"),
        ("Game Developer", "Unity, Unreal Engine, C#, Game Physics, AI", "$80,000 - $120,000", "Unity Certified Developer, Unreal Engine Certification"),
        ("Embedded Systems Engineer", "C, C++, Embedded Linux, Microcontrollers", "$85,000 - $125,000", "Certified Embedded Systems Engineer, ARM Accredited Engineer"),
        ("IT Support Specialist", "Troubleshooting, Windows, Linux, Networking", "$50,000 - $75,000", "CompTIA A+, Microsoft Certified IT Professional"),
        ("Network Engineer", "Routing, Switching, Firewall, VPN, SD-WAN", "$80,000 - $130,000", "Cisco CCNA, Juniper Networks Certified Associate"),
        ("AI Researcher", "Deep Learning, Reinforcement Learning, Neural Networks", "$120,000 - $180,000", "Deep Learning Specialization (Coursera), AI For Everyone"),
        ("Data Engineer", "Big Data, ETL, Spark, Hadoop, Cloud Data Platforms", "$95,000 - $140,000", "Google Cloud Data Engineer, AWS Big Data Specialty"),
        ("Database Administrator", "SQL, NoSQL, Performance Tuning, Backup/Recovery", "$85,000 - $125,000", "Oracle Certified MySQL DBA, Microsoft SQL Server Certification"),
        ("IT Project Manager", "Agile, Scrum, Jira, Risk Management", "$90,000 - $135,000", "PMP Certification, Certified Scrum Master (CSM)"),
        ("VR Developer", "Unity, Unreal Engine, C#, VR SDKs, 3D Modeling", "$85,000 - $130,000", "Unity Certified VR Developer, Oculus Developer Certification"),
        ("E-Commerce Developer", "Shopify, Magento, WooCommerce, Payment APIs", "$70,000 - $110,000", "Shopify Partner Academy, Magento Certified Developer"),
        ("Front-End Developer", "HTML, CSS, JavaScript, React, Vue.js", "$60,000 - $100,000", "Certified Web Developer, JavaScript Developer Certification"),
        ("Back-End Developer", "Node.js, Python, PHP, REST APIs, Databases", "$75,000 - $115,000", "Node.js Certification, PHP Developer Certification"),
        ("Full-Stack Developer", "React, Node.js, Databases, APIs, Git", "$85,000 - $130,000", "Full Stack Web Developer by Udacity, Google Mobile Web Specialist"),
        ("Software Architect", "System Design, Microservices, Cloud, Scalability", "$110,000 - $170,000", "AWS Certified Solutions Architect, Microsoft Azure Architect"),
        ("AI Product Manager", "AI Strategy, Product Development, Business Intelligence", "$100,000 - $150,000", "AI Product Management Specialization, IBM AI Certification"),
        ("Penetration Tester", "Ethical Hacking, Penetration Testing, Cybersecurity", "$90,000 - $140,000", "Offensive Security Certified Professional (OSCP), CEH"),
        ("Machine Learning Engineer", "ML Models, TensorFlow, PyTorch, NLP", "$110,000 - $160,000", "Google Machine Learning Engineer, TensorFlow Developer Certificate"),
        ("Game Designer", "Game Mechanics, Level Design, UI/UX, Storyboarding", "$75,000 - $120,000", "Game Design Certificate, Unity Game Development"),
        ("Automation Engineer", "Scripting, CI/CD, Ansible, DevOps, Jenkins", "$85,000 - $130,000", "Certified Automation Engineer, Jenkins Certification"),
        ("IoT Developer", "IoT Devices, MQTT, Embedded Systems, Cloud IoT", "$90,000 - $135,000", "Certified IoT Developer, Cisco IoT Specialist"),
        ("Cloud Security Engineer", "Cloud Security, IAM, Encryption, Zero Trust", "$95,000 - $145,000", "AWS Security Specialty, Google Cloud Security Engineer"),
        ("NLP Engineer", "Text Processing, Chatbots, Speech Recognition, BERT", "$110,000 - $165,000", "Deep Learning for NLP, Stanford NLP Certification"),
        ("Big Data Engineer", "Hadoop, Spark, Kafka, Data Warehousing", "$100,000 - $150,000", "Cloudera Certified Data Engineer, Google Data Engineer"),
        ("Digital Marketing Analyst", "SEO, PPC, Google Ads, Data Analytics", "$60,000 - $100,000", "Google Analytics Certification, HubSpot Content Marketing Certification"),
        ("Robotics Engineer", "ROS, AI, Automation, Mechatronics, Sensors", "$95,000 - $145,000", "Certified Robotics Engineer, ROS Developer Certification"),
        ("Hardware Engineer", "PCB Design, VLSI, FPGA, Embedded Systems", "$85,000 - $125,000", "Certified Hardware Engineer, Intel FPGA Developer"),
        ("VR/AR Developer", "3D Modeling, ARKit, Unity, Unreal Engine", "$90,000 - $140,000", "Unity AR/VR Certification, Oculus Developer Certification"),
        ("Product Manager", "Product Strategy, Agile, Business Analysis", "$95,000 - $145,000", "Certified Scrum Product Owner, PMI Agile Certified Practitioner"),
        ("UI/UX Designer", "Wireframing, Figma, Adobe XD, User Research", "$70,000 - $110,000", "Google UX Design Certification, Adobe Certified Expert"),
        ("Security Engineer", "Threat Analysis, Cybersecurity, Network Security", "$95,000 - $145,000", "CISSP, Offensive Security Certified Professional (OSCP)"),
        ("Data Analyst", "Excel, SQL, Tableau, Data Visualization", "$70,000 - $110,000", "Google Data Analytics Professional Certificate, Tableau Certification"),
        ("Systems Administrator", "Linux, Windows, Cloud Infrastructure, Scripting", "$75,000 - $115,000", "Microsoft Certified: Azure Administrator, CompTIA Server+"),
        ("Technical Support Engineer", "Troubleshooting, Windows, Linux, Networking", "$50,000 - $85,000", "CompTIA A+, Microsoft Certified Solutions Expert"),
        ("Autonomous Systems Engineer", "Robotics, AI, Sensor Fusion, Control Systems", "$110,000 - $160,000", "Autonomous Systems Certification, ROS Developer Certification"),
        ("Biomedical Engineer", "Medical Devices, Biomechanics, Signal Processing", "$85,000 - $130,000", "Certified Biomedical Equipment Technician (CBET)"),
        ("Cryptography Engineer", "Encryption, Public Key Infrastructure, Blockchain", "$100,000 - $150,000", "Certified Encryption Specialist, CISSP"),
        ("Firmware Engineer", "Embedded C, RTOS, Microcontrollers, Hardware Integration", "$90,000 - $140,000", "Certified Embedded Systems Engineer, ARM Accredited Engineer"),
        ("Geospatial Analyst", "GIS, Remote Sensing, Cartography, GPS", "$80,000 - $120,000", "GIS Certification, ESRI ArcGIS Specialist"),
        ("Cloud Database Administrator", "Cloud Databases, SQL, NoSQL, Backup Strategies", "$95,000 - $140,000", "Google Cloud Certified - Professional Data Engineer"),
        ("E-Learning Developer", "LMS, SCORM, Instructional Design, E-Learning Platforms", "$65,000 - $100,000", "Certified Instructional Designer, Adobe Captivate Certification"),
        ("Quantum Computing Researcher", "Quantum Algorithms, Qiskit, Quantum Cryptography", "$120,000 - $180,000", "Quantum Computing Specialization, IBM Quantum Developer"),
        ("Space Systems Engineer", "Aerospace Engineering, Orbital Mechanics, Satellite Design", "$100,000 - $160,000", "Certified Space Engineer, NASA Systems Engineering"),
        ("Bioinformatics Scientist", "Genomics, Machine Learning, Computational Biology", "$90,000 - $140,000", "Certified Bioinformatics Professional, Coursera Genomics Specialization"),
        ("Nanotechnology Engineer", "Nanomaterials, Quantum Mechanics, Molecular Biology", "$95,000 - $150,000", "Nanotechnology Certification, IEEE Nanotechnology Council"),
        ("Renewable Energy Engineer", "Solar Energy, Wind Power, Battery Storage Systems", "$85,000 - $130,000", "Certified Renewable Energy Professional, Solar PV Installer Certification"),
        ("Haptic Technology Engineer", "Haptic Feedback, Sensors, VR/AR, Robotics", "$90,000 - $140,000", "Haptic Technology Certification, IEEE Sensors Council"),
        ("Digital Twin Engineer", "Simulation, IoT, Cloud Platforms, Predictive Analytics", "$100,000 - $150,000", "Certified Digital Twin Developer, IBM Digital Twin Certification"),
        ("Cognitive Neuroscientist", "Neuroimaging, Brain-Computer Interface, Psychology", "$90,000 - $140,000", "Neuroscience Certification, Harvard Cognitive Science Program"),
        ("Ethical AI Researcher", "Fair AI, Bias Mitigation, Explainable AI, ML Ethics", "$100,000 - $160,000", "AI Ethics Certification, AI Fairness Specialization"),
        ("Mixed Reality Developer", "AR, VR, XR, 3D Modeling, Unity, Unreal Engine", "$90,000 - $140,000", "Unity Mixed Reality Certification, Microsoft HoloLens Developer"),
        ("Legal Tech Engineer", "AI in Law, NLP, Legal Document Processing", "$90,000 - $140,000", "LegalTech Certificate, AI in Law Specialization"),
        ("Digital Forensics Analyst", "Cybercrime Investigation, Data Recovery, Malware Analysis", "$90,000 - $140,000", "Certified Computer Forensics Examiner (CCFE)"),
        ("Biomechanics Engineer", "Kinesiology, Motion Analysis, Medical Device Development", "$85,000 - $130,000", "Certified Clinical Biomechanics Specialist"),
        ("Biohacker", "DIY Biology, CRISPR, Genetic Engineering, Human Augmentation", "$80,000 - $130,000", "Biotechnology Certification, CRISPR Specialization"),
        ("Edge AI Engineer", "AI on Edge Devices, Low-Power AI, TinyML", "$100,000 - $150,000", "TinyML Certification, Edge AI Developer Program"),
        ("Sensor Fusion Engineer", "Sensor Data Processing, Robotics, IoT", "$90,000 - $140,000", "IoT Sensor Fusion Certification, Robotics Specialization"),
        ("Astrobiologist", "Exoplanet Research, Microbiology, Space Science", "$90,000 - $140,000", "Astrobiology Specialization, NASA Research Program"),
        ("Neural Interface Engineer", "Brain-Computer Interface, Neural Networks, EEG", "$110,000 - $160,000", "Brain-Machine Interface Certification, Neural Engineering"),
        ("Synthetic Biologist", "Genetic Engineering, CRISPR, Bioprinting", "$100,000 - $150,000", "Synthetic Biology Certification, Genetic Engineering Program"),
        ("Quantum AI Developer", "Quantum ML, Qiskit, TensorFlow Quantum", "$120,000 - $180,000", "Quantum AI Certification, Google Quantum Research"),
        ("Human-Robot Interaction Engineer", "AI, NLP, Robotics, Psychology", "$100,000 - $150,000", "Human-Robot Interaction Certification"),
        ("Automotive AI Engineer", "Self-Driving Cars, LiDAR, Perception Systems", "$110,000 - $160,000", "Self-Driving Car Engineer Nanodegree"),
        ("Aerospace AI Researcher", "AI in Aviation, Space Robotics, Satellite AI", "$110,000 - $170,000", "Aerospace AI Certification, NASA AI Program"),
        ("Cyborg Technology Developer", "Wearable Tech, Neural Implants, AI Augmentation", "$110,000 - $170,000", "Neural Implant Certification, AI & Wearable Tech"),
        ("AI-Powered Cybersecurity Expert", "AI for Threat Detection, Adversarial ML, Cyber Threats", "$110,000 - $165,000", "AI in Cybersecurity Certification"),
        ("Tissue Engineer", "Bioprinting, Stem Cells, Regenerative Medicine", "$95,000 - $145,000", "Tissue Engineering Specialization, Bioprinting Certification"),
        ("Climate Data Scientist", "Climate Modeling, Remote Sensing, AI in Climate Science", "$90,000 - $140,000", "Climate Data Science Specialization"),
        ("Smart Agriculture Engineer", "IoT in Agriculture, Precision Farming, AI for Crops", "$85,000 - $130,000", "Precision Agriculture Certification"),
        ("Urban AI Planner", "AI in City Planning, Smart Cities, GIS", "$90,000 - $140,000", "Urban AI Planning Certification"),
        ("AI-Generated Art Expert", "GANs, DeepDream, AI Art Models", "$80,000 - $130,000", "AI Art & Creativity Specialization"),
        ("Neurotech Startup Founder", "AI in Neuroscience, Brain-Machine Interfaces", "$110,000 - $170,000", "Neurotech Entrepreneurship Certification"),
        ("AI in Music Engineer", "AI-Generated Music, Neural Audio, MIDI AI", "$80,000 - $130,000", "AI in Music Certification"),
        ("AR Navigation Developer", "AI Navigation Systems, AR Maps, 3D GPS", "$90,000 - $140,000", "Augmented Reality Navigation Certification"),
        ("AI-Powered Healthcare Researcher", "AI in Diagnostics, Medical Imaging, Deep Learning", "$110,000 - $165,000", "AI in Healthcare Certification"),
        ("5G Network Engineer", "5G Architecture, Wireless Communication, Edge Computing", "$90,000 - $140,000", "5G Technology Certification"),
        ("Holographic Display Engineer", "Holography, 3D Display, Light Field Technology", "$100,000 - $150,000", "Holographic Technology Certification"),
        ("AI-Powered Content Creator", "AI in Writing, GPT Models, Automated Journalism", "$75,000 - $115,000", "AI Content Creation Certification"),
        ("Metaverse Developer", "Blockchain, VR, Digital Assets, Smart Contracts", "$90,000 - $150,000", "Metaverse Developer Certification"),
        ("AI-Powered Finance Analyst", "AI in Trading, Algorithmic Finance, Financial AI", "$100,000 - $150,000", "AI in Finance Certification")
])
    
    conn.commit()  # Save changes

# Close connection
conn.close()
print("✅ Database initialized with salary range & certifications!")
