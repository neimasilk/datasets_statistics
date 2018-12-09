
import collections


downcase = True
delimiter = " "
min_frequency = 30
max_vocab_size = 1000

hitung = collections.Counter()

def hitung_statistik(file_teks):
    cnt = collections.Counter()
    with open(file_teks, 'r') as f:
        infile = f.read().splitlines()
        f.close()

    for line in infile:
      if downcase:
        line = line.lower()
      if delimiter == "":
        tokens = list(line.strip())
      else:
        tokens = line.strip().split(delimiter)
      tokens = [_ for _ in tokens if len(_) > 0]
      cnt.update(tokens)

    print(f'Found {len(cnt)} unique tokens in the vocabulary.')

    # Filter tokens below the frequency threshold
    if min_frequency > 0:
      filtered_tokens = [(w, c) for w, c in cnt.most_common()
                         if c > min_frequency]
      cnt = collections.Counter(dict(filtered_tokens))

    print(f"Found {len(cnt)} unique tokens with frequency > {min_frequency}.")
    return cnt

def tampilkan_vocab(penghitung):
    # Sort tokens by 1. frequency 2. lexically to break ties
    word_with_counts = penghitung.most_common()
    word_with_counts = sorted(word_with_counts, key=lambda x: (x[1], x[0]), reverse=True)
    # Take only max-vocab
    if max_vocab_size is not None:
        word_with_counts = word_with_counts[:max_vocab_size]
        for word, count in word_with_counts:
           print("{}\t{}".format(word, count))


if __name__ == '__main__':


    test_file_location_sebelum_separasi = 'test.id'
    test_file_location_setelah_separasi = 'test.tok.id'
    train_file_location_sebelum_separasi = 'train.id'
    train_file_location_setelah_separasi = 'train.tok.id'
    print('statistik testing file')
    hitung_statistik(test_file_location_sebelum_separasi)
    hitung_statistik(test_file_location_setelah_separasi)
    print('statistik training file')
    hitung_statistik(train_file_location_sebelum_separasi)
    hitung_statistik(train_file_location_setelah_separasi)
    # tampilkan_vocab(hit)
