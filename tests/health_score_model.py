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

    dimension = 9


    # =============== THE CHILDREN'S PHONE =========================

    inputs = [1, 1, 0, 1, 0, 0, 9, 3, 0]
    label = 7.33333333
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


    M = [[-2.36087590e-02,  4.46248800e-02, -2.23592725e-02,
        -2.07305329e-05, -2.57243309e-02, -5.93085289e-02,
         1.16910450e-02,  8.93315766e-03, -2.37425696e-02],
       [-5.20601034e-01,  1.11133903e-01, -2.75830179e-01,
        -6.59517109e-01,  3.01611751e-01,  3.11634302e-01,
        -9.27691981e-02, -3.26891579e-02,  2.90112440e-02],
       [ 3.79112303e-01, -5.28463066e-01, -2.02181607e-01,
        -1.88920185e-01,  4.58977133e-01,  2.74691582e-01,
         2.00206220e-01, -1.48632705e-01,  7.23632649e-02],
       [ 6.85166866e-02, -7.41788000e-02, -3.18101980e-02,
         1.94061212e-02,  2.39977330e-01,  4.55129683e-01,
        -2.68541705e-02, -1.29274294e-01,  4.08127874e-01],
       [-2.57370751e-02,  7.61075467e-02, -4.65674043e-01,
         2.11506918e-01, -1.31074879e-02, -3.57747078e-01,
         1.44670844e-01,  3.26632857e-01, -1.93478480e-01],
       [-1.94074169e-01, -3.07507068e-01, -1.54785335e-01,
        -4.03130263e-01, -4.59236115e-01, -3.33878756e-01,
        -2.10818231e-01, -1.01819344e-01, -2.93932587e-01],
       [-8.70853197e-03, -2.08253805e-02, -7.97070004e-03,
         6.62487606e-03, -1.35173211e-02, -9.00138356e-03,
        -2.22847168e-03,  1.71716306e-02,  2.12160610e-02],
       [ 3.57228220e-01,  1.19817443e-01, -7.04302788e-01,
         3.16875786e-01, -7.41272330e-01, -5.25740862e-01,
        -6.71090186e-02, -1.72078133e-01,  1.25051379e-01],
       [ 3.50797363e-02, -7.43552744e-02, -3.54508519e-01,
         5.79200447e-01,  4.29468714e-02,  3.66750538e-01,
        -1.27368644e-01, -1.70253590e-01, -4.96561453e-02]]


    W2 = DoubleVector([-0.00228387,
         0.13967429,
        -0.07893369,
         0.21867964,
        -0.10431205,
        -0.13585195,
         0.00322833,
         0.09382743,
         0.1062593 ])

        
    

    b1 = DoubleVector([ 0.02589241,  2.3318555 , -0.19546019, -2.3771975 , -0.9155854 ,
         1.9580336 ,  0.00623073,  0.5279099 ,  0.28359258])
    b2 = 4.8385687



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
