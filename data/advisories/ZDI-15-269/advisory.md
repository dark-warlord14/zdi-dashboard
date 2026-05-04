# ZDI-15-269: IBM Tivoli Storage Manager FastBack Server Opcode 1332 Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-269
- **ZDI-CAN:** ZDI-CAN-2807
- **Date:** 2015-06-30
- **CVE:** CVE-2015-1942
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager FastBack
- **Credit:** Lola Montez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-269/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Tivoli Storage Manager FastBack. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of opcode 1332. By sending a crafted packet on TCP port 11460, an attacker can force the process to write arbitrary data to an existing file on the system. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21959398

## Disclosure Timeline

- 2015-04-23 - Vulnerability reported to vendor
- 2015-06-30 - Coordinated public release of advisory
