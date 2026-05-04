# ZDI-18-293: Microsoft Windows Font Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-293
- **ZDI-CAN:** ZDI-CAN-5628
- **Date:** 2018-04-11
- **CVE:** CVE-2018-1008
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Haikuo Xie and Zheng Huang of Baidu Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-293/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the rendering of fonts. A crafted OpenType font rendered by the kernel can trigger an integer overflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute code as SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-1008

## Disclosure Timeline

- 2018-01-30 - Vulnerability reported to vendor
- 2018-04-11 - Coordinated public release of advisory
- 2018-04-11 - Advisory Updated
