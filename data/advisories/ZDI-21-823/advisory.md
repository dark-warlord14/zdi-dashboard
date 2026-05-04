# ZDI-21-823: (Pwn2Own) Microsoft Windows AppX Deployment Service Race Condition Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-823
- **ZDI-CAN:** ZDI-CAN-13600
- **Date:** 2021-07-19
- **CVE:** CVE-2021-34462
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Tao Yan ( @Ga1ois ) of Palo Alto Networks
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-823/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppX Deployment Service. The issue results from the lack of proper validation of a user-supplied link prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34462

## Disclosure Timeline

- 2021-04-27 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
