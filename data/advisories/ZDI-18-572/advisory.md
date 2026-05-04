# ZDI-18-572: (Pwn2Own) Microsoft Windows DirectX Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-572
- **ZDI-CAN:** ZDI-CAN-5816
- **Date:** 2018-06-08
- **CVE:** CVE-2018-8165
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-572/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the DirectX graphics kernel driver, dxgkrnl.sys. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8165

## Disclosure Timeline

- 2018-03-18 - Vulnerability reported to vendor
- 2018-06-08 - Coordinated public release of advisory
- 2018-06-08 - Advisory Updated
