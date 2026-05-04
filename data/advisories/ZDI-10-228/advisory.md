# ZDI-10-228: Adobe Shockwave Player Director File SetVertexArray Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-228
- **ZDI-CAN:** ZDI-CAN-894
- **Date:** 2010-10-29
- **CVE:** CVE-2010-4090
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-228/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within code responsible for parsing Director files (.dir). When handling the 3D record type 0xFFFFFF89. The module trusts size fields within a substructure and can be forced to make a faulty memory allocation. This can be abused by a remote attacker to execute arbitrary code under the context of the currently logged-in user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-25.html

## Disclosure Timeline

- 2010-09-24 - Vulnerability reported to vendor
- 2010-10-29 - Coordinated public release of advisory
