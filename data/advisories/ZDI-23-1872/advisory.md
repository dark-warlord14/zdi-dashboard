# ZDI-23-1872: Foxit PDF Reader Doc Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1872
- **ZDI-CAN:** ZDI-CAN-22258
- **Date:** 2023-12-20
- **CVE:** CVE-2023-51559
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1872/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Doc objects. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Foxit PDF Reader version v2023.2

## Disclosure Timeline

- 2023-10-03 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
- 2024-01-09 - Advisory Updated
