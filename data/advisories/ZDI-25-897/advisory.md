# ZDI-25-897: Avira Prime Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-897
- **ZDI-CAN:** ZDI-CAN-22241
- **Date:** 2025-09-18
- **CVE:** CVE-2024-13759
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Avira
- **Affected Products:** Prime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-897/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Avira Prime. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Avira Spotlight Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Avira has issued an update to correct this vulnerability. More details can be found at: https://www.gendigital.com/us/en/contact-us/security-advisories/

## Disclosure Timeline

- 2024-06-11 - Vulnerability reported to vendor
- 2025-09-18 - Coordinated public release of advisory
- 2025-09-18 - Advisory Updated
