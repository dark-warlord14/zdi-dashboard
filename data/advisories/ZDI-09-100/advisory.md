# ZDI-09-100: IBM DB2 Universal Database Multiple SQL Functions Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-09-100
- **ZDI-CAN:** ZDI-CAN-488
- **Date:** 2009-12-15
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** IBM
- **Affected Products:** DB2 Universal Database
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-100/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM DB2. Authentication is required to exploit this vulnerability. The specific flaw exists in the parsing of VARCHAR arguments to a number of stored procedures available by default on DB2 installations. The vulnerable functions accept VARCHAR(255) strings which are subsequently copied to 218 byte fixed size stack buffers without proper bounds checking resulting in a stack-based buffer overflow. Exploitation can result in system compromise under the credentials of the DB process user.

## Additional Details

IBM has issued fixes to address this issue. Further details are available at: http://www-01.ibm.com/support/docview.wss?uid=swg1IC61746 http://www-01.ibm.com/support/docview.wss?uid=swg1IC61962 http://www-01.ibm.com/support/docview.wss?uid=swg1IC62625 http://www-01.ibm.com/support/docview.wss?uid=swg1IC63525

## Disclosure Timeline

- 2009-06-23 - Vulnerability reported to vendor
- 2009-12-15 - Coordinated public release of advisory
