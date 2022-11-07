from django.db import models

class Project(models.Model):
    Text = models.TextField(default="")
    descript = models.TextField(default="")

class ProjectImages(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name = 'projectimage',
                                )
    img = models.ImageField(upload_to='project_files/images', default='tovar_files/pictures/Bi-group.png')
    main = models.ImageField(upload_to='project_files/images', default='tovar_files/pictures/Bi-group.png')

