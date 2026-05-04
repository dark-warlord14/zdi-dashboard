# ZDI-25-765: (0Day) (Pwn2Own) Alpine iLX-507 TIDAL Improper Certificate Validation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-765
- **ZDI-CAN:** ZDI-CAN-26322
- **Date:** 2025-08-01
- **CVE:** CVE-2025-8476
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Alpine
- **Affected Products:** iLX-507
- **Credit:** hama7230
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-765/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Alpine iLX-507 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the TIDAL music streaming application. The issue results from improper certificate validation. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

01/29/25 – ZDI reported the vulnerability to the vendor. 01/30/25 – The vendor acknowledged the report. 02/24/25 – The vendor requested additional details. 02/24/25 – ZDI followed up and provided more information about the case. 07/29/25 – ZDI asked for an update and informed the vendor that the case will be published as a zero-day advisory on 08/01/25. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-01-27 - Vulnerability reported to vendor
- 2025-08-01 - Coordinated public release of advisory
- 2025-08-01 - Advisory Updated
