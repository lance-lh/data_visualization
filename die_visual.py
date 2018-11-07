from die import Die
import pygal

# create a D6
die = Die()

# roll dice several times and store the results in a list
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)
# print(results)

frequencies = []

for value in range(1,die.num_sides+1):
    frequency = results.count(value) # results contain all roll dice results
    frequencies.append(frequency)

# print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_titles = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')


