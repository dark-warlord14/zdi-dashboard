# ZDI-24-1486: G DATA Total Security Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1486
- **ZDI-CAN:** ZDI-CAN-22629
- **Date:** 2024-12-11
- **CVE:** CVE-2024-6871
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** G DATA
- **Affected Products:** Total Security
- **Credit:** Kolja Grassmann (cirosec GmbH)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1486/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of G DATA Total Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of autostart tasks. The issue results from incorrect permissions set on folders. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version 25.5.18.333

## Disclosure Timeline

- 2024-02-13 - Vulnerability reported to vendor
- 2024-12-11 - Coordinated public release of advisory
- 2024-12-11 - Advisory Updated
