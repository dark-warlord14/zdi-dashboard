# ZDI-11-109: (Pwn2Own) Apple Safari OfficeArtBlip Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-109
- **ZDI-CAN:** ZDI-CAN-1156
- **Date:** 2011-03-22
- **CVE:** CVE-2011-1417
- **CVSS:** 9.7
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Charlie Miller and Dion Blazakis
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-109/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari on the iPhone. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the support for parsing Office files. When handling the OfficeArtMetafileHeader the process trusts the cbSize field and performs arithmetic on it before making an allocation. As the result is not checked for overflow, the subsequent allocation can be undersized. Later when copying into this buffer, memory can be corrupted leading to arbitrary code execution under the context of the mobile user on the iPhone.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4581

## Disclosure Timeline

- 2011-03-09 - Vulnerability reported to vendor
- 2011-03-22 - Coordinated public release of advisory
