### Konular

1.  [Introduction to Data Mining](02DataMining.pdf)

    - **Bölüm Amaçları**
    - Ham ve büyük veri kümelerinin temel temsillerini ve özelliklerini analiz etmek.
    - Sayısal öznitelikler üzerinde farklı normalizasyon tekniklerini uygulamak.
    - Öznitelik dönüştürme de dahil olmak üzere farklı veri hazırlama tekniklerini tanımak.
    - Eksik değerlerin giderilmesi için farklı yöntemleri karşılaştırmak.
    - Zamanla değişen verilerin homojen temsili için bir yöntem oluşturmak.
    - Aykırı değer tespiti için farklı yöntemleri karşılaştırmak.

2.  Data Mining Concepts and Data Preprocessing Techniques

    - Feature Selection
    - Dimensionality Reduction
    - Normalization
    - Data subsetting

3.  [Data Reduction and Data Discretization-I](03DataReduction.pdf)

    - **Bölüm Amaçları**
    - Özellikler, durumlar ve değer azaltma teknikleri temelinde boyutsallık farkını belirlemek.
    - Bir veri madenciliği sürecinin ön işlemesinde veri azaltmanın avantajlarını açıklamak.
    - Karşılık gelen istatistiksel yöntemler kullanarak özellik seçimi ve özellik bileşimi görevlerinin temel prensiplerini anlamak.
    - Özellik sıralama için entropi tabanlı teknik ve temel bileşen analizi uygulamak ve karşılaştırmak.
    - Azaltılmış ayrık değerler için ChiMerge ve Bin tabanlı tekniklerin temel prensiplerini anlamak ve uygulamak.
    - Azaltma, artan ve ortalama örnekler temelinde olduğunda yaklaşımları ayırt etmek.

4.  Data Reduction and Data Discretization-II
5.  [Decision Trees and Decision Rules](05DecisionTree.pdf)

    - Karar Ağacı indüksiyonu, sınıf etiketli eğitim demetlerinden (örnekler) karar ağaçlarının öğrenilmesidir.
    - Karar ağacı, her iç düğümün (yaprak olmayan düğüm) bir öznitelik testini gösterdiği, her dalın bir test sonucunu temsil ettiği ve yaprak düğümünün (veya terminalin) bir sınıf etiketi tuttuğu akış diyagramı benzeri bir ağaç yapısıdır.
    - Ağaçtaki en üst düğüm kök düğümüdür.

6.  [Statistical Classification Methods, Naïve Bayesian Classification](04NaiveBayes.pdf)

    - Measures of Classification Performance
      - Confusion Matrix:
        | Actual/Predicted | Positive | Negative |
        | ---------------- | -------- | -------- |
        | Positive | TP | FN |
        | Negative | FP | TN |

    ***

    | Measure     | Formula                                                          | Description                                                                   |
    | ----------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------- |
    | Accuracy    | (TP + TN) / (TP + TN + FP + FN)                                  | Proportion of correct predictions among the total number of cases evaluated.  |
    | Error Rate  | (FP + FN) / (TP + TN + FP + FN)                                  | Proportion of incorrect predictions among the total number of cases evaluated |
    | Sensitivity | TP / (TP + FN)                                                   | Proportion of positive cases correctly identified                             |
    | Specificity | TN / (TN + FP)                                                   | Proportion of negative cases correctly identified                             |
    | Precision   | TP / (TP + FP)                                                   | Proportion of positive predictions that are correct                           |
    | Recall      | TP / (TP + FN)                                                   | Proportion of positive cases that are correctly identified                    |
    | F1-Score    | $$ 2 \times \frac{Precision \times Recall}{Precision + Recall}$$ | Harmonic mean of precision and recall                                         |
    | FP Rate α   | FP / (FP + TN) [1 - specifity]                                   | Probability of incorrectly rejecting the null hypothesis                      |
    | FN Rate β   | FN / (TP + FN) [1 - sensitivity]                                 | Probability of incorrectly accepting the null hypothesis                      |
    | Power       | 1 - β                                                            | Probability of correctly rejecting the null hypothesis                        |

        - X, sınıf etiketi bilinmeyen bir veri örneği olsun.
        - H, veri örneğinin belirli bir sınıfa C ait olduğu hipotezidir.
        - Gözlemlenen veri örneği X'in verildiği durumda H'nin geçerlilik olasılığı olan P(H/X) hesaplanmak istenir.
        - P(H/X), X verildikten sonra hipoteze olan güvenimizi temsil eder.
        - Öte yandan, P(H) herhangi bir örnekteki veriye bakılmaksızın H'nin öncül olasılığıdır.
        - P(H|X) ise öncül olasılıktan daha fazla bilgiye dayanarak hesaplanan sonrasal olasılıktır.
        - Bayes Teoremi, olasılıklar P(H), P(X) ve P(X|H) kullanarak sonrasal olasılık P(H|X) hesaplamak için bir yöntem sağlar.
        - Temel ilişki şöyledir: `P(H|X) = P(X|H) * P(H) / P(X)`

7.  [Clustering Methods: K-Means](06K-means-clustering.pdf)

    - [K-means Clustering From Scratch In Python [Machine Learning Tutorial]](https://youtu.be/lX-3nGHDhQg)

    - Kümeleme:
    - Gözetimsiz öğrenme
    - Etiket yok, ancak veri gerektirir
    - Desenleri tespit eder, örneğin

      - E-postaları veya arama sonuçlarını gruplandırır
      - Müşteri alışveriş alışkanlıkları
      - Görüntülerin bölgeleri

    - Ne aradığınızı bilmediğinizde faydalıdır

8.  [Clustering Methods: Hierarchical Clustering](ch8-Cluster-Analysis.pdf)

    - Hiyerarşik kümeleme, küme sayısını önceden belirlemek zorunda kalmadan verileri kümelere ayırır.
    - Hiyerarşik kümeleme; aglomeratif ve bölümleme olmak üzere iki ana kategoriye ayrılır.
      - Aglomeratif kümeleme, her bir veri noktasını tek bir küme olarak başlatır ve ardından küme sayısı istenen değere ulaşılıncaya kadar kümeleme işlemini gerçekleştirir.
      - Bölümleme kümeleme, her bir veri noktasını tek bir küme olarak başlatır ve ardından her veri noktasını ayrı bir küme olarak ele alır.

9.  [Association Rules, Market Basket Analysis, Apriori Algorithm](08AssociationRules.pdf)

    - Birliktelik kuralları, veri madenciliğinin önemli tekniklerinden biridir ve denetimsiz öğrenme sistemlerinde yerel desen keşfinin en yaygın biçimi olabilir.
    - Birçok işletme, günlük işlemlerinden büyük miktarda veri biriktirir.
    - Örneğin, marketlerin kasalarında günlük olarak büyük miktarda müşteri satın alma verisi toplanır.
    - Bu, çoğu insanın veri madenciliği sürecini anlamaya çalışırken düşündüğü sürece en yakın veri madenciliği biçimidir; yani, geniş bir veritabanında altın arama sürecine benzer.
    - Bu durumda altın, veritabanınız hakkında size bilgi veren, zaten bilmediğiniz ve muhtemelen açıkça ifade etmediğiniz bir kural olacaktır.

10. Recommendation Systems, Collaborative Filters
    - Öneri sistemleri, kullanıcıların ürünlerle etkileşimlerini kullanarak kullanıcıların ilgisini çekebilecek yeni ürünler öneren sistemlerdir.
    - Öneri sistemleri; içerik tabanlı, işbirlikçi filtreleme ve hibrit olmak üzere üç ana kategoriye ayrılır.
      - İçerik Tabanlı Öneri Sistemleri: Bu tür bir öneri sistemi, kullanıcıların geçmiş etkileşimlerini veya tercihlerini temel almak yerine, öğelerin içeriği üzerinden öneriler sunar. Bu sistemler, öğelerin içeriğini analiz ederek benzer içeriğe sahip diğer öğeleri önerir. Örneğin, bir film izlediyseniz, içerik tabanlı bir öneri sistemi benzer türdeki filmleri size önerebilir.
      - İşbirlikçi Filtreleme (Collaborative Filtering): İşbirlikçi filtreleme, kullanıcıların veya izleyicilerin geçmiş etkileşimleri ve tercihleri üzerine dayalı olarak öneriler sunar. Bu yaklaşım, kullanıcıların benzer ilgi alanlarına sahip diğer kullanıcıların tercihlerini kullanarak öneriler sunar. Örneğin, "Bu ürünü alan diğer kullanıcılar şunları da beğendi" gibi bir öneri yapabilir.
      - Hibrit Öneri Sistemleri: Hibrit öneri sistemleri, içerik tabanlı ve işbirlikçi filtreleme yöntemlerini birleştirir. Bu şekilde, hem içerik tabanlı hem de işbirlikçi filtreleme avantajlarından yararlanarak daha kesin ve kişiselleştirilmiş öneriler sunar. Hibrit öneri sistemleri, daha karmaşık bir öneri mantığı kullanarak kullanıcıları daha iyi anlamaya ve daha iyi öneriler sunmaya çalışır.
