# ZDI-06-036: Novell Netmail User Authentication Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-036
- **ZDI-CAN:** ZDI-CAN-076
- **Date:** 2006-10-31
- **CVE:** CVE-2006-5478
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** NetMail
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-036/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Netmail. Exploitation does not require authentication. The specific flaw exists within the user authentication component of Novell Netmail. The routine responsible for authenticating Netmail users lacks adequate bounds checking when processing a username containing one or more period (.) characters. The affected code is reused by several Netmail services including SMTP, POP, IMAP, HTTP and the proprietary NMAP. Each of these services is vulnerable to an exploitable stack-based buffer overflow.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&externalId=3096026&sliceId=SAL_Public

## Disclosure Timeline

- 2006-09-08 - Vulnerability reported to vendor
- 2006-10-31 - Coordinated public release of advisory
