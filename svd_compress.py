import numpy as np
import cv2
from PIL import Image

file_name = 'test.JPEG'
# img_baw = cv2.imread(file_name,0)
img_col = cv2.imread(file_name)

def svd(img, k=1) :
	U, s, V = np.linalg.svd(img, full_matrices=False)
	for i in xrange(len(s)) :
		if i >= k :
			s[i] = 0
	S = np.diag(s)
	r_img = np.dot(U, np.dot(S, V))
	return r_img
	

print 'SVD_K,compression_ratio'

for k in range(10, img_col.shape[1]+1, 20) :
	M, N, c = img_col.shape
	compression_ratio = (M*N) / float(M*k + k + k*N) 


	r_img = np.zeros_like(img_col)
	for c in xrange(3) :
		r_img[:,:,c] = svd(img_col[:,:,c], k)
	
	diff = np.abs(r_img - img_col)

	cv2.imwrite(('img/svd_R_K_'+str(k)+'.png'), r_img)
	cv2.imwrite(('img/svd_D_K_'+str(k)+'.png'), diff)

	
	print k, ',', compression_ratio


