# ZDI-07-010: Apple Quicktime UDTA Parsing Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-010
- **ZDI-CAN:** ZDI-CAN-093
- **Date:** 2007-03-07
- **CVE:** CVE-2007-0714
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-010/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of forged size fields in user-defined data atoms (UDTA). By setting this field to an overly large value, an integer overflow occurs resulting in an exploitable heap overflow. Successful exploitation results in code execution under the context of the running user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://docs.info.apple.com/article.html?artnum=61798

## Disclosure Timeline

- 2006-08-14 - Vulnerability reported to vendor
- 2007-03-07 - Coordinated public release of advisory
