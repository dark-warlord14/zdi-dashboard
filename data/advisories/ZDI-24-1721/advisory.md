# ZDI-24-1721: Delta Electronics DTM Soft BIN File Parsing Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1721
- **ZDI-CAN:** ZDI-CAN-22331
- **Date:** 2024-12-20
- **CVE:** CVE-2024-12677
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** DTM Soft
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1721/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics DTM Soft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of BIN files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-354-03

## Disclosure Timeline

- 2024-02-29 - Vulnerability reported to vendor
- 2024-12-20 - Coordinated public release of advisory
- 2024-12-20 - Advisory Updated
