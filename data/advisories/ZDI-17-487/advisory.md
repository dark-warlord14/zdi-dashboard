# ZDI-17-487: (Pwn2Own) Microsoft Windows NtUserLinkDpiCursor Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-487
- **ZDI-CAN:** ZDI-CAN-4612
- **Date:** 2017-07-12
- **CVE:** CVE-2017-8465
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Liang Yin of Tencent PC manager team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-487/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of linked cursor objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privilege to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8465

## Disclosure Timeline

- 2017-03-16 - Vulnerability reported to vendor
- 2017-07-12 - Coordinated public release of advisory
