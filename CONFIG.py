"""
Configuration of vocabulary game server.
Generated Mon 17 Oct 22:06:58 UTC 2016
Edit to fit development or deployment environment.

"""

PORT=5000
DEBUG = True  # Set to False for production use
secret_key="ebb17306f698a73df89a3c9239687f43"
success_at_count = 3  # How many matches before we declare victory? 
vocab="data/vocab.txt"  # CHANGE THIS to use another vocabulary file

