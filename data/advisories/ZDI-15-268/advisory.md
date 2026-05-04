# ZDI-15-268: IBM Tivoli Storage Manager FastBack Server Opcode 1329 Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-268
- **ZDI-CAN:** ZDI-CAN-2806
- **Date:** 2015-06-30
- **CVE:** CVE-2015-1941
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager FastBack
- **Credit:** Lola Montez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-268/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of IBM Tivoli Storage Manager FastBack. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of opcode 1329. By sending a crafted packet on TCP port 11460, an attacker can force the process to read an arbitrary file and return the contents. An attacker can use this to disclose information under the context of SYSTEM.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21959398

## Disclosure Timeline

- 2015-04-23 - Vulnerability reported to vendor
- 2015-06-30 - Coordinated public release of advisory
