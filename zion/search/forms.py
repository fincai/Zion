from django import forms

class SearchFormSimple(forms.Form):
    search_query = forms.CharField(label="Search Phrases", max_length=255)
    search_in_titles = forms.BooleanField(label="Limit Search in Titles", required=False)
    search_author = forms.CharField(label="Author Name",
                                    help_text="Limit search to specified user by entering username here.",
                                    max_length=255,
                                    required=False)
                                    
    def clean_search_query(self):
        data = self.cleaned_data['search_query']
        if len(data) < 3:
            raise forms.ValidationError(_("Search Query string should contain at least 3 characters."))
        return data
