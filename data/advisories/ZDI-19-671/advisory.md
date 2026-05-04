# ZDI-19-671: Schneider Electric IGSS MDB Database BaseUnits UnitIdx Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-671
- **ZDI-CAN:** ZDI-CAN-8284
- **Date:** 2019-07-22
- **CVE:** CVE-2019-6827
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** mdm and rgod of 9SG Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-671/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric IGSS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within use of the UnitIdx data in the BaseUnits table. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-192-06

## Disclosure Timeline

- 2019-05-08 - Vulnerability reported to vendor
- 2019-07-22 - Coordinated public release of advisory
