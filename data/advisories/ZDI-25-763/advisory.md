# ZDI-25-763: (0Day) (Pwn2Own) Alpine iLX-507 CarPlay Stack-based Buffer Overflow Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-763
- **ZDI-CAN:** ZDI-CAN-26318
- **Date:** 2025-08-01
- **CVE:** CVE-2025-8474
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Alpine
- **Affected Products:** iLX-507
- **Credit:** Radu Motspan (@_moradek_) from PCAutomotive
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-763/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of Alpine iLX-507 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the Apple CarPlay protocol. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

01/29/25 – ZDI reported the vulnerability to the vendor. 01/30/25 – The vendor acknowledged the report. 02/24/25 – The vendor requested additional details. 02/24/25 – ZDI followed up and provided more information about the case. 07/29/25 – ZDI asked for an update and informed the vendor that the case will be published as a zero-day advisory on 08/01/25. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-01-27 - Vulnerability reported to vendor
- 2025-08-01 - Coordinated public release of advisory
- 2025-08-01 - Advisory Updated
