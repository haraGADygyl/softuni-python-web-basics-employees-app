from django.db import models


class Department(models.Model):
    name = models.CharField(
        max_length=20,
        null=True
    )


class Employee(models.Model):
    SOFTWARE_DEVELOPER = 1
    QA_ENGINEER = 2
    DEVOPS_SPECIALIST = 3

    SOFT_UNI = 'SoftUni'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'

    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=40,
        null=True,
        blank=True,
    )
    egn = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='EGN',
    )
    job_title = models.IntegerField(
        choices=(
            (SOFTWARE_DEVELOPER, 'dev'),
            (QA_ENGINEER, 'QA'),
            (DEVOPS_SPECIALIST, 'DevOps'),
        )
    )
    company = models.CharField(
        max_length=max(len(c) for c in [SOFT_UNI, GOOGLE, FACEBOOK]),
        choices=(
            (SOFT_UNI, SOFT_UNI),
            (GOOGLE, GOOGLE),
            (FACEBOOK, FACEBOOK),
        )
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )


class User(models.Model):
    email = models.EmailField()

    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )
    dead_line = models.DateField(
        null=True,
        blank=True,
    )

    employees = models.ManyToManyField(
        to=Employee,
    )
