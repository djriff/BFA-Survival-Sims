import os
import argparse
import sys
import secrets

from os import listdir
from os.path import isfile, join

profiles = []
apiKey = secrets.apiKey
version = 'nightly'
weights = '-s'

parser = argparse.ArgumentParser(description='Parses a list of reports from Raidbots.')
parser.add_argument('dir', help='Directory you wish to sim. Options are 1. talents/ 2. racials/ 3. gear/ 4. enchants/ 5. consumables/ 6. azerite-traits/')
parser.add_argument('--weights', help='For sims ran with weights this flag will change how simParser is ran.', action='store_true')
parser.add_argument('--iterations', help='Pass through specific iterations to run on. Default is "smart"')
parser.add_argument('--composite', help='Run a raidsimming batch of sims. Value can be either HH or MM.', choices=['HC','MM'])
parser.add_argument('--talents', help='indicate talent build for output.', choices=['ViV','ToE', 'AP'])
args = parser.parse_args()

if args.weights:
    weights = ''

if int(args.iterations) > 0:
    iterations = args.iterations
else:
    iterations = "smart"

#iterations=10000
sys.path.insert(0, args.dir)
import reports

print("Running sims on {0} in {1}".format(version, args.dir))

# determine sim files
if args.composite:
    for value in reports.reportsRS:
        profile = value.replace('results/_', 'profiles/%s_' % args.composite)
        profile = profile.replace('json', 'simc')
        profiles.append(profile)
else:
    for value in reports.reports:
        profile = value.replace('results', 'profiles')
        profile = profile.replace('json', 'simc')
        profiles.append(profile)

# determine existing jsons
existing = listdir(args.dir + 'results/')
count = 0

for value in profiles:
    count = count + 1
    
    name = value.replace('simc', 'json')
    name = name.replace('profiles', 'results')
    if name[8:] not in existing:
        print("Simming {0} out of {1}.".format(count, len(profiles)))
        reportName = args.dir + name[8:-5]
        name = args.dir + name
        value = args.dir + value
        cmd = "python api.py {0} {1} --simc_version {2} {3} {4} --iterations {5}".format(apiKey, value, version, name, reportName, iterations)
        os.system(cmd)
    else:
        print("{0} already exists. Skipping file.".format(name[8:]))

results_dir = args.dir + "results/"
cmd = "python3 simParser.py -c {0} -r -d {1}".format(weights, results_dir)
os.system(cmd)

# analyze.py
if args.composite:
    script = "analyzeRS.py"
else:
    script = "analyze.py"

cmd = "python2 {0} {1}".format(script, args.dir)

if args.weights:
    cmd += " --weights"
if args.composite:
    cmd += " --composite {0}".format(args.composite)
if args.talents:
    cmd += " --talents {0}".format(args.talents)
os.system(cmd)
