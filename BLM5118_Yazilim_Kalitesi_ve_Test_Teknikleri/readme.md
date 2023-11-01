# Yazılım Kalitesi ve Test Teknikleri

## Yapılacaklar

- [ ] Sunumlar bulunacak
- [ ] Sunumlar okunacak

Ders Öğrenim Çıktıları

- Öğrenciler Test Planı Yazabilme ve Test Yönetimi gerçekleştirebilme yeteneğine sahip olur.
- Öğrenciler yazılım kalite modellerini bilir.
- Öğrenciler yazılım hata önleme ve süreç iyileştirmeyi bilir.
- Öğrenciler yazılım formal doğrulama yöntemlerini uygulama becerisine sahip olur
- Öğrenciler, yazılım kapsam testlerinde sonlu durum makinaları ve markov zincirlerini uygulamayı bilir.

Hafta Konular Ön Hazırlık

1. Yazılım Kalite Yönetimi
2. Yazılım Hata Önleme ve Azaltma
3. Yazılım Hata Toleransı
4. Formal yazılım Doğrulama Yöntemleri
5. Kontrol Liste ile Kapsam Testleri
6. Sonlu Durum Makinaları ve Markov Zincirleri temelli Yazılım Kapsam Testleri
7. Kontrol Akışı ve Veri Bağımlılığı Testleri
8. Ara Sınav 1
9. Ara Sınav
10. Yazılım Kalite Modelleri ve Ölçümleri
11. Kalite İyileştirme için Risk Tanımlama
12. Yazılım Konfigurasyon Yönetimi
13. Küçük sınav ve Yazılım Test Uygulaması
14. Proje Sunumu
15. Final

Yazılım büyüklüğünü dolaylı ve doğrudan olarak ölçen iki metrik örneği:

a) Dolaylı ölçüm metriği: Kaynak kod satır sayısı. Bu metrik, yazılımın büyüklüğünü ölçmek için kullanılabilir. Ancak, kodun kalitesi veya karmaşıklığı hakkında doğrudan bilgi vermez. Daha fazla kod, genellikle daha büyük bir yazılımı temsil eder, ancak bu, yazılımın işlevselliği veya kalitesi hakkında herhangi bir şey söylemez.

b) Doğrudan ölçüm metriği: Kod karmaşıklığı. Kod karmaşıklığı, yazılımın anlaşılması ve bakımı için ne kadar zor olduğunu ölçer. Bu metrik, yazılımın iç yapısının karmaşıklığını değerlendirmeye yardımcı olur. Örneğin, Cyclomatic Complexity gibi metrikler, kodun karmaşıklığını ölçmek için kullanılabilir. Daha yüksek karmaşıklık, kodun daha zor anlaşılabilir olduğunu gösterebilir.

Temel yol testi (Basic Path test), yazılımın işlevselliğini ve kontrol akışını test etmek için kullanılan bir yöntemdir. Bu test, yazılımın farklı yol ve senaryoları boyunca nasıl davrandığını değerlendirmeye odaklanır. Temel yol testini gerçekleştirmek için aşağıdaki adımları takip edebilirsiniz:

a) Kod analizi: İlk olarak, yazılımın kaynak kodunu inceleyin ve işlevlerin ve kontrol yapılarının nasıl çalıştığını anlamaya çalışın.

b) Kontrol akış diyagramı oluşturma: Yazılımın kontrol akışını görselleştirmek için kontrol akış diyagramları oluşturun. Bu diyagramlar, farklı yol ve şartlar arasındaki ilişkileri netleştirmenize yardımcı olacaktır.

c) Temel yolları belirleme: Kontrol akış diyagramlarını kullanarak yazılımın farklı temel yollarını tanımlayın. Temel yollar, yazılımın farklı girdi kombinasyonlarına ve koşullarına nasıl tepki verdiğini temsil eder.

d) Test case'lerin oluşturulması: Her bir temel yol için uygun test case'ler oluşturun. Her test case, belirli bir girdi kombinasyonunu veya senaryoyu temsil etmelidir. Bu test case'ler, yazılımın farklı temel yollar üzerinde nasıl davrandığını test etmek için kullanılacaktır.

e) Testlerin yürütülmesi: Oluşturulan test case'leri kullanarak yazılımı test edin. Her bir temel yol ve senaryo için yazılımın beklenen davranışını doğrulayın ve herhangi bir hata veya uygunsuz davranışı tespit edin.

Temel yol testi, yazılımın farklı işlevlerini ve koşullarını kapsayan kapsamlı bir test stratejisi sunar. Bu sayede yazılımın daha güvenilir ve hatasız çalışmasını sağlamak için kullanılabilir.
