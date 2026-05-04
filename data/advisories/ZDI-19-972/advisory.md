# ZDI-19-972: Microsoft Windows IP Helper Service Hard Link Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-972
- **ZDI-CAN:** ZDI-CAN-8945
- **Date:** 2019-11-13
- **CVE:** CVE-2019-1422
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** kkokkokye@THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-972/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the IP Helper service. By creating a hard link, an attacker can abuse the service to overwrite the contents of a chosen file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1422

## Disclosure Timeline

- 2019-07-18 - Vulnerability reported to vendor
- 2019-11-13 - Coordinated public release of advisory
