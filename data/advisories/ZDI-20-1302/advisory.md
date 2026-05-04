# ZDI-20-1302: Micro Focus Operations Bridge Manager FolderService Deserialization Of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1302
- **ZDI-CAN:** ZDI-CAN-11394
- **Date:** 2020-10-28
- **CVE:** CVE-2020-11853
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Micro Focus
- **Affected Products:** Operations Bridge Manager
- **Credit:** Pedro Ribeiro (pedrib@gmail.com | @pedrib1337) from Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1302/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Micro Focus Operations Bridge Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the FolderService endpoint. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Micro Focus has issued an update to correct this vulnerability. More details can be found at: https://softwaresupport.softwaregrp.com/doc/KM03747658

## Disclosure Timeline

- 2020-06-26 - Vulnerability reported to vendor
- 2020-10-28 - Coordinated public release of advisory
