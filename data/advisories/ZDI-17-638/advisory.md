# ZDI-17-638: Microsoft Windows Jet Engine Library Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-638
- **ZDI-CAN:** ZDI-CAN-4405
- **Date:** 2017-08-08
- **CVE:** CVE-2017-0250
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Zhou Yu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-638/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Microsoft Jet Engine Library. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0250

## Disclosure Timeline

- 2017-01-05 - Vulnerability reported to vendor
- 2017-08-08 - Coordinated public release of advisory
