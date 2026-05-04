# ZDI-24-1711: AnyDesk Link Following Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1711
- **ZDI-CAN:** ZDI-CAN-23940
- **Date:** 2024-12-19
- **CVE:** CVE-2024-12754
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** AnyDesk
- **Affected Products:** AnyDesk
- **Credit:** Naor Hodorov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1711/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of AnyDesk. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of background images. By creating a junction, an attacker can abuse the service to read arbitrary files. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Fixed in AnyDesk version v9.0.1 available on: https://anydesk.com/en/downloads/windows

## Disclosure Timeline

- 2024-07-24 - Vulnerability reported to vendor
- 2024-12-19 - Coordinated public release of advisory
- 2024-12-19 - Advisory Updated
