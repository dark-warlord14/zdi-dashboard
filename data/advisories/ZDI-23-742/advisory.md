# ZDI-23-742: (0Day) Wacom Drivers for Windows Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-742
- **ZDI-CAN:** ZDI-CAN-16857
- **Date:** 2023-05-26
- **CVE:** CVE-2023-32163
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Wacom
- **Affected Products:** Drivers for Windows
- **Credit:** Luca Barile - https://lucabarile.github.io/
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-742/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Wacom Drivers for Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Tablet Service. By creating a symbolic link, an attacker can abuse the service to create a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

08/04/22 – ZDI reported the vulnerability to the vendor. 08/04/22 – The vendor acknowledged the report. 01/26/23 – ZDI asked for an update. 03/02/23 – ZDI asked for an update. 05/23/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 05/26/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-08-04 - Vulnerability reported to vendor
- 2023-05-26 - Coordinated public release of advisory
