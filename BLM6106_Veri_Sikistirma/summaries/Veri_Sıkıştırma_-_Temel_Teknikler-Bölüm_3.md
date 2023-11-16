## Sezgisel Sıkıştırma (Intuitive Compression)

- **Braille Kodlama**

  - Literary
  - Nemeth
  - CBC
  - Music

- **Mors Kodlama**
  - Her nokta 1 birim, her çizgi 3 birim
  - Nokta ve çizgiler arası 1 birim
  - Karakterler arası 3, kelimeler arası 6 birim
  - Hata yapıldığında son kelimenin silinmesi için 8 nokta

### Geri Dönüşümü Olmayan Sıkıştırma (Irreversible Text Compression)

- **Ad Hoc Sıkıştırma**

  - Geri dönüşümü olan basit, kişiye özel çözümler
  - Sparse String Sıkıştırma: `___dersin___adıverisıkıştırmavepazartesigünüyapılıyor` → boşluk yerine 1 kodlanıyor
    - L1=`00110000001111000010000001110010000010000110000000`
    - L2=`1011110011001100`
    - L3=`1111`
    - L1 ve L2 deki sıfır olan gruplar silinerek L1, L2 ve L3 stringleri ve arkasından boşluksuz olarak text gönderilir.
      - L1=`001100111000100011000000`
      - L2=`1011110011001100`
      - L3=`1111`

- **Baudot Kodlama**
- **Önek Sıkıştırma (Front Compression)**
- **Run Length Encoding Compression**
  - Eğer bir input stream içerisinde bir "d" verisi "n" defa arka arkaya geliyorsa, bunu bir seferde "nd" çifti ile gösterebiliriz.
  - "n" değerine "run" denir.
  - Hem text hem de görüntü sıkıştırmada kullanılır.
  - Kayıplı ve kayıpsız versiyonları vardır.
  - Run Length Encoding veya RLE olarak adlandırılır.
    - Örnek:
      - Uncompressed: `2. all is too well`
      - Compressed: `2. a2l is t2o we2l`
  - Nasıl Çözülür?
    - Özel escape kod kullanalım
      - Compressed: `2. a@2l is t@2o we@2l`
      - Problemler:
        - Orijinal veriden daha uzundur
        - İki karakter yerine 3 karakter kullanılmıştır
        - Tekrar faktörünü 3 veya daha fazla karakter için kullanmak gerekir
        - Tekrar sayısı 3’den az ise karakter aynen yazılır
      - Temel problemler: Doğal dilde yazılmış olan metinlerde arka arkaya tekrar eden karakter nadirdir (boşluklar hariç)
        - Tekrar sayısına 1 byte ayrılmış olup, 255 ile sınırlıdır. Tekrar sayısı 3 tekrar karakterden sonra kullanılacak ise 258 adet aynı karakter 3 byte ile kodlanır
        - Kullanılan özel escape kodu metin içerisinde geçebilir (farklı karakter seçilmelidir)
        - Exe türü dosyalarda tüm ASCII karakterler dosya içerisinde yer alabilir. Bu durumda farklı bir yol izlenmelidir.†
        - † MNP5 (Microcom Network Protocol) uygulanan yöntem kullanılır
        - Input stream’de 3 karakter arka arkaya tekrar ediyorsa, output stream 3 kopyada yazılır. Dördüncü byte ise run değeri yazılır.
        - 3 kopya için (aaa) → `aaa0` → 3 byte yerine 4 byte (genişleme)
        - 4 kopya için (aaaa) → `aaa1` → 4 byte yerine 4 byte (sıkıştırma yok)
        - 5 kopya için (aaaaa) → `aaa2` → 5 byte yerine 4 byte (sıkıştırma var)
      - RLE Compression Performance: `[(N - (M*L) + M*3] / N`
      - MNP5 Compression Performance: `[(N - (M*L) + M*4] / N`

### Görüntü Sıkıştırma

- Dijital bir görüntü, pixel adı verilen noktalardan oluşur.
- Her pixel (1 bit B&W, birkaç bit gray scale, 8 bit color table, 24 bit true color) oluşur.
- Uniform bir alanda RLE için sıkıştırma oranı (şeklin çevre uzunluğunun yarısı/alan içerisindeki toplam pixel sayısı)
- Her scanline için bir giriş bir çıkış noktası olduğundan 2\*scan line değeri uniform şeklin çevre uzunluğunu verir.
- RLE- Kayıplı Görüntü Sıkıştırma
  - Kayıplar kullanıcıya göre bazı uygulama alanlarında kabul edilebilir.
  - Kısa olan «run» değerleri ihmal edilebilir.
  - Kullanıcıya ihmal edilebilecek en büyük «run» uzunluğu sorulur. Kullanıcı üç demiş ise anlamı 1, 2 ve 3 pixel uzunluğundaki pixel’in değeri yerine, en yakın komşu pixel’in değerini kabul etmektir.

### Özet

- RLE kayıpsız bir sıkıştırma yöntemidir.
- Aynı değere sahip uzun verilerde en yüksek başarıyı verir.
- Kodlanması kolaydır.
- Çeşitli varyasyonları vardır.
- Hızlı çalışır.
- Karışık veri üzerinde negatif sıkıştırma yapar.
