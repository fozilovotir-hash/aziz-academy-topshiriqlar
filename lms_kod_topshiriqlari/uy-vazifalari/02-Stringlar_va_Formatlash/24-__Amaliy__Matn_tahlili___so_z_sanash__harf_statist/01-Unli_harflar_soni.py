matn = input().lower()
unli_harflar = 'aeiou'
unlilar_soni = sum(1 for harf in matn if harf in unli_harflar)
print(unlilar_soni)