import requests
import json

cidade = input("Escreva sua cidade: ")

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=62ddb3aac0bd579a6c962e21c6ccaa7d')
#tradu = requests.get()
tempo = json.loads(requisicao.text)
print('Condicao do tempo: ', tempo['weather'][0]['main'])
print('Tempratura',float(tempo['main']['temp']) - 273.15)


'''
{
  "type": "service_account",
  "project_id": "valiant-hangout-232723",
  "private_key_id": "dd99fcd97765d16b66c26f6f218d071c259d299d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCv+VqVD7PUfV6J\nCJY0R+jYOh88lliKmeZS4cq21j87UNqvhpvAKrSVNn2Ue1PpkjTs0/K473MKedIo\n8xjhEObWTrwUQE/EORWz+FxWlJd7kC+c7uzTqPbip9nDd6ynl8doj/veI9WIg/lX\nVEHj5Oqqlm69EcQ5vntdmGUnLxdEkj9P+/q++VVWah6HCUNFLw5EYPA4OG9nzHoG\ndB54FZsj/bovuxUmWIc+OQ4zkRqcMZxZlQJuj3qVLYk/scOmyHgfq6XmZ1l/62qt\nw0wbe/G5vfUwbtFax1rbc/xb8ZvxjxR8nJQ1DzSCSHGIMmPWOpUZD5whTl5PIfqI\n1/Dy3balAgMBAAECggEAAQK7ng0mPHT9eZs1BNcM47Q7Wn7twnRtbQU8kGqpyxtr\nX7eA/+XyF5FMJotdL50JWy4ODNKppHvCoaP6MDPt2RLZ5BV8Ev88IqzgfhbOyYTj\nreqpYL9trsUsBc75wBSp4bqoX0Q+OIR/7OjgLM2zYCHXc2Dwvl9bsgcecM7FoXBh\nh5dN7m8yiWw47dT9VYnVYDyxZZCZTKk6zw85pqyyXis6th8nKjoPFp8vHKpKvyXC\nz2nxwFalOu6zZHsTs48XI6Pa5q/iHLoFEcQMV2yErEqGkTCiO7NQpzQ2DUkcn91B\n3MfHDl3TL0ermJEHLCxl+CdhTv6UdWlO+nuoTqAZQQKBgQDzJmld7HHZmHaLCxdC\n093Kw3V3O4IUY5Hqn7ObgPMqggKXMdvR3P06j4oAvGLcQDjlLsTM9X200fMIQ8IO\nu2d2vF1dR4HGI+9NxwDDKvzoa1bgQb6VAzeWUKSR4NbJ/+avf1vvkQSLdqC6Yb86\nPCMfIK9/Erx+qeNtQXBo5+Nd+QKBgQC5Rh1pT3L2jy+7cE1vFJHvHqmc/p6ks50h\nkXDcic42GN6ESIGeTSYr2GT2tz73do8wPz+AXd3VAzUdJ2rSaZ2993ECm17pL0dW\nczG7FXRcRoObhNwn+6S/StWil/eDvt1btsOcYZsnEd/6dTE7SMSpAyfkfNOJruyr\n4/IDFvG5DQKBgHwj/F/LvETQJpXOz816xh4jtPFvHHa0b2dOqjCWoY/uWMxA1G5N\nWaxwZJEDnaW91E6OlkPegpOzLVXm4kkLPUPN4A0j2QoEhsU6+RSr+fvf8bcFWfxS\nbCr+eUdRd9giIvEvIQ0rCRr7Mgx2o19kHLpjwbYrJrm0mzzI0E9/NQJhAoGAHlQD\n7IE86G93+M7hXhWX7fSu/ywO/BcK2bvdJbzJLMHVawITdb5bSUIbBOfqPsgBmHxC\nANlcvsnPn/4b1mXDlJ00uqCEYNeEbfpdYaqZaaGBWavd/g2LYmT1o7AMrFxKEAFS\n8/5mT3b1myIj9PhseN4zYYutdRRVWa3up+LRnuECgYBKDHBUsWJSU96WRpUqUBAS\nyk8ArA7FJF6jjsn65CGNpiGggIO4wYGBcF1dfFCzOGIagevQOCcNl5qg1rvsIDP3\n/2aTAna8oDoxwhAoTBbe0/YI+LNl+wGFFIM9HRqattnkP/nrqOzQm6EMi20eZSNP\nP1WM6LqdfgxS2IbItzinBw==\n-----END PRIVATE KEY-----\n",
  "client_email": "cezar-719@valiant-hangout-232723.iam.gserviceaccount.com",
  "client_id": "103418091163999470242",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/cezar-719%40valiant-hangout-232723.iam.gserviceaccount.com"
}
'''