import math
import numbers
from django.db import models
from django.forms import CharField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Numeral(models.Model):

    def validate_max_value(value):
        if value > 3999:
            raise ValidationError(
                ('%(value)% ? The Romans only made it as far as 3999!'),
                params={'value': value}
            )

    def validate_roman_characters(value):
        romansDict = \
            {
                0: "",
                1: "I",
                5: "V",
                10: "X",
                50: "L",
                100: "C",
                500: "D",
                1000: "M",
                5000: "G",
                10000: "H"
            }
        value_list =  value.split()

        for val in value_list:
            if (val not in romansDict):
                raise ValidationError(
                    ('value: %(value)% contains invalid roman characters. ')
                )

    def convert_arabic_to_roman_numbers(A):
        romansDict = \
            {
                1: "I",
                5: "V",
                10: "X",
                50: "L",
                100: "C",
                500: "D",
                1000: "M",
                5000: "G",
                10000: "H"
            }

        div = 1
        while A >= div:
            div *= 10

        div /= 10

        res = ""

        while A:

            # main significant digit extracted
            # into lastNum
            lastNum = int(A / div)

            if lastNum <= 3:
                res += (romansDict[div] * lastNum)
            elif lastNum == 4:
                res += (romansDict[div] +
                            romansDict[div * 5])
            elif 5 <= lastNum <= 8:
                res += (romansDict[div * 5] +
                (romansDict[div] * (lastNum - 5)))
            elif lastNum == 9:
                res += (romansDict[div] +
                            romansDict[div * 10])

            A = math.floor(A % div)
            div /= 10
            
        return res

    arabic_number = models.IntegerField(max_length=4, primary_key=True, validators=[MinValueValidator(1), validate_max_value])
    roman_number = models.CharField(max_length=10, default="ROMAN_CHAR?", validators=[validate_roman_characters])