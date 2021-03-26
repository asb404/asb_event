from django import forms

class addevent(forms.Form):
    ename=models.CharField(max_length=255)
    elocation=models.CharField(max_length=255)
    edate=models.DateField()
    etime=models.TimeField()
    image = models.ImageField(null=True,upload_to="static/images/")