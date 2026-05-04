# ZDI-12-101: IBM Cognos tm1admsd.exe Multiple Operations Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-12-101
- **ZDI-CAN:** ZDI-CAN-1418
- **Date:** 2012-06-27
- **CVE:** CVE-2012-0202
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Cognos
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-101/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Cognos. Authentication is not required to exploit this vulnerability. The flaw exists within the tm1admsd.exe component. This process listens on TCP port 5498 by default. Requests to the service include a request type field, a data length field, and a data field. Multiple request types (opcodes) fail to validate user supplied length and data fields before copying their contents to a fixed length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the system.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21590314

## Disclosure Timeline

- 2011-11-21 - Vulnerability reported to vendor
- 2012-06-27 - Coordinated public release of advisory
