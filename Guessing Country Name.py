import random

asia= ('afghanistan', 'armenia', 'azerbaijan', 'bahrain', 'bangladesh', 'bhutan', 'brunei', 'cambodia', 'china', 'cyprus', 'georgia', 'india', 'indonesia', 'iran', 'iraq', 'israel', 'japan', 'jordan', 'kazakhstan', 'kenya', 'korea, north', 'korea, south', 'kuwait', 'kyrgyzstan', 'laos', 'lebanon', 'malaysia', 'maldives', 'mongolia', 'myanmar', 'nepal', 'oman', 'pakistan', 'palestine', 'philippines', 'qatar', 'saudi arabia', 'singapore', 'sri lanka', 'tajikistan', 'thailand', 'turkmenistan', 'united arab emirates', 'uzbekistan', 'vietnam', 'taiwan', 'yemen')
africa= ('algeria', 'angola', 'benin', 'botswana', 'burkina faso', 'burundi', 'cabo verde', 'cameroon', 'central african republic', 'chad', 'comoros', 'congo, democratic republic of the', 'congo, republic of the', 'djibouti', 'egypt', 'equatorial guinea', 'eritrea', 'eswatini', 'ethiopia', 'gabon', 'gambia', 'ghana', 'greece', 'guinea', 'guinea-bissau', 'ivory coast', 'kenya', 'lesotho', 'liberia', 'libya', 'madagascar', 'malawi', 'mali', 'mauritania', 'mauritius', 'morocco', 'mozambique', 'namibia', 'niger', 'nigeria', 'rwanda', 'sao tome and principe', 'senegal', 'seychelles', 'sierra leone', 'somalia', 'south africa', 'south sudan', 'sudan', 'tanzania', 'togo', 'uganda', 'zambia', 'zimbabwe')
europe= ('albania', 'andorra', 'armenia', 'austria', 'azerbaijan', 'belarus', 'belgium', 'bosnia and herzegovina', 'bulgaria', 'croatia', 'cyprus', 'czech republic', 'denmark', 'estonia', 'faroe islands', 'finland', 'france', 'georgia', 'germany', 'greece', 'hungary', 'iceland', 'ireland', 'italy', 'kazakhstan', 'kosovo', 'latvia', 'liechtenstein', 'lithuania', 'luxembourg', 'malta', 'moldova', 'monaco', 'montenegro', 'netherlands', 'north macedonia', 'norway', 'poland', 'portugal', 'romania', 'russia', 'san marino', 'serbia', 'slovakia', 'slovenia', 'spain', 'sweden', 'switzerland', 'ukraine', 'united kingdom', 'vatican city', 'venezuela')
australia= ('australia', 'fiji', 'kiribati', 'marshall islands', 'micronesia', 'nauru', 'new zealand', 'palau', 'papua new guinea', 'samoa', 'solomon islands', 'tonga', 'tuvalu', 'vanuatu')
north_america= ('antigua and barbuda', 'bahamas', 'barbados', 'belize', 'canada', 'costa rica', 'cuba', 'dominica', 'dominican republic', 'el salvador', 'grenada', 'guatemala', 'honduras', 'jamaica', 'mexico', 'nicaragua', 'panama', 'st. kitts and nevis', 'st. lucia', 'st. vincent and the grenadines', 'united states')
south_america= ('argentina', 'brazil', 'chile', 'colombia', 'ecuador', 'guyana', 'paraguay', 'peru', 'suriname', 'uruguay', 'venezuela')

world= asia+africa+europe+north_america+south_america+australia

continent_list= (asia, africa, europe, australia, north_america, south_america)
continent_name= {asia:'Asia',
                 africa: 'Africa',
                 europe: 'Europe',
                 australia: 'Australia',
                 north_america: 'North America',
                 south_america: 'South America'
                 }

select_continent= random.choice(continent_list)

computer_choice= random.choice(select_continent)


hint_continent= continent_name[select_continent]

print('WELCOME TO GUESS THE COUNTRY GAME!')

while True:
    user_choice= input('Guess a country name: ').lower()

    if user_choice not in world:
        print('NOT A COUNTRY')
    elif user_choice==computer_choice:
        print('You Won!')
        break
    else:
        print('You Lose!')

    yesno= input('Quit? (Yes/No/Hint): ').lower()
    if yesno=='yes':
        print(f"The secret country was '{computer_choice}'")
        break
    elif yesno=='hint':
        print(f"The secret country is in '{hint_continent}'")
        print(f"It starts with the letter '{(computer_choice[0]).upper()}'")
        
