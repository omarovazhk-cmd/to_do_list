from django.db import models

class Task(models.Model):
    status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

    description = models.TextField(verbose_name='Описание')
    status = models.CharField(verbose_name='Статус', max_length=20, choices=status_choices, default='new')
    due_date = models.DateField(verbose_name='Дата выполнения', blank=True, null=True)
    description_detail = models.TextField('Подробное описание', blank=True, null=True)



    def __str__(self):
        return f'{self.id} - {self.description}'