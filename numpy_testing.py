import numpy as np

print("==basic array==")
# making a basic np array
a = np.array([1,2,3,4])
print(a)
print("size: {}".format(a.size))
print("shape: {}".format(a.shape))
print("dtype: {}".format(a.dtype))

print("==multi dim array==")
# Multidimensional array
b = np.array([[1,2,3,4], [5,6,7,8]])
print(b)
print("shape: {}".format(b.shape))
print("size: {}".format(b.size))

print("==setting dtypes==")
# setting dtypes
a = np.array([1,2,3,4], dtype="uint8")
print(a)
print(a.dtype)

print("==truncated bits==")
# worth noting it truncates bits silently
b = np.array([111,222,333,444], dtype="uint8")
print(b)

print("==zero init==")
#initialize to 0s
a = np.zeros((3,4), dtype="uint32")
print(a)
a[0,3] = 42
a[1,1] = 66
print(a)

print("==initialize to ones==")
#initialize to 1s. note it defaults to float64
a = 11*np.ones((3,1))
print(a)
print(a.dtype)

print("==advanced indexing==")
#advanced indexing. note that the reshape shape must multiply to equal the total values it shapes
a = np.arange(12).reshape((3,4)) #equivalent to range() in np, exclusive like range(12).
# a = np.arange(12).reshape((4,4)) throws an error
print(a)
#defaults to int64
print(a.dtype)

print("==slicing lists==")
# slicing lists, works similar to normal python lists
print("index 2 onward: \n{}".format(a[2:]))
print("index up to 2, exclusive: \n{}".format(a[:2])) #exclusive
print("y index up to 2, x index up to 3 exclusive: \n{}".format(a[:2, :3])) #exclusive

b = np.arange(12)
print("print all stepped by 2: \n{}".format(b[::2]))
print("print all stepped by 3: \n{}".format(b[::3]))
print("print all reversed: \n{}".format(b[::-1]))

a = np.arange(24).reshape((4,3,2))
print("3d array: \n{}".format(a))
a[1] = [[11,22], [33,44], [55,66]]
print("edited 3d array: \n{}".format(a))

a[2,...] = [[99,99], [99,99], [99,99]]
print("another edit: \n{}".format(a))

print("==np.save and np.load==")
a = np.random.randint(0,5,(3,4))
print("a random initialized array: \n{}".format(a))
np.save("random.npy", a)
b = np.load("random.npy")
print("a loaded array: \n{}".format(b))
