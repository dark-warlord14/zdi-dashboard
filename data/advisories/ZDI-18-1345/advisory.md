# ZDI-18-1345: Cisco WebEx Recorder and Player asplayback Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1345
- **ZDI-CAN:** ZDI-CAN-6406
- **Date:** 2018-11-20
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** b0nd @garage4hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1345/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Cisco WebEx Recorder and Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of WRF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Fixed in Webex Player WBS32.15.10 and WBS33.6

## Disclosure Timeline

- 2018-07-16 - Vulnerability reported to vendor
- 2018-11-20 - Coordinated public release of advisory
- 2018-11-20 - Advisory Updated
