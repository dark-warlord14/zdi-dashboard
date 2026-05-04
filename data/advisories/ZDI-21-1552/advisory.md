# ZDI-21-1552: Microsoft Windows Print Spooler Link Following Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1552
- **ZDI-CAN:** ZDI-CAN-14459
- **Date:** 2021-12-21
- **CVE:** CVE-2021-41333
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1552/
## Vulnerability Details

This vulnerability allows local attackers to escape the low integrity sandbox on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Print Spooler service. The service can be abused to create an arbitrary file. An attacker can leverage this vulnerability to execute code in the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41333

## Disclosure Timeline

- 2021-08-10 - Vulnerability reported to vendor
- 2021-12-21 - Coordinated public release of advisory
