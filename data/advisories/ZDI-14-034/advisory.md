# ZDI-14-034: Microsoft Internet Explorer Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-034
- **ZDI-CAN:** ZDI-CAN-2046
- **Date:** 2014-04-03
- **CVE:** CVE-2014-0313
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Omair
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-034/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of text nodes. The issue lies in the combined usage of unicode characters and CSS properties resulting in writing past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/MS14-012

## Disclosure Timeline

- 2014-01-20 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
