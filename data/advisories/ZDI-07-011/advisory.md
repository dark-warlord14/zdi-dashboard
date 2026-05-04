# ZDI-07-011: IBM Lotus Domino IMAP Server CRAM-MD5 Authentication Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-011
- **ZDI-CAN:** ZDI-CAN-060
- **Date:** 2007-03-28
- **CVE:** CVE-2007-1675
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-011/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Domino Server. Authentication is not required to exploit this vulnerability. The specific flaw exists in the CRAM-MD5 authentication mechanism of nimap.exe which binds by default to TCP port 143. No check is done on the length on the supplied username prior to processing it through a custom copy loop. If the username is longer than 256 bytes, a pointer overwrite may occur in the function nnotes.dll.CStream::ToBase64() which is later called and can therefore result in execution of arbitrary code.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-1.ibm.com/support/docview.wss?uid=swg21257028

## Disclosure Timeline

- 2006-08-31 - Vulnerability reported to vendor
- 2007-03-28 - Coordinated public release of advisory
