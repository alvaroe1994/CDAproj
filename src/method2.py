import multiprocessing, numpy

def lineMult(start):
    global A, B, mp_arr, part
    n = len(A)
    # create a new numpy array using the same memory as mp_arr
    arr = numpy.frombuffer(mp_arr.get_obj(), dtype=ctypes.c_int)
    C = arr.reshape((n,n))
    for i in xrange(start, start+part):
        for k in xrange(n):
            for j in xrange(n):
                C[i][j] += A[i][k] * B[k][j]

def ikjMatrixProduct(A, B, threadNumber):
    n = len(A)
    part = n / threadNumber
    if part < 1:
        part = 1
    pool = multiprocessing.Pool(threadNumber)

    pool.map(lineMult, range(0,n, part))
    # mp_arr and arr share the same memory
    arr = numpy.frombuffer(mp_arr.get_obj(), dtype=ctypes.c_int) 
    C = arr.reshape((n,n))
    return C
