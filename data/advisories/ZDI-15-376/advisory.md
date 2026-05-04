# ZDI-15-376: IBM Tivoli Storage Manager FastBack Server Opcode 8192 Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-376
- **ZDI-CAN:** ZDI-CAN-2968
- **Date:** 2015-07-30
- **CVE:** CVE-2015-4934
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager FastBack
- **Credit:** Lola Montez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-376/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Tivoli Storage Manager FastBack. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of opcode 8192. By sending a crafted packet on TCP port 11460, an attacker is able to cause a stack buffer overflow when handling SymbolOperation debug dispatching. An attacker can use this to execute arbitrary code under the context of SYSTEM.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21961928

## Disclosure Timeline

- 2015-05-28 - Vulnerability reported to vendor
- 2015-07-30 - Coordinated public release of advisory
