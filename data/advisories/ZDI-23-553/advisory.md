# ZDI-23-553: (Pwn2Own) Canon imageCLASS MF743Cdw mDNS hostname Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-553
- **ZDI-CAN:** ZDI-CAN-19827
- **Date:** 2023-05-04
- **CVE:** CVE-2023-0853
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF743Cdw
- **Credit:** Angelboy (@scwuaptx) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-553/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF743Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within handling of mDNS packets. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.usa.canon.com/support/canon-product-advisories/Service-Notice-Vulnerabilities-Remediation-Against-Buffer-Overflow

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory
