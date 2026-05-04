# ZDI-21-798: Microsoft Exchange Server ECP Authentication Bypass Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-798
- **ZDI-CAN:** ZDI-CAN-13477
- **Date:** 2021-07-15
- **CVE:** CVE-2021-33766
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** LE XUAN TUYEN - VNPT ISC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-798/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Exchange Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the authentication of requests to web services within the ecp web application. By issuing a crafted request, an attacker can bypass authentication. An attacker can leverage this vulnerability to disclose information from the server.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-33766

## Disclosure Timeline

- 2021-04-05 - Vulnerability reported to vendor
- 2021-07-15 - Coordinated public release of advisory
