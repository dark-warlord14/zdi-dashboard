# ZDI-24-491: WithSecure Elements Endpoint Protection Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-491
- **ZDI-CAN:** ZDI-CAN-23035
- **Date:** 2024-05-22
- **CVE:** CVE-2024-4454
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WithSecure
- **Affected Products:** Elements
- **Credit:** Nicholas Zubrisky (@NZubrisky) and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-491/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of WithSecure Elements Endpoint Protection. User interaction on the part of an administrator is required to exploit this vulnerability. The specific flaw exists within the WithSecure plugin hosting service. By creating a symbolic link, an attacker can abuse the service to create a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

WithSecure has issued an update to correct this vulnerability. More details can be found at: https://www.withsecure.com/en/support/security-advisories/cve-2024-4454

## Disclosure Timeline

- 2024-02-23 - Vulnerability reported to vendor
- 2024-05-22 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
