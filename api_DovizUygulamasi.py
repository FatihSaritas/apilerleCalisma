import requests
import json

api_key = '78fe4b69f56d3a623ba570f3'
api_url = 'https://v6.exchangerate-api.com/v6/78fe4b69f56d3a623ba570f3/latest/'

bozulan_doviz = input('Bozulan Döviz Türü Nedir ?: ') #USD 
alinan_doviz = input('Alının Döviz türü: ') #TRY
miktar = input(f'Nekadar {bozulan_doviz} , Bozdurucaksınız: ')

sonuc = requests.get(api_url + bozulan_doviz)
#url bilgisine hangi para birimini dönüştürüceğimizi bildiriyoruz
sonuc_json = json.loads(sonuc.text)
#Burada api içerisinden gelen dönüşüm bilglerini json formatına çeviriyoruz
#verdiğimiz değerlerle cevaplarla işlemleri yapabilmek için


#print(sonuc_json['conversion_rates'][alinan_doviz])
#Burada ise sonucjson üzerinden para birimleri dönüşüm kısmı olan conversion_rates 'e ulaşıp tanımladıgımız
#inputt TRY yazdıgımız TL bilgisini veriyoruz.

print(f'{miktar}{bozulan_doviz} =',sonuc_json['conversion_rates'][alinan_doviz],f'{alinan_doviz} miktarına eşittir.')