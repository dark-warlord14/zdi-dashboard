# ZDI-25-766: (0Day) (Pwn2Own) Alpine iLX-507 Command Injection Remote Code Execution

## Metadata

- **ZDI ID:** ZDI-25-766
- **ZDI-CAN:** ZDI-CAN-26357
- **Date:** 2025-08-01
- **CVE:** CVE-2025-8480
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Alpine
- **Affected Products:** iLX-507
- **Credit:** hama7230
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-766/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Alpine iLX-507 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Tidal music streaming application. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

01/29/25 – ZDI reported the vulnerability to the vendor. 01/30/25 – The vendor acknowledged the report. 02/24/25 – The vendor requested additional details. 02/24/25 – ZDI followed up and provided more information about the case. 07/29/25 – ZDI asked for an update and informed the vendor that the case will be published as a zero-day advisory on 08/01/25. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-08-01 - Vulnerability reported to vendor
- 2025-08-01 - Coordinated public release of advisory
- 2025-08-01 - Advisory Updated
