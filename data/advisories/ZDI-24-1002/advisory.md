# ZDI-24-1002: (0Day) Avast Cleanup Premium Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1002
- **ZDI-CAN:** ZDI-CAN-22892
- **Date:** 2024-07-29
- **CVE:** CVE-2024-7229
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Avast
- **Affected Products:** Cleanup Premium
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1002/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Avast Cleanup Premium. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Avast Cleanup Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

03/08/24 – ZDI reported the vulnerability to Avast’s Security Reports team. 09/27/23 – ZDI asked for updates 06/19/24 –ZDI asked for updates. 07/26/24 - ZDI informed the vendor that since we have not received a response, we will publish the case as a zero-day advisory on 07/29/24 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2024-03-08 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
