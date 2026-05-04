# ZDI-10-012: Microsoft Internet Explorer Baseline Tag Rendering Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-012
- **ZDI-CAN:** ZDI-CAN-502
- **Date:** 2010-01-21
- **CVE:** CVE-2010-0246
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Sam Thomas of eshu.co.uk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-012/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that an attacker must coerce a victim to visit a malicious page. The specific flaw exists due to the application rendering intertwined strike and center tags containing an element that manipulates the font baseline such as 'sub' or 'sup'. When this element pointer is removed the application will later dereference it even though it has been freed. Successful exploitation can lead to arbitrary code execution under the context of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-002.mspx

## Disclosure Timeline

- 2009-07-16 - Vulnerability reported to vendor
- 2010-01-21 - Coordinated public release of advisory
