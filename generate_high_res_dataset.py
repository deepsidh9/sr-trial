from main_test_realapplication import enhance
import time

import glob
all_images=[image[10:] for image in glob.glob("bonafide/*.png")]
print(all_images)


start = time.time()
enhance(testset_name = 'set_real',test_image = '00002_940928_fa.png',scale_factor=2)
enhance(testset_name = 'set_real',test_image = '00002_940928_fa.png',scale_factor=3)
enhance(testset_name = 'set_real',test_image = '00002_940928_fa.png',scale_factor=4)
end=time.time()
print('Running time',end-start)
