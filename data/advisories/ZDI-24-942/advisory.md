# ZDI-24-942: Delta Electronics CNCSoft-G2 DPAX File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-942
- **ZDI-CAN:** ZDI-CAN-23914
- **Date:** 2024-07-22
- **CVE:** CVE-2024-39882
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** CNCSoft-G2
- **Credit:** Bobby Gould and Fritz Sands of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-942/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics CNCSoft-G2. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPAX files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-191-01

## Disclosure Timeline

- 2024-04-17 - Vulnerability reported to vendor
- 2024-07-22 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
