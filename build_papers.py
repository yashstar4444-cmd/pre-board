import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_pdf(filename, title, date_str, time_str, marks_str, sections_data):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        alignment=1, # Center
        textColor=colors.HexColor('#990000')
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        alignment=1,
        textColor=colors.HexColor('#1e3a8a')
    )
    
    meta_style = ParagraphStyle(
        'DocMeta',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        alignment=1,
        textColor=colors.HexColor('#334155')
    )
    
    section_style = ParagraphStyle(
        'SectionHeader',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#880808'),
        spaceBefore=12,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=6
    )

    story = []
    
    # Header
    story.append(Paragraph("CLASS X — PRE-BOARD EXAMINATION 2026", title_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph(title.upper(), subtitle_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph(f"Date: {date_str} &nbsp;&nbsp;|&nbsp;&nbsp; Time: {time_str} &nbsp;&nbsp;|&nbsp;&nbsp; Maximum Marks: {marks_str}", meta_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#990000'), spaceBefore=2, spaceAfter=10))

    # Sections & Questions
    for sec_title, items in sections_data:
        if sec_title:
            story.append(Paragraph(sec_title, section_style))
        for item in items:
            story.append(Paragraph(item.replace("\n", "<br/>"), body_style))
            story.append(Spacer(1, 4))
            
    doc.build(story)
    print(f"Generated PDF: {filename}")

# --- 1. Science (086) ---
science_sections = [
    ("GENERAL INSTRUCTIONS", [
        "1. This question paper contains 39 questions divided into Sections A to E.<br/>"
        "2. All questions are compulsory. Internal choices are provided in some questions.<br/>"
        "3. Section A: 20 x 1 = 20 marks; Section B: 6 x 2 = 12 marks; Section C: 7 x 3 = 21 marks; Section D: 3 x 5 = 15 marks; Section E: 3 x 4 = 12 marks.<br/>"
        "4. Draw neat, labelled diagrams wherever required."
    ]),
    ("SECTION A — OBJECTIVE TYPE (20 MARKS)", [
        "<b>Q1.</b> A student adds dilute HCl to zinc granules. The gas evolved turns a burning splint near bubbles into a pop sound. The gas is: (A) Oxygen (B) Hydrogen (C) Carbon dioxide (D) Chlorine",
        "<b>Q2.</b> A convex lens forms an image of an object placed beyond 2F. Which statement is correct? (A) Virtual, erect (B) Real, inverted and diminished (C) Real, erect (D) Virtual, inverted",
        "<b>Q3.</b> Assertion (A): A solution of sodium carbonate is basic in nature. Reason (R): Sodium carbonate reacts with water to produce hydroxide ions. (A) Both A and R are true and R explains A (B) Both true but R does not explain A (C) A true, R false (D) A false, R true",
        "<b>Q4.</b> The resistance of a conductor is doubled while potential difference remains constant. Current becomes: (A) doubled (B) halved (C) four times (D) unchanged",
        "<b>Q5.</b> Which structure controls the amount of light entering the human eye? (A) Retina (B) Cornea (C) Iris (D) Optic nerve",
        "<b>Q6.</b> A solution turns blue litmus red and reacts with sodium hydrogen carbonate producing brisk effervescence. Solution contains: (A) NaOH (B) HCl (C) NaCl (D) Ca(OH)2",
        "<b>Q7.</b> Which of the following represents oxidation? (A) Addition of hydrogen (B) Removal of oxygen (C) Addition of oxygen (D) Addition of electrons",
        "<b>Q8.</b> In a magnetic field, a current-carrying conductor experiences maximum force when angle between conductor and magnetic field is: (A) 0 deg (B) 30 deg (C) 60 deg (D) 90 deg",
        "<b>Q9.</b> A plant bends towards a source of light because of the unequal distribution of: (A) Auxin (B) Insulin (C) Thyroxine (D) Adrenaline",
        "<b>Q10.</b> Offspring produced by sexual reproduction show greater variation mainly because: (A) only one parent contributes (B) genetic material from two parents combines (C) DNA never copies (D) identical genes",
        "<b>Q11.</b> A ray of light passes from glass to air. The ray bends: (A) towards normal (B) away from normal (C) along normal (D) no bending",
        "<b>Q12.</b> The image formed on retina is: (A) virtual and erect (B) real and inverted (C) virtual and inverted (D) real and erect",
        "<b>Q13-Q20.</b> [Includes questions on Electrolysis of Sodium, Parallel Resistors Equivalent R, Cerebellum for posture & balance, Testosterone for male secondary traits, Convex Lens Focus, Displacement Reactions, Household parallel wiring, Nephron as functional unit of kidney.]"
    ]),
    ("SECTION B — VERY SHORT ANSWER (12 MARKS)", [
        "<b>Q21.</b> Why does dry HCl gas not change the colour of dry blue litmus paper, whereas aqueous HCl does?",
        "<b>Q22.</b> Two bulbs rated 60 W and 100 W are connected separately to the same voltage. Which bulb has greater resistance? Give reason.",
        "<b>Q23.</b> Explain why the sky appears blue during the day.",
        "<b>Q24.</b> What is reflex action? Explain the role of the spinal cord in a reflex arc.",
        "<b>Q25.</b> Give two differences between asexual and sexual reproduction.",
        "<b>Q26.</b> What happens when: (1) Copper is heated in air? (2) The black coating formed is treated with hydrogen?"
    ]),
    ("SECTION C — SHORT ANSWER (21 MARKS)", [
        "<b>Q27.</b> A student connects a 4 ohm and a 6 ohm resistor: (1) in series, and (2) in parallel. Calculate equivalent resistance in each case.",
        "<b>Q28.</b> Draw a labelled ray diagram for an object placed between F1 and 2F1 of a convex lens.",
        "<b>Q29.</b> Explain: (1) Why ionic compounds have high melting points? (2) Why do they conduct electricity in molten state?",
        "<b>Q30.</b> Explain how the human eye focuses on: (1) a nearby object, and (2) a distant object.",
        "<b>Q31-Q33.</b> [Structural isomerism C2H6O, Nerve impulse across synapse, 5 ohm resistor energy calculation.]"
    ]),
    ("SECTION D — LONG ANSWER (15 MARKS)", [
        "<b>Q34.</b> Convex Lens Experiment Analysis & Ray Diagrams OR Working of Human Eye & Myopia Correction.",
        "<b>Q35.</b> Iron nail in CuSO4, ZnSO4, AgNO3 solutions: Displacement observations, reactivity order of Fe, Cu, Zn, Ag. OR Metal extraction reactivity series.",
        "<b>Q36.</b> Reproduction mechanism in flowering plants from pollination to seed formation with labelled diagram."
    ]),
    ("SECTION E — CASE / COMPETENCY BASED (12 MARKS)", [
        "<b>Q37.</b> ELECTRICITY CASE STUDY: V-I graph data analysis and Ohm's law verification.",
        "<b>Q38.</b> LIFE PROCESSES CASE STUDY: Carbohydrate digestion, salivary amylase, small intestine absorption, aerobic respiration equation.",
        "<b>Q39.</b> MAGNETIC EFFECTS CASE STUDY: Force on current-carrying conductor in magnetic field, Fleming's Left Hand Rule."
    ]),
    ("PRINCIPAL'S CHALLENGE", [
        "<i>Difficulty Level: VERY HIGH. Original practice paper emphasizing application, numericals, diagrams and case studies.</i>"
    ])
]

create_pdf('assets/papers/paper1.pdf', 'Science (086) — Paper 1', '03 October 2026', '3 Hours', '80', science_sections)

# --- 2. Social Science (087) ---
sst_sections = [
    ("GENERAL INSTRUCTIONS", [
        "1. This question paper contains 37 questions divided into Sections A to F.<br/>"
        "2. Section A: 20 x 1 = 20; Section B: 4 x 2 = 8; Section C: 5 x 3 = 15; Section D: 4 x 5 = 20; Section E: 3 x 4 = 12; Section F (Map): 5 marks."
    ]),
    ("SECTION A — OBJECTIVE TYPE (20 MARKS)", [
        "<b>Q1.</b> The Treaty of Vienna (1815) aimed primarily to: (A) establish universal suffrage (B) restore monarchies & conservative order (C) abolish aristocracy (D) democratic federation",
        "<b>Q2.</b> Which development transformed nationalism in India into a broader mass movement? (A) Muslim League (B) Rowlatt Act & Jallianwala Bagh (C) Simon Commission (D) Govt of India Act 1935",
        "<b>Q3.</b> Assertion (A): Silk Routes are an example of pre-modern globalisation. Reason (R): Connected distant regions through trade and culture. (A) Both true & R explains A",
        "<b>Q4-Q20.</b> [Includes questions on Industrialisation in Britain, Print culture & Nationalism, Black soil for Cotton, Multipurpose river projects, Bauxite for Aluminium, Manufacturing industries, Federalism, Power sharing, Political parties, Disguised unemployment, Money medium of exchange, Self-Help Groups, UNDP Human Development Report.]"
    ]),
    ("SECTION B — VERY SHORT ANSWER (8 MARKS)", [
        "<b>Q21.</b> Explain two ways in which the French Revolution promoted nationalism in Europe.",
        "<b>Q22.</b> Distinguish between renewable and non-renewable resources with examples.",
        "<b>Q23.</b> Why is power sharing desirable in a democracy? Give two reasons.",
        "<b>Q24.</b> Distinguish between formal and informal sources of credit."
    ]),
    ("SECTION C — SHORT ANSWER (15 MARKS)", [
        "<b>Q25.</b> Explain three ways First World War created new economic and political situation in India.",
        "<b>Q26.</b> Why is conservation of forests and wildlife necessary? Explain three reasons.",
        "<b>Q27.</b> Explain three major challenges faced by political parties in India.",
        "<b>Q28.</b> 'Different persons can have different developmental goals.' Explain with examples.",
        "<b>Q29.</b> Explain three factors that enabled MNCs to organise production globally."
    ]),
    ("SECTION D — LONG ANSWER (20 MARKS)", [
        "<b>Q30.</b> European Nationalism post-1815 OR Role of Romanticism and language in nationalism.",
        "<b>Q31.</b> Water scarcity causes in high rainfall areas OR Features of Indian agriculture & farmer challenges.",
        "<b>Q32.</b> Belgian model of power sharing vs Sri Lankan majoritarianism.",
        "<b>Q33.</b> Organised vs Unorganised sector worker protection & improvement measures."
    ]),
    ("SECTION E & F — CASE BASED & MAP WORK (17 MARKS)", [
        "<b>Q34.</b> HISTORY SOURCE CASE STUDY: Citizenship, liberal nationalism & language.",
        "<b>Q35.</b> GEOGRAPHY CASE STUDY: Groundwater depletion & sustainable rainwater harvesting.",
        "<b>Q36.</b> ECONOMICS CASE STUDY: Formal vs informal credit loan terms.",
        "<b>Q37. MAP WORK:</b> Locate (a) Champaran (Indigo) (b) Kheda (Ptyagraha) (c) Mumbai (Cotton) (d) Bhakra Nangal (Dam) (e) Chennai (Seaport)."
    ])
]

create_pdf('assets/papers/paper2.pdf', 'Social Science (087) — Paper 1', '06 October 2026', '3 Hours', '80', sst_sections)

# --- 3. Mathematics (041) ---
maths_sections = [
    ("GENERAL INSTRUCTIONS", [
        "1. This question paper contains 38 questions divided into Sections A to E.<br/>"
        "2. Section A: 20 x 1 = 20; Section B: 5 x 2 = 10; Section C: 6 x 3 = 18; Section D: 4 x 5 = 20; Section E: 3 x 4 = 12 marks."
    ]),
    ("SECTION A — OBJECTIVE TYPE (20 MARKS)", [
        "<b>Q1.</b> If HCF(96, 404) = 4, then LCM(96, 404) is: (A) 9696 (B) 9796 (C) 9690 (D) 9792",
        "<b>Q2.</b> If alpha and beta are zeroes of 2x^2 - 7x + 3, then alpha^2*beta + alpha*beta^2 equals: (A) 21/4 (B) 21/2 (C) 7/2 (D) 3/2",
        "<b>Q3.</b> The pair 3x + 2y = 5 and 6x + ky = 10 has infinitely many solutions when k is: (A) 2 (B) 4 (C) 6 (D) 8",
        "<b>Q4.</b> If one root of x^2 - 5x + k = 0 is twice the other, then k equals: (A) 25/9 (B) 50/9 (C) 100/9 (D) 10/3",
        "<b>Q5.</b> The 20th term of AP 7, 11, 15, ... is: (A) 79 (B) 83 (C) 87 (D) 91",
        "<b>Q6-Q20.</b> [Midpoint formula, Trigonometric sec^2 - cos^2, Height & Distance 20m tower 60 deg, Circle tangent perpendicular to radius, Sector area 90 deg r=14, Cone curved surface area, Probability complement, Sphere volume r=6, Equal roots discriminant b^2-4ac=0.]"
    ]),
    ("SECTION B & C — SHORT ANSWER (28 MARKS)", [
        "<b>Q21.</b> Euclid's division algorithm HCF of 867 and 255.",
        "<b>Q22.</b> Find k for infinitely many solutions in linear system.",
        "<b>Q23.</b> Sum of 15 terms of AP is 420 and a=6. Find common difference d.",
        "<b>Q24.</b> Prove that sqrt(5) is irrational.",
        "<b>Q25-Q31.</b> [Form quadratic polynomial from zeroes alpha^2, beta^2; System of reducible equations 2/(x+y)+3/(x-y)=5; Triangle area & collinearity; Heights & Distances tower angles 30 deg & 60 deg; Quadrilateral circumscribing circle AB+CD=AD+BC.]"
    ]),
    ("SECTION D & E — LONG ANSWER & CASE STUDIES (32 MARKS)", [
        "<b>Q32.</b> Speed of train word problem / Quadratic equation 360 km at uniform speed.",
        "<b>Q33.</b> Basic Proportionality Theorem (Thales Theorem) proof and numerical application.",
        "<b>Q34.</b> Solid hemisphere + cylinder surface area & volume calculation.",
        "<b>Q35.</b> Statistics: Assumed mean method for marks distribution & median class identification.",
        "<b>Q36. AP CASE STUDY:</b> Auditorium seating arrangement AP (a=18, d=3, n=25).",
        "<b>Q37. COORDINATE GEOMETRY CASE STUDY:</b> Distance formula, midpoint & perpendicular bisector.",
        "<b>Q38. PROBABILITY CASE STUDY:</b> Drawing balls without replacement (white, black, red)."
    ])
]

create_pdf('assets/papers/paper3.pdf', 'Mathematics Standard (041) — Paper 1', '09 October 2026', '3 Hours', '80', maths_sections)

# --- 4. English (184) ---
english_sections = [
    ("GENERAL INSTRUCTIONS", [
        "1. This question paper contains 11 questions divided into Sections A, B and C.<br/>"
        "2. Section A — Reading Skills: 20 marks; Section B — Grammar & Writing: 20 marks; Section C — Literature: 40 marks."
    ]),
    ("SECTION A — READING SKILLS (20 MARKS)", [
        "<b>Q1. Discursive Passage (10 Marks):</b> Passage on digital information, attention span, sustained concentration in deep learning, and role of technology in education.",
        "<i>Questions: (a) Why access to info does not produce understanding (b) Meaning of 'attention as valuable resource' (c) Productive learning sign (d) Role of tech without replacing judgment (e) Central idea MCQ (f) Vocabulary & inference questions.</i>",
        "<b>Q2. Case-based Passage (10 Marks):</b> Data analysis on voluntary school reading programme (Month 1: 120, Month 2: 156, Month 3: 180 students).",
        "<i>Questions: Percentage increase calculation, student autonomy, flexible reading targets, conclusions and strategies.</i>"
    ]),
    ("SECTION B — GRAMMAR & CREATIVE WRITING SKILLS (20 MARKS)", [
        "<b>Q3. Grammar Tasks (10 Marks):</b> Modals, Determiners, Subject-Verb Agreement, Error Correction ('Each of the participants have...'), Reported Speech, Correct Tenses.",
        "<b>Q4. Formal Letter (5 Marks):</b> Letter to Editor expressing concern over excessive short-form digital video distraction among students.",
        "<b>Q5. Analytical Paragraph (5 Marks):</b> Compare 200 students' revision preferences (Self-study: 70, Group: 40, Online: 55, Classes: 35)."
    ]),
    ("SECTION C — LITERATURE (40 MARKS)", [
        "<b>Q6. Extract based on 'A Letter to God' (5 Marks):</b> Lencho's faith, hailstorm turning point, irony in receiving money.",
        "<b>Q7. Extract based on 'The Ball Poem' (5 Marks):</b> Ball symbolism, loss experience, epistemology of loss.",
        "<b>Q8. Short Answer Questions (5 x 2 = 10 Marks):</b> Nelson Mandela freedom concept, Anne Frank diary, Valli's bus journey, Mijbil the Otter, Fire and Ice, The Trees, The Proposal ending.",
        "<b>Q9. Supplementary Short Answer (3 x 2 = 6 Marks):</b> Thief's Story, Midnight Visitor Ausable, Bholi's transformation, Griffin's invisibility.",
        "<b>Q10 & Q11. Long Answer Questions (2 x 5 = 10 Marks):</b> Compare courage in Mandela vs Bholi OR Humour in The Proposal vs Book That Saved Earth; Trust as force in Thief's Story vs Appearance aspirations in The Necklace."
    ])
]

create_pdf('assets/papers/paper4.pdf', 'English Language & Literature (184) — Paper 1', '12 October 2026', '3 Hours', '80', english_sections)

# --- 5. Hindi (002) ---
hindi_sections = [
    ("सामान्य निर्देश", [
        "1. प्रश्न-पत्र में कुल 37 प्रश्न हैं, जो खंड अ, ब, स और द में विभाजित हैं।<br/>"
        "2. सभी प्रश्न अनिवार्य हैं। उत्तर स्पष्ट, क्रमबद्ध और शुद्ध भाषा में लिखें।"
    ]),
    ("खंड अ — अपठित बोध (14 अंक)", [
        "<b>प्रश्न 1. अपठित गद्यांश (7 अंक):</b> डिजिटल युग में सूचना और सच्चे ज्ञान में अंतर, कठिन प्रश्नों का महत्व, आत्म-अनुशासन।",
        "<b>प्रश्न 2. अपठित पद्यांश (7 अंक):</b> 'चलते रहो कि राह स्वयं राह बन जाएगी...' - निरंतर प्रयास, आशावाद और आत्मविश्वास का संदेश।"
    ]),
    ("खंड ब — व्यावहारिक व्याकरण (16 अंक)", [
        "<b>प्रश्न 3. वाक्य-भेद (4 अंक):</b> रचना के आधार पर सरल, संयुक्त और मिश्र वाक्य परिवर्तन।",
        "<b>प्रश्न 4. वाच्य परिवर्तन (4 अंक):</b> कर्तृवाच्य, कर्मवाच्य एवं भाववाच्य रूपांतरण।",
        "<b>प्रश्न 5. पद-परिचय (4 अंक):</b> रेखांकित शब्दों (मेहनती, बहुत, मैदान, धीरे-धीरे) का पद-परिचय।",
        "<b>प्रश्न 6. अलंकार (4 अंक):</b> अनुप्रास, यमक, श्लेष, उत्प्रेक्षा अलंकार पहचान।"
    ]),
    ("खंड स — रचनात्मक लेखन (20 अंक)", [
        "<b>प्रश्न 7. अनुच्छेद लेखन (6 अंक):</b> (क) परीक्षा में अंक और वास्तविक ज्ञान (ख) कृत्रिम बुद्धिमत्ता (AI) और विद्यार्थी (ग) समय का सदुपयोग।",
        "<b>प्रश्न 8. पत्र लेखन (5 अंक):</b> नगर निगम आयुक्त को वायु-प्रदूषण निवारण हेतु औपचारिक पत्र।",
        "<b>प्रश्न 9. सूचना/विज्ञापन (4 अंक):</b> विद्यालयी कार्यक्रम हेतु 50 शब्दों में सूचना।",
        "<b>प्रश्न 10. लघु कथा लेखन (5 अंक):</b> 'पुराना बैग — उसमें मिली डायरी — एक अधूरा सपना' पर आधारित कथा।"
    ]),
    ("खंड द — पाठ्यपुस्तक एवं साहित्य (30 अंक)", [
        "<b>प्रश्न 11-13. क्षितिज एवं कृतिका (18 अंक):</b> नेताजी का चश्मा, बालगोबिन भगत, लखनवी अंदाज़, संगतकार, उत्साह, माता का आँचल, साना-साना हाथ जोड़ि।",
        "<b>प्रश्न 14-15. दीर्घ उत्तरीय प्रश्न (12 अंक):</b> राम-लक्ष्मण-परशुराम संवाद, मानवीय करुणा की दिव्य चमक, सभ्यता और संस्कृति।"
    ])
]

create_pdf('assets/papers/paper5.pdf', 'Hindi Course-A (002) — Paper 1', '15 October 2026', '3 Hours', '80', hindi_sections)

# --- 6. Information Technology (402) ---
it_sections = [
    ("GENERAL INSTRUCTIONS", [
        "1. This question paper contains two parts: Part A (Employability Skills) and Part B (Subject Specific Skills).<br/>"
        "2. Total Time: 2 Hours | Maximum Marks: 80 (Theory/Practice Combined)."
    ]),
    ("PART A — EMPLOYABILITY SKILLS (10 MARKS)", [
        "<b>Q1. Communication Skills:</b> Verbal vs Non-verbal communication, active listening barriers.",
        "<b>Q2. Self-Management Skills:</b> Stress management techniques, goal setting SMART criteria.",
        "<b>Q3. ICT Skills:</b> Operating system functions, file management, cyber security basics & malware prevention.",
        "<b>Q4. Entrepreneurial & Green Skills:</b> Characteristics of successful entrepreneurs, sustainable development."
    ]),
    ("PART B — SUBJECT SPECIFIC SKILLS (70 MARKS)", [
        "<b>Q5. Digital Documentation (Advanced):</b> Styles in document, inserting and formatting images, creating TOC (Table of Contents), templates.",
        "<b>Q6. Electronic Spreadsheet (Advanced):</b> Subtotals, Consolidating data, What-If Analysis (Goal Seek & Solver), Linking sheets, Macros.",
        "<b>Q7. Database Management System (DBMS):</b> Relational database concepts, Primary key vs Foreign key, SQL queries (CREATE, SELECT, INSERT, UPDATE), Forms and Reports.",
        "<b>Q8. Web Applications & Security:</b> Network topologies, Internet security, Workplace safety, Ergonomics, Online transaction safety."
    ]),
    ("PRINCIPAL'S CHALLENGE", [
        "<i>Difficulty Level: VERY HIGH. Practical skill-based case scenarios and troubleshooting tasks for Class X IT-402.</i>"
    ])
]

create_pdf('assets/papers/paper6.pdf', 'Information Technology (402) — Paper 1', '17 October 2026', '2 Hours', '80', it_sections)

print("ALL 6 TEST PAPER PDFS CREATED SUCCESSFULLY!")
