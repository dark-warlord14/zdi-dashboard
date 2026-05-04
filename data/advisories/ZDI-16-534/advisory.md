# ZDI-16-534: Microsoft Internet Explorer s_DestroyMetaCallback Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-534
- **ZDI-CAN:** ZDI-CAN-3922
- **Date:** 2016-10-11
- **CVE:** CVE-2016-3384
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 62600BCA031B9EB5CB4A74ADDDD6771E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-534/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer keeps track of linked web resources. By manipulating a document's elements, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-118

## Disclosure Timeline

- 2016-07-26 - Vulnerability reported to vendor
- 2016-10-11 - Coordinated public release of advisory
