# ZDI-23-823: Fuji Electric Tellus Lite V-Simulator 6 X1 File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-823
- **ZDI-CAN:** ZDI-CAN-16781
- **Date:** 2023-06-08
- **CVE:** CVE-2022-3087
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Tellus Lite
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-823/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric Tellus Lite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of X1 files in the V-Simulator 6 application. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-22-354-01

## Disclosure Timeline

- 2022-03-25 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
