                                                     ###########################################
                                                     # flo.com.tr Customer Lifetime Prediction #
                                                     ###########################################


#    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    +                                                          UYGULAMA ÖNCESİ                                                                                                                                                                                                                                                                       +
#    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    +                                                                                                                                                                                                                                                                                                                                               +
#    +                  master_id                   order_channel    last_order_channel   first_order_date   last_order_date   last_order_date_online   last_order_date_offline   order_num_total_ever_online   order_num_total_ever_offline   customer_value_total_ever_offline   customer_value_total_ever_online    interested_in_categories_12   +
#    +   0  cc294636-19f0-11eb-8d74-000d3a38a36f     Android App           Offline           2020-10-30         2021-02-26           2021-02-21               2021-02-26                     4.000                         1.000                            139.990                           799.380                                      [KADIN]   +
#    +   1  f431bd5a-ab7b-11e9-a2fc-000d3a38a36f     Android App            Mobile           2017-02-08         2021-02-16           2021-02-16               2020-01-10                     19.000                        2.000                            159.970                          1853.580             [ERKEK, COCUK, KADIN, AKTIFSPOR]   +
#    +   2  69b69676-1a40-11ea-941b-000d3a38a36f     Android App       Android App           2019-11-27         2020-11-27           2020-11-27               2019-12-01                      3.000                        2.000                            189.970                           395.350                               [ERKEK, KADIN]   +
#    +   3  1854e56c-491f-11eb-806e-000d3a38a36f     Android App       Android App           2021-01-06         2021-01-17           2021-01-17               2021-01-06                      1.000                        1.000                             39.990                            81.980                          [AKTIFCOCUK, COCUK]   +
#    +   4  d6ea1074-f1f5-11e9-9346-000d3a38a36f       Desktop             Desktop           2019-08-03         2021-03-07           2021-03-07               2019-08-03                      1.000                        1.000                             49.990                           159.990                                  [AKTIFSPOR]   +
#    +                                                                                                                                                                                                                                                                                                                                               +
#    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    +                                                          UYGULAMA SONRASI                                                                                             +
#    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    +                                                                                                                                                                       +
#    +                                    Customer_ID   Recency         T  Frequency  Monetary  Exp_Sales_3_Month  Exp_Sales_6_Month  exp_average_value       CLTV Segment   +
#    +    0      cc294636-19f0-11eb-8d74-000d3a38a36f  17.00000  30.57143    5.00000 187.87400            0.97328            0.97328           193.63151 395.46844       A   +
#    +    1      f431bd5a-ab7b-11e9-a2fc-000d3a38a36f 209.85714 224.85714   21.00000  95.88333            0.98293            0.98293            96.66492 199.38340       B   +
#    +    2      69b69676-1a40-11ea-941b-000d3a38a36f  52.28571  78.85714    5.00000 117.06400            0.67031            0.67031           120.96691 170.15405       B   +
#    +    3      1854e56c-491f-11eb-806e-000d3a38a36f   1.57143  20.85714    2.00000  60.98500            0.69995            0.69995            67.31918  98.87883       D   +
#    +    4      d6ea1074-f1f5-11e9-9346-000d3a38a36f  83.14286  95.42857    2.00000 104.99000            0.39593            0.39593           114.32337  94.98500       D   +
#    +                                                                                                                                                                       +
#    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


"""
# 1. Business Problem
# 2. Data Understanding
# 3. Data Preparation
# 4. Preparation of CLTV Prediction Data Structure
# 5. BG-NBD Modeli ile Expected Number of Transaction
# 6. Gamma-Gamma Modeli ile Expected Average Profit
# 7. BG-NBD ve Gamma-Gamma Modeli ile CLTV'nin Hesaplanması
# 8. CLTV'ye göre Segmentlerin Oluşturulması
"""


# -----------------------
# - 1. Business Problem -
# -----------------------
# FLO, satış ve pazarlama faaliyetleri için roadmap oluşturmak istemektedir.
# Şirketin orta-uzun vaeli plan yapabilmesi için var olan müşterilerin
# gelecekte şirkete sağlayacakları potansiyel değerin tahmin edilmesi gerekmektedeir.



# -------------------------
# - 2. Data Understanding -
# -------------------------

# gerekli kütüphane, fonksiyon importları ve bazı görsel ayarlamalar
# pip install lifetimes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
pd.set_option("display.float_format", lambda x : "%.5f" % x)
pd.set_option('display.max_colwidth', None)



# flo_data_20k.csv veri setinin projeye daihl edilmesi
def load_dataset():
    data = pd.read_csv("data_sets/flo_data_20k.csv")
    return data

df_ = load_dataset()
df = df_.copy()


def check_dataframe(dataframe, head=10):
    """
    Bu fonksiyonun görevi, ilgili DataFrame'in temel istatistiksel bilgileri
    ve yapısal özellikleri hakkında özet bir rapor oluşturmaktır.

    -> Bu fonksiyon, veri setinin yapısını anlamak ve olası problemleri
       belirlemek için kullanılır.

    Parameters
    ----------
    dataframe : dataframe
                Raporu oluşturulmak istenilen veri seti.
    head : int
           Baştan kaç satır gözlem birimi gösterileceği bilgisi.
           Varsayılan değeri 10'dur.
    """
    print("###################################")
    print(f"#### İlk {head} Gözlem Birimi ####")
    print("###################################")
    print(dataframe.head(head), "\n\n")

    print("###################################")
    print("###### Veri Seti Boyut Bilgisi ####")
    print("###################################")
    print(dataframe.shape, "\n\n")

    print("###################################")
    print("######## Değişken İsimleri ########")
    print("###################################")
    print(dataframe.columns, "\n\n")

    print("###################################")
    print("####### Eksik Değer Var mı? #######")
    print("###################################")
    print(dataframe.isnull().values.any(), "\n\n")

    print("###################################")
    print("##### Betimsel İstatistikler ######")
    print("###################################")
    print(dataframe.describe().T, "\n\n")

    print("###################################")
    print("### Veri Seti Hakkında Bilgiler ###")
    print("###################################")
    print(dataframe.info())

check_dataframe(dataframe=df)


def grab_col_names(dataframe,
                   category_thresholds=10,
                   cardinal_thresholds=20,
                   numumeric_thresholds=20,
                   columns=False,
                   plot=False):
    """
    Bu fonksiyonun görevi, veri setindeki değişkenleri analiz ederek
    kategorik, kardinal ve numerik değişken isimlerini raporlamaktır.

    * Değişken analizi için ilgili değişkenin eşsiz sınıf sayısı ve
      tip bilgisi baz alınmaktadır.

    Parameters
    ----------
    dataframe: dataframe
         Değişken analizi yapılmak istenilen veri seti.
    category_thresholds: int, float
         Kategorik değişkenler için sınıf eşik değeri.
    cardinal_thresholds: int,float
         Kategorik görünümlü kardinal değişkenler için sınıf eşik değeri.
    numumeric_thresholds: int,float
         Sayısal değişkenler için sınıf eşik değeri.
    columns: bool
         True olması durumunda değişken isimlerini return eder.
    plot: bool
         True olması durumunda değişkenler görselleştirilir.

    Returns
    -------
    cat_cols: list
         Kategorik değişken listesi
    cat_but_car: list
         Kardinal görünümlü kategorik değişken listesi
    num_cols: list
         Numerik değişken listesi
    """

    # Kategorik değişken isimlerinin filtrelenemsi
    cat_cols = [col for col in dataframe.columns if dataframe[col].nunique() < category_thresholds and
                                                    dataframe[col].dtypes in ["category", "object", "bool"]]

    # Numerik görünümlü ancak kategorik olan değişken isimlerinin filtrelenemsi
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < numumeric_thresholds and
                                                       dataframe[col].dtypes in ["int", "float"]]

    # Kategorik değişkenlerin birleştirilmesi
    cat_cols += num_but_cat

    # plot argümanı True ise ilgili değişkenler betimlenir ve görselleştirilir.
    if plot:
        for cat in cat_cols:
            print(dataframe[cat].value_counts())
            print("###########################")

            sns.countplot(x=dataframe[cat], data=dataframe)
            plt.show(block=True)

    # Kardinal değişken isimlerinin filtrelenmesi
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > cardinal_thresholds and
                                                       dataframe[col].dtypes in ["category", "object"]]

    # Sayısal değişken isimlerinin filtrelenemsi
    num_cols = [col for col in dataframe.columns if dataframe[col].nunique() > numumeric_thresholds and
                                                    dataframe[col].dtypes in ["int", "float"]]

    # plot argümanı True ise ilgili değişkenler betimlenir ve görselleştirilir.
    if plot:
        for num in num_cols:
            print(dataframe[num].describe().T)
            print("###########################")

            dataframe[num].hist()
            plt.show(block=True)

    # Analizin raporlanması
    report = {
        "TİP" : ["Kategorik", "Kardinal", "Numerik"],
        "ADET" : [len(cat_cols), len(cat_but_car), len(num_cols)],
        "LİSTE" : [cat_cols, cat_but_car, num_cols]
    }

    report = pd.DataFrame(report)
    print(report)

    if columns:
        return cat_cols, cat_but_car, num_cols


grab_col_names(dataframe=df)


# -----------------------
# - 3. Data Preparation -
# -----------------------

def outlier_thresholds(dataframe, variable, q1=0.25, q3=0.75):
    """
        Bu fonksiyonun görevi kendisine girilen değişkenin
        eşik değerlerini hesaplamaktır.

        -> Bu işlem için IQR yöntemi tercih edilmektedir.

        Parameters
        ----------
        dataframe : dataframe
                    Aykırı değer eşikleri hesaplanacak veri seti.
        variable : str
                   Aykırı değer eşikleri hesaplanacak değişkenin adı.
        q1 : int, float
             Alt çeyreklik (1. çeyreklik) için yüzdelik değer.
             Varsayılan değer 0.25
        q3 : int, float
             Üst çeyreklik (3. çeyreklik) için yüzdelik değer.
             Varsayılan değer 0.75

        Returns
        -------
        up_limit : numpy.float64
            Belirlenen üst limit.
        low_limit : numpy.float64
            Belirlene alt limit.
        """
    quartile1 = dataframe[variable].quantile(q1)
    quartile3 = dataframe[variable].quantile(q3)
    iqr = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * iqr
    low_limit = quartile1 - 1.5 * iqr
    return low_limit, up_limit


# CLTV değeri hesaplanırken frequency değeri int olması gerekmektedir.
# Bu sebeple alt ve üst limitleri round() ile yuvarlıyoruz.
def replace_with_thresholds(dataframe, variable):
    """
    Bu fonksiyonun görevi ilgili değişkendeki aykırı değerleri
    alt ve üst limit değerleriyle değiştirmektir.

    Parameters
    ----------
    dataframe : dataframe
                Aykırı değerlerin değiştirileceği veri seti.
    variable : int
               Aykırı değerleri değiştirilecek değişkenin adı.

    Notes
    -----
    - Bu fonksiyon, "outlier_thresholds" fonksiyonunu kullanarak
      alt ve üst sınır eşik değerlerini hesaplar.
    - Aykırı değerler, alt sınırın yuvarlanmış değeri (round(low_limit))
      veya üst sınırın yuvarlanmış değeri (round(up_limit)) ile değiştirilir.
    """
    low_limit, up_limit = outlier_thresholds(dataframe, variable, q1=0.01, q3=0.99)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = round(low_limit)
    dataframe.loc[(dataframe[variable] > up_limit), variable] = round(up_limit)


df.describe().T # Veri setinde aykırı değerler söz konusu.
                # Kuracak olduğumuz modeller istatistiksel, olasılıksal
                # modelelr olduğundan dolayı yapılacak olan genellemeler
                # bazı sapmalara sebep olacaktır. Bu yüzden aykırı değerleri
                # baskılama işlemi uygulayacağız.


# Veri setindeki sayısal tipteki değişken isimlerini filtreliyoruz.
numerical_columns = [col for col in df.columns if df[col].nunique() > 20 and
                                                  df[col].dtypes in ["int", "float"]]

# Sayısal değişkenlerdeki aykırlıkları baskılıyoruz.
for col in numerical_columns:
    replace_with_thresholds(df, col)


# Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
date_columns = df.columns[df.columns.str.contains("date")]
df[date_columns] = df[date_columns].apply(pd.to_datetime)

# Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Herbir müşterinin toplam alışveriş sayısı ve toplam harcama tutarları için yeni değişkenler oluşturuyoruz.
df["total_order_num"] = df["order_num_total_ever_online"] \
                        + df["order_num_total_ever_offline"]

df["total_price"] = df["customer_value_total_ever_online"] \
                    + df["customer_value_total_ever_offline"]



# ----------------------------------------------------
# - 4. Preparation of CLTV Prediction Data Structure -
# ----------------------------------------------------

# flo_data_20k.csv veri setimizi BG-NBD ve Gamma-Gamma modellerinin
# bizden istediği metriklere cevap verecek bir formata çeviriyoruz.

# Recency -> Son satın alma üzerinden geçen zaman. Haftalık. = (son satın alma tarihi - ilk satın alma tarihi) / 7
# T -> Müşteri yaşı. Haftalık. (analiz tarihi - ilk satın alma tarihi) / 7
# Frequency -> Tekrar eden toplam satın alma sayısı. = (Frequency > 1)
# Monetary -> Satın alma başına ortalama kazanç. (monetary / frequency)

print(df["last_order_date"].max()) # 2021-05-30
analysis_date = dt.datetime(2021, 6, 1)

###
# CLTV_Precition veri setinin hazırlanması
###

# Veri setimizi oluşturuyoruz.
cltv_prediction = pd.DataFrame()

# Müşteri ID bilgilerini ekliyoruz.
cltv_prediction["Customer_ID"] = df["master_id"]

# Recency metriğini hesaplıyoruz.
cltv_prediction["Recency"] = (df["last_order_date"] - \
                              df["first_order_date"]).astype("timedelta64[D]") / 7

# T metriğini hesaplıyoruz.
cltv_prediction["T"] = (analysis_date - \
                        df["first_order_date"]).astype("timedelta64[D]") / 7

# Frequency Metriğini hesaplıyoruz.
cltv_prediction["Frequency"] = df["total_order_num"]
cltv_prediction = cltv_prediction[cltv_prediction["Frequency"] > 1]

# Monetary metriğinin hesaplanması
cltv_prediction["Monetary"] = df["total_price"] / df["total_order_num"]


cltv_prediction.describe().T # Recency ve T metriklerinde min = 0
                             # olması durumu bizim için yeni bir müşteri
                             # olduğunu göstermetkedir. Bu sebeple bu müşterilerin
                             # geçmiş davranışları olmadığı için veri setinin dışında
                             # bırakıyoruz.

cltv_prediction = cltv_prediction[cltv_prediction["Recency"] > 0]
cltv_prediction = cltv_prediction[cltv_prediction["T"] > 0]


# -------------------------------------------------------
# - 5. BG-NBD Modeli ile Expected Number of Transaction -
# -------------------------------------------------------

bgf = BetaGeoFitter(penalizer_coef=0.001)

bgf.fit(cltv_prediction["Frequency"],
        cltv_prediction["Recency"],
        cltv_prediction["T"])


# 3 ay içerisinde en çok satın alma beklediğimiz 10 müşteri kimdir?
bgf.conditional_expected_number_of_purchases_up_to_time(4 * 3,
                                                        cltv_prediction["Frequency"],
                                                        cltv_prediction["Recency"],
                                                        cltv_prediction["T"]).sort_values(ascending=False).head(10)


# 3 ay içerisindeki beklenen satın alma davranışlarının veri setine dahil edilmesi
cltv_prediction["Exp_Sales_3_Month"] = bgf.conditional_expected_number_of_purchases_up_to_time(4*3,
                                                                                               cltv_prediction["Frequency"],
                                                                                               cltv_prediction["Recency"],
                                                                                               cltv_prediction["T"])


# 6 ay içerisindeki beklenen satın alma davranışlarının veri setine dahil edilmesi
cltv_prediction["Exp_Sales_6_Month"] = bgf.conditional_expected_number_of_purchases_up_to_time(4*3,
                                                                                               cltv_prediction["Frequency"],
                                                                                               cltv_prediction["Recency"],
                                                                                               cltv_prediction["T"])


# 6 ay içerisinde toplam ne kadar satın alma olacak?
# Bu çok değerli bir çıktıdır birçok iş birimini destekleyeceek bir çıktıdır.
bgf.conditional_expected_number_of_purchases_up_to_time(4 * 3,
                                                        cltv_prediction["Frequency"],
                                                        cltv_prediction["Recency"],
                                                        cltv_prediction["T"]).sum()




# Tahmin Sonuçlarının Değerlendirilmesi
plot_period_transactions(bgf)
plt.show()


# -----------------------------------------------------
# - 6. Gamma-Gamma Modeli ile Expected Average Profit -
# -----------------------------------------------------

ggf = GammaGammaFitter(penalizer_coef=0.01)

ggf.fit(cltv_prediction["Frequency"],
        cltv_prediction["Monetary"])


# Müşterilerin ortalama bırakacakları parasal değeri veri setine dahil ediyoruz.
cltv_prediction["exp_average_value "] = ggf.conditional_expected_average_profit(cltv_prediction["Frequency"],
                                                                                cltv_prediction["Monetary"])


# -------------------------------------------------------------
# - 7. BG-NBD ve Gamma-Gamma Modeli ile CLTV'nin Hesaplanması -
# -------------------------------------------------------------

# 6 Aylık CLTV değerlerini hesaplayınız
cltv_prediction["CLTV"] = ggf.customer_lifetime_value(bgf,
                                                      cltv_prediction["Frequency"],
                                                      cltv_prediction["Recency"],
                                                      cltv_prediction["T"],
                                                      cltv_prediction["Monetary"],
                                                     time=6, # 6 aylık
                                                     freq="W", # T'nin frekans bilgisi
                                                     discount_rate=0.01)

cltv_prediction.sort_values(by="CLTV", ascending=False)

# ----------------------------------------------
# - 8. CLTV'ye göre Segmentlerin Oluşturulması -
# ----------------------------------------------

cltv_prediction["Segment"] = pd.qcut(cltv_prediction["CLTV"], 4, labels=["D", "C", "B", "A"])

# Analiz sonuçlarının çıktı olarak bastırılması
print(cltv_prediction)

# CLTV Prediction analiz sonuçlarının Excel formatında dış ortama aktarılması
CLTV_PREDİCTİON_Analysis = pd.DataFrame(cltv_prediction)

CLTV_PREDİCTİON_Analysis.to_excel("CLTV_PREDİCTİON_Analysis.xlsx")



