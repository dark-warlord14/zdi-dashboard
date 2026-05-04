# ZDI-10-164: Adobe Shockwave Player Director File FFFFFF88 Record Processing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-164
- **ZDI-CAN:** ZDI-CAN-864
- **Date:** 2010-08-24
- **CVE:** CVE-2010-2876
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-164/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code responsible for parsing .dir and .dcr files. The director file format is RIFF based. While parsing an undocumented record of type 0xFFFFFFF8 the process trusts two user supplied word values when performing arithmetic to calculate a heap buffer size. By specifying large enough values an integer wrap can occur. The allocated heap buffer can later be overflowed with user supplied data. This can be leveraged by attackers to execute remote code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-20.html

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-08-24 - Coordinated public release of advisory
