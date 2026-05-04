# ZDI-06-003: Ipswitch Collaboration Suite Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-003
- **ZDI-CAN:** ZDI-CAN-009
- **Date:** 2006-03-13
- **CVE:** CVE-2005-3526
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Ipswitch
- **Affected Products:** IMail
- **Credit:** Manuel Santamarina Suarez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-003/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Ipswitch Collaboration Suite. Authentication is required to exploit this vulnerability. This specific flaw exists within the IMAP daemon. A lack of bounds checking during the parsing of long arguments to the FETCH verb can result in an exploitable buffer overflow.

## Additional Details

Ipswitch has issued an update to correct this vulnerability. More details can be found at: http://www.ipswitch.com/support/ics/updates/ics200603prem.asp

## Disclosure Timeline

- 2005-12-13 - Vulnerability reported to vendor
- 2006-03-13 - Coordinated public release of advisory
- 2020-04-17 - Advisory Updated
