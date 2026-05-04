# ZDI-11-237: CA Total Defense Suite Gateway Security Malformed HTTP Packet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-237
- **ZDI-CAN:** ZDI-CAN-1017
- **Date:** 2011-07-20
- **CVE:** CVE-2011-2667
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** CA
- **Affected Products:** Total Defense Suite
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-237/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of CA Total Defense Suite r12. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Icihttp.exe module (CA Gateway Security for HTTP), which responds to incoming HTTP requests on port 8080. Due to a flawed copy-loop algorithm in the URL parsing routine, it is possible for a remote unauthenticated user to cause an exploitable heap corruption condition. This could result in the execution of arbitrary code under the context of the Gateway Security service.

## Additional Details

CA20110720-01: Security Notice for CA Gateway Security and Total Defense https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID=%7b5E404992-6B58-4C44-A29D-027D05B6285D%7d

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-07-20 - Coordinated public release of advisory
