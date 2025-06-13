from openfhe import *

# Set CryptoContext
parameters = CCParamsBFVRNS()
parameters.SetPlaintextModulus(65537)
parameters.SetMultiplicativeDepth(3)

# Enable necessary features
crypto_context = GenCryptoContext(parameters)
crypto_context.Enable(PKESchemeFeature.PKE)
crypto_context.Enable(PKESchemeFeature.LEVELEDSHE)
crypto_context.Enable(PKESchemeFeature.ADVANCEDSHE)
crypto_context.Enable(PKESchemeFeature.KEYSWITCH)

# Generate public/private keys
key_pair = crypto_context.KeyGen()

# Generate the relinearization keys
crypto_context.EvalMultKeyGen(key_pair.secretKey)
crypto_context.EvalSumKeyGen(key_pair.secretKey)

################# Fill in the code #################
# Encode and encrypt the values
values = [412, 8423, 66, 891, 277, 84, 5, 9]

# Add up the elements of the values

# Decrypt the sum and compute the mean in plaintext (because EvalDivide is supported only in CKKS)
