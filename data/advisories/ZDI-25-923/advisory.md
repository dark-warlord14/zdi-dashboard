# ZDI-25-923: Fuji Electric FRENIC-Loader 4 EXRTM File Parsing Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-923
- **ZDI-CAN:** ZDI-CAN-26503
- **Date:** 2025-10-01
- **CVE:** CVE-2025-9365
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** FRENIC-Loader 4
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-923/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric FRENIC-Loader 4. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EXRTM and EXHIM files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-245-02

## Disclosure Timeline

- 2025-03-28 - Vulnerability reported to vendor
- 2025-10-01 - Coordinated public release of advisory
- 2025-10-01 - Advisory Updated
