# ZDI-24-469: Avira Prime Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-469
- **ZDI-CAN:** ZDI-CAN-21600
- **Date:** 2024-05-17
- **CVE:** CVE-2023-51636
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Avira
- **Affected Products:** Prime
- **Credit:** Filip Dragovic (@filip_dragovic)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-469/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Avira Prime. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Avira Spotlight Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in Speedup version 6.27.19 https://public-beta.avira.com/download/speedup-windows/avira_system_speedup.exe

## Disclosure Timeline

- 2023-11-01 - Vulnerability reported to vendor
- 2024-05-17 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
