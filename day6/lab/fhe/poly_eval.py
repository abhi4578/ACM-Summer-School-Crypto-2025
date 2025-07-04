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

# Generate public/private keys
key_pair = crypto_context.KeyGen()

# Generate the relinearization key
crypto_context.EvalMultKeyGen(key_pair.secretKey)

############# Fill in the code ##############
# Encode and encrypt the input values
x = 3
y = 4


# Coefficients of the polynomial
a, b, c, d, e, f = 2, 3, 4, 5, 6, 7

# Compute the polynomial P(x, y) = 2x^2 + 3xy + 4y^2 + 5x + 6y + 7 (with x = 3, y = 4)

# Decrypt the result
