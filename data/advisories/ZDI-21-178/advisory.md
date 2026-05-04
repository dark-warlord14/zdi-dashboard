# ZDI-21-178: Microsoft Windows Device Management Enrollment Service Directory Junction Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-178
- **ZDI-CAN:** ZDI-CAN-12154
- **Date:** 2021-02-10
- **CVE:** CVE-2021-24084
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-178/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Device Management Enrollment Service. By creating a directory junction, an attacker can abuse the Device Management Enrollment Service to disclose the contents of arbitrary files. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-24084

## Disclosure Timeline

- 2020-10-28 - Vulnerability reported to vendor
- 2021-02-10 - Coordinated public release of advisory
