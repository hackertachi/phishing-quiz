from django import forms


class QuizForm(forms.Form):
	choices1 = (
		('Mispelled words', 'Mispelled words'),
		('A sense of urgency', 'A sense of urgency'),
		('A threatening and fear-based message', 'A threatening and fear-based message'),
		('All of the above', 'All of the above'),
		)

	choices2 = (
		('Yes', 'Yes'),
		('No', 'No'),
		)

	choices3 = (
		('https', 'https'),
		('http', 'http'),
		)

	choices4 = (
		('Yes', 'Yes'),
		('No', 'No'),
		)

	choices5 = (
		('By emailing them back', 'By emailing them back'),
		('By checking their FULL email address', 'By checking their FULL email address'),
		('By verifying any attachments that they sent you', 'By verifying any attachments that they sent you'),
		('By clicking any links visible in the body of the message', 'By clicking any links visible in the body of the message'),
		)

	question1 = forms.ChoiceField(choices=choices1, widget=forms.RadioSelect, label="<b>1. While reading an email, what would make the email's tone suspicious?</b>")
	question2 = forms.ChoiceField(choices=choices2, widget=forms.RadioSelect, label="<b>2. HR Department sends you a link to update some personal information. The URL is</b> <i><u>http://169.54.233.119/unistar.com/contactinfo?id=2345</u></i>.<br><b>Can you trust it?</b>")
	question3 = forms.ChoiceField(choices=choices3, widget=forms.RadioSelect, label="<b>3. Which is more secure: http or https?</b>")
	question4 = forms.ChoiceField(choices=choices4, widget=forms.RadioSelect, label="<b>4. Can your system be compromised from simply clicking a phishing link?</b>")
	question5 = forms.ChoiceField(choices=choices5, widget=forms.RadioSelect, label="<b>5. How can you verify that the sender is who they say they are?</b>")