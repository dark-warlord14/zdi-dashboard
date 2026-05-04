# ZDI-25-762: (0Day) (Pwn2Own) Alpine iLX-507 UPDM_wstpCBCUpdStart Command Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-762
- **ZDI-CAN:** ZDI-CAN-26317
- **Date:** 2025-08-01
- **CVE:** CVE-2025-8473
- **CVSS:** 6.4
- **CVSS Vector:** AV:P/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Alpine
- **Affected Products:** iLX-507
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-762/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of Alpine iLX-507 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UPDM_wstpCBCUpdStart function. The issue results from the lack of proper validation of user-supplied data before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

01/29/25 – ZDI reported the vulnerability to the vendor. 01/30/25 – The vendor acknowledged the report. 02/24/25 – The vendor requested additional details. 02/24/25 – ZDI followed up and provided more information about the case. 07/29/25 – ZDI asked for an update and informed the vendor that the case will be published as a zero-day advisory on 08/01/25. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-01-27 - Vulnerability reported to vendor
- 2025-08-01 - Coordinated public release of advisory
- 2025-08-01 - Advisory Updated
