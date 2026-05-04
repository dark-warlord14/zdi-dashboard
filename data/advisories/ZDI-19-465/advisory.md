# ZDI-19-465: Microsoft Windows JET Database Engine Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-465
- **ZDI-CAN:** ZDI-CAN-7866
- **Date:** 2019-05-15
- **CVE:** CVE-2019-0894
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-465/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the JET database engine. Crafted data in an MDB file can trigger an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0894

## Disclosure Timeline

- 2019-02-07 - Vulnerability reported to vendor
- 2019-05-15 - Coordinated public release of advisory
