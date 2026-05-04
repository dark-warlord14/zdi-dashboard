# ZDI-13-213: IBM Lotus iNotes ActiveX Control Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-213
- **ZDI-CAN:** ZDI-CAN-1971
- **Date:** 2013-09-11
- **CVE:** CVE-2013-3027
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** Lotus iNotes
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-213/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus iNotes. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of user provided input in ActiveX controls. An integer overflow exists which leads to a heap buffer overflow. An attacker could use this vulnerability to execute arbitrary code in the context of the user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21645503

## Disclosure Timeline

- 2013-09-04 - Vulnerability reported to vendor
- 2013-09-11 - Coordinated public release of advisory
