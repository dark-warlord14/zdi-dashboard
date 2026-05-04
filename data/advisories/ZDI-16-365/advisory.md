# ZDI-16-365: Microsoft Internet Explorer s_DestroyLinkCallback Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-365
- **ZDI-CAN:** ZDI-CAN-3666
- **Date:** 2016-06-15
- **CVE:** CVE-2016-0200
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 62600BCA031B9EB5CB4A74ADDDD6771E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-365/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer keeps track of linked web resources. By manipulating a document's elements, an attacker can cause Internet Explorer to use an array address after the array has been relocated elsewhere in memory. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-063

## Disclosure Timeline

- 2016-04-07 - Vulnerability reported to vendor
- 2016-06-15 - Coordinated public release of advisory
