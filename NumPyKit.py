import numpy

print(numpy.array((1., 2., 3., 4., 5., 6., 7., 8., 9.)))  # `: Create an array from a list or a sequence.

print(numpy.zeros(9))  # `: Create an array filled with zeros.

print(numpy.ones(9))  # `: Create an array filled with ones.

print(numpy.empty(9))  # `: Create an array without initializing its elements.

print(numpy.arange(9.))  # `: Create an array with a range of values.

print(numpy.linspace(0, 54))  # `: Create an array with a specified number of evenly spaced values between a specified
# range.


print(numpy.shape([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # `: Return the shape (dimensions) of an array.

print(numpy.reshape([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], (3, 4)))  # `: Reshape an array into a specified
# shape.

print(numpy.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # `: Transpose an array.

print(numpy.concatenate(([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]])))  # `: Concatenate arrays along a
# specified axis.

print(numpy.split(numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]), 4))  # `: Split an array into
# multiple sub-arrays along a specified axis.

print(numpy.sort([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # `: Sort an array.

print(numpy.argmax([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # `: Return the indices of the maximum value
# along a specified axis.

print(numpy.argmin([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # `: Return the indices of the minimum value
# along a specified axis.


print(numpy.add([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]))  # `: Element-wise addition of two arrays.

print(numpy.subtract([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]))  # `: Element-wise subtraction of two arrays.

print(numpy.multiply([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]))  # `: Element-wise multiplication of two
# arrays.

print(numpy.divide([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]))  # `: Element-wise division of two arrays.

print(numpy.exp([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # `: Compute the element-wise exponential of the
# input array.

print(numpy.log([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # `: Compute the element-wise natural logarithm of
# the input array.

print(numpy.sin([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # `: Compute the element-wise sine of the input
# array.

print(numpy.cos([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # `: Compute the element-wise cosine of the input
# array.


print(numpy.mean([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # `: Compute the mean of an array.

print(numpy.median([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # `: Compute the median of an array.

print(numpy.std([[[1, 52, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]))  # `: Compute the standard deviation of an array.

print(numpy.sum([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]))  # `: Compute the sum of all elements in an array.

print(numpy.max([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]))  # `: Find the maximum value in an array.

print(numpy.min([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]))  # `: Find the minimum value in an array.


print(numpy.dot([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]))  # `: Compute the dot product of two arrays.

print(numpy.matmul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]))  # `: Matrix multiplication of two arrays.

print(numpy.linalg.inv([[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1], [10, 11, 12, 1]]))  # `: Compute the inverse of a
# matrix.

print(numpy.linalg.det([[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1], [10, 11, 12, 1]]))  # `: Compute the determinant of
# a matrix.
