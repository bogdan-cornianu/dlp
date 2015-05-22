from django import forms


class PageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        page = kwargs.pop('page')
        super(PageForm, self).__init__(*args, **kwargs)

        for question in page.question_set.values(
                'id', 'question_text', 'answer', 'answer__answer_text'):
            field_key = 'question_%s' % question['id']

            self.fields.setdefault(field_key, forms.MultipleChoiceField(
                choices=[],
                label=question['question_text']))

            self.fields[field_key].choices.append(
                (question['answer'], question['answer__answer_text']))
