# ZDI-17-471: (Pwn2Own) Microsoft Windows win32kfull CopyOutputString Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-471
- **ZDI-CAN:** ZDI-CAN-4576
- **Date:** 2017-07-11
- **CVE:** CVE-2017-8486
- **CVSS:** 2.1
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** pgboy and zhong_sf of Qihoo 360Vulcan Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-471/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the win32kfull!CopyOutputString function. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privilege to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8486

## Disclosure Timeline

- 2017-03-16 - Vulnerability reported to vendor
- 2017-07-11 - Coordinated public release of advisory
