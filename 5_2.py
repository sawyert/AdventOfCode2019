INPUT="""3,225,1,225,6,6,1100,1,238,225,104,0,1101,72,36,225,1101,87,26,225,2,144,13,224,101,-1872,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,66,61,225,1102,25,49,224,101,-1225,224,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1101,35,77,224,101,-112,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1002,195,30,224,1001,224,-2550,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1102,30,44,225,1102,24,21,225,1,170,117,224,101,-46,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1102,63,26,225,102,74,114,224,1001,224,-3256,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1101,58,22,225,101,13,17,224,101,-100,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1101,85,18,225,1001,44,7,224,101,-68,224,224,4,224,102,8,223,223,1001,224,5,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,677,226,224,102,2,223,223,1005,224,329,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,344,1001,223,1,223,1107,677,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,374,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,389,101,1,223,223,8,226,677,224,1002,223,2,223,1005,224,404,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,419,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,434,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1108,677,677,224,102,2,223,223,1006,224,464,101,1,223,223,1007,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,509,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,524,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,539,1001,223,1,223,108,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,569,101,1,223,223,8,226,226,224,102,2,223,223,1006,224,584,101,1,223,223,1008,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,614,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,629,101,1,223,223,7,677,677,224,1002,223,2,223,1005,224,644,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,659,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226"""


INPUT2 = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""

def getValue(values, param_mode, location):
    param_mode = "00000000000" + param_mode
    #print ("Start param mode %s" % param_mode)
    pm = param_mode[-1:]
    #print ("Next param mode %s" % pm)
    param_mode = param_mode[:-1]
    #print ("End param mode %s" % param_mode)
    if pm == '1':
        val = int(values[location])
    elif pm == '0':
        pos = int(values[location])
        val = int(values[pos])
    else:
        print "Borked"
        exit(1)

    return int(val), param_mode

def processAdd(values, index, param_mode):
    index += 1
    val1, param_mode = getValue(values, param_mode, index)
    index += 1
    val2, param_mode = getValue(values, param_mode, index)
    index += 1
    result = int(values[index])

    print ("ADD %d %d %d" % (val1, val2, result))
    values[result] = val1 + val2
    print "Result is %d" % values[result]

    index += 1
    return index, values

def processMultiply(values, index, param_mode):
    index += 1
    val1, param_mode = getValue(values, param_mode, index)
    index += 1
    val2, param_mode = getValue(values, param_mode, index)
    index += 1
    result = int(values[index])

    values[result] = val1 * val2
    print "Result is %d" % values[result]

    index += 1
    return index, values

def processInput(values, index, param_mode):
    input_string = raw_input("value? ")
    index += 1
    param1 = int(values[index])
    print ("STR %s in %d" % (input_string, param1))
    values[int(param1)] = input_string

    index += 1
    return index, values

def processOutput(values, index, param_mode):
    index += 1
    param1, param_mode = getValue(values, param_mode, index)
    print "!!! OUTPUT %d" % param1

    index += 1
    return index, values

def processJumpIfTrue(values, index, param_mode):
    index += 1
    val1, param_mode = getValue(values, param_mode, index)
    index += 1
    val2, param_mode = getValue(values, param_mode, index)

    if val1 != 0:
        index = val2
    else:
        index += 1
    return index, values

def processJumpIfFalse(values, index, param_mode):
    index += 1
    val1, param_mode = getValue(values, param_mode, index)
    index += 1
    val2, param_mode = getValue(values, param_mode, index)

    if val1 == 0:
        index = val2
    else:
        index += 1
    return index, values

def processLessThan(values, index, param_mode):
    index += 1
    val1, param_mode = getValue(values, param_mode, index)
    index += 1
    val2, param_mode = getValue(values, param_mode, index)
    index += 1
    val3, param_mode = getValue(values, param_mode, index)

    if val1 < val2:
        values[val3] = 1
    else:
        values[val3] = 0
    index += 1
    return index, values

def processEquals(values, index, param_mode):
    index += 1
    val1, param_mode = getValue(values, param_mode, index)
    index += 1
    val2, param_mode = getValue(values, param_mode, index)
    index += 1
    val3, param_mode = getValue(values, param_mode, index)

    if val1 == val2:
        values[val3] = 1
    else:
        values[val3] = 0
    index += 1
    return index, values

def process(values):
  index = 0

  opcode_full = values[index]
  while (opcode_full != 99):
      opcode = int(opcode_full[-2:])
      param_mode = opcode_full[:-2]
      print ("Index %d, opcode %s parammode %s %s" % (index, opcode, param_mode, values[index:index+10]))
      if opcode == 1:
          index, values = processAdd(values, index, param_mode)
      elif opcode == 2:
          index, values = processMultiply(values, index, param_mode)
      elif opcode == 3:
          index, values = processInput(values, index, param_mode)
      elif opcode == 4:
          index, values = processOutput(values, index, param_mode)
      elif opcode == 5:
          index, values = processJumpIfTrue(values, index, param_mode)
      elif opcode == 6:
          index, values = processJumpIfFalse(values, index, param_mode)
      elif opcode == 7:
          index, values = processLessThan(values, index, param_mode)
      elif opcode == 8:
          index, values = processEquals(values, index, param_mode)
      elif opcode == 99:
          print ("DONE")
          exit(2)
      else:
          print ("Broken %s" % opcode)
          exit(1)

      if index > len(values):
          break
      opcode_full = str(values[index])

vals = INPUT2.split(',')
print process(vals)
