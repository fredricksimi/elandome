# Generated by Django 4.1.2 on 2022-10-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('preferred_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state_or_province', models.CharField(max_length=100)),
                ('country_of_origin', models.CharField(choices=[('AF', 'AFGHANISTAN'), ('AL', 'ALBANIA'), ('DZ', 'ALGERIA'), ('AS', 'AMERICAN SAMOA'), ('AD', 'ANDORRA'), ('AO', 'ANGOLA'), ('AI', 'ANGUILLA'), ('AQ', 'ANTARCTICA'), ('AG', 'ANTIGUA AND BARBUDA'), ('AR', 'ARGENTINA'), ('AM', 'ARMENIA'), ('AW', 'ARUBA'), ('AU', 'AUSTRALIA'), ('AT', 'AUSTRIA'), ('AZ', 'AZERBAIJAN'), ('BS', 'BAHAMAS'), ('BH', 'BAHRAIN'), ('BD', 'BANGLADESH'), ('BB', 'BARBADOS'), ('BY', 'BELARUS'), ('BE', 'BELGIUM'), ('BZ', 'BELIZE'), ('BJ', 'BENIN'), ('BM', 'BERMUDA'), ('BT', 'BHUTAN'), ('BO', 'BOLIVIA'), ('BA', 'BOSNIA AND HERZEGOVINA'), ('BW', 'BOTSWANA'), ('BV', 'BOUVET ISLAND'), ('BR', 'BRAZIL'), ('IO', 'BRITISH INDIAN OCEAN TERRITORY'), ('BN', 'BRUNEI DARUSSALAM'), ('BG', 'BULGARIA'), ('BF', 'BURKINA FASO'), ('BI', 'BURUNDI'), ('KH', 'CAMBODIA'), ('CM', 'CAMEROON'), ('CA', 'CANADA'), ('CV', 'CAPE VERDE'), ('KY', 'CAYMAN ISLANDS'), ('CF', 'CENTRAL AFRICAN REPUBLIC'), ('TD', 'CHAD'), ('CL', 'CHILE'), ('CN', 'CHINA'), ('CX', 'CHRISTMAS ISLAND'), ('CC', 'COCOS (KEELING) ISLANDS'), ('CO', 'COLOMBIA'), ('KM', 'COMOROS'), ('CG', 'CONGO'), ('CD', 'CONGO, THE DEMOCRATIC REPUBLIC OF'), ('CK', 'COOK ISLANDS'), ('CR', 'COSTA RICA'), ('CI', "CÃ”TE D'IVOIRE"), ('HR', 'CROATIA'), ('CU', 'CUBA'), ('CY', 'CYPRUS'), ('CZ', 'CZECH REPUBLIC'), ('DK', 'DENMARK'), ('DJ', 'DJIBOUTI'), ('DM', 'DOMINICA'), ('DO', 'DOMINICAN REPUBLIC'), ('EC', 'ECUADOR'), ('EG', 'EGYPT'), ('SV', 'EL SALVADOR'), ('GQ', 'EQUATORIAL GUINEA'), ('ER', 'ERITREA'), ('EE', 'ESTONIA'), ('ET', 'ETHIOPIA'), ('FK', 'FALKLAND ISLANDS (MALVINAS)'), ('FO', 'FAROE ISLANDS'), ('FJ', 'FIJI'), ('FI', 'FINLAND'), ('FR', 'FRANCE'), ('GF', 'FRENCH GUIANA'), ('PF', 'FRENCH POLYNESIA'), ('TF', 'FRENCH SOUTHERN TERRITORIES'), ('GA', 'GABON'), ('GM', 'GAMBIA'), ('GE', 'GEORGIA'), ('DE', 'GERMANY'), ('GH', 'GHANA'), ('GI', 'GIBRALTAR'), ('GR', 'GREECE'), ('GL', 'GREENLAND'), ('GD', 'GRENADA'), ('GP', 'GUADELOUPE'), ('GU', 'GUAM'), ('GT', 'GUATEMALA'), ('GN', 'GUINEA'), ('GW', 'GUINEA'), ('GY', 'GUYANA'), ('HT', 'HAITI'), ('HM', 'HEARD ISLAND AND MCDONALD ISLANDS'), ('HN', 'HONDURAS'), ('HK', 'HONG KONG'), ('HU', 'HUNGARY'), ('IS', 'ICELAND'), ('IN', 'INDIA'), ('ID', 'INDONESIA'), ('IR', 'IRAN, ISLAMIC REPUBLIC OF'), ('IQ', 'IRAQ'), ('IE', 'IRELAND'), ('IL', 'ISRAEL'), ('IT', 'ITALY'), ('JM', 'JAMAICA'), ('JP', 'JAPAN'), ('JO', 'JORDAN'), ('KZ', 'KAZAKHSTAN'), ('KE', 'KENYA'), ('KI', 'KIRIBATI'), ('KP', "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"), ('KR', 'KOREA, REPUBLIC OF'), ('KW', 'KUWAIT'), ('KG', 'KYRGYZSTAN'), ('LA', "LAO PEOPLE'S DEMOCRATIC REPUBLIC"), ('LV', 'LATVIA'), ('LB', 'LEBANON'), ('LS', 'LESOTHO'), ('LR', 'LIBERIA'), ('LY', 'LIBYAN ARAB JAMAHIRIYA'), ('LI', 'LIECHTENSTEIN'), ('LT', 'LITHUANIA'), ('LU', 'LUXEMBOURG'), ('MO', 'MACAO'), ('MK', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF'), ('MG', 'MADAGASCAR'), ('MW', 'MALAWI'), ('MY', 'MALAYSIA'), ('MV', 'MALDIVES'), ('ML', 'MALI'), ('MT', 'MALTA'), ('MH', 'MARSHALL ISLANDS'), ('MQ', 'MARTINIQUE'), ('MR', 'MAURITANIA'), ('MU', 'MAURITIUS'), ('YT', 'MAYOTTE'), ('MX', 'MEXICO'), ('FM', 'MICRONESIA, FEDERATED STATES OF'), ('MD', 'MOLDOVA, REPUBLIC OF'), ('MC', 'MONACO'), ('MN', 'MONGOLIA'), ('MS', 'MONTSERRAT'), ('MA', 'MOROCCO'), ('MZ', 'MOZAMBIQUE'), ('MM', 'MYANMAR'), ('NA', 'NAMIBIA'), ('NR', 'NAURU'), ('NP', 'NEPAL'), ('NL', 'NETHERLANDS'), ('AN', 'NETHERLANDS ANTILLES'), ('NC', 'NEW CALEDONIA'), ('NZ', 'NEW ZEALAND'), ('NI', 'NICARAGUA'), ('NE', 'NIGER'), ('NG', 'NIGERIA'), ('NU', 'NIUE'), ('NF', 'NORFOLK ISLAND'), ('MP', 'NORTHERN MARIANA ISLANDS'), ('NO', 'NORWAY'), ('OM', 'OMAN'), ('PK', 'PAKISTAN'), ('PW', 'PALAU'), ('PS', 'PALESTINIAN TERRITORY, OCCUPIED'), ('PA', 'PANAMA'), ('PG', 'PAPUA NEW GUINEA'), ('PY', 'PARAGUAY'), ('PE', 'PERU'), ('PH', 'PHILIPPINES'), ('PN', 'PITCAIRN'), ('PL', 'POLAND'), ('PT', 'PORTUGAL'), ('PR', 'PUERTO RICO'), ('QA', 'QATAR'), ('RE', 'RÃ‰UNION'), ('RO', 'ROMANIA'), ('RU', 'RUSSIAN FEDERATION'), ('RW', 'RWANDA'), ('SH', 'SAINT HELENA'), ('KN', 'SAINT KITTS AND NEVIS'), ('LC', 'SAINT LUCIA'), ('PM', 'SAINT PIERRE AND MIQUELON'), ('VC', 'SAINT VINCENT AND THE GRENADINES'), ('WS', 'SAMOA'), ('SM', 'SAN MARINO'), ('ST', 'SAO TOME AND PRINCIPE'), ('SA', 'SAUDI ARABIA'), ('SN', 'SENEGAL'), ('CS', 'SERBIA AND MONTENEGRO'), ('SC', 'SEYCHELLES'), ('SL', 'SIERRA LEONE'), ('SG', 'SINGAPORE'), ('SK', 'SLOVAKIA'), ('SI', 'SLOVENIA'), ('SB', 'SOLOMON ISLANDS'), ('SO', 'SOMALIA'), ('ZA', 'SOUTH AFRICA'), ('GS', 'SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS'), ('ES', 'SPAIN'), ('LK', 'SRI LANKA'), ('SD', 'SUDAN'), ('SR', 'SURINAME'), ('SJ', 'SVALBARD AND JAN MAYEN'), ('SZ', 'SWAZILAND'), ('SE', 'SWEDEN'), ('CH', 'SWITZERLAND'), ('SY', 'SYRIAN ARAB REPUBLIC'), ('TW', 'TAIWAN, PROVINCE OF CHINA'), ('TJ', 'TAJIKISTAN'), ('TZ', 'TANZANIA, UNITED REPUBLIC OF'), ('TH', 'THAILAND'), ('TL', 'TIMOR'), ('TG', 'TOGO'), ('TK', 'TOKELAU'), ('TO', 'TONGA'), ('TT', 'TRINIDAD AND TOBAGO'), ('TN', 'TUNISIA'), ('TR', 'TURKEY'), ('TM', 'TURKMENISTAN'), ('TC', 'TURKS AND CAICOS ISLANDS'), ('TV', 'TUVALU'), ('UG', 'UGANDA'), ('UA', 'UKRAINE'), ('AE', 'UNITED ARAB EMIRATES'), ('GB', 'UNITED KINGDOM'), ('US', 'UNITED STATES'), ('UM', 'UNITED STATES MINOR OUTLYING ISLANDS'), ('UY', 'URUGUAY'), ('UZ', 'UZBEKISTAN'), ('VU', 'VANUATU'), ('VN', 'VIET NAM'), ('VG', 'VIRGIN ISLANDS, BRITISH'), ('VI', 'VIRGIN ISLANDS, U.S.'), ('WF', 'WALLIS AND FUTUNA'), ('EH', 'WESTERN SAHARA'), ('YE', 'YEMEN'), ('ZW', 'ZIMBABWE')], max_length=50)),
                ('home_phone', models.CharField(max_length=50)),
                ('mobile_phone', models.CharField(max_length=50)),
                ('office_tel', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('- Select -', '- Select -'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
                ('education_or_experience', models.TextField()),
                ('health_conditions_disabilities', models.TextField()),
                ('preferred_program', models.CharField(choices=[('- Select -', '- Select -'), ('Volunteer Services', 'Volunteer Services'), ('Strategic Planning, Coordination & Monitoring', 'Strategic Planning, Coordination & Monitoring'), ('Project Management', 'Project Management'), ('Workshops & Training', 'Workshops & Training'), ('Career Counselling', 'Career Counselling')], max_length=50)),
                ('personalized_preferrences', models.TextField()),
                ('travel_pack', models.CharField(choices=[('- Select -', '- Select -'), ('Individual', 'Individual'), ('Group', 'Group')], max_length=50)),
                ('preferred_package', models.CharField(choices=[('- Select -', '- Select -'), ('Family', 'Family'), ('Friends', 'Friends'), ('Students', 'Students'), ('Employees', 'Employees'), ('Individuals', 'Individuals'), ('Teachers', 'Teachers')], max_length=50)),
                ('duration_of_stay', models.CharField(max_length=100)),
                ('preferred_city', models.CharField(max_length=100)),
                ('date_of_travel', models.DateField()),
                ('do_you_require_further_information', models.TextField()),
                ('how_did_you_hear_about_us', models.CharField(choices=[('- Select -', '- Select -'), ('Through a friend', 'Through a friend'), ('LinkedIn', 'LinkedIn'), ('Social Media', 'Social Media'), ('Blog Post', 'Blog Post'), ('Word of Mouth', 'Word of Mouth'), ('Email', 'Email'), ('Online Ad', 'Online Ad'), ('Other', 'Other')], max_length=100)),
                ('any_other_comments', models.TextField()),
                ('emergency_contact_full_name', models.CharField(max_length=100)),
                ('emergency_contact_telephone_no', models.CharField(max_length=50)),
                ('emergency_contact_residential_address', models.CharField(max_length=100)),
                ('emergency_contact_relationship', models.CharField(max_length=100)),
                ('referee_contact_full_name', models.CharField(max_length=100)),
                ('referee_contact_organization', models.CharField(max_length=100)),
                ('referee_contact_telephone_no', models.CharField(max_length=50)),
                ('referee_contact_work_address', models.CharField(max_length=100)),
                ('date_of_application', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
