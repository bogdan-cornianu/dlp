from django import forms
from questionnaire.models import Answer


class PageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        page = kwargs.pop('page')
        super(PageForm, self).__init__(*args, **kwargs)

        for question in page.question_set.values('id', 'question_text'):
            answers = Answer.objects.filter(
                question_id=question['id']).values_list('id', 'answer_text')
            field_key = 'question_%s' % question['id']
            self.fields[field_key] = forms.MultipleChoiceField(
                choices=answers,
                label=question['question_text']
            )
