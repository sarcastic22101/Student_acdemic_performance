# Student Alcohol Consumption <br>
## About the Project: - 
<p><i> This is an educational data set which is collected from learning management system (LMS) called Kalboard 360. Kalboard 360 is a multi-agent LMS, which has been designed to facilitate learning through the use of leading-edge technology. Such system provides users with a synchronous access to educational resources from any device with Internet connection.

The data is collected using a learner activity tracker tool, which called experience API (xAPI). The xAPI is a component of the training and learning architecture (TLA) that enables to monitor learning progress and learner’s actions like reading an article or watching a training video. The experience API helps the learning activity providers to determine the learner, activity and objects that describe a learning experience.
The dataset consists of 480 student records and 16 features. The features are classified into three major categories: (1) Demographic features such as gender and nationality. (2) Academic background features such as educational stage, grade Level and section. (3) Behavioral features such as raised hand on class, opening resources, answering survey by parents, and school satisfaction.

The dataset consists of 305 males and 175 females. The students come from different origins such as 179 students are from Kuwait, 172 students are from Jordan, 28 students from Palestine, 22 students are from Iraq, 17 students from Lebanon, 12 students from Tunis, 11 students from Saudi Arabia, 9 students from Egypt, 7 students from Syria, 6 students from USA, Iran and Libya, 4 students from Morocco and one student from Venezuela.

The dataset is collected through two educational semesters: 245 student records are collected during the first semester and 235 student records are collected during the second semester.

The data set includes also the school attendance feature such as the students are classified into two categories based on their absence days: 191 students exceed 7 absence days and 289 students their absence days under 7.

This dataset includes also a new category of features; this feature is parent parturition in the educational process. Parent participation feature have two sub features: Parent Answering Survey and Parent School Satisfaction. There are 270 of the parents answered survey and 210 are not, 292 of the parents are satisfied from the school and 188 are not.</i> <br>

<b>The columns in this <a href="https://github.com/nilavya2000/Student_alcohol_consumption/blob/master/data/student.csv">dataset</a> are:</b>
  <ul><i>
  <li><b>Gender -</b> student's gender (nominal: 'Male' or 'Female’)</li>
<li><b> Nationality-</b>student's nationality (nominal:’ Kuwait’,’ Lebanon’,’ Egypt’,’ SaudiArabia’,’ USA’,’ Jordan’,’
Venezuela’,’ Iran’,’ Tunis’,’ Morocco’,’ Syria’,’ Palestine’,’ Iraq’,’ Lybia’)</li>
<li><b> Place of birth-</b>student's Place of birth (nominal:’ Kuwait’,’ Lebanon’,’ Egypt’,’ SaudiArabia’,’ USA’,’ Jordan’,’
Venezuela’,’ Iran’,’ Tunis’,’ Morocco’,’ Syria’,’ Palestine’,’ Iraq’,’ Lybia’)</li>
<li><b>Educational Stages-</b>educational level student belongs (nominal: ‘lowerlevel’,’MiddleSchool’,’HighSchool’)</li>
<li><b>Grade Levels-</b>grade student belongs (nominal: ‘G-01’, ‘G-02’, ‘G-03’, ‘G-04’, ‘G-05’, ‘G-06’, ‘G-07’, ‘G-08’, ‘G-09’, ‘G-10’, ‘G-11’, ‘G-12 ‘)</li>
<li><b>Section ID-</b> classroom student belongs (nominal:’A’,’B’,’C’)</li>
<li><b>Topic-</b>course topic (nominal:’ English’,’ Spanish’, ‘French’,’ Arabic’,’ IT’,’ Math’,’ Chemistry’, ‘Biology’, ‘Science’,’ History’,’ Quran’,’ Geology’)</li>
<li><b>Semester-</b>school year semester (nominal:’ First’,’ Second’)</li>
<li>Parent responsible for student (nominal:’mom’,’father’)</li>
<li><b> Raised hand- </b>how many times the student raises his/her hand on classroom (numeric:0-100)</li>
<li><b>Visited resources- </b>how many times the student visits a course content(numeric:0-100)</li>
<li><b> Viewing announcements-</b>how many times the student checks the new announcements(numeric:0-100)</li>
<li><b> Discussion groups- </b>how many times the student participate on discussion groups (numeric:0-100)</li>
<li><b>Parent Answering Survey- </b> parent answered the surveys which are provided from school or not
(nominal:’Yes’,’No’)</li>

<li><b>Parent School Satisfaction-</b>the Degree of parent satisfaction from school(nominal:’Yes’,’No’)</li>
<li><b>Student Absence Days-</b>the number of absence days for each student (nominal: above-7, under-7)</li>

  </i></ul>
  <ul>The students are classified into three numerical intervals based on their total grade/mark:
  <li> <b>Low-Level:</b> interval includes values from 0 to 69.</li>
  <li> <b>Middle-Level:</b> interval includes values from 70 to 89.</li>
  <li><b>High-Level:</b> interval includes values from 90-100.</li>
  </ul>

</p>

## Language used: - 
[Python3](https://docs.python.org/3/)<br>
#### Note: <br>
Make Tab for indentation (tab = 3 spaces), and afer writing a code use the comment to describe the code ``` # add comment ```

## FrameWorks: -
1. [Pandas](https://pandas.pydata.org/docs/) (version: 1.0.2) <br>
```pip install pandas ```
2. [Numpy](https://numpy.org/doc/) (version: 1.18.3)<br>
``` pip install numpy```
3. [sklearn](https://scikit-learn.org/stable/install.html) (version: 0.10.0)<br>
``` pip install scikit-learn```
4. [Matplotlib](https://matplotlib.org/3.3.1/contents.html) (version: 3.2.0)<br>
``` pip install scikit-learn```
5. [Seaborn](https://seaborn.pydata.org/)(version: 0.10.0)<br>
```pip install seaborn ```

## How to contribute on open-source project: 
  <p><ul>
  <li>Fork this repository.</li>
  <li>Clone the repository.</li>
  <li>Create a branch.</li>
  <li>Make necessary changes and commit those changes.</li>
  <li>Push changes to GitHub.</li>
  <li>Submit your changes for review.</li>
  <li>Refer to <a href="https://github.com/Hack-Club-SIT/Git-Learning-Resources">Git Resources</a> for git commands.</li></ul></p>
 