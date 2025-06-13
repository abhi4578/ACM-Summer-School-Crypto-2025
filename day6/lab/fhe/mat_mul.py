from openfhe import *

# Set CryptoContext
parameters = CCParamsBFVRNS()
parameters.SetPlaintextModulus(65537)
#parameters.SetMultiplicativeDepth(3)

# Enable necessary features
crypto_context = GenCryptoContext(parameters)
crypto_context.Enable(PKESchemeFeature.PKE)
crypto_context.Enable(PKESchemeFeature.LEVELEDSHE)
crypto_context.Enable(PKESchemeFeature.KEYSWITCH)

# Generate public/private keys
key_pair = crypto_context.KeyGen()

# Generate the relinearization key
crypto_context.EvalMultKeyGen(key_pair.secretKey)

################## Fill in the code ################

# Encode and encrypt matrices A and B as individual elements
A = [1, 2, 3, 4]
B = [5, 6, 7, 8]

# Homomorphic multiplication and addition for matrix product

# Decrypt the results

# Extract the result
