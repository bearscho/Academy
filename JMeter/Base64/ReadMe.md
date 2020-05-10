
JSR223(Groovy) 를 통한 Base64 Encode/Decode


def s1 = ''
s1 = vars.get('string_1')
String encoded = s1.bytes.encodeBase64().toString()

log.info(encoded)
 
byte[] decoded = encoded.decodeBase64()
def d1 = new String(decoded)

log.info(d1)

vars.put('decode_s',d1)



https://docs.google.com/document/d/e/2PACX-1vTABOGZS8_VWEbtUwyWW_T3hbfVllUskqMoxoCA7SXqVBY7vETbHWMnYmiH_TgNQxX82817Kn88bEPn/pub

