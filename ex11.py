### @export "fake"
import fake_input
input, input = fake_input.create(['38', '6\'2"', '180lbs'])

### @export "code"
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

