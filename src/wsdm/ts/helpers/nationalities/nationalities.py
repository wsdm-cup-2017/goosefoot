
def remove_spaces(input):
    for nationality, modified_nationality in nationality_spaces_dict.items():
        input = input.replace(nationality, modified_nationality)
    return input


def process_line(line):
    for synonym, nationality in nationalities_dict.items():
        line = line.replace(synonym, nationality)
        line = remove_spaces(line)
    return line

nationality_spaces_dict = {
    'Bosnia and Herzegovina': 'Bosnia_and_Herzegovina',
    'Czech Republic': 'Czech_Republic',
    'Dominican Republic': 'Dominican_Republic',
    'Hong Kong': 'Hong_Kong',
    'Ivory Coast': 'Ivory_Coast',
    'New Zealand': 'New_Zealand',
    'Northern Ireland': 'Northern_Ireland',
    'Puerto Rico': 'Puerto_Rico',
    'Republic of Ireland': 'Republic_of_Ireland',
    'Saudi Arabia': 'Saudi_Arabia',
    'South Africa': 'South_Africa',
    'South Korea': 'South_Korea',
    'Soviet Union': 'Soviet_Union',
    'Sri Lanka': 'Sri_Lanka',
    'United Kingdom': 'United_Kingdom',
    'United States of America': 'United_States_of_America'
}

nationalities_dict = {
    'Dane': 'Denmark',
    'Czechoslovak': 'Czechoslovakia',
    'Trinidadian': 'Trinidad and Tobago',
    'Burmese': 'Burma',
    'Indonesian': 'Indonesia',
    'Hong Konger': 'Hong Kong',
    'Irishwoman': 'Northern Ireland Republic of Ireland',
    'Honduran': 'Honduras',
    'Bangladeshi': 'Bangladesh',
    'Czechoslovakian': 'Czechoslovakia',
    'Tunisian': 'Tunisia',
    'Solomon Islander': 'Solomon Islands',
    'UAE': 'United Arab Emirates',
    'Guyanese': 'Guyana',
    'Australian': 'Australia',
    'UK': 'United Kingdom',
    'Czech': 'Czech Republic',
    'Turkish': 'Turkey',
    'Dutch': 'Netherlands',
    'Moldovan': 'Moldova',
    'Irish': 'Northern Ireland Republic of Ireland',
    'Cuban': 'Cuba',
    'Serb': 'Serbia',
    'Puerto Rican': 'Puerto Rico',
    'Dominican': 'Dominican Republic',
    'New Zealander': 'New Zealand',
    'Lithuanian': 'Lithuania',
    'Thai': 'Thailand',
    'Icelandic': 'Iceland',
    'Yugoslav': 'Yugoslavia',
    'British': 'United Kingdom',
    'Namibian': 'Namibia',
    'Briton': 'United Kingdom',
    'Monégasque': 'Monaco',
    'Zambian': 'Zambia',
    'Portuguese': 'Portugal',
    'Bosnian': 'Bosnia and Herzegovina',
    'Burundian': 'Burundi',
    'Danish': 'Denmark',
    'Filipino': 'Philippines',
    'Hungarian': 'Hungary',
    'Kazakh': 'Kazakhstan',
    'Malaysian': 'Malaysia',
    'Swedish': 'Sweden',
    "Côte d'Ivoire": 'Ivory Coast',
    'Sudanese': 'Sudan',
    'Croat': 'Croatia',
    'South African': 'South Africa',
    'Ghanaian': 'Ghana',
    'Icelander': 'Iceland',
    'Somali': 'Somalia',
    'Tswana': 'Botswana',
    'Cape Verdean': 'Cape Verde Islands',
    'Maltese': 'Malta',
    'Guatemalan': 'Guatemala',
    'Swiss': 'Switzerland',
    'Beninese': 'Benin',
    'Spanish': 'Spain',
    'Pole': 'Poland',
    'Chadian': 'Chad',
    'Gabonese': 'Gabon',
    'Malian': 'Mali',
    'Liechtensteiner': 'Liechtenstein',
    'Venezuelan': 'Venezuela',
    'Slovene': 'Slovenia',
    'Scottish': 'Scotland',
    'Haitian': 'Haiti',
    'Jordanian': 'Jordan',
    'North Korean': 'North Korea',
    'Kenyan': 'Kenya',
    'Grenadian': 'Grenada',
    'Cameroonian': 'Cameroon',
    'Mauritian': 'Mauritius',
    'Russian': 'Russia',
    'Malagasy': 'Madagascar',
    'Zimbabwean': 'Zimbabwe',
    'Malawian': 'Malawi',
    'Lebanese': 'Lebanon',
    'Egyptian': 'Egypt',
    'Vanuatuan': 'Vanuatu',
    'Austrian': 'Austria',
    'Finnish': 'Finland',
    'Laotian': 'Laos',
    'Barbadian': 'Barbados',
    'Qatari': 'Qatar',
    'Saudi Arabian': 'Saudi Arabia',
    'Cypriot': 'Cyprus',
    'Chinese': 'China',
    'Western Samoan': 'Western Samoa',
    'Yemeni': 'Yemen',
    'Luxembourger': 'Luxembourg',
    'Frenchman': 'France',
    'Tobagonian': 'Trinidad and Tobago',
    'Tobagan': 'Trinidad and Tobago',
    'Swede': 'Sweden',
    'Georgian': 'Georgia',
    'Nigerien': 'Niger',
    'Nepalese': 'Nepal',
    'Belgian': 'Belgium',
    'US': 'United States of America',
    'American': 'United States of America',
    'Latvian': 'Latvia',
    'Peruvian': 'Peru',
    'Turkic': 'Turkey',
    'Turk': 'Turkey',
    'Hong Kongese': 'Hong Kong',
    'Englishman': 'England',
    'Iraqi': 'Iraq',
    'Bruneian': 'Brunei',
    'Afghan': 'Afghanistan',
    'Kuwaiti': 'Kuwait',
    'Canadian': 'Canada',
    'Serbian': 'Serbia',
    'Englishwoman': 'England',
    'Ukrainian': 'Ukraine',
    'Greek': 'Greece',
    'Zaïrean': 'Zaire',
    'Solomonian': 'Solomon Islands',
    'Welshman': 'Wales',
    'Tajik': 'Tajikistan',
    'Cambodian': 'Cambodia',
    'Turkmen': 'Turkmenistan',
    'Brazilian': 'Brazil',
    'Tadjik': 'Tajikistan',
    "Cote d'ivoire": 'Ivory Coast',
    'English': 'England',
    'Montenegrin': 'Montenegro',
    'Taiwanese': 'Taiwan',
    'Bhutanese': 'Bhutan',
    'Ivorian': 'Ivory Coast',
    'Botswanan': 'Botswana',
    'Bolivian': 'Bolivia',
    'Bahamian': 'Bahamas',
    'Macedonian': 'Macedonia',
    'Vietnamese': 'Vietnam',
    'Seychellois': 'Seychelles',
    'Ethiopian': 'Ethiopia',
    'Estonian': 'Estonia',
    'Senegalese': 'Senegal',
    'Spaniard': 'Spain',
    'Israeli': 'Israel',
    'Rwandan': 'Rwanda',
    'Liberian': 'Liberia',
    'Guinean': 'Papua New Guinea',
    'Singaporean': 'Singapore',
    'Tanzanian': 'Tanzania',
    'Japanese': 'Japan',
    'Emirates': 'United Arab Emirates',
    'Sierra Leonian': 'Sierra Leone',
    'Madagascan': 'Madagascar',
    'Polish': 'Poland',
    'Surinamer': 'Suriname',
    'Belarusian': 'Belarus',
    'Bahraini': 'Bahrain',
    'Algerian': 'Algeria',
    'USSR': 'Soviet Union',
    'Burkinese': 'Burkina',
    'Belarusan': 'Belarus',
    'Slovenian': 'Slovenia',
    'Chilean': 'Chile',
    'Costa Rican': 'Costa Rica',
    'Maldivian': 'Maldives',
    'Armenian': 'Armenia',
    'Ecuadorean': 'Ecuador',
    'Emirati': 'United Arab Emirates',
    'Mozambican': 'Mozambique',
    'Togolese': 'Togo',
    'Finn': 'Finland',
    'Turkoman': 'Turkmenistan',
    'Panamanian': 'Panama',
    'Angolan': 'Angola',
    'Scot': 'Scotland',
    'Syrian': 'Syria',
    'Frenchwoman': 'France',
    'Bulgarian': 'Bulgaria',
    'Croatian': 'Croatia',
    'Surinamese': 'Suriname',
    'Netherlander': 'Netherlands',
    'Paraguayan': 'Paraguay',
    'Nigerian': 'Nigeria',
    'German': 'Germany',
    'Tuvaluan': 'Tuvalu',
    'Uruguayan': 'Uruguay',
    'Mexican': 'Mexico',
    'Swazi': 'Swaziland',
    'Djiboutian': 'Djibouti',
    'Mauritanian': 'Mauritania',
    'Azerbaijani': 'Azerbaijan',
    'Libyan': 'Libya',
    'South Korean': 'South Korea',
    'Salvadorean': 'El Salvador',
    'French': 'France',
    'Nicaraguan': 'Nicaragua',
    'Omani': 'Oman',
    'Jamaican': 'Jamaica',
    'Uzbek': 'Uzbekistan',
    'Congolese': 'Congo',
    'Gambian': 'Gambia',
    'Dutchman': 'Netherlands',
    'Fijian': 'Fiji',
    'Ugandan': 'Uganda',
    'Argentinian': 'Argentina',
    'Papua New Guinean': 'Papua New Guinea',
    'Indian': 'India',
    'Dutchwoman': 'Netherlands',
    'Eritrean': 'Eritrea',
    'Ivory Coaster': 'Ivory Coast',
    'Saudi': 'Saudi Arabia',
    'Iranian': 'Iran',
    'Philippine': 'Philippines',
    'Mongolian': 'Mongolia',
    'Pakistani': 'Pakistan',
    'Sri Lankan': 'Sri Lanka',
    'Welshwoman': 'Wales',
    'Albanian': 'Albania',
    'Romanian': 'Romania',
    'Welsh': 'Wales',
    'Italian': 'Italy',
    'Slovak': 'Slovakia',
    'Colombian': 'Colombia',
    'Irishman': 'Northern Ireland Republic of Ireland',
    'Belizean': 'Belize',
    'Monacan': 'Monaco',
    'Norwegian': 'Norway',
    'Andorran': 'Andorra',
    'Moroccan': 'Morocco'
}

capitals_dict = {
    'vanuatu': 'port vila',
    'palestine': 'ramallah and gaza',
    'france': 'paris',
    'norway': 'oslo',
    'seychelles': 'victoria',
    'turks and caicos islands': 'cockburn town',
    'south korea': 'seoul',
    'nepal': 'kathmandu',
    'uganda': 'kampala',
    'ethiopia': 'addis ababa',
    'belize': 'belmopan',
    'bermuda': 'hamilton',
    'greece': 'athens',
    'bahrain': 'manama',
    'british virgin islands': 'road town',
    'liberia': 'monrovia',
    'mali': 'bamako',
    'greenland': 'nuuk',
    'cuba': 'havana',
    'venezuela': 'caracas',
    'thailand': 'bangkok',
    'barbados': 'bridgetown',
    'new zealand': 'wellington',
    'nigeria': 'abuja',
    'vatican city': 'vatican city',
    'croatia': 'zagreb',
    'aruba': 'oranjestad',
    'colombia': 'bogota',
    'kuwait': 'kuwait city',
    'belgium': 'brussels',
    'monaco': 'monaco',
    'austria': 'vienna',
    'sint maarten': 'philipsburg',
    'east timor': 'dili',
    'nauru': 'yaren',
    'iceland': 'reykjavik',
    'transnistria': 'tiraspol',
    'poland': 'warsaw',
    'taiwan': 'taipei',
    'saint pierre and miquelon': 'saint-pierre',
    'yemen': "sana'a", 'portugal': 'lisbon',
    'vietnam': 'hanoi',
    'bahamas': 'nassau',
    'somalia': 'mogadishu',
    'palau': 'ngerulmud',
    'anguilla': 'the valley',
    'ivory coast': 'yamoussoukro',
    'jamaica': 'kingston',
    'brazil': 'brasilia',
    'french guiana': 'cayenne',
    'niger': 'niamey',
    'guatemala': 'guatemala city',
    'd.r congo': 'kinshasa',
    'guinea-bissau': 'bissau',
    'pakistan': 'islamabad',
    'saint martin': 'philipsburg',
    'bulgaria': 'sofia',
    'paraguay': 'asuncion',
    'puerto rico': 'san juan',
    'israel': 'jerusalem',
    'trinidad and tobago': 'port of spain',
    'ghana': 'accra',
    'dominican republic': 'santo domingo',
    'spain': 'madrid',
    'madagascar': 'antananarivo',
    'botswana': 'gaborone',
    'luxembourg': 'luxembourg',
    'kazakhstan': 'astana',
    'bolivia': 'sucre',
    'christmas island': 'flying fish cove',
    'suriname': 'paramaribo',
    'estonia': 'tallinn',
    'cape verde': 'praia',
    'slovenia': 'ljubljana',
    'bangladesh': 'dhaka',
    'guam': 'hagatna',
    'south sudan': 'juba',
    'malaysia': 'kuala lumpur',
    'tanzania': 'dodoma',
    'japan': 'tokyo',
    'brunei': 'bandar seri begawan',
    'syria': 'damascus',
    'tonga': 'nukualofa',
    'cameroon': 'yaounde',
    'montenegro': 'podgorica',
    'montserrat': 'brades, plymouth',
    'gabon': 'libreville',
    'swaziland': 'mata-utu',
    'hungary': 'budapest',
    'jersey': 'saint helier',
    'mozambique': 'maputo',
    'honduras': 'tegucigalpa',
    'chad': "n'djamena", 'lesotho': 'maseru',
    'philippines': 'manila',
    'fiji': 'suva',
    'nicaragua': 'managua',
    'saint kitts and nevis': 'basseterre',
    'papua new guinea': 'port moresby',
    'republic of the congo': 'brazzaville',
    'tuvalu': 'funafuti',
    'guyana': 'georgetown',
    'czech republic': 'prague',
    'kiribati': 'tarawa',
    'slovakia': 'bratislava',
    'maldives': 'male',
    'united states of america': 'washington d.c.',
    'zimbabwe': 'harare',
    'azerbaijan': 'baku',
    'canada': 'ottawa',
    'gibraltar': 'gibraltar',
    'senegal': 'dakar',
    'new caledonia': 'noumea',
    'el salvador': 'san salvador',
    'china': 'beijing',
    'qatar': 'doha',
    'saint lucia': 'castries',
    'libya': 'tripoli',
    'kenya': 'nairobi',
    'kyrgyzstan': 'bishkek',
    'cambodia': 'phnom penh',
    'guinea': 'conakry',
    'uruguay': 'montevideo',
    'american samoa': 'pago pago',
    'zambia': 'lusaka',
    'micronesia': 'palikir',
    'faroe islands': 'torshavn',
    'tajikistan': 'dushanbe',
    'egypt': 'cairo',
    'dominica': 'roseau',
    'malawi': 'lilongwe',
    'bosnia and herzegovina': 'sarajevo',
    'united states virgin islands': 'charlotte amalie',
    'angola': 'luanda',
    'comoros': 'moroni',
    'central african republic': 'bangui',
    'myanmar': 'naypyidaw',
    'switzerland': 'bern',
    'sri lanka': 'sri jayawardenapura-kotte',
    'australia': 'canberra',
    'norfolk island': 'kingston',
    'afghanistan': 'kabul',
    'tokelau': 'nukunonu',
    'north korea': 'pyongyang',
    'isle of man': 'douglas',
    'burkina faso': 'ouagadougou',
    'laos': 'vientiane',
    'saint vincent and the grenadines': 'kingstown',
    'iraq': 'baghdad',
    'wallis and futuna': 'mata-utu',
    'northern mariana islands': 'saipan',
    'western sahara': 'el aaiun',
    'mauritania': 'nouakchott',
    'malta': 'valletta',
    'marshall islands': 'majuro',
    'georgia': 'tbilisi',
    'hong kong': 'hong kong city',
    'algeria': 'algiers',
    'iran': 'tehran',
    'morocco': 'rabat',
    'armenia': 'yerevan',
    'bhutan': 'thimphu',
    'ukraine': 'kiev',
    'sweden': 'stockholm',
    'lithuania': 'vilnius',
    'equatorial guinea': 'malabo',
    'denmark': 'copenhagen',
    'saudi arabia': 'riyadh',
    'andorra': 'andorra la vella',
    'niue': 'alofi',
    'india': 'new delhi',
    'italy': 'rome',
    'costa rica': 'san jose',
    'chile': 'santiago',
    'united kingdom': 'london',
    'pitcairn islands': 'adamstown',
    'kosovo': 'pristina',
    'grenada': "st. george's", 'moldova': 'chisinau',
    'finland': 'helsinki',
    'djibouti': 'djibouti-city',
    'sudan': 'khartoum',
    'cyprus': 'nicosia',
    'belarus': 'minsk',
    'mexico': 'mexico city',
    'antigua and barbuda': 'saint johns',
    'albania': 'tirana',
    'haiti': 'port-au-prince',
    'russia': 'moscow',
    'benin': 'porto-novo',
    'cocos islands': 'west island',
    'togo': 'lome',
    'argentina': 'buenos aires',
    'falkland islands': 'stanley',
    'rwanda': 'kigali',
    'samoa': 'apia',
    'eritrea': 'asmara',
    'united arab emirates': 'abu dhabi',
    'oman': 'muscat',
    'turkey': 'ankara',
    'saint barthelemy': 'gustavia',
    'burundi': 'bujumbura',
    'french polynesia': 'papeete',
    'mauritius': 'port louis',
    'liechtenstein': 'vaduz',
    'south africa': 'cape town',
    'serbia': 'belgrade',
    'turkmenistan': 'ashgabat',
    'tunisia': 'tunis',
    'panama': 'panama city',
    'peru': 'lima',
    'namibia': 'windhoek',
    'romania': 'bucharest',
    'singapore': 'singapore',
    'curacao': 'willemstad',
    'solomon islands': 'honiara',
    'guernsey': 'saint peter port',
    'latvia': 'riga',
    'indonesia': 'jakarta',
    'saint helena, ascension, and tristan da cunha': 'jamestown',
    'sierra leone': 'freetown',
    'netherlands': 'amsterdam',
    'mongolia': 'ulan bator',
    'ecuador': 'quito',
    'cook islands': 'avarua',
    'lebanon': 'beirut',
    'ireland': 'dublin',
    'germany': 'berlin',
    'uzbekistan': 'tashkent',
    'sao tome and principe': 'sao tome',
    'jordan': 'amman',
    'gambia': 'banjul',
    'macedonia': 'skopje',
    'san marino': 'san marino',
    'cayman islands': 'george town'
}

# if __name__ == '__main__':
#   html_content = open('nationalities_table.html', mode='r', encoding='utf8')
#   soup = BeautifulSoup(html_content, "html.parser")
#   rows = soup.find_all("tr")
#
#   for row in rows:
#       cells = row.find_all("td")
#       nationality = cells[0].text
#       for cell in cells:
#           descriptions = cell.text.split('&')
#           for desc in descriptions:
#               if desc and desc != nationality:
#                   nationalities_dict[desc] = nationality
#                   print(desc + ' -> ' + nationality)
#   print(nationalities_dict)
