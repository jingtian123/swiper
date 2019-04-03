from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    # 最小距离的校验
    def clean_min_distance(self):
        cleaned_data = super().clean()
        min_distance = cleaned_data['min_distance']
        print(cleaned_data)
        print(self.errors)

        max_distance = cleaned_data['maxdistance']
        if min_distance > max_distance:
            raise forms.ValidationError('min_distance 大于 max_distance')
        return min_distance

    # 最小年龄的校验
    def clean_min_dating_age(self):
        cleaned_data = super().clean()
        min_age = cleaned_data['min_age']
        max_age = cleaned_data['max_age']
        if min_age > max_age:
            raise forms.ValidationError('min_age 大于 max_age')
        return min_age


