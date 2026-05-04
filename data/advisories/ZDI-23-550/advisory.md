# ZDI-23-550: (Pwn2Own) Canon imageCLASS MF743Cdw CADM resourceStart2 Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-550
- **ZDI-CAN:** ZDI-CAN-19644
- **Date:** 2023-05-04
- **CVE:** CVE-2023-0851
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF743Cdw
- **Credit:** Le Tran Hai Tung (@tacbliw)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-550/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF743Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the resourceStart2 command in the CADM service. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.usa.canon.com/support/canon-product-advisories/Service-Notice-Vulnerabilities-Remediation-Against-Buffer-Overflow

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory
