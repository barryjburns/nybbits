MODULUS := 4096
CONFIG := openssl.cnf
CERT_EXT := crt
#CACERT := certs/ca.cert.pem
CACERT := pub/nybbits.$(CERT_EXT)
CAKEY := private/ca.key
EXTENSIONS := usr_cert
SSL_BASE := /etc/ssl
CERTS_DIR := $(SSL_BASE)/certs
CACERT_HASH := $(shell openssl x509 -noout -hash -in "$(CACERT)")
CACERT_SUB_CN := $(shell openssl x509 -noout -subject -in "$(CACERT)" | sed -n -e 's|.*/CN=\(.*\)|\1|p')
CACERT_CANON_FN := $(shell echo "$(CACERT_SUB_CN)" | sed -e 's/ /_/g').$(CERT_EXT)
CACERT_SUB_DETAIL := $(shell openssl x509 -noout -subject -in pub/nybbits.crt | sed -e 's/subject= //' | sed -n -e 's|/\([^=]*\)=\([^/=]*\)|\1: \2\n|pg')

help:
	@echo 'Use "make file.txt" to make the whole assortment of files (RSA key in'
	@echo '*.key, certificate in *.crt, PKCS12 in *.p12) and verify the key.'
	@echo
	@echo 'Use "make file.crl" to generate the current CRL. You are responsible'
	@echo 'for making sure it gets to the right place (web server).'
	@echo
	@echo 'Use "make trusted" to install this CA certificate to the system'
	@echo 'trusted root CA store.'

trusted:
	rm -f "$(CERTS_DIR)/$(CACERT_CANON_FN)" "$(CERTS_DIR)/$(CACERT_HASH).0"
	install $(CACERT) "$(CERTS_DIR)/$(CACERT_CANON_FN)"
	ln -s "$(CERTS_DIR)/$(CACERT_CANON_FN)" "$(CERTS_DIR)/$(CACERT_HASH).0"
	openssl verify -CApath "$(CERTS_DIR)" "$(CACERT)"

%.crl:
	openssl ca -config $(CONFIG) -gencrl -out -cert $(CACERT) -key $(CAKEY) -out $@.pem

%.txt:	%.crt %.p12
	openssl x509 -in $< -text -noout > $@
	@cat $@

%.p12:	%.crt
	openssl pkcs12 -export -in $< -inkey $(@:.p12=.key) -out $@

%.crt:	%.csr
	openssl ca -config $(CONFIG) -in $< -cert $(CACERT) -key $(CAKEY) -out $@ 

%.csr:	%.key
	openssl req -new -key $< -out $@ -days 365 -sha256 -config $(CONFIG) -extensions $(EXTENSIONS)

%.key:	
	openssl genrsa -out $@ $(MODULUS) -config $(CONFIG)


.PHONY:	help trusted
.PRECIOUS:	%.key %.crt %.p12 %.csr

#keytool -importcert -file ldap.nybbits.com.pem -keystore nybbits.ks -storepass k0rNf14k3
