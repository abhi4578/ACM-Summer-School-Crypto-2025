from openfhe import *

# Set CryptoContext
parameters = CCParamsBFVRNS()
parameters.SetPlaintextModulus(65537)
parameters.SetMultiplicativeDepth(2)

# Enable necessary features
crypto_context = GenCryptoContext(parameters)
crypto_context.Enable(PKESchemeFeature.PKE)
crypto_context.Enable(PKESchemeFeature.LEVELEDSHE)
crypto_context.Enable(PKESchemeFeature.KEYSWITCH)

# Generate public/private keys
key_pair = crypto_context.KeyGen()

# Generate the relinearization key
crypto_context.EvalMultKeyGen(key_pair.secretKey)

############ Fill in the code ############
a = [12]
pt1 = crypto_context.MakePackedPlaintext(a)

# Encode second plaintext vector
b = [11]
pt2 = crypto_context.MakePackedPlaintext(b)

# Encrypt the plaintexts
ct1 = crypto_context.Encrypt(key_pair.publicKey, pt1)
ct2 = crypto_context.Encrypt(key_pair.publicKey, pt2)


# Homomorphic operations go here
a_sub_b = crypto_context.EvalSub(ct1, ct2)
a_add_b = crypto_context.EvalAdd(ct1, ct2)
a_2 = crypto_context.EvalMult(ct1, ct1)
b_2 = crypto_context.EvalMult(ct2, ct2)

lhs = crypto_context.EvalSub(a_2, b_2)
lhs_dec = crypto_context.Decrypt(lhs, key_pair.secretKey)
rhs_dec =  crypto_context.Decrypt( crypto_context.EvalMult(a_add_b, a_sub_b), key_pair.secretKey) 


# Prove a^2 - b^2 = (a + b)(a - b)
print("a^2 _ b^2", lhs_dec)
print("rhs_dec", str(rhs_dec))
if (str(lhs_dec) == str(rhs_dec)):
    print("Proved a^2 - b^2 = (a + b)(a - b)")