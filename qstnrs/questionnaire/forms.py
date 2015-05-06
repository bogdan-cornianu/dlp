from django import forms


class PageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        page = kwargs.pop('page')
        super(PageForm, self).__init__(*args, **kwargs)

        for question in page.question_set.all():
            answers = [(answer.id, answer.answer_text) for
                       answer in question.answer_set.all()]
            field_key = 'question_%s' % question.id
            self.fields[field_key] = forms.MultipleChoiceField(choices=answers,
                                                  label=question.question_text)
