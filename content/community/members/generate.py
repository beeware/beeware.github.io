import csv
import os
import sys
from urllib.parse import quote


def generate(filename, basedir):
    with open(filename) as datafile:
        reader = csv.reader(datafile)
        next(reader)
        for line in reader:
            print(line[0], line[1], line[2], line[4])

            level = {
                'BeeWare Enthusiast Membership': 'individual',
                'BeeWare Professional Membership': 'professional',
                'BeeWare Bronze Membership': 'bronze',
                'BeeWare Silver Membership': 'silver',
                'BeeWare Gold Membership': 'gold',
            }.get(line[0], 'other')

            outdir = os.path.join(basedir, quote(line[2]))
            if os.path.exists(outdir):
                print("User %s already exists" % line[2])
            else:
                os.mkdir(outdir)
                with open(os.path.join(outdir, 'contents.lr'), 'w') as outfile:
                    outfile.write('name: %s\n' % line[1])
                    outfile.write('---\n')
                    outfile.write('email: %s\n' % line[2])
                    outfile.write('---\n')
                    outfile.write('level: %s\n' % level)
                    outfile.write('---\n')
                    outfile.write('join_date: %s\n' % line[4])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: %s <data.csv> <output directory>" % sys.argv[0])
        sys.exit(1)

    generate(sys.argv[1], sys.argv[2])
