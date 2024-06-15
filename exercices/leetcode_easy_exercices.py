# LeetCode python exercices

#1
games = ["3:2", "2,1", "1:0", "0:0", "0:5"]


def points(list_games):
  team_points = 0
  for game in list_games:
    if game[0] > game[2]:
      team_points += 3
    elif game[0] == game[2]:
      team_points += 1

  return team_points


# print(points(games))


#2
def even_or_odd(number):
  return 'Even' if number % 2 == 0 else 'Odd'


# print(even_or_odd(51))


#3
def sum_array(arr):
  return sum(arr)


# print(sum_array([]))


#4
def paperwork(n, m):
  if n <= 0 or m <= 0:
    return 0
  return n * m


#5
def double(nums):
  return [2 * n for n in nums]


#6
def twice_age(father_age, son_age):
  return abs(father_age - 2 * son_age)


# print(twice_age(47, 30))


#7
def count_by(x, n):
  counter = 0
  result = []
  num = 1
  while True:
    if counter == n:
      break
    if num % x == 0:
      counter += 1
      result.append(num)
    num += 1
  return result


def count_by_second_solution(x, n):
  return list(range(x, x * n + 1, x))


def count_by_third_solution(x, n):
  return [x * i for i in range(1, n + 1)]