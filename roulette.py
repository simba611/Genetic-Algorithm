from client import get_errors, API_ENDPOINT, MAX_DEG
from config import *
import random
import time
from mutation import *
from sex import *
import numpy as np

random.seed(time.time())

Generation = []

new = []



############# generate first generation
# for i in range(0,GENERATION_SIZE):
#     new.append(mutation_generation_first())
#     err = get_errors(SECRET_KEY_ID, new[i])
#     Generation.append([new[i], err[0], err[1], FITNESS_FACTOR*err[0]+err[1]])
# # print(new)
# Generation = [[[0, 0, -2.2608634487124868e-13, 0, 0, -1.7818201147874334e-15, 0, 0, 0, 0, 0], 1755829966853.6807, 2152896314693.9707, 3381977291491.547], [[0.0, 0.0, -1.9345909439637096e-13, 0.0, 0.0, -1.6587598654943387e-15, 0.0, 0.0, 0.0, -2.364767917444848e-09, 0.0], 2855983928135.503, 1846353728756.4355, 3845542478451.287], [[0, 0, -2.1988488647294413e-13, 0, 0, 0, 8.068709083260226e-16, 0, 0, 0, 0], 2031280283262.1824, 3624979221727.693, 5046875420011.221], [[0.0, -2.569361740828404e-13, -2.2677020139497484e-13, 0.0, 0.0, -1.6469333823456224e-15, 1.649103654638205e-16, 0.0, -3.4709880997896415e-07, 0.0, 0.0], 10292722474758.305, 13688858337703.664, 20893764070034.477], [[0, 0, -2.415903225490085e-13, 0, 0, -1.7406624125272973e-15, 8.913975459169505e-16, 0, -1.944889701878946e-06, 0, 1.0128701407508952e-09], 16245836590553.176, 35152862353586.35, 46524947966973.58], [[0.0, 0.0, -2.5836714666557256e-13, 0.0, 0.0, -1.7427624968404662e-15, 8.675836657430601e-16, 0.0, -1.8485086127965933e-06, -4.3776507485145854e-10, 9.858110936691114e-10], 17079721656514.746, 36921370086142.016, 48877175245702.336], [[0, -1.3370576327323695e-12, 0, 0, -1.5983721227032377e-10, 0, 0, 0, -2.143156454508772e-06, 0, 1.0863395628387384e-09], 23205731342777.04, 43502248855940.734, 59746260795884.66], [[0, -1.3901223052032975e-12, 0, 4.872328063321771e-11, 0, 0, 0, 2.4624776989998566e-05, 0, 0, 0], 31379733404301.242, 69281029534170.4, 91246842917181.27]]
# Generation = [[[0.0, 7.276360151668641e-14, -2.37935144094506e-13, -2.750542686658241e-12, 0.0, -1.8753039399672114e-15, -1.975404473711345e-18, -1.3159396018522174e-06, 0.0, 0.0, 0.0], 1941903722349.2058, 1694220709286.0168, 3053553314930.461], [[0.0, 6.428971863272197e-14, -2.410182179458877e-13, -2.460888287321348e-12, 0.0, -1.8650344524941792e-15, -1.2571174325770867e-18, -1.1773605146098985e-06, -1.0933383594104783e-09, 0.0, 0.0], 1915909269887.1567, 1715023501402.2202, 3056159990323.2295], [[0.0, 4.845634566798112e-14, -2.1798857479022204e-13, -1.831702175553868e-12, 0.0, -1.7479047895158991e-15, 0.0, -8.048382194655715e-07, 0.0, 0.0, 0.0], 1787837540007.2336, 1828625718436.0403, 3080111996441.1035], [[0.0, 4.845634566798112e-14, -2.4426024183297556e-13, -1.8317021755538677e-12, 0.0, -1.843930111207982e-15, 0.0, -9.709254627656379e-07, 0.0, 0.0, 0.0], 1870792373111.648, 1782858319386.3472, 3092412980564.501], [[0.0, 4.8456345667981115e-14, -2.3396717523911295e-13, -1.8317021755538677e-12, 0.0, -1.8439301112079823e-15, 0.0, -8.583609523838375e-07, 0.0, 0.0, 0.0], 1857765534133.405, 1818014588115.0464, 3118450462008.4297], [[0.0, 4.8456345667981115e-14, -2.3396717523911295e-13, -1.8317021755538677e-12, 0.0, -1.8439301112079823e-15, 0.0, -8.583609523838375e-07, 0.0, 0.0, 0.0], 1857765534133.405, 1818014588115.0464, 3118450462008.4297], [[0.0, 4.7208547346787815e-14, -2.33967175239113e-13, -1.8317021755538677e-12, 0.0, -1.8439301112079823e-15, 0.0, -8.583609523838376e-07, 0.0, 0.0, 0.0], 1857765534133.405, 1818014588115.0464, 3118450462008.4297], [[0.0, -7.703937203406894e-15, -2.4695341378814566e-13, 0.0, 0.0, -1.6579218683602256e-15, 5.295254413466696e-18, 0.0, -1.0382282594029201e-08, 0.0, 0.0], 1669255781230.872, 1964660416173.941, 3133139463035.5513]]
Generation = [[[0.0, 0.0, 0.0, 4.138918000943626e-12, 0.0, 3.5945213577699226e-16, -1.1770395496643185e-09, -1.6371861140946626e-05, 0.0, 5.631982165388069e-09, 0.0], 1817249537477.0261, 1199621903563.672, 2471696579797.5903], [[1.2191266922312972e-09, 1.045796841545353e-14, 9.37272117093537e-10, 2.923586624821709e-12, 4.332208654725043e-13, 3.2490852786390632e-16, -2.601319922383713e-09, -2.1446978494208386e-05, 5.748095349675292e-11, 7.936624581798838e-09, 0.0], 2006424191555.9478, 1240746871944.1719, 2645243806033.335], [[-3.056103266137151e-09, -6.527510854401019e-14, 2.627317577555417e-14, 1.067724945360622e-10, -2.220939861180985e-11, -2.791408649509014e-16, 2.0794556282439678e-16, 1.0549520388050306e-05, 4.3118292138640735e-08, -8.639464349804407e-09, 0.0], 1954366142488.1414, 1378277923718.641, 2746334223460.34], [[1.0213407104965182e-09, 1.0067461700448557e-14, 9.207940961245056e-10, 4.414834787398749e-12, 3.5915523734644327e-13, 4.784768945565036e-16, -2.5555865613193823e-09, -2.1089314678132057e-05, -3.873984737565715e-11, 7.787318604430619e-09, 0.0], 2099087886743.0684, 1419646281547.143, 2889007802267.291], [[-6.401303186128531e-09, -1.338678383166953e-13, 2.1179032281083874e-15, 9.726131008785255e-11, -1.4734132457281955e-11, -2.4963518469075403e-16, 2.2129379704360765e-16, 1.105174369382619e-05, 4.5658335628640135e-08, -9.197604864035665e-09, 0.0], 2129757803640.6616, 1527975034530.896, 3018805497079.3594], [[-1.0030967368237413e-08, 2.700860639566886e-14, 0.0, 8.774598884637815e-11, 1.175386202121352e-11, 3.9836207521101965e-16, -4.953839236804525e-18, -1.1030110522664117e-06, -4.7674918807481375e-09, -5.559201094376191e-10, 0.0], 1584773193829.6196, 2036576517162.5298, 3145917752843.2637], [[-9.833181386502634e-09, 3.331725462809244e-14, 1.6478020969031478e-11, 8.62547406838011e-11, 5.598846523266077e-12, 4.409640939130991e-16, -4.573336601817028e-11, -1.4606748683427398e-06, -4.6826648576374516e-09, -4.066141320693991e-10, 0.0], 1615254523556.247, 2065723652650.1355, 3196401819139.5083], [[-8.929209650324918e-09, -1.982727297315199e-14, 5.256927267414699e-09, 5.2548112503474606e-11, -4.342082066431212e-14, -6.93493223703578e-16, 2.821501442757822e-10, 2.237327653167127e-05, 2.43501665644361e-10, -1.2037172587226253e-08, 0.0], 1781088496455.2336, 2145225474679.5906, 3391987422198.254], [[-2.5045026301811913e-10, -5.28169857811711e-14, 9.832881645556049e-16, 2.864848022790567e-12, -1.5904398982001103e-11, -1.5688637617277568e-15, 5.1352453053740285e-17, 4.064411356466043e-06, 1.1358812695480195e-08, -2.091020810125094e-09, 0.0], 1720189272086.7078, 2334145119905.961, 3538277610366.6562], [[-9.192290912820241e-10, -7.165720714414913e-14, 2.5887869453487854e-13, 1.1818034524274394e-11, -1.8205512791995463e-11, -5.632686490517708e-16, 8.818340706633426e-17, 5.713312792231845e-06, 1.865869920703331e-08, -3.264796620498006e-09, 0.0], 1557248435357.4414, 2535929211105.2954, 3626003115855.5044], [[-4.0454098273695505e-10, -6.974950335303584e-14, 2.9591606085297785e-13, 3.8797577078354816e-12, -1.880533496347058e-11, -5.861915788195894e-16, 7.966616335844737e-14, 5.083946674527064e-06, 1.6536698929111033e-08, -2.7549821685928263e-09, 0.0], 1616490546121.3044, 2775243235290.4746, 3906786617575.3877], [[-1.3562035642843647e-09, 1.318755603631569e-12, 5.505781487307982e-10, -2.674282560477331e-11, 7.897339028742694e-11, -2.9056768961015548e-15, -1.6295501204860467e-11, -2.003995436302274e-05, -1.3173050691753524e-07, 1.3218421626894497e-08, 0.0], 1630263937334.6484, 2809969756839.882, 3951154512974.1357], [[-1.217319915112306e-09, -5.359084731921928e-14, 8.612621754795119e-10, 6.257405951619671e-12, -2.2095197077785072e-11, -2.2645610765654184e-15, 3.785396759718477e-12, 7.184140275480711e-06, 9.993328487547526e-09, -3.6817676170703136e-09, 0.0], 2338864439197.829, 2439979600143.1416, 4077184707581.622], [[-2.5517254392584365e-09, -5.883899899904048e-14, 7.966707450343231e-10, 1.0203892206631913e-11, -1.6902885945584624e-11, -3.072633696638738e-16, 3.564844288840551e-11, 8.110292446126464e-06, 1.8129162862011436e-08, -4.120240197818063e-09, 0.0], 1675090613793.9558, 3147607758525.312, 4320171188181.081], [[8.749011159371596e-10, -7.276061521297855e-14, -1.0836064382675314e-09, -3.611616474550191e-13, -2.0852936103410753e-11, -8.248766657156146e-16, -2.808910796705956e-12, 1.4461001402150884e-06, 1.8506743548216835e-08, -7.912447373858246e-10, 0.0], 1770086603133.6094, 3092789886173.113, 4331850508366.639], [[1.9683894146482858e-10, -4.887536528740399e-13, 5.21353069499658e-15, 8.134156143574135e-11, -2.814497532577153e-11, -1.05982629221841e-15, 1.6195534138067293e-10, 2.613543610332161e-05, 3.640371975249621e-08, -1.4195479133480247e-08, 0.0], 2268294405793.197, 2753292785475.679, 4341098869530.917], [[-7.933800330648542e-09, -5.896657284062705e-14, 6.844120275829803e-09, 2.982423198468371e-11, -3.963517024396069e-12, -1.365892564755098e-15, 3.5997070109724235e-11, 2.885572562409487e-05, 5.078224315457234e-10, -1.4732088362770555e-08, 0.0], 2693793703874.7964, 3270878751832.548, 5156534344544.905], [[-7.643788980381576e-09, -2.4306317242461558e-14, 8.789270940255762e-09, 4.7275455211119896e-11, 2.8707200615927514e-13, -1.118339101976496e-15, 3.863011082121448e-11, 3.57404438893504e-05, -3.2457496075698732e-09, -1.82382465385967e-08, 0.0], 2976995806157.6772, 3825783174604.2476, 5909680238914.621], [[-6.575925313692979e-09, 1.7841707527424325e-13, 6.59050226828056e-09, 6.459511837832189e-11, 1.53923511984947e-11, -6.692312251850135e-16, 2.1223680880076887e-10, 1.4301547930081093e-05, -1.4863807000024706e-08, -1.078234858377624e-08, 0.0], 4128075033924.5366, 4203950677096.366, 7093603200843.541], [[-7.573407409292542e-09, 2.368830723425653e-14, -2.7762208345943746e-17, 6.622402874910105e-11, 7.529350812549453e-12, -2.1918149031773342e-16, -2.746231282045556e-12, 2.7708018777234963e-06, -5.434517205004903e-09, 6.873177116970661e-10, 0.0], 3574027574786.1577, 8059529116148.711, 10561348418499.021]]
new = []
Generation.sort(key = lambda x: x[3])
print(Generation)
############# now that we have first generation, we take the best MATING_POOL_SIZE of them
# Generation = Generation[:MATING_POOL_SIZE]


# Generating new children 
for j in range(4):
    for i in range(GENERATION_SIZE-MATING_POOL_SIZE):
        fit_sum = 0
        for h in Generation:
            fit_sum += h[3]
        p = random.uniform(0, fit_sum)
        fit_index = -1
        for index, f in enumerate(Generation):
            if p <= 0:
                fit_index = index
                break
            p -= f[3]
        Generation.pop(fit_index)
        # return i
    for i in range(0,int(GENERATION_SIZE/2)):
        rand1 = random.randint(0,int(len(Generation))-1)
        rand2 = random.randint(0,int(len(Generation))-1)
        # while(rand1==rand2):
        #     rand2 = random.randint(0,int(len(Generation)))

        children = sex_two(Generation[rand1][0], Generation[rand2][0])
        new.append(mutation_two(children[0]))
        new.append(mutation_two(children[1]))
    # Adding them to Generation
    Generation.sort(key = lambda x: x[3])
    Generation = Generation[:OLD_GENERATION]
    # Generation = []
    Generation2 = []
    for i, val in enumerate(new):
        # new.append(mutation(INITIAL_ARR, 0.5, 0.5))
        err = get_errors(SECRET_KEY_ID, new[i])
        Generation2.append([new[i], err[0], err[1], FITNESS_FACTOR*err[0]+err[1]])
        # print(get_errors(SECRET_KEY_ID, GENERATION[i]))
    new = []
    Generation2.sort(key = lambda x: x[3])
    Generation2 = Generation2[:GENERATION_SIZE-OLD_GENERATION]
    for val in Generation2:
        Generation.append(val)
    print(str(j)+ " generation:")
    Generation.sort(key = lambda x: x[3])
    print(Generation)
# print(str(random.randint(0,9)) + "  " + str(random.randint(0,9)))
# print(GENERATION)
# print(sex(GENERATION[random.randint(0,9)], GENERATION[random.randint(0,9)], 0,0))








