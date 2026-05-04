# ZDI-10-155: Cisco WebEx Player ARF String Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-155
- **ZDI-CAN:** ZDI-CAN-627
- **Date:** 2010-08-23
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Gabriel Menezes Nunes
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-155/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists during the parsing of strings defined within the ARF file format. Strings are typically prefixed by their valid length. By supplying a string much longer than the defined length a heap overflow will occur which can be further leveraged to execute arbitrary code under the context of the current user.

## Additional Details

This issue has been resolved in T27FR14, deployed to WebEx customers in April.

## Disclosure Timeline

- 2010-01-06 - Vulnerability reported to vendor
- 2010-08-23 - Coordinated public release of advisory
