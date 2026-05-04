# ZDI-22-1666: Canon imageCLASS MF644Cdw BJNP Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1666
- **ZDI-CAN:** ZDI-CAN-16032
- **Date:** 2022-12-15
- **CVE:** CVE-2022-43608
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF644Cdw
- **Credit:** Angelboy(@scwuaptx) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1666/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF644Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the BJNP service. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.psirt.canon/advisory-information/cve-2022-43608_20221125

## Disclosure Timeline

- 2022-07-14 - Vulnerability reported to vendor
- 2022-12-15 - Coordinated public release of advisory
