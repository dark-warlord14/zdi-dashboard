# ZDI-23-1541: (Pwn2Own) Microsoft Teams Incorrect Privilege Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1541
- **ZDI-CAN:** ZDI-CAN-20751
- **Date:** 2023-10-11
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** vcslab of Team Viettel (@vcslab)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1541/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Microsoft Teams. An attacker must first obtain the ability to execute script within the application window in order to exploit this vulnerability. The specific flaw exists within the processing of global settings. The issue results from an incorrect privilege assignment. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/acknowledgement/online

## Disclosure Timeline

- 2023-04-05 - Vulnerability reported to vendor
- 2023-10-11 - Coordinated public release of advisory
