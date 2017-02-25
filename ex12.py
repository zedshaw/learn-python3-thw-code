### @export "fake"
import fake_input
input, input = fake_input.create(['38', '6\'2"', '180lbs'])

### @export "code"
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

