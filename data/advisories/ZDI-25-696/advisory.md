# ZDI-25-696: Avast Cleanup Premium TuneupSvc Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-696
- **ZDI-CAN:** ZDI-CAN-25549
- **Date:** 2025-07-29
- **CVE:** CVE-2024-13961
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Avast
- **Affected Products:** Cleanup Premium
- **Credit:** Vladislav Berghici
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-696/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Avast Cleanup Premium. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Avast Cleanup Service. By creating a symbolic link, an attacker can abuse the service to delete a directory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in Avast Cleanup 24.3-SU1 - 24.3.17165.19178

## Disclosure Timeline

- 2024-11-05 - Vulnerability reported to vendor
- 2025-07-29 - Coordinated public release of advisory
- 2025-07-29 - Advisory Updated
