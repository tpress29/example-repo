name = "Timothy"
print("My Name is", name)

for i in range(1, 28):
  print (i ** 2)

## Class Engineer
class Engineer:
  def __init__(self, name, type, yrs_exp):
    self.name = name
    self.type = type
    self.yrs_exp = yrs_exp
    self.skill = "Problem Solver"
  
  def getName(self):
    return self.name

  def getType(self):
    return self.type

  def getYrs(self):
    return self.yrs_exp

  def getSkill(self):
    return self.skill

e1=Engineer("Peter", "Electrical", 4)
e2=Engineer("Rob", "Aerospace", 25)

print(e1.getName(),e1.getType(),e1.getYrs(),e1.getSkill())
print(e2.getName(),e2.getType(),e2.getYrs(),e2.getSkill())

  ## Fixed Attribute - Skill = Problem solver
  ## Inital Attributes - name, type, years of Experience
## Create 2x different engineers and print attributes

## print name backwards
print (name[::-1])
