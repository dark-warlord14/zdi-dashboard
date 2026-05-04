# ZDI-19-177: Cisco WebEx Recorder and Player asplayback Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-177
- **ZDI-CAN:** ZDI-CAN-6496
- **Date:** 2019-02-11
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** b0nd @garage4hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-177/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of WebEx Recorder and Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of WRF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to disclose sensitive information in the context of the current process.

## Additional Details

Fixed in Webex T33.4.0

## Disclosure Timeline

- 2018-07-18 - Vulnerability reported to vendor
- 2019-02-11 - Coordinated public release of advisory
- 2019-03-27 - Advisory Updated
