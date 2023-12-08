from copy import deepcopy
data = open('input/3', 'r').read().splitlines()

num_cols = len(data[0])

#part 1

def gamma_most_digits(nums, pos):
    bit_counts = sum(int(num[pos]) for num in nums)
    return '1' if bit_counts > len(nums) / 2 else '0'

def epsilon_most_digits(nums, pos):
    bit_counts = sum(int(num[pos]) for num in nums)
    return '0' if bit_counts > len(nums) / 2 else '1'


gamma_digits = ''.join((gamma_most_digits(data, bit_index)) for bit_index in range(num_cols))
epsilon_digits = ''.join((epsilon_most_digits(data, bit_index) for bit_index in range(num_cols)))
gamma_rate = int(gamma_digits, 2)
epsilon_rate = int(epsilon_digits, 2)
print(gamma_rate * epsilon_rate)

#part 2
def oxygen_scrubber_rating(nums, pos):
    bit_counts = sum(int(num[pos]) for num in nums)
    print("pos = " + str(pos) + ". bit count is: " + str(bit_counts))
    if bit_counts > len(nums) / 2:
        return 1
    elif bit_counts < len(nums) / 2:
        return 0
    else:
        return 1

def CO2_scrubber_rating(nums, pos):
    bit_counts = sum(int(num[pos]) for num in nums)
    print("pos = " + str(pos) + ". bit count is: " + str(bit_counts))
    if bit_counts > len(nums) / 2:
        return 0
    elif bit_counts < len(nums) / 2:
        return 1
    else:
        return 0

oxygen_data = deepcopy(data)
while len(oxygen_data) != 1:
    for col in range(num_cols):
        most_common = oxygen_scrubber_rating(oxygen_data, col)
        res = filter(lambda x: int(x[col]) == most_common, oxygen_data)
        oxygen_data = list(res)

oxy_res = int(oxygen_data[0], 2)

co2data = deepcopy(data)
for col in range(num_cols):
    least_common = CO2_scrubber_rating(co2data, col)
    res = list(filter(lambda x: int(x[col]) == least_common, co2data))
    co2data = res
    if len(co2data) == 1:
        break

c02_res = int(co2data[0], 2)

print(oxy_res * c02_res)
