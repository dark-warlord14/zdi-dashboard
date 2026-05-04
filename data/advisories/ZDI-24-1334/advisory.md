# ZDI-24-1334: SonicWALL Connect Tunnel Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1334
- **ZDI-CAN:** ZDI-CAN-22655
- **Date:** 2024-10-11
- **CVE:** CVE-2024-45316
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SonicWALL
- **Affected Products:** Connect Tunnel
- **Credit:** Hashim Jawad (@ihack4falafel)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1334/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of SonicWALL Connect Tunnel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Secure Mobile Access service. By creating a symbolic link, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2024-0017

## Disclosure Timeline

- 2024-02-13 - Vulnerability reported to vendor
- 2024-10-11 - Coordinated public release of advisory
- 2024-10-11 - Advisory Updated
