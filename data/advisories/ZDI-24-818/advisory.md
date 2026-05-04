# ZDI-24-818: VIPRE Advanced Security PMAgent Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-818
- **ZDI-CAN:** ZDI-CAN-22316
- **Date:** 2024-06-20
- **CVE:** CVE-2024-5929
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VIPRE
- **Affected Products:** Advanced Security
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-818/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VIPRE Advanced Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Patch Management Agent. The issue results from loading a file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

VIPRE has issued an update to correct this vulnerability. More details can be found at: https://success.vipre.com/en_US/home-windows-release-notes/home-windows-release-notes-20240227

## Disclosure Timeline

- 2023-12-01 - Vulnerability reported to vendor
- 2024-06-20 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
