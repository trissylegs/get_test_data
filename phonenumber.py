
from faker import Faker

seed = 0x6cf299f16584611d

print('seed = {:x}'.format(seed))

locales = [
    'en_AU',
    'en_CA',
    'en_GB',
    'en_NZ',
    'id_ID',
    'th_TH',
    'zh_TW',
]

print('_DATA = [')

for lc in locales:
    region = lc.split('_')[1]
    fake = Faker(lc)
    Faker.seed(seed)
    for i in range(10):
        ph = fake.phone_number()
        t = region, ph
        print('    ', t, ',', sep='')

print(']')
