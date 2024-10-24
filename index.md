## Jack Griffiths     
## Deciphering Big Data, July-October 2024

---

### [Collaborateive Discussion 1](Discussion-Summary-1.pdf)
The first collaborative discussion focused on critically evaluating the rationale behind the Internet of Things (IoT), highlighting the opportunities, limitations, risks, and challenges in the context of large-scale processing of data. I received feedback from other students on the course during the discussion period, which allowed me to further develop my initial post, with additional context added concerning IoT security, and mitigating the trade-off between accuracy and timeliness when processing large amounts of real-time data.

### [Web Scraping Activity](Web-Scraping.md)
The web scraping activity made use of Python’s BeautifulSoup library, which scrapes the HTML code from a specified webpage for use in data analysis. I was able to extract the HTML form University of Essex Online’s data science course page, and count the number of times the phrase ‘Data Science’ appeared and recorded the results in a JSON file. I was able to compare my code with contributions in the module’s Wiki page.

### [Data Cleaning Activity](Data-Cleaning.md)
The data cleaning activities were followed using Chapter 7 of the Kazil & Jarmul (2016) textbook. Data was downloaded from the UNICEF household survey data. Part of cleaning the data can involve making the set more human-readable. This allowed me to further practice using the Beautiful Soup library to scrape the human readable headings from the UNICEF website. The textbook continued to elaborate, with examples, how this is implemented as well as further cleaning techniques for large data sets like these. Attached is the human readable table headings along with their corresponding codes, as well as the Python script used to scrape them.

### [Normalisation and Data Build Task](Normalisation-and-Build.md)
This task involved a table containing un-normalised student data, which needed to be normalised using first normal, second normal, and third normal forms. This was initially done as a visual exercise using Excel, the .xlsx file is attached. A database was then built based on the data in third normal form with MySQL. The data was entered mostly manually, and in bulk by converting some tables in the Excel sheet to .csv. A document is attached explaining some of the queries used to test the referential integrity of the data once it was inputted to the database.

### [Collaborative Discussion 2](Discussion-Summary-2.pdf) 
The second collaborative discussion was centred around comparing the EU’s GDPR with that of the UK, with a particular focus on security. The feedback I received on my initial post helped me to into further detail on the subtle differences between the two jurisdictions and improve my understanding on how GDPR works among the various member states. Through engaging with other students during the discussion, I provided feedback to peers highlighting the differences in compliance procedures thanks to the EU’s one-stop shop mechanism, and learned about how GDPR works in non-EU country that also happens to be in the EEA country, such as Norway.

### Module Reflection
Throughout this module, I have enjoyed learning about the ever-increasing amount of data being produced and how it can be of use to many different organisations, through developments in data wrangling, to different storage methods, structures, and management. This has been achieved through completing different exercises and tasks throughout the module, as well as participating in group work and discussions with peers. I’ve also enjoyed learning about new libraries in Python for big data analysis, as well as further practice using MySQL. As the module draws to a close, I will use Rolfe et al.’s (2001) approach to reflection – focusing on what I’ve done, or the outcomes of various tasks, provide an analysis, and how it can be used or learned from going forward (What, So What, Now What?).

The collaborative discussions provided a good opportunity to learn from and provide feedback to other students in the cohort. As a result of both discussions, I enhanced my initial discussion posts with help from the peer responses. However, I feel I could have implemented more information from the additional research I carried out while formulating responses to my peers’ posts, as this would have also enhanced my initial posts further.

I feel the data collection task went well, based on Chapter 7 of the book by Kazil & Jarmul (2016). This provided an opportunity to exercise my existing research skills to source the most up to date dataset for the Multiple Indicator Cluster Survey (MICS) for Zimbabwe, as well as develop further skills in data scraping by using the BeautifulSoup library in Python. Another interesting aspect about this activity is that it required me to learn some basic aspects of HTML, and what to look out for. After identifying which containers the relevant data was sat in, and realising the positioning of each item could be used to effectively when loop through the list, the coded short headers and their definitions were piped into a .csv file so they could be easily identified. However, more attention could have been given to the data cleaning portion of this task. The textbook ran through further exercises in cleaning this set of data by providing the Python code; however, I could have researched this further and sought further examples from elsewhere to maximise the learning opportunity.

Another area that went well, but had some area for improvement was the data management pipeline test in Unit 4. I achieved a score 8.75 of 10 and there was an opportunity to review the incorrect responses. I mixed up the definitions for Python Best Practices and the Zen of Python, which are covered in Chapter 8 of the Kazil & Jarmul book; these should have been “A basic outline of some best practices to follow as a new Python developer” and “A philosophy for how to write and think like a Python programmer” respectfully. This has highlighted the need for me to revisit these definitions going forward, as I could also benefit from learning to tidy my code.

The data normalisation and build task was an enjoyable part of the course, as this allowed me to practice and further develop my SQL skills, while learning about database normalisation. I feel that I organized the normalized data tables well by using Microsoft Excel, as this allowed me to manipulate and visualise the tables easily due to the formatting tools. To ensure I understood the definitions of each normal form, I referred to the examples provided by Database Star (2022). To further my understanding and verify the task was completed correctly before beginning the build task, I could have sought feedback from peers or from the course tutor. However, the build task was successful, as by practicing inputting a variety of different queries using MySQL, I produced the five tables as outlined in my Excel sheet. I also used a mixture of manual inputs, and tried inputting the data bulk using a .csv. Additionally, when querying data from this database, I was able to confirm the referential integrity by reproducing the original un-normalised table from the normalised set. Going forward, I am confident I could continue to develop in this area and learn some more advanced querying techniques and take on some more challenging tasks.

The group project was an aspect I feel could have gone better and was a weaker point during the module. Areas of improvement I identified during the peer review process included setting up more frequent and regular meetings to ensure the project was on track. Initially, there was also confusion over the project brief and exactly what to include. Although tutor feedback indicated a good level of knowledge and understanding of the module topics, the report lacked detail in the logical design and didn’t require the sections on DBMS selection and design benefits were not required. As I wrote the initial draft of the logical design section, I felt that I was running out of usable word count, which resulted in cutting out details that would have improved the piece. During future group work, I should aim to be more confident to share ideas and air concerns, particularly in areas where the quality of the final product could be affected.

Additionally, I feel the group was too ambitious when deciding which tables to include in the logical design, as this made it difficult to attempt to build for the final project. As a result, I relied more on researching and justifying the choices of database model and DBMS. In hindsight, I could have chosen a smaller portion of the logical design and attempted to build that instead, using the data that could be obtained from TfL’s APIs. This way, I could have enhanced my executive summary with details of the database build, as well as some diagrams.

To conclude, I feel the module has been positive on the whole, with existing skills developed and new skills learned, and plenty of experiences to reflect on. Going forward my biggest area for improvement would be developing my skills in working as a group, so I will continue to reflect on my experience here in preparation for future projects. On the other hand, I feel I’ve most improved with my database knowledge and querying skills, and look forward to developing these further and using them for future projects.


<u>References</u>

Database Star. (2022) Database Normalization: A Step-By-Step Guide With Examples. Available from: https://www.databasestar.com/database-normalization/ [Accessed on 18 October 2024].

Kazil, J. & Jarmul, K. (2016) Data Wrangling with Python: Tips and Tools to Make Your Life Easier. Sebastopol: O’Reilly Media.

Rolfe, G., Freshwater, D. & Jasper, M. (2001) Critical reflection in nursing and the helping professions: a user’s guide. Basingstoke: Palgrave Macmillan.

---

---

Page template forked from [evanca](https://github.com/evanca/quick-portfolio)
