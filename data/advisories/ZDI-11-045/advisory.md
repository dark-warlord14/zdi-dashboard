# ZDI-11-045: (0Day) IBM Lotus Domino IMAP/POP3 Non-Printable Character Expansion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-045
- **ZDI-CAN:** ZDI-CAN-374
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0919
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-045/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of IBM Lotus Domino. Authentication is not required to exploit this vulnerability. The specific flaw exists within the POP3 and IMAP services while processing malformed e-mails. The vulnerable code expands specific non-printable characters within a "mail from" command without allocating adequate space. By providing enough of these characters, memory can be corrupted leading to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

http://www-01.ibm.com/support/docview.wss?uid=swg21461514

## Disclosure Timeline

- 2008-08-26 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
