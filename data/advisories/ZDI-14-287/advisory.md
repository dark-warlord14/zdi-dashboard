# ZDI-14-287: Microsoft Windows Media Center CSyncBasePlayer Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-287
- **ZDI-CAN:** ZDI-CAN-2277
- **Date:** 2014-08-12
- **CVE:** CVE-2014-4060
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows Media Center
- **Credit:** Alisa Esage (@alisaesage)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-287/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows Media Center. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Microsoft Windows Media Center. By providing a specially crafted Office document, it is possible to corrupt certain allocations that lead to memory corruption. An attacker could leverage this to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-043

## Disclosure Timeline

- 2014-04-24 - Vulnerability reported to vendor
- 2014-08-12 - Coordinated public release of advisory
