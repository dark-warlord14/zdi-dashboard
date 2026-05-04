# ZDI-18-430: Microsoft Office Graph Serialized Data Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-430
- **ZDI-CAN:** ZDI-CAN-5633
- **Date:** 2018-05-14
- **CVE:** CVE-2018-8157
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** willJ of Tencent PC Manager
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-430/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Graph. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of serialized data. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8157

## Disclosure Timeline

- 2018-02-01 - Vulnerability reported to vendor
- 2018-05-14 - Coordinated public release of advisory
- 2018-05-14 - Advisory Updated
