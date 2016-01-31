class Contact:

    def __init__(self):
        self.data={ 'firstname' : '', 'middlename' : '', 'lastname' : '', 'nickname' : '',
        'title' : '',  'company' : '', 'address' : '',
        'home' : '', 'mobile' : '', 'work' : '', 'fax' : '',
        'email' : '', 'email2' : '', 'email3' : '', 'homepage' : '',
        'byear' : '', 'ayear' : '', 'address2' : '', 'phone2' : '', 'notes' : ''}

    def fill_data_with_trash(self):
        for key in self.data:
            self.data[key]='123'