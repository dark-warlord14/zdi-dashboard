# ZDI-24-1032: NI FlexLogger Redis Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1032
- **ZDI-CAN:** ZDI-CAN-21802
- **Date:** 2024-07-30
- **CVE:** CVE-2024-6121
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NI
- **Affected Products:** FlexLogger
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1032/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of NI FlexLogger. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from the use of a vulnerable version of Redis. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/ni-systemlink-server-ships-out-of-date-redis-version.html

## Disclosure Timeline

- 2024-01-23 - Vulnerability reported to vendor
- 2024-07-30 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
