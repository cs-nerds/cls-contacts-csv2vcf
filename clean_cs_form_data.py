#!/usr/bin/env python3

import csv

def clean_row(row: list) -> list:
    """
    Transform csv row to desired format for the ContactConverter csv.
    Returns:
        [given_name,additional_name,family_name,prefix,suffix,home_email,
        work_email,mobile_phone,work_phone,organisation,title,admission_number]
    """
    cleaned_row = []
    _, name, adm, wmail, hmail, mphone, wphone, _ = row
    # correct some phone numbers
    mphone = mphone if mphone.startswith(('07', '+254')) or not mphone else '0' + mphone
    wphone = wphone if wphone.startswith(('07', '+254')) or not wphone else '0' + wphone
    # capitalize names
    fnames = [name.capitalize() for name in name.split(' ')]
    # given_name,additional_name,family_name
    if len(fnames) > 2:
        cleaned_row.append(fnames[0])
        cleaned_row.append(fnames[1])
        cleaned_row.append(' '.join(fnames[2:]))
    else:
        cleaned_row.append(fnames[0])
        cleaned_row.append('')
        cleaned_row.append(fnames[1])
    # prefix,suffix,home_email,work_email,mobile_phone,work_phone
    cleaned_row.append('')
    cleaned_row.append('')
    cleaned_row.append(hmail.lower())
    cleaned_row.append(wmail.lower())
    cleaned_row.append(mphone)
    cleaned_row.append(wphone)
    # organisation,title,admission_number
    cleaned_row.append('JKUAT')
    cleaned_row.append('CS Classmate')
    cleaned_row.append(adm.upper())
    return cleaned_row

def clean_csv_data(csv_file: str, clean_file: str) -> None:
    """
    Transform csv data to consumable format and save to clean file.
    """
    with open(csv_file, 'r') as infile, open(clean_file, 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None) # skip the headers
        writer = csv.writer(outfile)
        writer.writerow(
        ['given_name','additional_name','family_name','prefix','suffix','home_email',
        'work_email','mobile_phone','work_phone','organisation','title','admission_number']
        ) # write headers first
        for row in reader:
            writer.writerow(clean_row(row))
    

if __name__ == '__main__':
    clean_csv_data('cs_nerds.csv', 'cs_nerds_clean.csv')

