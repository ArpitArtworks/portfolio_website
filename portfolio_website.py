import streamlit as st
import google.generativeai as genai

api_key_local = st.secrets["API_KEY"]
genai.configure(api_key = api_key_local)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hey :wave:")
    st.header("I am Arpit Saxena")
    st.write("As a Business Analyst, my goal is to help clients make better business decisions. I enable them to perform to higher standards by analysing complex data and developing countermeasures for business problem statements. "
             "In my current role, I analyse data on Cloud Supply Chain and present it an easy-to-follow manner to Senior Management.")

with col2:
    st.image("images/Arpit_Saxena.png")

persona = """ You are Arpit AI bot. You help people answer questions about your self (i.e Arpit)
Answer as if you are responding . dont answer in second or third person.
If you don't know they answer you simply say "That's a secret"
Here is more info about Arpit:
As a Business Analyst, my goal is to help clients make better business decisions. 
I enable them to perform to higher standards by analysing complex data and developing countermeasures forbusiness problem statements.
In my current role, I analyse data on Cloud Supply Chain and present it an easy-to-follow manner to Senior Management. 
If you want to know more, please email me at arpitsaxena91@gmail.com to start a chat.
Specialities: SQL, R, Python, Git, Machine Learning, Computer Vision, Artificial Intelligence, Tableau, PowerBI and Lean Six Sigma.
Job Experiences
Microsoft
Business Analyst - Microsoft Cloud Planning
January 2023 - Present (1 year 7 months)
Noida, Uttar Pradesh, India
Developing executive level dashboards empowering leadership team with visibility and actionable insights into the performance of key metrics.

Emeritus
Marketing Analytics - Senior Manager
September 2021 - January 2023 (1 year 5 months)
Bengaluru, Karnataka, India
Lead Analytics and Business Growth Advisor for various Digital Marketing functions - Email, Referral, Affiliate, Events.
Optimized Marketing Spends and Revenue across multiple marketing channels, countries and schools. 
Segmented 1.4 Million customers based on demographics in 5 clusters to improve Click-to-Open-Ratio.
Demographics: Work Experience, Region, Channel, Device, City
Segmented frequently contacted users in 4 clusters to improve Click-Open-Ratio.
Developed Tableau dashboards to gauge Affiliate, Zoom & Bigmarker Webinar and EMail Funnel performance for Lead Reactivation and Lead
Nurturing.
Structured UTM and campaign taxonomy for EMail Marketing.
Enhanced L2PA propensity by A/B experimentation.
Structured and automated content for 150+ different email templates to 8 standard templates using Python (Regex).

Flipkart
Data Analytics - Senior Manager
June 2021 - September 2021 (4 months)
Gurugram, Haryana, India
Internally promoted to Senior Manager within Flipkart-Myntra group.
Lead a team of 88 members : 9 in Data Analytics, 79 in Process Audit, 5S & Kaizen at Binola & Bilaspur FC.
Awarded for developing a Facial Recognition-based attendance management system using Computer Vision for Binola FC.

Myntra
1 year 8 months
Data Analytics - Senior Manager
April 2021 - May 2021 (2 months)
Gurugram, Haryana, India
Lead a team of 88 members : 9 in Data Analytics, 79 in Process Audit, 5S & Kaizen at Binola & Bilaspur FC.
Data Analytics - Manager
October 2019 - March 2021 (1 year 6 months)
Gurugram, Haryana, India
Lead a team of 56 members : 5 in Data Analytics, 51 in Process Audit, 5S & Kaizen
Projects implemented at pan India level
Live Dashboard at a refresh frequency of 10 minutes backed by SQL and Python queries for key metrics.
Live Flagging of key metrics when achievement is less than target using Google Apps Script.
FIFO Visualization of lots at Inwards for capacity enhancement by 7%.
Vendor Scorecard to provide star rating based on Shortage, AMM and rejection in lots.
Real time manpower scanner to reduce shift start production loss by 14 minutes.
Key Roles & Responsibility
Automation & sustenance of daily MIS, Dashboards [Tableau / Power BI] & Ad-Hoc reports.
Creation, Structuring and Automation of KPIs for Operation Managers.
Reduction in manpower cost through operational excellence from Rs 17.9 to Rs 16.3.
People power planning for FC on monthly basis.

Toyota Kirloskar Motor
Territory Manager
March 2016 - September 2019 (3 years 7 months)
Territory Manager for after-sales operations of Haryana state and Ludhiana, Sangrur & Chandigarh.
Platinum Award (Number 1 in India) for assigned dealer in 2018.
Forecasting, planning and distribution of 2018 Business Targets at dealer level for North Region. 
Recorded vehicle Inflow increased by 8%, with Units in operation increase of 11% in CY'18 for Haryana through Toyota Business Practice and PDCA
approach.

Zeros
Cofounder
January 2015 - March 2016 (1 year 3 months)
Delhi, India
Co-founder of an E-Commerce business for building one stop solution to connect all Doctors, Pharmacies and patients. 
Onboarded 44 Clinics, 280 Patients/day & 4 pharmacies and thousands of Medical Prescriptions online.
Everything from idea generation, strategy making, on-floor execution.
Data Analytics, Web-Designing, Recruitment, Team Management

Tata Motors
Customer Support Manager
August 2012 - January 2015 (2 years 6 months)
961 JDP CSI in 2014 at Hyderabad.
Improvement in Mumbai city Scores from 788 to 856 in JD Power, Customer Service Index for 2013
Headed tele-marketing project to improve operations through kaizens based on 25,000 Customer Voices
Headed Home Visit Campaigns for 7500 customers
Ensure service marketing products (Annual Maintenance Contract, Extended Warranty and Road Side Assistance) targets in order to increase customer
retention.
Co-ordinate with various vendors, supplier and internal team to resolve concerns.

Education
Liverpool John Moores University
Master's degree, Machine Learning and Artificial Intelligence · (December 2021 - December 2023)
International Institute of Information Technology Bangalore
Master of Science - MS, Machine Learning and Artificial Intelligence · (December 2021 - February 2023)

Delhi College of Engineering
B.E., Mechanical Engineering · (2008 - 2012)

List of 10 awards
1. Mountain Mover Award
Issued by Microsoft · Mar 2024
Awarded for initiating, planning, executing, monitoring and control of Reservation process.
2. AHSI Impact Award - People
Issued by Microsoft · Dec 2023
Outstanding collaboration and leadership for domain growth via Skill Enhancement and Employee Development (SEED) Learning Series.
3. CSCP "STELLAR QUEST" AWARDS - CULTURE CATALYST
Issued by Microsoft · Oct 2023
For playing a pivotal role in building & nurturing a strong & positive culture within CSCP.
4. Month of Learning Winner
Issued by Microsoft · Jun 2023Issued by Microsoft · Jun 2023
Winner in Month of Learning Challenge across Cloud Supply Chain during May 2023.
5. Week of Learning Winner
Issued by Microsoft · Feb 2023
Winner in Week of Learning Game across Cloud Supply Chain during 30 Jan - 3 Feb 2023.
6. Innovation Award
Issued by Flipkart · Aug 2021
Innovation Award from Flipkart for developing Computer Vision based Face Recognition tool.
7. Top Learner Award
Issued by Myntra · Jan 2021
Awarded for Top Learner across Myntra from Oct - Dec 2020.
8. Platinum Award
Issued by Toyota Kirloskar Motor · Jan 2019
Received the Platinum Award for successfully guiding the Car Dealership to achieve the topmost position across India.
9. Mountain Trekking
Issued by Tata Steel Adventure Foundation · Nov 2012
Trekked from Uttarkashi Base Camp (4500 ft) to Dayara Top (12500 ft) under Tata Steel Adventure Foundation from 9 Nov - 18 Nov, 2012 under esteemed leadership of Bachendri Pal ma'm.
10. Distinction in Mathematics
Issued by University of New South Wales · Dec 2004
Distinction in International Assessment for Indian Schools (Mathematics), Education Testing Centre, University of New South Wales, 2004.

List of 113 Certificates
100 Python Exercises : Evaluate and Improve Your Skills100 Python Exercises : Evaluate and Improve Your Skills
AB testing and Experimentation for BeginnersAB testing and Experimentation for Beginners
Ace Data Science InterviewsAce Data Science Interviews
AI and ML for Business LeadersAI and ML for Business Leaders
Applied Machine Learning Beginner to ProfessionalApplied Machine Learning Beginner to Professional
Become a learning machine 2.0 Read 300 books this yearBecome a learning machine 2.0 Read 300 books this year
Beginners Watercolor. Get clear on the basics and just paintBeginners Watercolor. Get clear on the basics and just paint
Colors for Data Science A-Z: Data Visualization Color THeoryColors for Data Science A-Z: Data Visualization Color THeory
Computer Vision using Deep LearningComputer Vision using Deep Learning
Data Engineering in 3 WeeksData Engineering in 3 Weeks
Data Ethics Making Data Driven DecisionsData Ethics Making Data Driven Decisions
Data Ethics Watching Out for Data MisuseData Ethics Watching Out for Data Misuse
Data Rights FoundationData Rights Foundation
Data Science Foundations: Choosing the Right DatabaseData Science Foundations: Choosing the Right Database
Data Steward FoundationsData Steward Foundations
Data VisualizationData Visualization
Dealing with Microaggression as an EmployeeDealing with Microaggression as an Employee
Describe cloud computingDescribe cloud computing
Describe cloud service typesDescribe cloud service types
Describe the benefits of using cloud servicesDescribe the benefits of using cloud services
Designing a better PowerPointDesigning a better PowerPoint
Difficult Conversations Talking about race at workDifficult Conversations Talking about race at work
Digital Transformation: 5 Game-Changing Technologies for BusinessDigital Transformation: 5 Game-Changing Technologies for Business
Effective ChatGPT PromptsEffective ChatGPT Prompts
Executive Briefing : Computer VisionExecutive Briefing : Computer Vision
Executive Post Graduate Programme in Machine Learning and Artificial IntelligenceExecutive Post Graduate Programme in Machine Learning and Artificial Intelligence
Explore the possibilities with Copilot for Microsoft 365Explore the possibilities with Copilot for Microsoft 365
Generative AI with Dan JeffriesGenerative AI with Dan Jeffries
Get People to Do StuffGet People to Do Stuff
Get started with Copilot for Microsoft 365Get started with Copilot for Microsoft 365
Get started with lakehouses in Microsoft FabricGet started with lakehouses in Microsoft Fabric
Give great presentationsGive great presentations
Google Digital UnlockedGoogle Digital Unlocked
Graphic Design Foundations: ColorGraphic Design Foundations: Color
Identify what M365 Copilot can do and what activities can be enhanced using generative AI.
Ingest Data with Dataflows Gen2 in Microsoft FabricIngest Data with Dataflows Gen2 in Microsoft Fabric
Integrate AI : Copilot Training CadetIntegrate AI : Copilot Training Cadet
Integrate AI ProgramIntegrate AI Program
Integrate AI: Copilot Flying AceIntegrate AI: Copilot Flying Ace
Integrate AI: Copilot Training CaptainIntegrate AI: Copilot Training Captain
Introduction to building apps for Microsoft TeamsIntroduction to building apps for Microsoft Teams
Introduction to Copilot for Microsoft 365Introduction to Copilot for Microsoft 365
Introduction to Data ScienceIntroduction to Data Science
Introduction to end-to-end analytics using Microsoft FabricIntroduction to end-to-end analytics using Microsoft Fabric
Leadership Communication SkillsLeadership Communication Skills
Lean Six Sigma FoundationsLean Six Sigma Foundations
Lean Six Sigma: Analyze, Improve, and Control ToolsLean Six Sigma: Analyze, Improve, and Control Tools
Lean Six Sigma: Define and Measure ToolsLean Six Sigma: Define and Measure Tools
Learning Data GovernanceLearning Data Governance
Learning FundamentalsLearning Fundamentals
Learning Microsoft 365 CopilotLearning Microsoft 365 Copilot
Learning MinitabLearning Minitab
Learning SOLID Programming PrinciplesLearning SOLID Programming Principles
Load data into a Microsoft Fabric data warehouseLoad data into a Microsoft Fabric data warehouse
Manage your managerManage your manager
Microsoft Azure Fundamentals: Describe Azure architecture and servicesMicrosoft Azure Fundamentals: Describe Azure architecture and services
Microsoft Azure Fundamentals: Describe Azure management and governanceMicrosoft Azure Fundamentals: Describe Azure management and governance
Microsoft Azure Fundamentals: Describe cloud conceptsMicrosoft Azure Fundamentals: Describe cloud concepts
Microsoft Build Challenge : Microsoft FabricMicrosoft Build Challenge : Microsoft Fabric
Microsoft Build Challenge: Microsoft FabricMicrosoft Build Challenge: Microsoft Fabric
Microsoft Certified Ready 2023Microsoft Certified Ready 2023
Microsoft Excel Beginners to AdvancedMicrosoft Excel Beginners to Advanced
Microsoft Global Hackathon 2023Microsoft Global Hackathon 2023
Microsoft Power BI Desktop for Business IntelligenceMicrosoft Power BI Desktop for Business Intelligence
Natural Language Processing (NLP) Using PythonNatural Language Processing (NLP) Using Python
Negotiation FundamentalsNegotiation Fundamentals
Operational Excellence FoundationsOperational Excellence Foundations
Optimize and extend Copilot for Microsoft 365Optimize and extend Copilot for Microsoft 365
Preparatory Course - EPGP in Machine Learning and Artificial IntelligencePreparatory Course - EPGP in Machine Learning and Artificial Intelligence
Process Improvement FoundationsProcess Improvement Foundations
Python A-Z : Python for Data Science with real exercisesPython A-Z : Python for Data Science with real exercises
Python face Recognition Using Webcam - Learn Computer VisionPython face Recognition Using Webcam - Learn Computer Vision
Root Cause Analysis : Getting to the Root of Business ProblemsRoot Cause Analysis : Getting to the Root of Business Problems
Scrum: The BasicsScrum: The Basics
Six Sigma FoundationsSix Sigma Foundations
Six Sigma: Green BeltSix Sigma: Green Belt
Six Sigma: White BeltSix Sigma: White Belt
Statistics Foundations 3 Using Data SetsStatistics Foundations 3 Using Data Sets
Statistics Foundations 4 Advanced TopicsStatistics Foundations 4 Advanced Topics
Statistics FoundationsStatistics Foundations
Storytelling Fundamentals for allStorytelling Fundamentals for all
Storytelling Masterclass Business Storytelling for LeadersStorytelling Masterclass Business Storytelling for Leaders
Streamlining Your Work with CopilotStreamlining Your Work with Copilot
Structured Query Language (SQL) for Data ScienceStructured Query Language (SQL) for Data Science
Structured Thinking and Communication for data Science ProfessionalsStructured Thinking and Communication for data Science Professionals
Tableau 10 A-Z Hands on Tableau Training for Data ScienceTableau 10 A-Z Hands on Tableau Training for Data Science
Tableau Visual Best Practices Go from Good to GREAT!Tableau Visual Best Practices Go from Good to GREAT!
Technical PresentationsTechnical Presentations
Use Apache Spark in Microsoft FabricUse Apache Spark in Microsoft Fabric
Use Data Factory pipelines in Microsoft FabricUse Data Factory pipelines in Microsoft Fabric
Verified International Academic QualificationsVerified International Academic Qualifications
What Is Generative AI?What Is Generative AI?
Work with Delta Lake tables in Microsoft FabricWork with Delta Lake tables in Microsoft Fabric
Writing with flair : How to become an exceptional writerWriting with flair : How to become an exceptional writer

Arpit's LinkedIn: https://www.linkedin.com/in/arpitsaxena-ai/
Blog: https://www.silentinvocation.wordpress.com/
Facebook:https://www.facebook.com/ArpitsArtworks
"""

st.title("Arpit's AI Bot")
st.write("Ask anything about me")
user_question = st.text_input("")
if st.button("ASK", use_container_width = 400):
    prompt = persona + "Here i sthe question that the user asked:" + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title("")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Blog : Silent Invocation")
    st.write("Success: An Illusion")
    st.write("Unsyced Energy At 4 Levels")
    st.write("Pleasure Is Pain")
    st.write("Happyness Found!")
    st.write("Death Is Life")
    st.write("Keeping Up With The Joneses")
    st.write("Ishavasya Upanishad")
    st.write("The Guru")
    st.write("मंगल भवन अमंगल हारी")
    st.write("Om Namah Shivay")

with col2:
    st.write("")
    st.write("https://silentinvocation.wordpress.com/")

st.title("My Skills")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.slider("Excel", 0, 100, 90)
    st.slider("SQL", 0, 100, 90)
    st.slider("Python", 0, 100, 90)

with col2:
    st.slider("Power BI", 0, 100, 90)
    st.slider("Tableau", 0, 100, 90)
    st.slider("Azure", 0, 100, 50)

with col3:
    st.slider("Machine Learning", 0, 100, 50)
    st.slider("Computer Vision", 0, 100, 80)
    st.slider("NLP", 0, 100, 50)

with col4:
    st.slider("Lean Six Sigma", 0, 100, 90)
    st.slider("Critical Thinking", 0, 100, 90)
    st.slider("Story Telling", 0, 100, 80)

st.title("Contact")
st.write("For any queries, please contact me at arpitsaxena91@gmail.com")