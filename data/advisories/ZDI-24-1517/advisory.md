# ZDI-24-1517: McAfee Total Protection Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1517
- **ZDI-CAN:** ZDI-CAN-24269
- **Date:** 2024-11-19
- **CVE:** CVE-2024-49592
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** McAfee
- **Affected Products:** Total Protection
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1517/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of McAfee Total Protection. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the McAfee Direct Stub Installer. The product loads a library from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of an administrator.

## Additional Details

McAfee has issued an update to correct this vulnerability. More details can be found at: https://www.mcafee.com/support/s/article/000002516

## Disclosure Timeline

- 2024-07-24 - Vulnerability reported to vendor
- 2024-11-19 - Coordinated public release of advisory
- 2024-11-19 - Advisory Updated
