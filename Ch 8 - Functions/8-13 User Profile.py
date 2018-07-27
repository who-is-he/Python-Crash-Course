def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for k, v in user_info.items():
        profile[k] = v

    return profile

my_profile = build_profile('mike', 'evans', hair='brown', height='5\'9', age=18)
print(my_profile)