# ZDI-15-119: IBM Tivoli Storage Manager FastBack CRYPTO_S_EncryptBufferToBuffer Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-119
- **ZDI-CAN:** ZDI-CAN-2656
- **Date:** 2015-04-08
- **CVE:** CVE-2015-0120
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager FastBack
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-119/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Storage Manager FastBack. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CRYPTO_S_EncryptBufferToBuffer function. By sending a specially crafted packet on TCP port 30051, an attacker is able to cause a stack buffer overflow. An attacker can use this to execute arbitrary code in the context of the SYSTEM.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21700549

## Disclosure Timeline

- 2015-01-08 - Vulnerability reported to vendor
- 2015-04-08 - Coordinated public release of advisory
