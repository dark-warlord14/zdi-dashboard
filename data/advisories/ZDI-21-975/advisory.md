# ZDI-21-975: (Pwn2Own) Microsoft Windows storport Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-975
- **ZDI-CAN:** ZDI-CAN-13444
- **Date:** 2021-08-18
- **CVE:** CVE-2021-34510
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** z3r09 from Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-975/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the storport.sys driver. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34510

## Disclosure Timeline

- 2021-04-27 - Vulnerability reported to vendor
- 2021-08-18 - Coordinated public release of advisory
