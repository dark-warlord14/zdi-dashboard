# ZDI-21-1334: Microsoft Windows Update Assistant Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1334
- **ZDI-CAN:** ZDI-CAN-14954
- **Date:** 2021-11-24
- **CVE:** CVE-2021-42297
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1334/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability. The specific flaw exists within Windows Update Assistant. By creating a symbolic link, an attacker can abuse the Update Assistant to delete a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42297

## Disclosure Timeline

- 2021-10-06 - Vulnerability reported to vendor
- 2021-11-24 - Coordinated public release of advisory
