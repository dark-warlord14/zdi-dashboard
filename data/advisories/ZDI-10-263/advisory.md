# ZDI-10-263: CA Multiple Products create_session_bab SOAP Request Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-263
- **ZDI-CAN:** ZDI-CAN-878
- **Date:** 2010-12-09
- **CVE:** CVE-2010-3984
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** CA, CA, CA, CA
- **Affected Products:** XOsoft High Availability, XOsoft Replication
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-263/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of CA ARCserve Replication and High Availability. Authentication is not required to exploit this vulnerability. The specific flaw exists within the "create_session_bab" SOAP operation, which is handled by the xosoapapi.asmx process that is crucial to the remote administration of both the High Availability and the Replication products. By sending a specially crafted POST request to the xosoapapi.asmx process a remote, unauthenticated attacker can trigger a buffer overflow condition that results in arbitrary code execution under the context of the SOAP server process.

## Additional Details

https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID={FEB41CE8-5023-46DF-B257-5299F492BF23}

## Disclosure Timeline

- 2010-08-12 - Vulnerability reported to vendor
- 2010-12-09 - Coordinated public release of advisory
