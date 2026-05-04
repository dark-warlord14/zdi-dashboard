# ZDI-25-806: (0Day) AOMEI Backupper Workstation Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-806
- **ZDI-CAN:** ZDI-CAN-27059
- **Date:** 2025-08-06
- **CVE:** CVE-2025-8612
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** AOMEI
- **Affected Products:** Backupper Workstation
- **Credit:** Zeze and Sharkkcode with TeamT5
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-806/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of AOMEI Backupper Workstation. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. User interaction on the part of an administrator is needed additionally. The specific flaw exists within the restore functionality. By creating a junction, an attacker can abuse the service to create arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

03/04/25 – ZDI contacted the vendor’s support team to request their PSIRT contacts 04/11/25 – ZDI asked for updates 07/29/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-07-29 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated
