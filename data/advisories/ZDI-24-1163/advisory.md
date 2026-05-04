# ZDI-24-1163: Allegra loadFieldMatch Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1163
- **ZDI-CAN:** ZDI-CAN-23452
- **Date:** 2024-08-22
- **CVE:** CVE-2024-5580
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Allegra
- **Affected Products:** Allegra
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1163/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Allegra. Authentication is required to exploit this vulnerability. The specific flaw exists within the loadFieldMatch method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of LOCAL SERVICE.

## Additional Details

Allegra has issued an update to correct this vulnerability. More details can be found at: https://alltena.com/en/resources/release-notes/relnotes-7-5-2

## Disclosure Timeline

- 2024-03-13 - Vulnerability reported to vendor
- 2024-08-22 - Coordinated public release of advisory
- 2024-08-22 - Advisory Updated
