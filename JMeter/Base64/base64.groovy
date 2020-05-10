def s1 = ''
s1 = vars.get('string_1')
String encoded = s1.bytes.encodeBase64().toString()

log.info(encoded)
 
byte[] decoded = encoded.decodeBase64()
def d1 = new String(decoded)

log.info(d1)

vars.put('decode_s',d1)
