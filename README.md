Henry Gustafsson, Y2 Strategia peli projekti.

Y2project kansio sisältää kaikki koodin tiedostot (.py), pelin tallennus tiedostot (.json), README (.md) ja suunnitelmat/dokumentit (.pdf). Ohjelmassa käytetään PyQt5, math, json ja sys kirjastoja, mutta mitään näistä ei tarvitse asentaa.

Ohjelma käynnistetään main.py moduulissa. Aluksi kysytään halutaanko luoda uusi peli 'n' tai ladata aiempi peli tallennus tiedostoista 'l'. Jos ladataan peli tallennuksesta, kysytään tallennus tiedoston nimeä, tämä kirjoitetaan ilman '.json' päätettä. Jos luodaan uusi peli, kysytään seuraavaksi onko pelaajia yksi vai kaksi.
Jos pelaajia on yksi, on toisena pelaajana botti. Kirjoitetaan pelaajien nimet seuraavaksi. Tämän jälkeen peli käynnistyy ja aukeaa peli-ikkuna. Ikkunassa lukee pelaajien ja hahmojen tiedot sekä mitä pitää tehdä. Peliä voidaan pelata klikkaamalla omalla vuorolla omaa hahmoa ja klikkaamalla uudestaan viereistä ruutua jos halutaan liikkua. Tai voit myös klikata omaa hahmoa ja vastustajan hahmoa jolloin teet vahinkoa vastustajaan. Pelin oikeassa reunassa näkyy ajankohtainen tieto mitä kukin on tehnyt viime toiminnosta. Tehtäväsi on tuhota kaikki vastustajan hahmot kentältä. Jos pelaaja tuhoaa hahmon, saa hän pelata uuden vuoron heti. Voit myös tallentaa pelin painamalla savegame nappia. Tämän jälkeen aukeaa ikkuna johon voit kirjoittaa tallennustiedoston nimen ilman '.json' päätettä. Voit lopettaa pelin sulkemalla peli-ikkunan painamalla punaista raksia oikeassa yläkulmassa.

Peliä voidaan pelata komentoriviltä jolloin tapahtumat näkyvät printtinä. Tai voit pelata graafisen liittymän kautta. Pelikentän ja hahmojen ominaisuuksia voi helposti muokata Main ja Character luokissa.