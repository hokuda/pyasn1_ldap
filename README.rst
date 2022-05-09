pyasn1_ldap
===========

*Python module to decode ASN1 stream of LDAP message using pyasn1*

Install
-------

::
   
   pip install pyasn1_ldap

Usage
-----

::

   #!/usr/bin/python
   from pyasn1.codec.ber.decoder import decode as ber_decoder
   from pyasn1_ldap import rfc4511
   
   hex_text = '302f020101602a020103041a41646d696e6973747261746f72404558414d504c45322e434f4d800950617373773072642e'
   substrate = bytes.fromhex(hex_text)
   ldap_message, rest = ber_decoder(substrate, asn1Spec=rfc4511.LDAPMessage())
   print(ldap_message)
   
   # the output should be:
   # LDAPMessage:
   #  messageID=1
   #  protocolOp=Choice:
   #   bindRequest=BindRequest:
   #    version=3
   #    name=Administrator@EXAMPLE2.COM
   #    authentication=AuthenticationChoice:
   #     simple=Passw0rd.

Thanks
------

- Thanks to `pyasn1 <https://github.com/etingof/pyasn1>`_ for implementing ASN.1 types and codecs.
- Thanks to `asn1ate <https://github.com/kimgr/asn1ate>`_ for implementing ASN.1 translation library.
