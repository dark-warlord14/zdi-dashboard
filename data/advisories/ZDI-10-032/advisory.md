# ZDI-10-032: SAP MaxDB Malformed Handshake Request Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-032
- **ZDI-CAN:** ZDI-CAN-610
- **Date:** 2010-03-16
- **CVE:** CVE-2010-1185
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SAP
- **Affected Products:** MaxDB
- **Credit:** AbdulAziz Hariri of Insight Technologies
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-032/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP MaxDB. Authentication is not required to exploit this vulnerability. The specific flaw exists within the serv.exe process which listens by default on TCP port 7210. The process trusts a value from a handshake packet and uses it as a length when copying data to the stack. If provided a malicious value and packet data, this can be leveraged to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

A solution was provided via SAP note 1409425 ( https://service.sap.com/sap/support/notes/1409425 )

## Disclosure Timeline

- 2009-11-09 - Vulnerability reported to vendor
- 2010-03-16 - Coordinated public release of advisory
