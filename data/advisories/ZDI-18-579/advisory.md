# ZDI-18-579: Microsoft Windows Media Foundation Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-579
- **ZDI-CAN:** ZDI-CAN-5707
- **Date:** 2018-06-13
- **CVE:** CVE-2018-8251
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** akayn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-579/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Media Foundation libraries. By performing actions in script, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8251

## Disclosure Timeline

- 2018-03-08 - Vulnerability reported to vendor
- 2018-06-13 - Coordinated public release of advisory
- 2018-06-13 - Advisory Updated
