data = [int(i) for i in (open('input/1', 'r').read().split('\n'))]

res = 0
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        res += 1

print(res)

res2 = 0
sliding_window_sum = []
for i in range(0, len(data) - 2):
    sliding_window_sum.append(sum(data[i:i+3]))
for i in range(1, len(sliding_window_sum)):
    if sliding_window_sum[i] > sliding_window_sum[i-1]:
        res2 += 1

print(res2)