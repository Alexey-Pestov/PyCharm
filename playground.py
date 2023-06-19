def draw(characters):
  c = 0
  for i in range(10):
    draw = True
    for j in range(len(characters)):
        if c > characters[j][0]:
          continue
        if i == characters[j][0]:
          s = ''
          for k in characters[j:]:
              if k[0] == i:

                s = s + '_' * k[1] + 'M'
          if len(s) < 10:
              s = s + '_' * (10-len(s))
              c += 1
          if s == '':
              print('_' * j[1] + 'M' + '_' * (9 - j[1]))
              c += 1
          else:
              print(s)
          draw = False

    if draw == True:
        print('_' * 10)
        c += 1
    # print (c)