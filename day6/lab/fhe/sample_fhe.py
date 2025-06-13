from openfhe import *

# Set CryptoContext
parameters = CCParamsBFVRNS()
parameters.SetPlaintextModulus(65537)
parameters.SetMultiplicativeDepth(4)

# Enable necessary features
crypto_context = GenCryptoContext(parameters)
crypto_context.Enable(PKESchemeFeature.PKE)
crypto_context.Enable(PKESchemeFeature.LEVELEDSHE)
# Needed for homo morphic enc
crypto_context.Enable(PKESchemeFeature.KEYSWITCH)

# Generate public/private keys
key_pair = crypto_context.KeyGen()

# Generate the relinearization key
crypto_context.EvalMultKeyGen(key_pair.secretKey)

# Encode first plaintext vector
vec1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pt1 = crypto_context.MakePackedPlaintext(vec1)

# Encode second plaintext vector
vec2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pt2 = crypto_context.MakePackedPlaintext(vec2)

# Encrypt the two vectors using the same public key
ct1 = crypto_context.Encrypt(key_pair.publicKey, pt1)
ct2 = crypto_context.Encrypt(key_pair.publicKey, pt2)

# Homomorphic addition
ct_add = crypto_context.EvalAdd(ct1, ct2)
v1 = [1, 2, 3]

# Homomorphic multiplication
ct_mult = crypto_context.EvalMult(ct1, ct2)

# Decrypt the result of the addition
pt_add = crypto_context.Decrypt(ct_add, key_pair.secretKey)

# Decrypt the result of the multiplication
pt_mult = crypto_context.Decrypt(ct_mult ,key_pair.secretKey)

print("Plaintext #1: " + str(pt1))
print("Plaintext #2: " + str(pt2))

# Print the result
print("Addition #1 + #2 = " + str(pt_add))
print("Multiplication #1 * #2 = " + str(pt_mult))
