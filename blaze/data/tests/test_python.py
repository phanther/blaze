from blaze.data.python import *
from dynd import nd

def test_basic():
    data = ((1, 1), (2, 2))
    dd = Python([], schema='2 * int32')

    dd.extend(data)

    assert str(dd.dshape) == 'var * 2 * int32'
    assert str(dd.schema) == '2 * int32'

    assert tuple(dd) == data
    print(dd.as_py())
    assert dd.as_py() == data

    chunks = list(dd.chunks())

    assert all(isinstance(chunk, nd.array) for chunk in chunks)
    assert nd.as_py(chunks[0]) == list(map(list, data))

    assert isinstance(dd.as_dynd(), nd.array)
