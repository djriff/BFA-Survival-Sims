source_profile = "test.simc"
pClass = 'hunter'
spec = 'survival'

profile = source_profile + "\n"
profile += "default_actions=1\n"

def getname( talent_numbers, select_spec ):
    if(select_spec == 'survival') : talent_names_gen = getname_survival(talent_numbers)
    if(select_spec == 'shadow') : talent_names_gen = getname_shadow(talent_numbers)
    return talent_names_gen

def getname_survival( talent_numbers ):
    talents = [
        ('ViV', 'ToE', 'AP'),
        ('GT', 'HB', 'Butc'),
        ('', '', ''),
        ('BS', 'ST', 'AMoC'),
        ('', '', ''),
        ('TotS', 'MB', 'FS'),
        ('BoP', 'WI', 'Chak')
    ]
    res = [row[x-1] for (row, x) in zip(talents, talent_numbers)]
    return '_'.join(r for r in res if r != '')

def getname_shadow( talent_numbers ):
    talents = [
        ('FotM', 'SI', 'SWV'),
        ('', '', ''),
        ('ToF', 'Mis', 'DV'),
        ('', '', ''),
        ('AS', 'SWD', 'SC'),
        ('LI', 'MB', 'VT'),
        ('LotV', 'DA', 'STM')
    ]
    res = [row[x-1] for (row, x) in zip(talents, talent_numbers)]
    return '_'.join(r for r in res if r != '')



import itertools
if pClass == 'hunter':
	options = [range(1,4), range(1,4), [1], range(1,4), [1], range(1,4), range(1,4)]
else:
	options = [range(1,4), [1], range(1,4), range(1,4), range(1,4), range(1,4), range(1,4)]

for talents in itertools.product(*options):
    temp_names = getname( talents, spec )
    profile += "\n" + 'profileset."' + temp_names + '"' + "+=talents=" + ''.join(map(str, talents))

print(profile)