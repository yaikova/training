class Contact:

    def __init__(self, base_str=''):
        self.field_list = [ 'firstname', 'middlename', 'lastname', 'nickname',
            'title',  'company', 'address',
            'home', 'mobile', 'work', 'fax',
            'email', 'email2', 'email3', 'homepage',
            'byear', 'ayear', 'address2', 'phone2', 'notes']
        self.data={}
        for key in self.field_list:
                self.data.update({key: base_str})
