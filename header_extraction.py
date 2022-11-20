import re

# create list for the headers
headers = []

with open('attributes.txt') as f_hand:
    for line in f_hand:
        line = line.strip()

        # Extract list of headers
        x = re.findall('^[0-9]+\. (\S+):', line)
        headers.extend(x)

print(headers, '\n')
print(len(headers))

# Write the list of headers to a text file.
print("Please enter the file name you'd like to save to.\n"
      "Do not add the suffix.")
raw_headers_file = str(input())
headersfile = raw_headers_file + '.txt'

with open(headersfile, mode='w') as hfile:
    for val in headers:
        if val != headers[len(headers) - 1]:
            hfile.write(f'{val}, ')
        else:
            hfile.write(val)

print(f"Please check the file, {headersfile}.\n"
      f"Thank you!")