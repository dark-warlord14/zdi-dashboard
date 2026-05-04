# ZDI-08-063: Novell eDirectory dhost.exe Content-Length Header Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-063
- **ZDI-CAN:** ZDI-CAN-312
- **Date:** 2008-10-08
- **CVE:** CVE-2008-4478
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-063/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Novell eDirectory. Authentication is not required to exploit this vulnerability. The specific flaw resides in the web console running on TCP ports 8028 and 8030. The server exposes a web interface and accepts SOAP connections. While parsing the Content-Length header within a SOAP request an integer overflow can occur. This integer overflow triggers a subsequent overflow during a memory copy operation leading to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/php/search.do?cmd=displayKC&docType=kc&externalId=7000087&sliceId=1&docTypeID=DT_TID_1_1&dialogID=78066829&stateId=0%200%2078062953

## Disclosure Timeline

- 2008-04-08 - Vulnerability reported to vendor
- 2008-10-08 - Coordinated public release of advisory
