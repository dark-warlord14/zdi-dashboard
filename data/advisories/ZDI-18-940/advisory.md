# ZDI-18-940: Microsoft Windows LNK File Uninitialized Pointer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-940
- **ZDI-CAN:** ZDI-CAN-6194
- **Date:** 2018-08-14
- **CVE:** CVE-2018-8346
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Lucas Leong (@wmliang)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-940/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of .LNK files. Crafted data in a .LNK file can trigger access to a pointer prior to initialization. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8346

## Disclosure Timeline

- 2018-05-08 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
