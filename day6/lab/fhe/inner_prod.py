from openfhe import *

# Set CryptoContext
parameters = CCParamsBFVRNS()
parameters.SetPlaintextModulus(65537)
parameters.SetMultiplicativeDepth(3)

# Enable necessary features
crypto_context = GenCryptoContext(parameters)
crypto_context.Enable(PKESchemeFeature.PKE)
crypto_context.Enable(PKESchemeFeature.LEVELEDSHE)
crypto_context.Enable(PKESchemeFeature.KEYSWITCH)
crypto_context.Enable(PKESchemeFeature.ADVANCEDSHE)

# Generate public/private keys
key_pair = crypto_context.KeyGen()

# Generate the relinearization and automorphism keys
crypto_context.EvalMultKeyGen(key_pair.secretKey)
crypto_context.EvalSumKeyGen(key_pair.secretKey)

############## Fill in the code #############
# Encode vectors v1 and v2
v1 = [1, 2, 3]
v2 = [4, 5, 6]
pt1 = crypto_context.MakePackedPlaintext(v1)
pt2 = crypto_context.MakePackedPlaintext(v2)

# Encrypt the vectors
ct1 = crypto_context.Encrypt(key_pair.publicKey, pt1)
ct2 = crypto_context.Encrypt(key_pair.publicKey, pt2)

# Compute homomorphic element-wise multiplication
ct_mult = crypto_context.EvalMult(ct1, ct2)
# Add up the elements of the resulting ciphertext
ct_v_sum= crypto_context.EvalSum(ct_mult,3)
# Decrypt the result
pt_mult = crypto_context.Decrypt(ct_mult ,key_pair.secretKey)
pt_v_sum= crypto_context.Decrypt(ct_v_sum, key_pair.secretKey)
# Extract the result
print(pt_mult)
print(pt_v_sum)