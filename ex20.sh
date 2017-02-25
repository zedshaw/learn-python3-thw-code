### @export "setup"
echo "This is line 1" > test.txt
echo "This is line 2" >> test.txt
echo "This is line 3" >> test.txt
### @export "run"
python3.6 ex20.py test.txt
