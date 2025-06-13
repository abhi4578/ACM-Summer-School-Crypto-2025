from openfhe import *

# Set CryptoContext
parameters = CCParamsBFVRNS()
parameters.SetPlaintextModulus(65537)
#parameters.SetMultiplicativeDepth(2)

# Enable necessary features
crypto_context = GenCryptoContext(parameters)
crypto_context.Enable(PKESchemeFeature.PKE)
crypto_context.Enable(PKESchemeFeature.LEVELEDSHE)
crypto_context.Enable(PKESchemeFeature.KEYSWITCH)

# Generate public/private keys
key_pair = crypto_context.KeyGen()

# Generate the relinearization key
crypto_context.EvalMultKeyGen(key_pair.secretKey)

########## Fill in the code ##########
# Encode plaintext vectors for a and b

# Encrypt the plaintexts

# Homomorphic operations go here

# Prove (a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)
