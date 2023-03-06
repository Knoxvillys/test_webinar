from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=20) # Имя учителя
    surname = models.CharField(max_length=40) # Фамилия
    image_avatar = models.ImageField(upload_to='image', null=True) # Аватар учителя
    hourly_rate = models.IntegerField(null=True) # Часовая ставка, тип: int
    
    def __str__(self):
        return f'{self.name} {self.surname}'


class Video(models.Model):
    CONFIRMED = 'подтвержден'
    REJECT = 'отклонен'
    DECISION = [
        (CONFIRMED, 'подтвержден.'),
        (REJECT, 'отменен.')
    ]
    
    title = models.CharField(max_length=200) # Название
    description = models.TextField(max_length=300) # Описание
    image = models.ImageField(upload_to='image', null=True) # Превью изображение
    creat_at = models.DateTimeField(auto_now_add=True) # Дата которая установиться автоматически при создании
    pub_date = models.DateTimeField() # Дата самого вебинара.
    teacher = models.ManyToManyField(Teacher) # Связываем модели
    decision = models.CharField(max_length=11, choices=DECISION, default=CONFIRMED) # решение по проведению
    
    def __str__(self):
        if self.decision == self.CONFIRMED:
            return f'Вебинар {self.title} {self.decision}'
        else:
            return f'Вебинар {self.title} {self.decision}'


class Сourse(models.Model):
    title_course = models.CharField(max_length=30) # Название курса
    image_course = models.ImageField(upload_to='image', null=True) # Превью изображение
    text_course = models.TextField() # Сам курс
    
    def __str__(self):
        return self.title_course
