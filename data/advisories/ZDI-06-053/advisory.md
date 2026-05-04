# ZDI-06-053: Novell NetMail IMAP Verb Literal Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-053
- **ZDI-CAN:** ZDI-CAN-085
- **Date:** 2006-12-22
- **CVE:** CVE-2006-6424
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** NetMail
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-053/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected versions of Novell NetMail. Authentication is not required to exploit this vulnerability. The specific flaw exists in the NetMail IMAP service, imapd.exe. The service does not sufficiently validate user-input length values when literals are appended to IMAP verbs to specify a command continuation request. The memory allocated to store the additional data may be insufficient, leading to an exploitable heap-based buffer overflow.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&externalId=3096026&sliceId=SAL_Public

## Disclosure Timeline

- 2006-08-14 - Vulnerability reported to vendor
- 2006-12-22 - Coordinated public release of advisory
