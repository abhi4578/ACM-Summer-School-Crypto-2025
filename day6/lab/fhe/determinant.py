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
crypto_context.Enable(PKESchemeFeature.ADVANCEDSHE)

# Generate public/private keys
key_pair = crypto_context.KeyGen()

# Generate the relinearization key and rotation keys
crypto_context.EvalMultKeyGen(key_pair.secretKey)
crypto_context.EvalAtIndexKeyGen(key_pair.secretKey, [1, 2, 3])

############ Fill in the code ############

# Initialize a 2x2 matrix
matrix = [[1,2], [2,1]]
pt1 = crypto_context.MakePackedPlaintext(vec1)

# Encode plaintext matrix

# Encrypt the matrix
ct1 = crypto_context.Encrypt(key_pair.publicKey, pt1)

# Extract elements using rotations

# Homomorphically compute the determinant: ad - bc
