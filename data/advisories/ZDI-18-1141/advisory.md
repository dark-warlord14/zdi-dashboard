# ZDI-18-1141: Cisco WebEx Network Recording Player ARF File Out-of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1141
- **ZDI-CAN:** ZDI-CAN-6145
- **Date:** 2018-10-10
- **CVE:** N/A
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1141/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ARF files. Crafted data can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code under the context of the current process.

## Additional Details

Fixed in Webex Network Recording Player WBS32.15.10 and WBS33.3

## Disclosure Timeline

- 2018-05-16 - Vulnerability reported to vendor
- 2018-10-10 - Coordinated public release of advisory
- 2018-10-10 - Advisory Updated
