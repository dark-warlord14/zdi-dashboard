# ZDI-07-057: Firebird process_packet() Remote Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-057
- **ZDI-CAN:** ZDI-CAN-237
- **Date:** 2007-10-10
- **CVE:** CVE-2007-4992
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Firebird
- **Affected Products:** Firebird SQL
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-057/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Firebird SQL server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the database service fbserver.exe, which binds to TCP port 3050. When processing an overly long request, a stack buffer can be overflowed through a vulnerable call to sprintf() within the function process_packet(). If properly exploited, remote control of the affected system can be attained with SYSTEM credentials.

## Additional Details

Firebird has issued an update to correct this vulnerability. More details can be found at: http://www.firebirdsql.org/rlsnotes/Firebird-2.0.3-ReleaseNotes.pdf

## Disclosure Timeline

- 2007-09-14 - Vulnerability reported to vendor
- 2007-10-10 - Coordinated public release of advisory
