# Different print formats
name = "sars_cov_2"
disease = "covid19"

# First
print("the name of the virus is", name)

# Second
# Whereever is the curly braces'{}' the variable is replaces
print("The name of the virus is {}".format(name))
print("{} is the name of the virus".format(name))

# Third for two variables printing
print("The name of the virus is {} and it causes {}".format(name, disease))

# Fourth for two or single variable
# It only will work latest version from 3.6 and above
# f funtion print format
print(f"The name of the virus is {name} and it causes {disease}")

# fifth (cancatination)
print("The name of the virus is" + " " + name)