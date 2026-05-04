# ZDI-22-496: Microsoft Azure Defender for IoT Password Change Command Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-496
- **ZDI-CAN:** ZDI-CAN-16123
- **Date:** 2022-03-09
- **CVE:** CVE-2022-23266
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure Defender for IoT
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-496/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Microsoft Azure Defender for IoT. Authentication is required to exploit this vulnerability. The specific flaw exists within the password change mechanism. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-23266

## Disclosure Timeline

- 2021-12-10 - Vulnerability reported to vendor
- 2022-03-09 - Coordinated public release of advisory
