# Attendance-system-main using facial recognition
In this project we have created a "Automated Attendance Systek Based On Face Recognition".The application includes facial identification of students for creating ease in attendance management.

<h3>TECHNOLOGY USED: </h3>
<ol>
<li>Streamlit for application</li>
<li>OpenCV for taking images and face recognition</li> 
<li>CSV, Numpy, Pandas, datetime etc. for other purposes.</li>
</ol>


<h3>Instructions to run</h3>
<ol>
	<li>Clone the project and download the source code.</li>
	<li>Once inside the folder, run the following command: streamlit run '.\p1 
  html\Attendance-System-Project-main\4. Deployment\Home_Page.py'</li>
	<li>Go to: localhost:8504 in your browser</li>
	<li>First Register yourself by clicking on option Add_new_student</li>
	<li>Mark your attendance by clicking on Intiate Attendance on Attendance_with 
 camera.</li>
	<li>We can also mark attendance using Manual attendance
	</li>
</ol>

<h3>Error Analysis</h3>
<p>The possible reasons for the errors could be:</p>

<ol>
	<li>Change in the person’s face over time - considerable facial change from the photo used in training.</li>
  <li>Two or more similar-looking people - If there are multiple people with similar faces, then the model may wrongly classify a person as someone else.</li>
</ol>
<h3>SCREENSHOT</h3>
<p><b>Registering student by taking pictures and entering name</b></p>
<img width="960" alt="image" src="https://github.com/srishtibhardwaj073/Attendance-system-main/assets/97687683/c95fae48-0572-4018-9d61-a50d19fdfcd3">
