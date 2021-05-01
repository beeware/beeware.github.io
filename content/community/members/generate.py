import csv
import os
import sys
from urllib.parse import quote
import hashlib


def generate(filename, basedir):
    with open(filename) as datafile:
        reader = csv.reader(datafile)
        got_header = False

        for line in reader:
            name = line[2]
            email = line[4]
            join_date = line[6]

            uid = hashlib.sha1(email.encode()).hexdigest()[0:8]

            if not got_header:
                if name != 'Buyer Name':
                    raise Exception("'Buyer name' column not in the expected location")
                elif email != 'Buyer Email':
                    raise Exception("'Buyer Email' column not in the expected location")
                elif join_date != 'Purchase Date':
                    raise Exception("'Purchase Date' column not in the expected location")
                got_header = True
                continue

            level = {
                'BeeWare Enthusiast Membership': 'individual',
                'BeeWare Professional Membership': 'professional',
                'BeeWare Bronze Membership': 'bronze',
                'BeeWare Silver Membership': 'silver',
                'BeeWare Gold Membership': 'gold',
            }.get(line[1], 'other')

            if level != "professional":
                email = "%s@******.com" % email.split("@")[0]

            outdir = os.path.join(basedir, uid)
            if os.path.exists(outdir):
                print("User %s already exists" % uid)
            else:
                os.mkdir(outdir)
                with open(os.path.join(outdir, 'contents.lr'), 'w') as outfile:
                    outfile.write('name: %s\n' % name)
                    outfile.write('---\n')
                    outfile.write('uid: %s\n' % uid)
                    outfile.write('---\n')
                    outfile.write('email: %s\n' % email)
                    outfile.write('---\n')
                    outfile.write('level: %s\n' % level)
                    outfile.write('---\n')
                    outfile.write('join_date: %s\n' % join_date)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: %s <data.csv> <output directory>" % sys.argv[0])
        sys.exit(1)

    generate(sys.argv[1], sys.argv[2])
