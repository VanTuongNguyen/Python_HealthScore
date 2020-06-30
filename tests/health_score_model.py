import math
from seal import *
from seal_helper import *
import datetime as dt
import sys

def thesis_demo():
    
    print_example_banner("Health Score model using CKKS")

    parms = EncryptionParameters(scheme_type.CKKS)  

    poly_modulus_degree = 8192
    my_scale = 30
    

    parms.set_poly_modulus_degree(poly_modulus_degree)
    parms.set_coeff_modulus(CoeffModulus.Create(
        poly_modulus_degree, [60, my_scale, my_scale, my_scale, 60]))

    scale = pow(2.0, my_scale)

    context = SEALContext.Create(parms)
    print_parameters(context)

    keygen = KeyGenerator(context)
    public_key = keygen.public_key()
    secret_key = keygen.secret_key()
    relin_keys = keygen.relin_keys()

    rots = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048 ]
    # galk = GaloisKeys()
    galk = keygen.galois_keys(rots)

    encryptor = Encryptor(context, public_key)
    evaluator = Evaluator(context)
    decryptor = Decryptor(context, secret_key)

    encoder = CKKSEncoder(context)

    dimension = 15


    # =============== THE CHILDREN'S PHONE =========================

    inputs = [ 1,  1,  0,  1,  0,  0,  9,  3,  0,  9, -1,  9, -3,  9, -3]
    label = 4.67656012
    ptxt_vec = Plaintext()
    vrep = DoubleVector()
    for i in range(encoder.slot_count()):
        vrep.append(inputs[i % len(inputs)])
    # print(vrep)

    startTime = dt.datetime.now()

    encoder.encode(vrep, scale, ptxt_vec)

    executionTime = (dt.datetime.now()- startTime)
    print("Encode messages time:", executionTime.total_seconds() * 1000, 'ms')

    ct = Ciphertext()
    startTime = dt.datetime.now()

    encryptor.encrypt(ptxt_vec, ct)

    executionTime = (dt.datetime.now()- startTime)
    print("Encrypt plaintext time:", executionTime.total_seconds() * 1000 ,'ms')
    print("inputs:", inputs,)
    print("Actual score", label)
    # ======================= THE SERVER =========================


    M = [[ 0.05328287, -0.16178964, -0.39097965,  0.41615433,  0.01889587,
         0.3713742 , -0.16446845,  0.11293173,  0.05505809,  0.12692362,
        -0.15178066, -0.29750225, -0.21516082,  0.06488706,  0.11108878],
       [-0.02561562, -0.03269858, -0.01216358, -0.11297752, -0.2738169 ,
        -0.03692625, -0.00530095,  0.01176923,  0.19429125, -0.2729761 ,
        -0.20749274,  0.14368728, -0.05490598,  0.19706288,  0.07502966],
       [-0.15894748, -0.26874754, -0.05988424, -0.30172905,  0.2593911 ,
         0.18413709,  0.06479167,  0.16517809, -0.13770425, -0.08189211,
        -0.20792095,  0.08105072,  0.01933746,  0.24221788, -0.14212598],
       [-0.03912208, -0.09510133, -0.08593238, -0.26998731, -0.24941245,
        -0.1718206 ,  0.02192089,  0.24693109, -0.02897537, -0.243429  ,
        -0.14015515,  0.19767338,  0.13509378, -0.24110667, -0.1042549 ],
       [ 0.24942295,  0.35098198,  0.20846674,  0.16086772,  0.3406923 ,
        -0.04017446,  0.09415895, -0.09169883, -0.02298942, -0.11931356,
        -0.04367464, -0.25625843, -0.06830733, -0.03923444, -0.14939554],
       [-0.25239146, -0.53899604, -0.14509988,  0.00675901,  0.03890299,
        -0.06173677, -0.06280438,  0.1560059 , -0.12489604,  0.3560419 ,
         0.12061124,  0.0060205 ,  0.6501865 , -0.14744161, -0.05643116],
       [-0.12695698, -0.12265964, -0.2738482 , -0.09126022,  0.03216364,
        -0.00700721,  0.10724843, -0.04569022, -0.14998381,  0.00798092,
        -0.18080969, -0.2113741 , -0.19016302,  0.21170075, -0.8077361 ],
       [ 0.1844692 , -0.05976046,  0.2893701 , -0.31323946, -0.22158808,
         0.20591849, -0.17622443,  0.47042605,  0.4512592 , -0.3002473 ,
        -0.25633094,  0.3698981 ,  0.01756008, -0.28247648,  0.40910396],
       [ 0.18942234, -0.09219372, -0.0976105 , -0.03647816, -0.07299504,
         0.11300416, -0.17270242, -0.03261101, -0.11616515, -0.22153966,
         0.0416703 ,  0.24506326, -0.21631448,  0.00859736,  0.23069601],
       [-0.13320594, -0.25815815, -0.078593  , -0.07375473, -0.10476236,
        -0.02751808,  0.0024771 , -0.01635172,  0.32171994,  0.03652896,
        -0.15958506, -0.29584262, -0.20745626,  0.22688003,  0.06999159],
       [ 0.21888058, -0.15049644, -0.01212863,  0.02940671, -0.00167897,
        -0.15774627, -0.09218478,  0.23563243, -0.16785406, -0.11489175,
         0.25294292,  0.2740795 , -0.3431292 , -0.20945613,  0.12176304],
       [-0.51552254, -0.6210259 , -0.43848512, -0.09336843, -0.23097046,
         0.32647398, -0.09907157, -0.17894275, -0.20179908,  0.2751528 ,
         0.17022604,  0.34283224, -0.2762507 ,  0.2402467 ,  0.24129954],
       [ 0.14639282,  0.31082126,  0.05880466,  0.49572706,  0.5533546 ,
        -0.06065308,  0.08177202, -0.27722335, -0.29515997,  0.26542598,
         0.29260692, -0.37296152, -0.0771603 , -0.01869466, -0.14263546],
       [ 0.04612566,  0.21075283,  0.1742968 , -0.2376434 ,  0.10639938,
        -0.04246457,  0.07631122, -0.03630028, -0.26880452, -0.09918286,
         0.3840471 ,  0.28687474,  0.39920488, -0.16245653, -0.25311172],
       [ 0.13121656,  0.35117078,  0.3215371 ,  0.08745524,  0.01075196,
        -0.3299996 , -0.02874128,  0.14417566, -0.36359918, -0.15573539,
        -0.71312934,  0.33119583,  0.25473446, -0.37138397, -0.15447725]]


    W2 = DoubleVector([ 0.11071269,
         0.22808005,
         0.08247361,
         0.14395869,
         0.3453494 ,
        -0.07529078,
        -0.11085724,
         0.08463932,
         0.10595647,
         0.2888619 ,
        -0.12066234,
        -0.05952526,
        -0.20898722,
        -0.2241344 ,
        -0.06900433])

        
    

    b1 = DoubleVector([ 1.3708298 ,  0.15697935,  0.21439597, -0.910595  , -0.07737892,
         0.20408946,  0.14003058, -0.13682148,  0.73729855, -0.61451185,
         0.12001876, -0.35709542,  0.10856057, -0.05652325,  0.2758754 ])
    b2 = 2.9239743



    W2_plaintext = Plaintext()
    b1_plaintext = Plaintext()
    b2_plaintext = Plaintext()

    ptxt_diag = [Plaintext() for i in range(dimension)]
    for i in range(dimension):
        
        diag = DoubleVector()
        for j in range(dimension):
            diag.append(M[j][(j+i) % dimension])
        encoder.encode(diag, scale, ptxt_diag[i])
        # print(id(ptxt_diag[i]))
    # print(math.log(ptxt_vec.scale(),2))
    
    temp = Ciphertext()
    temp2 = Ciphertext(ct)
    enc_result = Ciphertext()
    
    # print(id(temp2))
    # print(id(ct))
    # print(temp2.parms_id())
    # print(ct.parms_id())
    print(" ========= Predicting on Homomorphic circuit: ===============")
    startTime = dt.datetime.now()
    for i in range(dimension):
        temp = Ciphertext(temp2)
        evaluator.multiply_plain_inplace(temp, ptxt_diag[i])
        if i == 0:
            enc_result = Ciphertext(temp)
        else:
            evaluator.add_inplace(enc_result, temp)
        evaluator.rotate_vector(temp2, 1, galk, temp2)
    
    
    evaluator.rescale_to_next_inplace(enc_result)
    
    enc_result.scale(pow(2.0, my_scale))
    
    encoder.encode(b1, enc_result.parms_id(), scale, b1_plaintext)
    # print(b1_plaintext.scale())
    evaluator.add_plain_inplace(enc_result, b1_plaintext)

    evaluator.square(enc_result, enc_result)
    evaluator.relinearize_inplace(enc_result, relin_keys)
    evaluator.rescale_to_next_inplace(enc_result)
    
    enc_result.scale(pow(2.0, my_scale))

    encoder.encode(W2, enc_result.parms_id(), scale, W2_plaintext)
    
    evaluator.multiply_plain_inplace(enc_result, W2_plaintext)
    
    evaluator.rescale_to_next_inplace(enc_result)
    enc_result.scale(pow(2.0, my_scale))
    
    temp_ct = Ciphertext()
    _iter = 1
    
    while _iter <= encoder.slot_count()/2:
        
        evaluator.rotate_vector(enc_result, _iter, galk, temp_ct)
        evaluator.add_inplace(enc_result, temp_ct)
        _iter <<= 1
        
    
    encoder.encode(b2, enc_result.parms_id(), enc_result.scale(), b2_plaintext)
    evaluator.add_plain_inplace(enc_result, b2_plaintext)

    executionTime = (dt.datetime.now()- startTime)
    print("Evaluation on HE time:", executionTime.total_seconds() * 1000, 'ms')


    # ==================== THE PARENTS' PHONE =========================

    plain_result = Plaintext()
    result = DoubleVector()
    
    startTime = dt.datetime.now()

    decryptor.decrypt(enc_result, plain_result)

    executionTime = (dt.datetime.now()- startTime)
    print("Decrypt result ciphertext time:", executionTime.total_seconds() * 1000, 'ms')
    


    startTime = dt.datetime.now()

    encoder.decode(plain_result, result)

    executionTime = (dt.datetime.now()- startTime)
    print("Decode result plaintext time:", executionTime.total_seconds() * 1000, 'ms')
    
    
    


    # === TEST RESULT WITHOUT HOMOMORPHIC ENCRYPTION ============
    Mv = [0.0]*dimension
    
    for i in range(dimension):
        for j in range(dimension):
            
            Mv[i] += M[i][j] * inputs[j]
    
    for j in range(dimension):
        Mv[j] = Mv[j] + b1[j]

    for j in range(dimension):
        Mv[j] = Mv[j] * Mv[j]

    sum = 0.0
    for j in range(dimension):
        Mv[j] = Mv[j] * W2[j]
        sum += Mv[j]
    sum += b2
    #####

    print("\n Predicting on HE result: %.4f" % result[0])
    print("Predicting on non-HE result: %.4f" %  sum)
    print("diff HE and non-HE: %.4f" %  abs(result[0] - sum))
    print("diff HE and actual: %.4f" %  abs(result[0] - label))
    print("Size of public key", sys.getsizeof(public_key))
    print("Size of secret key", sys.getsizeof(secret_key))
    print("Size of evalation key", sys.getsizeof(relin_keys))
    
if __name__ == '__main__':
    thesis_demo()
