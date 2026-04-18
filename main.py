def almashtir(matnlar):
    unli_harflar = 'aeiouAEIOU'
    yangi_matnlar = []
    for matn in matnlar:
        yangi_matn = ''
        for harf in matn:
            if harf in unli_harflar:
                yangi_matn += '_'
            else:
                yangi_matn += harf
        yangi_matnlar.append(yangi_matn)
    return yangi_matnlar

matnlar = ["Assalomu alaykum", "Python dasturlash tili", "Dunyo bo'ylab mashhur"]
print(almashtir(matnlar))
