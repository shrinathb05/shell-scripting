# 🔹 TOPIC 3: Data Types (ABSOLUTE MUST)
# Type	Example	DevOps Use
# str	"nginx"	service names
# int	5	retry count
# float	75.5	CPU usage
# bool	True	health checks
# list	["web", "db"]	server groups
# dict	{"host": "localhost", "port": 80}	server config
# NoneType	None	unset values
# Complex	3 + 4j	advanced calculations
# bytes	b"data"	binary data handling
# bytearray	bytearray(b"data")	mutable binary data
# set	{"web", "db"}	unique server tags
# frozenset	frozenset({"web", "db"})	immutable server tags
# range	range(5)	loop iterations
# tuple	("web", "db")	server roles
# memoryview	memoryview(b"data")	efficient data processing

# 🔹 Example Code Demonstrating Each Data Type
# str
name = "nginx"
print(name)

# int
retry_count = 5
print(retry_count)

# float
cpu_usage = 75.5
print(cpu_usage)

# bool
is_healthy = True
print(is_healthy)

# list
server_groups = ["web", "db"]
print(server_groups)

# dict
server_config = {"host": "localhost", "port": 80}
print(server_config)

# NoneType
unset_value = None
print(unset_value)

# Complex
complex_number = 3 + 4j
print(complex_number)

# bytes
binary_data = b"data"
print(binary_data)

# bytearray
mutable_binary_data = bytearray(b"data")
print(mutable_binary_data)

# set
unique_tags = {"web", "db"}
print(unique_tags)

# frozenset
immutable_tags = frozenset({"web", "db"})
print(immutable_tags)

# range
loop_iterations = range(5)
for i in loop_iterations:
    print(i)

# tuple
server_roles = ("web", "db")
print(server_roles)

# memoryview
data = b"data"
data_view = memoryview(data)
print(data_view)    

# Check type:
print(type(name))
print(type(retry_count))
print(type(cpu_usage))          
print(type(is_healthy))
print(type(server_groups))
print(type(server_config))
print(type(unset_value))
print(type(complex_number))
print(type(binary_data))
print(type(mutable_binary_data))
print(type(unique_tags))
print(type(immutable_tags))
print(type(loop_iterations))
print(type(server_roles))
print(type(data_view))  
