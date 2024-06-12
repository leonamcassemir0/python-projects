def build_profile(first, last, **user_info):
    profile = {}
    profile['First name'] = first
    profile['Last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    print(profile)


build_profile('Leonam', 'Cassemiro', location='Minas Gerais, Brasil', field='Software engenniring', hobbies='Read and train')
