import sys
script , input_encoding , error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file,encoding,errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    rawbytes = next_lang.encode(encoding, errors=errors)
    coostr = rawbytes.decode(encoding, errors=errors)

    print(rawbytes, ":===:" ,coostr)

languages = open("languages.txt",encoding="utf-8")

main(languages ,input_encoding ,error)
