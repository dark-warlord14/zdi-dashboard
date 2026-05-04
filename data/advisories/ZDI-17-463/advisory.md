# ZDI-17-463: (Pwn2Own) Microsoft Windows basicrender WarpKMEscape Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-463
- **ZDI-CAN:** ZDI-CAN-4603
- **Date:** 2017-07-10
- **CVE:** CVE-2017-8575
- **CVSS:** 2.1
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** pgboy of Qihoo 360Vulcan Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-463/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the basicrender!WarpKMEscape function. When called with certain parameters, this function will return sensitive data to the caller. An attacker can leverage this in conjunction with other vulnerabilities to escalate privilege to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8575

## Disclosure Timeline

- 2017-03-16 - Vulnerability reported to vendor
- 2017-07-10 - Coordinated public release of advisory
