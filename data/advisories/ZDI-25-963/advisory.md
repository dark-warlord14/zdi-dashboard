# ZDI-25-963: Veeam Agent for Microsoft Windows Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-963
- **ZDI-CAN:** ZDI-CAN-27061
- **Date:** 2025-10-27
- **CVE:** CVE-2025-48982
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Veeam
- **Affected Products:** Veeam Agent for Microsoft Windows
- **Credit:** Zeze and Sharkkcode with TeamT5
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-963/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Veeam Agent for Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. User interaction on the part of an administrator is needed additionally. The specific flaw exists within the restore functionality. By creating a junction, an attacker can abuse the service to create arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Veeam has issued an update to correct this vulnerability. More details can be found at: https://www.veeam.com/kb4771

## Disclosure Timeline

- 2025-06-10 - Vulnerability reported to vendor
- 2025-10-27 - Coordinated public release of advisory
- 2025-10-27 - Advisory Updated
