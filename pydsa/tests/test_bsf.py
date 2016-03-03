from pydsa import bsf

def test_bsf():
	graph = [[1,2],[2],[0,3],[3]]
	bsf_order = bsf(a,2)
	assert bsf_order == [2,0,3,1]