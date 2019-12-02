INPUT="""1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,2,9,19,23,1,23,6,27,1,13,27,31,1,31,10,35,1,9,35,39,1,39,9,43,2,6,43,47,1,47,5,51,2,10,51,55,1,6,55,59,2,13,59,63,2,13,63,67,1,6,67,71,1,71,5,75,2,75,6,79,1,5,79,83,1,83,6,87,2,10,87,91,1,9,91,95,1,6,95,99,1,99,6,103,2,103,9,107,2,107,10,111,1,5,111,115,1,115,6,119,2,6,119,123,1,10,123,127,1,127,5,131,1,131,2,135,1,135,5,0,99,2,0,14,0"""


def processAdd(values, index):
    print (values)
    pos1 = int(values[index+1])
    pos2 = int(values[index+2])
    result = int(values[index+3])
    print ("ADD %d %d %d" % (pos1, pos2, result))

    val1 = int(values[pos1])
    val2 = int(values[pos2])
    values[result] = val1 + val2
    print ("%d+%d into %d" % (val1, val2, result))
    return values

def processMultiply(values, index):
    print (values)
    pos1 = int(values[index+1])
    pos2 = int(values[index+2])
    result = int(values[index+3])
    print ("MUL %d %d %d" % (pos1, pos2, result))

    val1 = int(values[pos1])
    val2 = int(values[pos2])
    values[result] = val1 * val2
    print ("%d*%d into %d" % (val1, val2, result))
    return values

def process(values):
  index = 0

  opcode = int(values[index])
  while (opcode != 99):
      print ("Index %d, opcode %d" % (index, opcode))
      if opcode == 1:
          values = processAdd(values, index)
      elif opcode == 2:
          values = processMultiply(values, index)

      index += 4
      if index > len(values):
          break
      opcode = int(values[index])


  return values[0]

print process("1,0,0,0,99".split(','))
print process("2,3,0,3,99".split(','))
print process("2,4,4,5,99,0".split(','))
print process("1,1,1,4,99,5,6,0,99".split(','))
print process("1,9,10,3,2,3,11,0,99,30,40,50".split(','))
vals = INPUT.split(',')
vals[1] = 12
vals[2] = 2
print process(vals)
