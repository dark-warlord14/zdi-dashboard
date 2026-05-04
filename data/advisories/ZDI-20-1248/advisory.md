# ZDI-20-1248: Microsoft Windows User Profile Service Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1248
- **ZDI-CAN:** ZDI-CAN-11129
- **Date:** 2020-10-19
- **CVE:** CVE-2020-16940
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1248/
## Vulnerability Details

This vulnerability allows local attackers to delete arbitrary files on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within handling of the local registry hive by the User Profile service. By creating a junction, an attacker can abuse the service to delete files in an incorrect location. An attacker can leverage this vulnerability to delete files in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-16940

## Disclosure Timeline

- 2020-07-01 - Vulnerability reported to vendor
- 2020-10-19 - Coordinated public release of advisory
