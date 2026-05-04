# ZDI-23-343: ICONICS GENESIS64 PKGX File Parsing Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-343
- **ZDI-CAN:** ZDI-CAN-17369
- **Date:** 2023-03-31
- **CVE:** CVE-2022-33320
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** ICONICS
- **Affected Products:** GENESIS64
- **Credit:** Noam Moshe of Claroty Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-343/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ICONICS GENESIS64. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PKGX files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

ICONICS has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-22-202-04

## Disclosure Timeline

- 2022-06-07 - Vulnerability reported to vendor
- 2023-03-31 - Coordinated public release of advisory
