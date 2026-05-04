# ZDI-11-058: (0Day) SCO Openserver IMAP Daemon Long Verb Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-058
- **ZDI-CAN:** ZDI-CAN-407
- **Date:** 2011-02-07
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SCO
- **Affected Products:** OpenServer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-058/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the SCO OpenServer IMAP daemon. Authentication is not required to exploit this vulnerability. The specific flaw exists within the imapd process responsible for handling remote IMAP requests. The process does not properly validate IMAP commands and arguments. Supplying an overly long command followed by an invalid argument can cause an exploitable overflow to occur. This vulnerability can be leveraged to execute arbitrary code.

## Disclosure Timeline

- 2008-11-10 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
