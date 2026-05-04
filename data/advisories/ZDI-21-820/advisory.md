# ZDI-21-820: (Pwn2Own) Microsoft Windows storport Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-820
- **ZDI-CAN:** ZDI-CAN-13589
- **Date:** 2021-07-19
- **CVE:** CVE-2021-34512
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** nghiadt12, huyna of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-820/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the storport.sys driver. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/en-us/vulnerability/CVE-2021-34512

## Disclosure Timeline

- 2021-04-27 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
