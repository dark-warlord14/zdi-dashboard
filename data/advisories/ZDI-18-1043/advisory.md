# ZDI-18-1043: Cisco WebEx Network Recording Player ATPDMOD ARF File Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1043
- **ZDI-CAN:** ZDI-CAN-6210
- **Date:** 2018-09-12
- **CVE:** N/A
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1043/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ARF files. Crafted data can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code under the context of the current process.

## Additional Details

Fixed in WebEx Business Suite T31.23, T32.15 and T33.2, WebEx Meetings Server 3.0MR1, and WebEx Meetings 1.3.35.

## Disclosure Timeline

- 2018-05-23 - Vulnerability reported to vendor
- 2018-09-12 - Coordinated public release of advisory
- 2018-09-12 - Advisory Updated
