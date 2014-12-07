Documentation for CRIMSON ALERTS, A CS50 final project by Juliet Nelson.

Accessing the site:
This URL will take you to the sign up site for Crimson Alerts: https://frozen-peak-9783.herokuapp.com/
The CSS for this is adapted from the Harvard Crimson in order to integrate with their site, since this project is ultimately designed for use
by The Crimson Staff.

Signing up:
Once you are on the site enter the demographic information requested then click submit. The form should either prompt you to fix mistakes or take you to the confirmation page indicating that you have sucessfully signed up for Crimson Alerts! You should receive a text message from the number "(267)875-2746" confirming your sign up and welcoming you to Crimson Alerts. To enter another subscriber simply reload the page. 

Unsubscribing: 
To unsubscribe without using admin privilidges respond STOP to the Crimson Alerts number ((267)875-2746). You can also delete yourself from the database, but that takes administrative privilidges. 

Administration: 
To access Administration of Crimson Alerts visit https://frozen-peak-9783.herokuapp.com/admin and use the admin username:janelson12 and password: juliet

	Adding Breaking News:
	Breaking news can be added by an administrator by clicking the news link in django admin and then the add news button on the top right hand corner. One will then be prompted for the headline and URL. The Alert Sent feild should be left unchecked (it will automatically be filled in when an alert is sent).

	Sending Alerts:
	Heroku is set to run the send alerts app every 10 minutes. Any new breaking news added in the interum will be sent automatically.

	

