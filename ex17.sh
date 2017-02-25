# first make a sample file
echo "This is a test file." > test.txt
# then look at it
cat test.txt
# now run our script on it
python3.6 ex17.py test.txt new_file.txt
