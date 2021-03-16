from client import get_errors, API_ENDPOINT, MAX_DEG
from config import *
import random
import time
from mutation import *
from sex import *
import numpy as np

random.seed(time.time())
# Generation = [[[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 13510723304.19212, 368296592820.6967, 381807316124.88885], [[0.0, -0.40549164191454984, -0.2504542821945545, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 0.3072608324140497, 0.022917305853459212, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 1.87273428555432e+19, 3.6600681076082495e+19, 5.53280239316257e+19], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, 0.1865609231395227, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -0.36111781889595224, 9.98214034e-10], 2.515098781545027e+28, 4.821650355202122e+28, 7.336749136747149e+28], [[0.0, 0.18859615774899835, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, 0.13204235365474587, 0.13898414682079993, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, -0.3236022167331814], 6.39107531476219e+39, 6.503251343617573e+39, 1.2894326658379762e+40], [[0.0, 0.4634972641253709, 0.18882348533082755, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.16842877839445078, -0.3748270684343527, -1.59792834e-08, 0.06854832855804102], 2.122547173448763e+30, 4.015336960999137e+30, 6.1378841344479e+30], [[-0.3058947475460849, 0.04721142589929967, 0.3208620706400887, -0.39306681507208857, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.2455274524925469, -0.19183196552763843, -0.15839490959325525, -0.1901010381410452], 1.6973709740731489e+31, 3.2138548171477546e+31, 4.911225791220903e+31], [[0.22307074338631572, -0.49423645547451317, 0.05568928143006341, 0.04654468033045892, -1.75214813e-10, -1.8366977e-15, 0.23666944597532888, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 13517951608.780087, 369592118368.83105, 383110069977.61115], [[0.0, -1.45799022e-12, -0.3870876664411222, 0.4307631917905251, -1.75214813e-10, -0.18253152019739077, 8.5294406e-16, 2.29423303e-05, 0.0916438896139728, -0.1789961192316662, 0.42874461978210804], 1.2213117896832156e+40, 1.2427515494144282e+40, 2.464063339097644e+40], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.1967754433128299, 0.09053394557327027, -1.59792834e-08, 0.033821617790497825], 5.202783909462842e+29, 9.843267621974835e+29, 1.5046051531437677e+30], [[0.0765411748699979, 0.06759260450049305, -2.28980078e-13, 0.0691121076239947, -1.75214813e-10, -0.0870507345011377, 0.23473344329624243, 2.29423303e-05, -0.4187427030084078, -1.59792834e-08, 0.01245668826022236], 2.7781561161732255e+39, 2.827060989736066e+39, 5.605217105909292e+39], [[0.4859673069138053, -0.18836832175574786, 0.3642454482226452, 0.3451082830545837, -0.3386719768163177, 0.3677727202631366, 0.1806175398706847, 2.29423303e-05, 0.38031953152924797, -0.14004967607436297, 9.98214034e-10], 4.958776327971735e+40, 5.046082158494216e+40, 1.000485848646595e+41]]
# Generation = [[[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 13510723304.19212, 368296592820.6967, 381807316124.88885], [[0.22307074338631572, -0.49423645547451317, 0.05568928143006341, 0.04654468033045892, -1.75214813e-10, -1.8366977e-15, 0.23666944597532888, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 13517951608.780087, 369592118368.83105, 383110069977.61115], [[0.0, -0.40549164191454984, -2.28980078e-13, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 0.13898414682079993, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 791172413408.6516, 1157368766804.3938, 1948541180213.0454], [[0.0, -0.40549164191454984, -0.2504542821945545, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 791575942892.2073, 1157980767929.1619, 1949556710821.3691], [[0.0, -0.40549164191454984, -0.2504542821945545, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 0.3072608324140497, 0.022917305853459212, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 1.87273428555432e+19, 3.6600681076082495e+19, 5.53280239316257e+19], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 0.3072608324140497, 0.022917305853459212, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 1.8733778573532656e+19, 3.6615256747483628e+19, 5.534903532101629e+19], [[0.0, -0.49423645547451317, 0.18882348533082755, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.16842877839445078, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 1.0141867759679472e+21, 1.981954338189504e+21, 2.996141114157451e+21], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, 0.1865609231395227, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -0.36111781889595224, 9.98214034e-10], 2.515098781545027e+28, 4.821650355202122e+28, 7.336749136747149e+28], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.1967754433128299, 0.09053394557327027, -1.59792834e-08, 0.033821617790497825], 5.202783909462842e+29, 9.843267621974835e+29, 1.5046051531437677e+30], [[0.0, 0.18859615774899835, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 0.13898414682079993, -0.1967754433128299, 0.09053394557327027, -1.59792834e-08, 0.033821617790497825], 5.202783909462878e+29, 9.843267621974917e+29, 1.5046051531437795e+30], [[0.0, 0.4634972641253709, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.1967754433128299, 0.09053394557327027, -1.59792834e-08, 0.033821617790497825], 5.202783909462929e+29, 9.843267621975038e+29, 1.5046051531437967e+30], [[0.0, -1.45799022e-12, 0.18882348533082755, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.16842877839445078, -0.3748270684343527, -1.59792834e-08, 0.06854832855804102], 2.1225471734487445e+30, 4.0153369609990966e+30, 6.13788413444784e+30], [[0.0, 0.4634972641253709, 0.18882348533082755, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.16842877839445078, -0.3748270684343527, -1.59792834e-08, 0.06854832855804102], 2.122547173448763e+30, 4.015336960999137e+30, 6.1378841344479e+30], [[0.22307074338631572, 0.4634972641253709, 0.05568928143006341, 0.04654468033045892, -1.75214813e-10, -1.8366977e-15, 0.23666944597532888, 2.29423303e-05, -0.3748270684343527, -1.59792834e-08, 0.06854832855804102], 2.122636313475023e+30, 4.015514080744751e+30, 6.138150394219774e+30], [[-0.3058947475460849, 0.04721142589929967, 0.3208620706400887, -0.39306681507208857, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.2455274524925469, -0.19183196552763843, -0.15839490959325525, -0.1901010381410452], 1.6973709740731489e+31, 3.2138548171477546e+31, 4.911225791220903e+31], [[0.0765411748699979, 0.06759260450049305, -2.28980078e-13, 0.0691121076239947, -1.75214813e-10, -0.0870507345011377, 0.23473344329624243, 2.29423303e-05, -0.4187427030084078, -1.59792834e-08, 0.01245668826022236], 2.7781561161732255e+39, 2.827060989736066e+39, 5.605217105909292e+39], [[0.0, 0.18859615774899835, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, 0.13204235365474587, 0.13898414682079993, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, -0.3236022167331814], 6.39107531476219e+39, 6.503251343617573e+39, 1.2894326658379762e+40], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, 0.13204235365474587, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, -0.3236022167331814], 6.39107531476219e+39, 6.503251343617573e+39, 1.2894326658379762e+40], [[0.0, 0.18859615774899835, -0.2504542821945545, 4.62010753e-11, -1.75214813e-10, 0.13204235365474587, 0.3072608324140497, 0.022917305853459212, -2.04721003e-06, -1.59792834e-08, -0.3236022167331814], 6.391075315355708e+39, 6.503251344447332e+39, 1.289432665980304e+40], [[0.0, -1.45799022e-12, -0.3870876664411222, 0.4307631917905251, -1.75214813e-10, -0.18253152019739077, 8.5294406e-16, 2.29423303e-05, 0.0916438896139728, -0.1789961192316662, 0.42874461978210804], 1.2213117896832156e+40, 1.2427515494144282e+40, 2.464063339097644e+40], [[0.4859673069138053, -0.18836832175574786, 0.3642454482226452, 0.3451082830545837, -0.3386719768163177, 0.3677727202631366, 0.1806175398706847, 2.29423303e-05, 0.38031953152924797, -0.14004967607436297, 9.98214034e-10], 4.958776327971735e+40, 5.046082158494216e+40, 1.000485848646595e+41]]
Generation = []
# Generation = [[[0.0, -0.40549164191454984, -0.2504542821945545, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 13497747914.053047, 368169073177.6824, 381666821091.7354], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 13510723304.19212, 368296592820.6967, 381807316124.88885], [[0.22307074338631572, -0.49423645547451317, 0.05568928143006341, 0.04654468033045892, -1.75214813e-10, -1.8366977e-15, 0.23666944597532888, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 13517951608.780087, 369592118368.83105, 383110069977.61115], [[0.22307074338631572, -0.49423645547451317, 0.05568928143006341, 0.04654468033045892, -1.75214813e-10, -1.8366977e-15, 0.23666944597532888, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 13517951608.780087, 369592118368.83105, 383110069977.61115], [[0.22307074338631572, -0.40549164191454984, 0.05568928143006341, 0.04654468033045892, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 13517870965.35532, 369592837291.969, 383110708257.32434], [[0.0, -0.49423645547451317, 0.18882348533082755, 0.04654468033045892, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 13525340480.896769, 369659172997.3953, 383184513478.2921], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 791164393464.7, 1157345488220.2935, 1948509881684.9934], [[0.0, -0.40549164191454984, -2.28980078e-13, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 0.13898414682079993, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 791172413408.6516, 1157368766804.3938, 1948541180213.0454], [[0.0, -0.40549164191454984, -2.28980078e-13, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 0.13898414682079993, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 791172413408.6516, 1157368766804.3938, 1948541180213.0454], [[0.0, -0.40549164191454984, -0.2504542821945545, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 791575942892.2073, 1157980767929.1619, 1949556710821.3691], [[0.0, -0.40549164191454984, -0.2504542821945545, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 791575942892.2073, 1157980767929.1619, 1949556710821.3691], [[0.0, -0.49423645547451317, -0.2504542821945545, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 0.23666944597532888, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 791577689622.9325, 1157985871488.5747, 1949563561111.5073], [[0.0, -0.40549164191454984, -0.2504542821945545, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 0.3072608324140497, 0.022917305853459212, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 1.87273428555432e+19, 3.6600681076082495e+19, 5.53280239316257e+19], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 0.3072608324140497, 0.022917305853459212, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 1.8733778573532656e+19, 3.6615256747483628e+19, 5.534903532101629e+19], [[0.0, -0.49423645547451317, 0.18882348533082755, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.16842877839445078, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 1.0141867759679472e+21, 1.981954338189504e+21, 2.996141114157451e+21], [[0.22307074338631572, -0.49423645547451317, 0.05568928143006341, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 0.23666944597532888, -0.16842877839445078, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 1.014186781304592e+21, 1.9819543513695757e+21, 2.9961411326741677e+21], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, 0.1865609231395227, -1.8366977e-15, 0.3072608324140497, 0.022917305853459212, -2.04721003e-06, -0.36111781889595224, 9.98214034e-10], 2.51496223764744e+28, 4.821385628381867e+28, 7.336347866029306e+28], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, 0.1865609231395227, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -0.36111781889595224, 9.98214034e-10], 2.515098781545027e+28, 4.821650355202122e+28, 7.336749136747149e+28], [[0.0, 0.4634972641253709, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.1967754433128299, -0.3748270684343527, -1.59792834e-08, 0.033821617790497825], 5.142184554836953e+29, 9.727096459508016e+29, 1.486928101434497e+30], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.1967754433128299, 0.09053394557327027, -1.59792834e-08, 0.033821617790497825], 5.202783909462842e+29, 9.843267621974835e+29, 1.5046051531437677e+30], [[0.0, 0.18859615774899835, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 0.13898414682079993, -0.1967754433128299, 0.09053394557327027, -1.59792834e-08, 0.033821617790497825], 5.202783909462878e+29, 9.843267621974917e+29, 1.5046051531437795e+30], [[0.0, 0.4634972641253709, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.1967754433128299, 0.09053394557327027, -1.59792834e-08, 0.033821617790497825], 5.202783909462929e+29, 9.843267621975038e+29, 1.5046051531437967e+30], [[0.0, 0.4634972641253709, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.1967754433128299, 0.09053394557327027, -1.59792834e-08, 0.033821617790497825], 5.202783909462929e+29, 9.843267621975038e+29, 1.5046051531437967e+30], [[0.0, -1.45799022e-12, 0.18882348533082755, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.16842877839445078, -0.3748270684343527, -1.59792834e-08, 0.06854832855804102], 2.1225471734487445e+30, 4.0153369609990966e+30, 6.13788413444784e+30], [[0.0, 0.4634972641253709, 0.18882348533082755, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.16842877839445078, -0.3748270684343527, -1.59792834e-08, 0.06854832855804102], 2.122547173448763e+30, 4.015336960999137e+30, 6.1378841344479e+30], [[-0.3058947475460849, 0.04721142589929967, 0.3208620706400887, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.16842877839445078, -0.3748270684343527, -1.59792834e-08, 0.06854832855804102], 2.1225471734490302e+30, 4.0153369609996556e+30, 6.137884134448686e+30], [[0.22307074338631572, 0.4634972641253709, 0.05568928143006341, 0.04654468033045892, -1.75214813e-10, -1.8366977e-15, 0.23666944597532888, 2.29423303e-05, -0.3748270684343527, -1.59792834e-08, 0.06854832855804102], 2.122636313475023e+30, 4.015514080744751e+30, 6.138150394219774e+30], [[0.0, -1.45799022e-12, 0.18882348533082755, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.16842877839445078, 0.09053394557327027, -1.59792834e-08, 0.06854832855804102], 2.1348407800668377e+30, 4.038904541137045e+30, 6.173745321203882e+30], [[-0.3058947475460849, 0.04721142589929967, 0.3208620706400887, -0.39306681507208857, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.2455274524925469, -0.19183196552763843, -0.15839490959325525, -0.1901010381410452], 1.6973709740731489e+31, 3.2138548171477546e+31, 4.911225791220903e+31], [[0.0, -1.45799022e-12, 0.18882348533082755, -0.39306681507208857, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.2455274524925469, -0.19183196552763843, -0.15839490959325525, -0.1901010381410452], 1.6973709740732293e+31, 3.2138548171479127e+31, 4.911225791221142e+31], [[0.0, 0.4634972641253709, 0.18882348533082755, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, -0.3236022167331814], 4.752537388985898e+31, 8.991208415695406e+31, 1.3743745804681305e+32], [[0.0, -0.40549164191454984, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 0.13898414682079993, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, -0.3236022167331814], 4.752537388986107e+31, 8.991208415695819e+31, 1.3743745804681926e+32], [[0.0765411748699979, 0.06759260450049305, -2.28980078e-13, 0.0691121076239947, -1.75214813e-10, -0.0870507345011377, 0.23473344329624243, 2.29423303e-05, -0.4187427030084078, -1.59792834e-08, 0.01245668826022236], 2.7781561161732255e+39, 2.827060989736066e+39, 5.605217105909292e+39], [[0.0, 0.18859615774899835, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, 0.13204235365474587, 0.13898414682079993, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, -0.3236022167331814], 6.39107531476219e+39, 6.503251343617573e+39, 1.2894326658379762e+40], [[0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, 0.13204235365474587, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, -0.3236022167331814], 6.39107531476219e+39, 6.503251343617573e+39, 1.2894326658379762e+40], [[0.0, 0.18859615774899835, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, 0.13204235365474587, 0.13898414682079993, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, -0.3236022167331814], 6.39107531476219e+39, 6.503251343617573e+39, 1.2894326658379762e+40], [[0.0, 0.18859615774899835, -0.2504542821945545, 4.62010753e-11, -1.75214813e-10, 0.13204235365474587, 0.3072608324140497, 0.022917305853459212, -2.04721003e-06, -1.59792834e-08, -0.3236022167331814], 6.391075315355708e+39, 6.503251344447332e+39, 1.289432665980304e+40], [[0.0, 0.18859615774899835, -2.28980078e-13, 4.62010753e-11, -0.48957333106489215, 0.13204235365474587, 0.13898414682079993, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], 6.392080159266522e+39, 6.504622272710603e+39, 1.2896702431977125e+40], [[0.0, 0.18859615774899835, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, 0.13204235365474587, 0.13898414682079993, -0.16842877839445078, -0.3748270684343527, -1.59792834e-08, 0.06854832855804102], 6.392292543285707e+39, 6.504912027965341e+39, 1.2897204571251047e+40], [[0.0, -1.45799022e-12, -0.3870876664411222, 0.4307631917905251, -1.75214813e-10, -0.18253152019739077, 8.5294406e-16, 2.29423303e-05, 0.0916438896139728, -0.1789961192316662, 0.42874461978210804], 1.2213117896832156e+40, 1.2427515494144282e+40, 2.464063339097644e+40], [[0.4859673069138053, -0.18836832175574786, 0.3642454482226452, 0.3451082830545837, -0.3386719768163177, 0.3677727202631366, 0.1806175398706847, 2.29423303e-05, 0.38031953152924797, -0.14004967607436297, 9.98214034e-10], 4.958776327971735e+40, 5.046082158494216e+40, 1.000485848646595e+41]]
new = []
# Generation.append([INITIAL_ARR, INITIAL_ERR[0], INITIAL_ERR[1], INITIAL_ERR[0]+INITIAL_ERR[1]])
for i in range(0,GENERATION_SIZE):
    new.append(mutation(INITIAL_ARR, 0.5, 1))
    err = get_errors(SECRET_KEY_ID, new[i])
    Generation.append([new[i], err[0], err[1], err[0]+err[1]])
new = []
print(Generation)
# print(time.time())
# print(INITIAL_ARR)
# # print(get_errors(SECRET_KEY_ID, INITIAL_ARR))
# new = [[0.0, 0.18859615774899835, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 0.13898414682079993, -0.1967754433128299, 0.09053394557327027, -1.59792834e-08, 0.033821617790497825], [0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, 0.13204235365474587, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, -0.3236022167331814], [0.0, -0.40549164191454984, -2.28980078e-13, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 0.13898414682079993, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], [0.0, 0.18859615774899835, -0.2504542821945545, 4.62010753e-11, -1.75214813e-10, 0.13204235365474587, 0.3072608324140497, 0.022917305853459212, -2.04721003e-06, -1.59792834e-08, -0.3236022167331814], [0.0, -1.45799022e-12, 0.18882348533082755, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.16842877839445078, -0.3748270684343527, -1.59792834e-08, 0.06854832855804102], [0.0, 0.4634972641253709, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.1967754433128299, 0.09053394557327027, -1.59792834e-08, 0.033821617790497825], [0.0, -0.40549164191454984, -0.2504542821945545, 4.62010753e-11, -0.48957333106489215, -1.8366977e-15, 8.5294406e-16, 2.29423303e-05, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], [0.0, -1.45799022e-12, -2.28980078e-13, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 0.3072608324140497, 0.022917305853459212, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], [0.0, -0.49423645547451317, 0.18882348533082755, 4.62010753e-11, -1.75214813e-10, -1.8366977e-15, 8.5294406e-16, -0.16842877839445078, -2.04721003e-06, -1.59792834e-08, 9.98214034e-10], [0.22307074338631572, 0.4634972641253709, 0.05568928143006341, 0.04654468033045892, -1.75214813e-10, -1.8366977e-15, 0.23666944597532888, 2.29423303e-05, -0.3748270684343527, -1.59792834e-08, 0.06854832855804102]]
# Generating new children 
for j in range(0,15):
    for i in range(0,GENERATION_SIZE):
        rand1 = random.randint(0,int(len(Generation)*0.8))
        rand2 = random.randint(0,int(len(Generation)*0.8))
        while(rand1==rand2):
            rand2 = random.randint(0,int(len(Generation)*0.8))
        children = sex(Generation[rand1][0], Generation[rand2][0], 0.2, 0.2)
        new.append(children[0])
        new.append(children[1])
    # Adding them to Generation
    for i, val in enumerate(new):
        # new.append(mutation(INITIAL_ARR, 0.5, 0.5))
        err = get_errors(SECRET_KEY_ID, new[i])
        Generation.append([new[i], err[0], err[1], err[0]+err[1]])
        # print(get_errors(SECRET_KEY_ID, GENERATION[i]))
    new = []
    Generation.sort(key = lambda x: x[3])
    Generation = Generation[:GENERATION_SIZE]
    print(str(j)+ " generation:")
    print(Generation)
# print(str(random.randint(0,9)) + "  " + str(random.randint(0,9)))
# print(GENERATION)
# print(sex(GENERATION[random.randint(0,9)], GENERATION[random.randint(0,9)], 0,0))








