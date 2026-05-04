# ZDI-22-495: Microsoft Azure Defender for IoT Password Change Command Injection Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-495
- **ZDI-CAN:** ZDI-CAN-15761
- **Date:** 2022-03-09
- **CVE:** CVE-2022-23265
- **CVSS:** 4.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure Defender for IoT
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-495/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Azure Defender for IoT. An attacker must first obtain the ability to execute code as the www-data user on the target system in order to exploit this vulnerability. The specific flaw exists within the password change mechanism. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-23265

## Disclosure Timeline

- 2021-12-10 - Vulnerability reported to vendor
- 2022-03-09 - Coordinated public release of advisory
