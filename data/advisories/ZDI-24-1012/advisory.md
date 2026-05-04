# ZDI-24-1012: (0Day) F-Secure Total Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1012
- **ZDI-CAN:** ZDI-CAN-23005
- **Date:** 2024-07-29
- **CVE:** CVE-2024-7240
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** F-Secure
- **Affected Products:** Total
- **Credit:** Nicholas Zubrisky (@NZubrisky) and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1012/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of F-Secure Total. User interaction on the part of an administrator is required to exploit this vulnerability. The specific flaw exists within the WithSecure plugin hosting service. By creating a symbolic link, an attacker can abuse the service to create a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

02/22/24 – ZDI reported the vulnerability to F-secure’s Security team. 06/19/24 – ZDI asked for updates. 07/26/24 – ZDI informed the vendor that since we have not received a response that we will publish the case as a zero-day advisory on 07/29/24 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2024-02-22 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
