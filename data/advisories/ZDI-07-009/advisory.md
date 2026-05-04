# ZDI-07-009: Novell Netmail WebAdmin Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-009
- **ZDI-CAN:** ZDI-CAN-133
- **Date:** 2007-03-07
- **CVE:** CVE-2007-1350
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** NetMail
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-009/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell NetMail. Authentication is not required to exploit this vulnerability. The specific flaw exists in the webadmin.exe process bound by default on TCP port 89. During HTTP Basic authentication, a long username of at least 213 bytes will trigger a stack based buffer overflow due to a vulnerable sprintf() call. Exploitation of this issue can result in arbitrary code execution.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=sMYRODW09pw

## Disclosure Timeline

- 2006-12-12 - Vulnerability reported to vendor
- 2007-03-07 - Coordinated public release of advisory
