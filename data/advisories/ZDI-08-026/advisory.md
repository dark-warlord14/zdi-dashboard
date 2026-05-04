# ZDI-08-026: CA BrightStor ARCserve Backup XDR Parsing Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-026
- **ZDI-CAN:** ZDI-CAN-063
- **Date:** 2008-05-19
- **CVE:** CVE-2008-2242
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** BrightStor ARCserve Server
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-026/
## Vulnerability Details

This vulnerability allws attackers to execute arbitrary code on vulnerable installations of CA BrightStor ARCserve Backup for Linux. User interaction is not required to exploit this vulnerability. The specific flaw exists due to improper bounds checking in the xdr_rwsstring() library function. By sending a long parameter into a daemon using this function to process strings, a stack based buffer overflow occurs, leading to execution of arbitrary code.

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID=176798

## Disclosure Timeline

- 2006-09-12 - Vulnerability reported to vendor
- 2008-05-19 - Coordinated public release of advisory
