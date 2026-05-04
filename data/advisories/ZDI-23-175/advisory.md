# ZDI-23-175: Oracle WebRTC Session Controller parseCert Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-175
- **ZDI-CAN:** ZDI-CAN-18862
- **Date:** 2023-02-24
- **CVE:** CVE-2023-21890
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** WebRTC Session Controller
- **Credit:** Peter Mularien, Nightcrawler Security, LLC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-175/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle WebRTC Session Controller. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parseCert function. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2023.html

## Disclosure Timeline

- 2022-10-26 - Vulnerability reported to vendor
- 2023-02-24 - Coordinated public release of advisory
