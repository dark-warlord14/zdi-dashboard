# ZDI-21-253: Siemens SINEC NMS FirmwareFileUtils extractToFolder Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-253
- **ZDI-CAN:** ZDI-CAN-12054
- **Date:** 2021-02-25
- **CVE:** CVE-2020-25237
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** SINEC NMS
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-253/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens SINEC NMS. Authentication is required to exploit this vulnerability. The specific flaw exists within the FirmwareFileUtils class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

https://us-cert.cisa.gov/ics/advisories/icsa-21-040-03 https://cert-portal.siemens.com/productcert/pdf/ssa-156833.pdf

## Disclosure Timeline

- 2020-10-16 - Vulnerability reported to vendor
- 2021-02-25 - Coordinated public release of advisory
