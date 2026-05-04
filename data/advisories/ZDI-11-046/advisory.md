# ZDI-11-046: (0Day) IBM Lotus Domino Calendar Request Attachment Name Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-046
- **ZDI-CAN:** ZDI-CAN-372
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0918
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-046/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of IBM Lotus Domino. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NRouter service while transporting malformed e-mails. The vulnerable code copies data from the ATTACH:CID and Content-ID headers within an e-mail into a fixed length stack buffer. By providing a large enough file name, this buffer can overflow leading to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

http://www-01.ibm.com/support/docview.wss?uid=swg21461514

## Disclosure Timeline

- 2008-08-26 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
