# ZDI-15-329: Microsoft Internet Explorer CTableLayout Out-of-Bounds Memory Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-329
- **ZDI-CAN:** ZDI-CAN-2792
- **Date:** 2015-07-14
- **CVE:** CVE-2015-2403
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** ca0nguyen
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-329/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CTableLayout objects. By manipulating a document's elements an attacker can force out-of-bounds reads and writes. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-065

## Disclosure Timeline

- 2015-03-03 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
