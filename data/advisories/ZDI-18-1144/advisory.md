# ZDI-18-1144: Cisco Webex Recorder and Player ATAS32 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1144
- **ZDI-CAN:** ZDI-CAN-6314
- **Date:** 2018-10-10
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Michael Flanders of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1144/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Cisco WebEx. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of WRF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to disclose sensitive information in the context of the current process.

## Additional Details

Fixed in Webex Player WBS33.3

## Disclosure Timeline

- 2018-06-13 - Vulnerability reported to vendor
- 2018-10-10 - Coordinated public release of advisory
- 2018-10-10 - Advisory Updated
