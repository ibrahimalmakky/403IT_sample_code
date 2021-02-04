import loremipsum
import random
import sorting

plaintext = loremipsum.generate(50000, loremipsum.ParagraphLength.LONG)
plaintext = plaintext+loremipsum.generate(25000, loremipsum.ParagraphLength.LONG)
text_arr = plaintext.split(" ")

secrets = ["Herbert", "Weronika", "Kasia"]
rand_nums = []
for i in range(len(secrets)):
    rand_nums.append(random.randrange(0, len(text_arr))) 
    text_arr[rand_nums[i]] = secrets[i]

plaintext = ' '.join(text_arr)

print(rand_nums)

me_file = open("name_challenge.txt", "w")
me_file.write(plaintext)
me_file.close()

