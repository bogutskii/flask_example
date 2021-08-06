say = 'Welcome. I will quiz you. Are you ready?y/n'
input(say)
score = 0
print('I don\'t care. Get ready, if you aren\'t.')
print('Question 1.')
print('Who is Trump\'s vice president in 2020?')
a = 'Aaron Burr'
b = 'Thomas Jefferson'
c = 'Mike Pence'
print('A =', a)
print('B =', b)
print('C =', c)
correct_ans = 'c'
ans = input('Which one do you pick? A, B, or C?')
if ans == correct_ans:
  print('Correct!', end='\n\n\n\n')
  score = score + 1
else:
  print('Incorrect!', end='\n\n')
print('Question 2.')
print('Who was Thomas Jefferson\'s vice president?')
a = 'Woodrow Wilson'
b = 'Aaron Burr'
c = 'John Adams'
print('A =', a)
print('B =', b)
print('C =', c)
correct_ans = 'b'
ans = input('Which one do you pick? A, B, or C?')
if ans == correct_ans:
  print('Correct!', end='\n\n\n\n')
  score = score + 1
else:
  print('Incorrect!', end='\n\n')
print('Question 3.')
print('Which holiday is not just celebrated by America?')
a = 'Thanksgiving'
b = 'Independence Day'
c = 'Presidents\' Day'
d = 'New Year\'s'
print('A =', a)
print('B =', b)
print('C =', c)
print('D =', d)
correct_ans = 'd'
ans = input('Which one do you pick? A, B, C, or D?')
if ans == correct_ans:
  print('Correct!', end='\n\n\n\n')
  score = score + 1
else:
  print('Incorrect!', end='\n\n')
print('Question 4.')
print('Which president wasn\'t part of the "Whig" political party?')
a = 'William Henry Harrison'
b = 'John Tyler'
c = 'James Polk'
d = 'Zachary Taylor'
print('A =', a)
print('B =', b)
print('C =', c)
print('D =', d)
correct_ans = 'c'
ans = input('Which one do you pick? A, B, C, or D?')
if ans == correct_ans:
  print('Correct!', end='\n\n\n\n')
  score = score + 1
else:
  print('Incorrect!', end='\n\n')
print('Question 5.')
print('What is Mario\'s last name?')
a = 'Luigi'
b = 'Man'
c = 'Mario'
d = 'Jumpman'
print('A =', a)
print('B =', b)
print('C =', c)
print('D =', d)
correct_ans = 'c'
ans = input('Which one do you pick?A, B, C, or D?')
if ans == correct_ans:
  print('Correct!', end='\n\n\n\n')
  score = score + 1
else:
  print('Incorrect!', end='\n\n')
print('Question 6.')
print('The first web browser, WORLDWIDEWEB, was later renamed Nexus.')
correct_ans = 'true'
ans = input('True or false?')
if ans == correct_ans:
  print('Correct!', end='\n\n\n\n')
  score = score + 1
else:
  print('Incorrect!', end='\n\n')
print('Question 7.')
print('The venus flytrap has many species.')
correct_ans = 'false'
ans = input('True or false?')
if ans == correct_ans:
  print('Correct!', end='\n\n\n\n')
  score = score + 1
else:
  print('Incorrect!', end='\n\n')
print('Question 8.')
print('Which sickness does the tsetse fly carry?')
a = 'malaria'
b = 'sleeping sickness'
c = 'COVID-19'
print('A =', a)
print('B =', b)
print('C =', c)
correct_ans = 'b'
ans = input('Which one do you pick? A, B, or C?')
if ans == correct_ans:
  print('Correct!', end='\n\n\n\n')
  score = score + 1
else:
  print('Incorrect!', end='\n\n')