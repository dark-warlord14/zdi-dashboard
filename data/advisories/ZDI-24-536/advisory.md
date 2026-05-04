# ZDI-24-536: Fuji Electric Alpha5 C5V File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-536
- **ZDI-CAN:** ZDI-CAN-21423
- **Date:** 2024-05-31
- **CVE:** CVE-2024-34579
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Alpha5 Smart
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-536/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric Alpha5 Smart. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of C5V files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

07/06/23 - ZDI reported the vulnerability to ICS-CERT 07/11/23 - ICS-CERT acknowledged the receipt of the report 11/17/23 - ZDI asked for updates 11/20/23 - The vendor communicated that the fix would be ready in 03/31/2024 02/15/24 - ICS-CERT asked the vendor for updates 02/23/24 -The vendor communicated that there will be no fix for the issue and the users should migrate to the Alpha7 units 05/16/24 - ZDI notified the vendor of the intention to publish the case as 0-day advisory on 05/30/24 -- Mitigation: The vendor's recommended path is to migrate to the Alpha7 units. https://www.fujielectric.com/products/drives_inverters/servo/product_series/alpha7_overview.html

## Disclosure Timeline

- 2023-07-10 - Vulnerability reported to vendor
- 2024-05-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
