from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Courses(models.Model):
    name = models.CharField(_('Название'), max_length=128)
    description = models.TextField(_('Описание'), null=True, blank=True)
    image = models.ImageField(_('Изображение'), upload_to='courses_images')

    class Meta:
        verbose_name = _('Курс')
        verbose_name_plural = _('Курсы')

    def __str__(self):
        return f'Курс: {self.name}'

class CoursesTheory(models.Model):
    course = models.ForeignKey(Courses, verbose_name=_('Курс'), related_name='theories', on_delete=models.CASCADE)
    title = models.CharField(_('Название'), max_length=128)
    theory = models.TextField(_('Теория'), max_length=1000)

    class Meta:
        verbose_name = _('Теория курса')
        verbose_name_plural = _('Теории курсов')

    def __str__(self):
        return f'{self.title} для курса: {self.course.name}'

class PracticeTasks(models.Model):
    theory = models.ForeignKey(CoursesTheory, verbose_name=_('Теория'), related_name='tasks', on_delete=models.CASCADE)
    description = models.TextField(_('Описание'))
    difficulty = models.CharField(_('Сложность'), max_length=50)
    answer = models.TextField(_('Ответ'), blank=True, null=True)

    class Meta:
        verbose_name = _('Практическое задание')
        verbose_name_plural = _('Практические задания')

    def __str__(self):
        return f'Практическая задача для теории: {self.theory.title}'

class Like(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Пользователь'), on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, verbose_name=_('Курс'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')
        verbose_name = _('Лайк')
        verbose_name_plural = _('Лайки')

class Reviews(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Пользователь'), on_delete=models.SET_NULL, null=True)
    rating = models.PositiveSmallIntegerField(_('Оценка'), validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.TextField(_('Отзыв'))
    create_date = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __str__(self):
        return self.review
