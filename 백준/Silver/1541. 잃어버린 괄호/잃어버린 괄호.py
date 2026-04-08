# 양수와 +, -, 괄호를 가지고 식을 만들었다.
# 괄호를 모두 지운 식을 주었을때
# 괄호를 적절히 쳐서 이식의 값을 최소로 만들려고 한다.
# 입력으로 식이 주어진다.
import sys
input_data = sys.stdin.readline().rstrip().split('-')

result = 0


first_group = input_data[0].split('+')
for num in first_group:
    result += int(num)

# 2. 나머지 그룹 처리 (괄호를 쳐서 합친 뒤 뺌)
for group in input_data[1:]:
    sub_sum = sum(map(int, group.split('+')))
    result -= sub_sum

print(result)