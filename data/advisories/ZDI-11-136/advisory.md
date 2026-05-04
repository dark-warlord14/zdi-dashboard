# ZDI-11-136: IBM Tivoli Directory Server ibmslapd.exe SASL Bind Request Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-136
- **ZDI-CAN:** ZDI-CAN-1022
- **Date:** 2011-04-18
- **CVE:** CVE-2011-1206
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Directory Server
- **Credit:** Francis Provencher for Protek Research Lab's
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-136/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Tivoli Directory Server. Authentication is not required to exploit this vulnerability. The specific flaw exists in how ibmslapd.exe handles LDAP CRAM-MD5 packets. ibmslapd.exe listens by default on port TCP 389. When the process receives an LDAP CRAM-MD5 packet, it uses libibmldap.dll to handle the allocation of a buffer for the packet data. A specially crafted packet can cause the ber_get_int function to allocate a buffer that is too small to fit the packet data, causing a subsequent stack-based buffer overflow. This can be leveraged by a remote attacker to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www-304.ibm.com/support/docview.wss?uid=swg21496117

## Disclosure Timeline

- 2011-02-17 - Vulnerability reported to vendor
- 2011-04-18 - Coordinated public release of advisory
