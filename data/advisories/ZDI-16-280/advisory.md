# ZDI-16-280: (Pwn2Own) Microsoft Windows NtGdiGetEmbUFI Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-280
- **ZDI-CAN:** ZDI-CAN-3617
- **Date:** 2016-05-10
- **CVE:** CVE-2016-0174
- **CVSS:** 4.9
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Tencent PC Manager
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-280/
## Vulnerability Details

This vulnerability allows local attackers to leak sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of fonts. The issue lies in failure to sanitize values prior to copying a structure to userland. An attacker can leverage this vulnerability to leak sensitive information in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms16-062.aspx

## Disclosure Timeline

- 2016-03-12 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
