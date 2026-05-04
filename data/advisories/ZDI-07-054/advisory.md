# ZDI-07-054: IBM Tivoli Storage Manager Express CAD Service Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-054
- **ZDI-CAN:** ZDI-CAN-188
- **Date:** 2007-09-24
- **CVE:** CVE-2007-4880
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** IBM, IBM
- **Affected Products:** Tivoli Storage Manager V5
- **Credit:** Sebastian Apelt (webmaster@buzzworld.org)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-054/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Tivoli Storage Manager Express. Authentication is not required to exploit this vulnerability. The specific flaw exists in the dsmcad.exe process bound by default on TCP port 1581. During HTTP header parsing, a host parameter of sufficient length will trigger an overflow through a call to vswprintf(). The call overflows into imported function pointers which are later called. Exploitation of this issue can result in arbitrary code execution.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-1.ibm.com/support/docview.wss?uid=swg21268775

## Disclosure Timeline

- 2007-05-22 - Vulnerability reported to vendor
- 2007-09-24 - Coordinated public release of advisory
