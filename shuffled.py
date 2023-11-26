import random


with open('/content/googletrans.txt', 'r') as f:
    lines = f.readlines()


shuffled_lines = []
for line in lines:
    words = line.split()
    random.shuffle(words)
    shuffled_line = ' '.join(words)
    shuffled_lines.append(shuffled_line)


shuffled_text = '\n'.join(shuffled_lines)


with open('/content/googletrans_shuffled.txt', 'w') as f:
    f.write(shuffled_text)